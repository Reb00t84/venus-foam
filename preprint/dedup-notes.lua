-- Схлопывает повторные сноски: если один и тот же источник [^n] цитируется
-- в тексте несколько раз, pandoc-LaTeX по умолчанию печатает \footnote{...}
-- (у нас -> \endnote) на каждую ссылку, и список Источников разбухает
-- дублями. Здесь первое вхождение остаётся полноценной сноской (нумеруется
-- enotez по порядку 1..N), а повторные заменяются простым надстрочным
-- номером первого вхождения.
local seen = {}
local n = 0

function Note(el)
  local key = pandoc.utils.stringify(el.content)
  local m = seen[key]
  if m then
    return pandoc.Superscript(pandoc.Str(tostring(m)))
  end
  n = n + 1
  seen[key] = n
  return el
end
