#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сборка PDF из md-исходника через pandoc + xelatex. Русский исходник —
venus-foam-ru.md; английский (перевод, базовое имя файла) — venus-foam.md,
собирается с флагом --en. Все выходные и промежуточные файлы (PDF, _build_*)
пишутся в директорию самого этого скрипта (preprint/), а не в CWD и не рядом
с .md — вызов из любой директории не мусорит вовне preprint/.

Использование:
    python3 preprint/build_preprint.py venus-foam-ru.md        # RU
    python3 preprint/build_preprint.py venus-foam.md --en       # EN

Что делает:
1. Первая строка '# Заголовок' переносится в YAML title pandoc -> центрированный
   тайтл. Автор/дата не угадываются из текста — их в исходниках проекта нет.
2. Фигуры: маркер '<!-- fig:N -->' + СЛЕДУЮЩАЯ строка (подпись 'Рис. N. ...'
   / 'Fig. N. ...') ищутся в тексте; если в FIG_FILES есть файл под этим
   номером — на место этих двух строк вставляется figure[H] (пакет float):
   картинка по центру, под ней подпись обычным абзацем дока (тот же
   размер/цвет, без caption-пакета). Блок неразрывен и стоит строго на
   месте — подпись всегда на одной странице с картинкой. На самой картинке
   текста подписи нет. Для ru-сборки берётся {имя}-ru.pdf с откатом на
   {имя}.pdf (англ.), если ru-варианта нет; для --en — сразу {имя}.pdf.
   Файла нет вообще — фигура не встраивается, без падения скрипта, это
   печатается в консоль.
3. NEEDSPACE_ANCHORS ниже — пустой по умолчанию; если появится таблица,
   которую нельзя рвать по странице, добавить сюда её первую строку дословно.
4. pandoc -f markdown+autolink_bare_uris (голые URL -> \\url, xurl их переносит).
5. xelatex x2, затем QC: overfull=0, missing characters=0, FFFD=0 (мусорные
   символы от нехватки шрифта/кодировки), ru_hyph_broken=False — иначе exit 1.

Требования: pandoc, xelatex (TeX-дистрибутив), шрифты DejaVu (Serif/Sans/Mono),
пакет с русскими правилами переноса (texlive-lang-cyrillic или аналог) — без
него сборка бракуется QC-проверкой ru_hyph_broken. xelatex ищется через PATH,
а если там нет — по известным локальным путям установки TeX Live без прав
администратора (см. find_xelatex ниже); если не найден нигде — падает с
понятной ошибкой, а не невнятным "command not found".
"""
import subprocess, sys, os, re, glob, shutil, datetime

RU_MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
             'августа', 'сентября', 'октября', 'ноября', 'декабря']


def find_xelatex():
    found = shutil.which('xelatex')
    if found:
        return found
    for pattern in (
        os.path.expanduser('~/.texlive-local/bin/*/xelatex'),
        '/usr/local/texlive/*/bin/*/xelatex',
        '/Library/TeX/texbin/xelatex',
    ):
        matches = glob.glob(pattern)
        if matches:
            return matches[0]
    sys.exit('xelatex не найден ни в PATH, ни в известных локальных путях TeX Live')


# Номер маркера "<!-- fig:N -->" -> имя файла (без .pdf), лежащего рядом с исходником.
FIG_FILES = {
    1: 'atmosphere-profile',
    2: 'platform-cross-section',
    3: 'platform-topdown',
    4: 'airlock-docking',
    5: 'energy-balance',
    6: 'deployment-sequence',
    7: 'radiation-shielding',
}
FIG_EXTS = ('.pdf', '.jpg', '.jpeg', '.png')  # порядок = приоритет при поиске файла

# Первая строка (дословно) таблиц, которые нельзя рвать по границе страницы:
# перед ней вставляется \needspace, и таблица целиком уезжает на следующую
# страницу, если не влезает. По одной записи на язык — для чужого языка
# строка просто не находится и пропускается. Держать здесь ВСЕ таблицы обоих
# документов.
NEEDSPACE_ANCHORS = [
    '| Высота | Температура | Давление | Ветер |',      # профиль атмосферы, ru
    '| Параметр | Значение |',                          # характеристики, ru
    '| Altitude | Temperature | Pressure | Wind |',     # профиль атмосферы, en
    '| Parameter | Value |',                            # характеристики, en
]
FIG_WIDTH = r'0.8\linewidth'
# Маркер '<!-- fig:N -->' и сразу СЛЕДУЮЩАЯ строка — подпись ('Рис. N. ...' /
# 'Fig. N. ...'). Картинка и подпись кладутся в один float figure: подпись —
# обычным текстом дока (тот же размер/цвет, без caption-пакета), разрыва
# страницы между картинкой и её подписью быть не может, а текст вокруг
# заполняет страницу (не остаётся полупустых листов, как было бы у minipage/[H]).
FIG_ANCHOR_RE = re.compile(r'<!-- fig:(\d+) -->\n(.+)')


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    xelatex = find_xelatex()
    src = sys.argv[1]
    en = '--en' in sys.argv
    base = os.path.splitext(os.path.basename(src))[0]

    # Всё, что касается сборки и самих PDF, живёт в этой директории (preprint/),
    # а не в CWD и не рядом с .md-исходником — так и промежуточные, и итоговые
    # файлы всегда собираются в одном месте независимо от того, откуда запущен
    # скрипт и где лежит сам markdown-документ.
    out_dir = os.path.dirname(os.path.abspath(__file__))
    build_md = os.path.join(out_dir, f'_build_{base}.md')
    tex = os.path.join(out_dir, f'_build_{base}.tex')
    pdf = os.path.join(out_dir, f'{base}.pdf')

    t = open(src, encoding='utf-8').read()
    lines = t.split('\n')
    assert lines[0].startswith('# '), 'первая строка должна быть "# Заголовок"'
    title = lines[0][2:].strip()

    # Тайтл-блок: строка 1 пустая, строка 2 — **Автор**, строка 3 пустая,
    # строка 4 — *Дата/версия*. Формат строгий (как в science-проекте) —
    # если он не совпадает один в один, автор/дата не угадываются, а
    # остаются пустыми: лучше отсутствие подписи, чем неверно угаданная.
    author = date = ''
    body_start = 1
    if (len(lines) > 4 and lines[1].strip() == ''
            and lines[2].startswith('**') and lines[2].strip().endswith('**')
            and lines[3].strip() == ''
            and lines[4].startswith('*') and not lines[4].startswith('**')
            and lines[4].strip().endswith('*')):
        author = lines[2].strip().strip('*').strip()
        date = lines[4].strip().strip('*').strip()
        # Дата в исходнике не редактируется руками -- versию (vN) сохраняем
        # как есть, дату справа от "—" всегда подставляем текущую на момент
        # сборки, чтобы файл не расходился с реальной датой билда.
        today = datetime.date.today()
        if en:
            new_date_str = today.strftime('%B %-d, %Y')
        else:
            new_date_str = f'{today.day} {RU_MONTHS[today.month - 1]} {today.year}'
        m = re.match(r'^(.*?—)\s*.*$', date)
        if m:
            date = f'{m.group(1)} {new_date_str}'
        body_start = 5
    body = '\n'.join(lines[body_start:]).lstrip('\n')

    fig_dir = out_dir  # фигуры лежат рядом со скриптом сборки (preprint/), не с .md
    # Базовое имя файла фигуры -- английский текст на самой картинке (график,
    # подписи осей, легенда); '-ru' суффикс -- русский вариант. Для ru-сборки
    # ищем сначала -ru, откатываемся на базовый (англ.), если ru-варианта нет.
    for m in FIG_ANCHOR_RE.finditer(body):
        num = int(m.group(1))
        anchor = m.group(0)
        caption = m.group(2).strip()
        name = FIG_FILES.get(num)
        fig_file = None
        if name:
            candidates = [f'{name}-ru{ext}' for ext in FIG_EXTS] if not en else []
            candidates += [f'{name}{ext}' for ext in FIG_EXTS]
            for cand in candidates:
                path = os.path.join(fig_dir, cand)
                if os.path.exists(path):
                    fig_file = path
                    break
        if fig_file:
            # Весь блок — один raw-latex figure[H]: картинка по центру, под ней
            # подпись обычным абзацем дока. [H] (пакет float) держит блок строго
            # на месте, без float-страниц; сам блок неразрывен, поэтому подпись
            # всегда на одной странице с картинкой. height ограничивает самые
            # высокие картинки (topdown), чтобы блок влезал и не гнал overfull.
            # Спецсимволов LaTeX в подписях нет — вставляем как есть.
            pic = (f'```{{=latex}}\n'
                   f'\\begin{{figure}}[H]\n'
                   f'{{\\centering\n'
                   f'\\includegraphics[width={FIG_WIDTH},height=0.42\\textheight,'
                   f'keepaspectratio]{{{fig_file}}}\\par}}\n'
                   f'\\medskip\n'
                   f'\\noindent {caption}\n'
                   f'\\end{{figure}}\n'
                   f'```\n')
            body = body.replace(anchor, pic, 1)
        else:
            print(f'[инфо] нет файла для номера {num} — фигура не встроена')

    # 7 baselineskip (~3 см) — с запасом больше, чем ~10-строчная таблица в
    # \scriptsize (~1,7 см), но не настолько, чтобы гнать таблицу на новую
    # страницу, когда места на текущей явно хватает. Поднять, если появится
    # заметно более высокая защищаемая таблица.
    for a in NEEDSPACE_ANCHORS:
        if body.count(a) == 1:
            body = body.replace(a, '\\needspace{7\\baselineskip}\n\n' + a)

    yaml = f'---\ntitle: "{title}"\n'
    if author:
        yaml += f'author: "{author}"\n'
    if date:
        yaml += f'date: "{date}"\n'
    yaml += '---\n\n'
    open(build_md, 'w', encoding='utf-8').write(yaml + body)

    hdr_dir = os.path.dirname(os.path.abspath(__file__))
    header = os.path.join(hdr_dir, 'header.tex')
    dedup = os.path.join(hdr_dir, 'dedup-notes.lua')
    cmd = ['pandoc', build_md, '-f', 'markdown+autolink_bare_uris', '-s', '-o', tex,
           f'--pdf-engine={xelatex}', '-H', header, '--lua-filter', dedup,
           '-V', 'mainfont=DejaVu Serif', '-V', 'sansfont=DejaVu Sans',
           '-V', 'monofont=DejaVu Sans Mono', '-V', 'fontsize=10pt',
           '-V', 'geometry:margin=2cm', '-V', 'colorlinks=true',
           '-V', 'linkcolor=blue', '-V', 'urlcolor=blue', '-V', 'citecolor=blue']
    if not en:
        cmd += ['-V', 'lang=ru']
    r = run(cmd)
    assert r.returncode == 0, r.stderr

    for _ in range(2):
        run([xelatex, '-interaction=nonstopmode', f'-output-directory={out_dir}', tex])
    texlog = open(tex.replace('.tex', '.log'), encoding='utf-8', errors='replace').read()

    overfull = texlog.count('Overfull')
    missing = len(re.findall(r'Missing character', texlog))
    nohyph = 'No hyphenation patterns were loaded' in texlog and not en
    txt = run(['pdftotext', tex.replace('.tex', '.pdf'), '-']).stdout
    fffd = txt.count('�')
    os.replace(tex.replace('.tex', '.pdf'), pdf)
    print(f'{pdf}: overfull={overfull} missing_chars={missing} FFFD={fffd} ru_hyph_broken={nohyph}')
    failed = overfull or missing or fffd or nohyph
    if failed:
        print('QC FAILED', file=sys.stderr)
    for junk in glob.glob(os.path.join(out_dir, f'_build_{base}.*')):
        os.remove(junk)
    if failed:
        sys.exit(1)
    print('QC OK')


if __name__ == '__main__':
    main()
