#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генерирует 8 PDF-иллюстраций для сборки через build_preprint.py, каждую в
двух языковых вариантах: atmosphere-profile, energy-balance,
battery-divergence, radiation-shielding, platform-cross-section,
platform-topdown, airlock-docking, cell-legend. Базовое имя файла (без
суффикса) — английский текст на самой картинке (оси, легенда, заголовок);
'-ru' суффикс — русский вариант. build_preprint.py ищет -ru для ru-сборки,
откатывается на базовый (англ.), если ru-варианта нет.
Числа продублированы из verify.py (разделы 1, 3-4, 7, 14) — если там
поменяются константы, эти цифры тоже надо пересчитать вручную, скрипты не
связаны. Геометрия ячеек (Fig 5/6) — фиксированная проверенная раскладка
(смежность проверена численно при построении, см. историю), не выводится из
verify.py заново при каждом запуске.
Пишет PDF в директорию источника (по умолчанию — preprint/, рядом с самим
этим скриптом, где их и ищет build_preprint.py).
Запуск: python3 preprint/make_figures.py [outdir]
"""
import os
import sys
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import Polygon, Rectangle
from matplotlib.lines import Line2D

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(OUT)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": "#c3c2b7",
    "axes.labelcolor": "#0b0b0b",
    "text.color": "#0b0b0b",
    "xtick.color": "#52514e",
    "ytick.color": "#52514e",
    "axes.grid": True,
    "grid.color": "#e1e0d9",
    "grid.linewidth": 0.7,
    "axes.axisbelow": True,
})

BLUE, ORANGE, AQUA, YELLOW, MAGENTA = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"
MUTED = "#c3c2b7"
DARK_GREY = "#898781"  # прежнее значение MUTED, теперь отдельно -- для шлюзов

CELL_COLOR = {
    "cell-panel": ORANGE,
    "cell-structural": MUTED,
    "cell-float": MAGENTA,
    "cell-habitat": AQUA,
    "cell-production": BLUE,
    "cell-airlock": DARK_GREY,
}
CELL_LABEL = {
    "en": {
        "cell-panel": "panel (solar + Li-ion)",
        "cell-structural": "structure (H2, load-bearing volume)",
        "cell-float": "float (H2 + batteries)",
        "cell-habitat": "habitat (O2+N2)",
        "cell-production": "production bay",
        "cell-airlock": "airlock",
    },
    "ru": {
        "cell-panel": "панель (солнечные + Li-ion)",
        "cell-structural": "структура (H2, несущий объём)",
        "cell-float": "поплавок (H2 + батареи)",
        "cell-habitat": "жилой отсек (O2+N2)",
        "cell-production": "производственный отсек",
        "cell-airlock": "шлюз",
    },
}

# ---------------------------------------------------------------------
# Все надписи на картинках, по языкам. Числа/геометрия -- вне этого словаря,
# общие для обоих проходов.
# ---------------------------------------------------------------------
S = {
    "en": dict(
        fig1_platform_point="platform\n22°C", fig1_xlabel_t="Temperature, °C",
        fig1_ylabel="Altitude, km", fig1_title_t="Temperature",
        fig1_xlabel_p="Pressure, atm (log scale)", fig1_title_p="Pressure",
        fig1_suptitle="Venus atmosphere profile by altitude",
        fig2_gen="panel generation", fig2_demand="station load (2 MW)",
        fig2_ylabel_p="MW", fig2_title_p="Power",
        fig2_ylabel_b="MWh", fig2_xlabel_b="Cycle hours (0-60 day, 60-120 night)",
        fig2_title_b="Storage charge",
        fig2_suptitle="Power balance: closed day/night cycle",
        fig3_threshold="k = 1 (divergence threshold)",
        fig3_low=" low\n insolation", fig3_high=" high\n insolation",
        fig3_xlabel="Panel power density, W/m²",
        fig3_ylabel="k (extra m² of battery per extra m² of panel)",
        fig3_suptitle="Why full smoothing with batteries does not converge",
        fig4_labels=["Earth,\nsea level", "Airliner\naltitude\n(~11 km)",
                     "Platform\n(55.7 km)"],
        fig4_ylabel="Atmospheric column, g/cm²",
        fig4_suptitle="Radiation shielding: atmospheric column overhead",
        fig5_sky="CO₂ 0.49 atm, 22°C", fig5_width="~600 m", fig5_height="up to ~20 m",
        fig5_suptitle="Platform cross-section: cells by function",
        fig6_width="~600 m",
        fig6_suptitle="Platform from above: zones under the panel skin",
        fig7_h2="H₂", fig7_o2="O₂+N₂ (habitat + production, shared environment)",
        fig7_leaf="leaf",
        fig7_suptitle="Compartment docking: H₂ cell / habitat / production",
    ),
    "ru": dict(
        fig1_platform_point="платформа\n22°C", fig1_xlabel_t="Температура, °C",
        fig1_ylabel="Высота, км", fig1_title_t="Температура",
        fig1_xlabel_p="Давление, атм (лог. шкала)", fig1_title_p="Давление",
        fig1_suptitle="Профиль атмосферы Венеры по высоте",
        fig2_gen="генерация панелей", fig2_demand="нагрузка станции (2 МВт)",
        fig2_ylabel_p="МВт", fig2_title_p="Мощность",
        fig2_ylabel_b="МВт·ч", fig2_xlabel_b="Часы цикла (0-60 день, 60-120 ночь)",
        fig2_title_b="Заряд накопителя",
        fig2_suptitle="Энергобаланс: замкнутый цикл день/ночь",
        fig3_threshold="k = 1 (порог расходимости)",
        fig3_low=" низкая\n инсоляция", fig3_high=" высокая\n инсоляция",
        fig3_xlabel="Плотность мощности панелей, Вт/м²",
        fig3_ylabel="k (доп. м² батареи на доп. м² панели)",
        fig3_suptitle="Почему полное сглаживание батареей не сходится",
        fig4_labels=["Земля,\nуровень моря", "Высота\nавиаперелёта\n(~11 км)",
                     "Платформа\n(55,7 км)"],
        fig4_ylabel="Столб атмосферы, г/см²",
        fig4_suptitle="Радиационное экранирование: столб атмосферы над точкой",
        fig5_sky="CO₂ 0,49 атм, 22°C", fig5_width="~600 м", fig5_height="до ~20 м",
        fig5_suptitle="Продольный разрез платформы: ячейки по функции",
        fig6_width="~600 м",
        fig6_suptitle="Платформа сверху: план зон под панельной обшивкой",
        fig7_h2="H₂", fig7_o2="O₂+N₂ (жилой + производственный, общая среда)",
        fig7_leaf="створка",
        fig7_suptitle="Стыковка отсеков: H₂-ячейка / жилой / производственный",
    ),
}


def save(fig, base, lang):
    suffix = "" if lang == "en" else f"-{lang}"
    path = os.path.join(OUT, f"{base}{suffix}.pdf")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {path}")


# ---------------------------------------------------------------------
# Геометрия и числа, общие для обоих языков (verify.py §1, 3-4, 7, 14 и
# фиксированная раскладка гексов Fig 5/6)
# ---------------------------------------------------------------------
alt = [0, 10, 20, 30, 40, 50, 55, 60, 65]
T_vals = [462, 385, 306, 222, 143, 75, 27, -10, -30]
P_vals = [92.1, 47.4, 22.5, 9.85, 3.50, 1.07, 0.531, 0.236, 0.098]
alt_platform, T_platform, P_platform = 55.68, 22, 0.491

TARGET_MW = 2.0
T_DAY = T_NIGHT = 60.0
ETA_RT = 0.90
P_day = TARGET_MW * T_DAY / T_DAY + (TARGET_MW * T_NIGHT) / ETA_RT / T_DAY  # = 4.222 МВт
t_p = [0, T_DAY, T_DAY, T_DAY + T_NIGHT]
gen = [P_day, P_day, 0, 0]
demand = [TARGET_MW, TARGET_MW, TARGET_MW, TARGET_MW]
soc_day_end = (P_day - TARGET_MW) * T_DAY * ETA_RT  # МВт*ч, замыкается на E_night
t_soc = [0, T_DAY, T_DAY + T_NIGHT]
soc = [0, soc_day_end, 0]

PACK_WH_KG = 149.0
lift_h2_used = 0.8522
CELL_THICKNESS = 20.0
CONV = 1 + 1 / ETA_RT


def marginal_gain(I):
    dP = I / (1e6 * CONV)
    dM = (T_NIGHT * 1000) / PACK_WH_KG
    dA = 1000 / lift_h2_used / CELL_THICKNESS
    return dP * dM * dA


I_range = [x for x in range(80, 300, 2)]
k_range = [marginal_gain(I) for I in I_range]
I_low, I_high = 114.4, 286.1

values4 = [1032.9, 225, 561.0]  # г/см^2; 225 — среднее из "200-250" в тексте, не выведено
colors4 = [MUTED, YELLOW, BLUE]

HEXES = [
    ([(151.0,266.3), (135.5,293.1), (104.5,293.1), (89.0,266.3), (104.5,239.5), (135.5,239.5)], "cell-panel"),
    ([(151.0,321.7), (135.5,348.5), (104.5,348.5), (89.0,321.7), (104.5,294.9), (135.5,294.9)], "cell-structural"),
    ([(199.0,238.6), (183.5,265.4), (152.5,265.4), (137.0,238.6), (152.5,211.8), (183.5,211.8)], "cell-panel"),
    ([(199.0,294.0), (183.5,320.8), (152.5,320.8), (137.0,294.0), (152.5,267.2), (183.5,267.2)], "cell-float"),
    ([(199.0,349.4), (183.5,376.2), (152.5,376.2), (137.0,349.4), (152.5,322.6), (183.5,322.6)], "cell-float"),
    ([(247.0,210.9), (231.5,237.7), (200.5,237.7), (185.0,210.9), (200.5,184.1), (231.5,184.1)], "cell-panel"),
    ([(247.0,266.3), (231.5,293.1), (200.5,293.1), (185.0,266.3), (200.5,239.5), (231.5,239.5)], "cell-float"),
    ([(247.0,321.7), (231.5,348.5), (200.5,348.5), (185.0,321.7), (200.5,294.9), (231.5,294.9)], "cell-float"),
    ([(247.0,377.1), (231.5,403.9), (200.5,403.9), (185.0,377.1), (200.5,350.3), (231.5,350.3)], "cell-float"),
    ([(295.0,238.6), (279.5,265.4), (248.5,265.4), (233.0,238.6), (248.5,211.8), (279.5,211.8)], "cell-panel"),
    ([(295.0,294.0), (279.5,320.8), (248.5,320.8), (233.0,294.0), (248.5,267.2), (279.5,267.2)], "cell-float"),
    ([(295.0,349.4), (279.5,376.2), (248.5,376.2), (233.0,349.4), (248.5,322.6), (279.5,322.6)], "cell-float"),
    ([(343.0,266.3), (327.5,293.1), (296.5,293.1), (281.0,266.3), (296.5,239.5), (327.5,239.5)], "cell-panel"),
    ([(343.0,321.7), (327.5,348.5), (296.5,348.5), (281.0,321.7), (296.5,294.9), (327.5,294.9)], "cell-airlock"),
    ([(343.0,377.1), (327.5,403.9), (296.5,403.9), (281.0,377.1), (296.5,350.3), (327.5,350.3)], "cell-structural"),
    ([(391.0,238.6), (375.5,265.4), (344.5,265.4), (329.0,238.6), (344.5,211.8), (375.5,211.8)], "cell-panel"),
    ([(391.0,294.0), (375.5,320.8), (344.5,320.8), (329.0,294.0), (344.5,267.2), (375.5,267.2)], "cell-production"),
    ([(391.0,349.4), (375.5,376.2), (344.5,376.2), (329.0,349.4), (344.5,322.6), (375.5,322.6)], "cell-production"),
    ([(439.0,210.9), (423.5,237.7), (392.5,237.7), (377.0,210.9), (392.5,184.1), (423.5,184.1)], "cell-panel"),
    ([(439.0,266.3), (423.5,293.1), (392.5,293.1), (377.0,266.3), (392.5,239.5), (423.5,239.5)], "cell-production"),
    ([(439.0,321.7), (423.5,348.5), (392.5,348.5), (377.0,321.7), (392.5,294.9), (423.5,294.9)], "cell-production"),
    ([(439.0,377.1), (423.5,403.9), (392.5,403.9), (377.0,377.1), (392.5,350.3), (423.5,350.3)], "cell-production"),
    ([(487.0,238.6), (471.5,265.4), (440.5,265.4), (425.0,238.6), (440.5,211.8), (471.5,211.8)], "cell-panel"),
    ([(487.0,294.0), (471.5,320.8), (440.5,320.8), (425.0,294.0), (440.5,267.2), (471.5,267.2)], "cell-production"),
    ([(487.0,349.4), (471.5,376.2), (440.5,376.2), (425.0,349.4), (440.5,322.6), (471.5,322.6)], "cell-production"),
    ([(535.0,266.3), (519.5,293.1), (488.5,293.1), (473.0,266.3), (488.5,239.5), (519.5,239.5)], "cell-panel"),
    ([(535.0,321.7), (519.5,348.5), (488.5,348.5), (473.0,321.7), (488.5,294.9), (519.5,294.9)], "cell-airlock"),
    ([(535.0,377.1), (519.5,403.9), (488.5,403.9), (473.0,377.1), (488.5,350.3), (519.5,350.3)], "cell-structural"),
    ([(583.0,238.6), (567.5,265.4), (536.5,265.4), (521.0,238.6), (536.5,211.8), (567.5,211.8)], "cell-panel"),
    ([(583.0,294.0), (567.5,320.8), (536.5,320.8), (521.0,294.0), (536.5,267.2), (567.5,267.2)], "cell-habitat"),
    ([(583.0,349.4), (567.5,376.2), (536.5,376.2), (521.0,349.4), (536.5,322.6), (567.5,322.6)], "cell-habitat"),
    ([(631.0,210.9), (615.5,237.7), (584.5,237.7), (569.0,210.9), (584.5,184.1), (615.5,184.1)], "cell-panel"),
    ([(631.0,266.3), (615.5,293.1), (584.5,293.1), (569.0,266.3), (584.5,239.5), (615.5,239.5)], "cell-habitat"),
    ([(631.0,321.7), (615.5,348.5), (584.5,348.5), (569.0,321.7), (584.5,294.9), (615.5,294.9)], "cell-habitat"),
    ([(631.0,377.1), (615.5,403.9), (584.5,403.9), (569.0,377.1), (584.5,350.3), (615.5,350.3)], "cell-habitat"),
    ([(679.0,238.6), (663.5,265.4), (632.5,265.4), (617.0,238.6), (632.5,211.8), (663.5,211.8)], "cell-panel"),
    ([(679.0,294.0), (663.5,320.8), (632.5,320.8), (617.0,294.0), (632.5,267.2), (663.5,267.2)], "cell-habitat"),
    ([(679.0,349.4), (663.5,376.2), (632.5,376.2), (617.0,349.4), (632.5,322.6), (663.5,322.6)], "cell-habitat"),
    ([(727.0,266.3), (711.5,293.1), (680.5,293.1), (665.0,266.3), (680.5,239.5), (711.5,239.5)], "cell-panel"),
    ([(727.0,321.7), (711.5,348.5), (680.5,348.5), (665.0,321.7), (680.5,294.9), (711.5,294.9)], "cell-airlock"),
    ([(727.0,377.1), (711.5,403.9), (680.5,403.9), (665.0,377.1), (680.5,350.3), (711.5,350.3)], "cell-structural"),
    ([(775.0,238.6), (759.5,265.4), (728.5,265.4), (713.0,238.6), (728.5,211.8), (759.5,211.8)], "cell-panel"),
    ([(775.0,294.0), (759.5,320.8), (728.5,320.8), (713.0,294.0), (728.5,267.2), (759.5,267.2)], "cell-production"),
    ([(775.0,349.4), (759.5,376.2), (728.5,376.2), (713.0,349.4), (728.5,322.6), (759.5,322.6)], "cell-production"),
    ([(823.0,210.9), (807.5,237.7), (776.5,237.7), (761.0,210.9), (776.5,184.1), (807.5,184.1)], "cell-panel"),
    ([(823.0,266.3), (807.5,293.1), (776.5,293.1), (761.0,266.3), (776.5,239.5), (807.5,239.5)], "cell-production"),
    ([(823.0,321.7), (807.5,348.5), (776.5,348.5), (761.0,321.7), (776.5,294.9), (807.5,294.9)], "cell-production"),
    ([(823.0,377.1), (807.5,403.9), (776.5,403.9), (761.0,377.1), (776.5,350.3), (807.5,350.3)], "cell-production"),
    ([(871.0,238.6), (855.5,265.4), (824.5,265.4), (809.0,238.6), (824.5,211.8), (855.5,211.8)], "cell-panel"),
    ([(871.0,294.0), (855.5,320.8), (824.5,320.8), (809.0,294.0), (824.5,267.2), (855.5,267.2)], "cell-production"),
    ([(871.0,349.4), (855.5,376.2), (824.5,376.2), (809.0,349.4), (824.5,322.6), (855.5,322.6)], "cell-production"),
    ([(919.0,266.3), (903.5,293.1), (872.5,293.1), (857.0,266.3), (872.5,239.5), (903.5,239.5)], "cell-panel"),
    ([(919.0,321.7), (903.5,348.5), (872.5,348.5), (857.0,321.7), (872.5,294.9), (903.5,294.9)], "cell-airlock"),
    ([(919.0,377.1), (903.5,403.9), (872.5,403.9), (857.0,377.1), (872.5,350.3), (903.5,350.3)], "cell-structural"),
    ([(967.0,238.6), (951.5,265.4), (920.5,265.4), (905.0,238.6), (920.5,211.8), (951.5,211.8)], "cell-panel"),
    ([(967.0,294.0), (951.5,320.8), (920.5,320.8), (905.0,294.0), (920.5,267.2), (951.5,267.2)], "cell-float"),
    ([(967.0,349.4), (951.5,376.2), (920.5,376.2), (905.0,349.4), (920.5,322.6), (951.5,322.6)], "cell-float"),
    ([(1015.0,210.9), (999.5,237.7), (968.5,237.7), (953.0,210.9), (968.5,184.1), (999.5,184.1)], "cell-panel"),
    ([(1015.0,266.3), (999.5,293.1), (968.5,293.1), (953.0,266.3), (968.5,239.5), (999.5,239.5)], "cell-float"),
    ([(1015.0,321.7), (999.5,348.5), (968.5,348.5), (953.0,321.7), (968.5,294.9), (999.5,294.9)], "cell-float"),
    ([(1015.0,377.1), (999.5,403.9), (968.5,403.9), (953.0,377.1), (968.5,350.3), (999.5,350.3)], "cell-float"),
    ([(1063.0,238.6), (1047.5,265.4), (1016.5,265.4), (1001.0,238.6), (1016.5,211.8), (1047.5,211.8)], "cell-panel"),
    ([(1063.0,294.0), (1047.5,320.8), (1016.5,320.8), (1001.0,294.0), (1016.5,267.2), (1047.5,267.2)], "cell-float"),
    ([(1063.0,349.4), (1047.5,376.2), (1016.5,376.2), (1001.0,349.4), (1016.5,322.6), (1047.5,322.6)], "cell-float"),
    ([(1111.0,266.3), (1095.5,293.1), (1064.5,293.1), (1049.0,266.3), (1064.5,239.5), (1095.5,239.5)], "cell-panel"),
    ([(1111.0,321.7), (1095.5,348.5), (1064.5,348.5), (1049.0,321.7), (1064.5,294.9), (1095.5,294.9)], "cell-structural"),
    ([(199.0,404.8), (183.5,431.6), (152.5,431.6), (137.0,404.8), (152.5,378.0), (183.5,378.0)], "cell-structural"),
    ([(247.0,432.5), (231.5,459.3), (200.5,459.3), (185.0,432.5), (200.5,405.7), (231.5,405.7)], "cell-structural"),
    ([(295.0,404.8), (279.5,431.6), (248.5,431.6), (233.0,404.8), (248.5,378.0), (279.5,378.0)], "cell-structural"),
    ([(391.0,404.8), (375.5,431.6), (344.5,431.6), (329.0,404.8), (344.5,378.0), (375.5,378.0)], "cell-structural"),
    ([(439.0,432.5), (423.5,459.3), (392.5,459.3), (377.0,432.5), (392.5,405.7), (423.5,405.7)], "cell-structural"),
    ([(487.0,404.8), (471.5,431.6), (440.5,431.6), (425.0,404.8), (440.5,378.0), (471.5,378.0)], "cell-structural"),
    ([(583.0,404.8), (567.5,431.6), (536.5,431.6), (521.0,404.8), (536.5,378.0), (567.5,378.0)], "cell-structural"),
    ([(631.0,432.5), (615.5,459.3), (584.5,459.3), (569.0,432.5), (584.5,405.7), (615.5,405.7)], "cell-structural"),
    ([(679.0,404.8), (663.5,431.6), (632.5,431.6), (617.0,404.8), (632.5,378.0), (663.5,378.0)], "cell-structural"),
    ([(775.0,404.8), (759.5,431.6), (728.5,431.6), (713.0,404.8), (728.5,378.0), (759.5,378.0)], "cell-structural"),
    ([(823.0,432.5), (807.5,459.3), (776.5,459.3), (761.0,432.5), (776.5,405.7), (807.5,405.7)], "cell-structural"),
    ([(871.0,404.8), (855.5,431.6), (824.5,431.6), (809.0,404.8), (824.5,378.0), (855.5,378.0)], "cell-structural"),
    ([(967.0,404.8), (951.5,431.6), (920.5,431.6), (905.0,404.8), (920.5,378.0), (951.5,378.0)], "cell-structural"),
    ([(1015.0,432.5), (999.5,459.3), (968.5,459.3), (953.0,432.5), (968.5,405.7), (999.5,405.7)], "cell-structural"),
    ([(1063.0,404.8), (1047.5,431.6), (1016.5,431.6), (1001.0,404.8), (1016.5,378.0), (1047.5,378.0)], "cell-structural"),
    ([(151.0,377.1), (135.5,403.9), (104.5,403.9), (89.0,377.1), (104.5,350.3), (135.5,350.3)], "cell-structural"),
    ([(1111.0,377.1), (1095.5,403.9), (1064.5,403.9), (1049.0,377.1), (1064.5,350.3), (1095.5,350.3)], "cell-structural"),
]

SIZE = 31.0  # тот же радиус гекса в разрезе (Fig 5) и в топдауне (Fig 6)


def hex_vertices(cx, cy, size):
    return [(cx + size * math.cos(math.radians(a)), cy + size * math.sin(math.radians(a)))
            for a in range(0, 360, 60)]


def axial_to_pixel(q, r_ax, size):
    x = size * 1.5 * q
    y = size * (3 ** 0.5) * (r_ax + q / 2)
    return x, y


HEX_DIRS = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]


def hex_ring(radius):
    if radius == 0:
        return [(0, 0)]
    results = []
    q, r_ax = HEX_DIRS[4][0] * radius, HEX_DIRS[4][1] * radius
    for side in range(6):
        dq, dr = HEX_DIRS[side]
        for _ in range(radius):
            results.append((q, r_ax))
            q, r_ax = q + dq, r_ax + dr
    return results


def cluster_232(center_x, center_y, cls):
    cells = []
    for q, r_ax in hex_ring(0) + hex_ring(1):
        lx, ly = axial_to_pixel(q, r_ax, SIZE)
        cells.append((center_x + lx, center_y + ly, cls))
    return cells


# топдаун-раскладка (Fig 6): жильё -- центральный кластер-хаб (ring0+ring1);
# 6 лучей: шаг2 -- гекс-шлюз, шаг4 -- кластер производства, шаг6 -- гекс-шлюз;
# тангенциальные шлюзы между соседними кластерами производства; кольцо
# поплавков на шаге 8 (12 кластеров: 6 угловых + 6 средних, между каждой
# парой -- гекс-шлюз); подложка структурными ячейками до радиуса 7. Все
# смежности проверены численно при построении (см. историю), не выводятся
# из verify.py заново.
TOP_CELLS = []
TOP_CELLS.extend(cluster_232(0.0, 0.0, "cell-habitat"))
for dq, dr in HEX_DIRS:
    ax_, ay = axial_to_pixel(dq * 2, dr * 2, SIZE)
    TOP_CELLS.append((ax_, ay, "cell-airlock"))
    px, py = axial_to_pixel(dq * 4, dr * 4, SIZE)
    TOP_CELLS.extend(cluster_232(px, py, "cell-production"))
    bx, by = axial_to_pixel(dq * 6, dr * 6, SIZE)
    TOP_CELLS.append((bx, by, "cell-airlock"))
for i in range(6):
    d0 = HEX_DIRS[i]
    d1 = HEX_DIRS[(i + 1) % 6]
    q = (d0[0] + d1[0]) * 4 // 2
    r = (d0[1] + d1[1]) * 4 // 2
    tx, ty = axial_to_pixel(q, r, SIZE)
    TOP_CELLS.append((tx, ty, "cell-airlock"))
FLOAT_RING_CENTERS = []
for i in range(6):
    d0 = HEX_DIRS[i]
    d1 = HEX_DIRS[(i + 1) % 6]
    FLOAT_RING_CENTERS.append((d0[0] * 8, d0[1] * 8))
    FLOAT_RING_CENTERS.append(((d0[0] + d1[0]) * 8 // 2, (d0[1] + d1[1]) * 8 // 2))
for cq, cr in FLOAT_RING_CENTERS:
    fx, fy = axial_to_pixel(cq, cr, SIZE)
    TOP_CELLS.extend(cluster_232(fx, fy, "cell-float"))
_n = len(FLOAT_RING_CENTERS)
for i in range(_n):
    q0, r0 = FLOAT_RING_CENTERS[i]
    q1, r1 = FLOAT_RING_CENTERS[(i + 1) % _n]
    tq, tr = (q0 + q1) // 2, (r0 + r1) // 2
    tx, ty = axial_to_pixel(tq, tr, SIZE)
    TOP_CELLS.append((tx, ty, "cell-airlock"))
_occupied = {(round(cx, 1), round(cy, 1)) for cx, cy, _ in TOP_CELLS}
FILL_RADIUS = 7
_fill_cells = []
for radius in range(FILL_RADIUS + 1):
    for q, r_ax in hex_ring(radius):
        px, py = axial_to_pixel(q, r_ax, SIZE)
        key = (round(px, 1), round(py, 1))
        if key not in _occupied:
            _fill_cells.append((px, py, "cell-structural"))
            _occupied.add(key)
TOP_CELLS = _fill_cells + TOP_CELLS  # подложка рисуется первой, ниже остальных

# докинг-схема (Fig 7): 2 больших отсека + низкая камера-перемычка со
# створками между ними, 3 у H2-ячейки, 2 у общей среды
H_CELL = 3 * SIZE
H_LOCK = H_CELL * 0.55
CELL_W = 2 * SIZE
LOCK_W = 1.8 * SIZE
y0_c, y1_c = -H_CELL / 2, H_CELL / 2
y0_l, y1_l = -H_LOCK / 2, H_LOCK / 2
_x = 0.0
DOCK_SEGMENTS = []
DOCK_SEGMENTS.append((_x, _x + CELL_W, y0_c, y1_c, "cell-float")); _x += CELL_W
LOCK_A_X0 = _x; LOCK_A_X1 = _x + LOCK_W; _x = LOCK_A_X1
DOCK_SEGMENTS.append((LOCK_A_X0, LOCK_A_X1, y0_l, y1_l, "cell-airlock"))
DOCK_SEGMENTS.append((_x, _x + CELL_W, y0_c, y1_c, "cell-habitat")); _x += CELL_W
LOCK_B_X0 = _x; LOCK_B_X1 = _x + LOCK_W; _x = LOCK_B_X1
DOCK_SEGMENTS.append((LOCK_B_X0, LOCK_B_X1, y0_l, y1_l, "cell-airlock"))
DOCK_SEGMENTS.append((_x, _x + CELL_W, y0_c, y1_c, "cell-production")); _x += CELL_W
DOCK_X_FULL = _x
DOCK_FLAP_W = SIZE * 0.22


def build(lang):
    T = S[lang]
    labels = CELL_LABEL[lang]

    # -------------------------------------------------------------
    # Fig 1 — профиль T и P по высоте (verify.py §1 + таблица "Среда")
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 4.2), sharey=True)
    ax1.plot(T_vals, alt, color=BLUE, linewidth=2)
    ax1.scatter([T_platform], [alt_platform], color=ORANGE, s=40, zorder=5)
    ax1.annotate(T["fig1_platform_point"], (T_platform, alt_platform), xytext=(8, -4),
                 textcoords="offset points", fontsize=8, color=ORANGE)
    ax1.set_xlabel(T["fig1_xlabel_t"])
    ax1.set_ylabel(T["fig1_ylabel"])
    ax1.set_title(T["fig1_title_t"], fontsize=10, loc="left", color="#52514e")

    ax2.plot(P_vals, alt, color=BLUE, linewidth=2)
    ax2.scatter([P_platform], [alt_platform], color=ORANGE, s=40, zorder=5)
    ax2.set_xscale("log")
    ax2.set_xlabel(T["fig1_xlabel_p"])
    ax2.set_title(T["fig1_title_p"], fontsize=10, loc="left", color="#52514e")

    for ax in (ax1, ax2):
        ax.axhline(alt_platform, color=MUTED, linewidth=0.7, linestyle="--", zorder=0)
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(T["fig1_suptitle"], fontsize=11, x=0.02, ha="left")
    fig.tight_layout()
    save(fig, "atmosphere-profile", lang)

    # -------------------------------------------------------------
    # Fig 2 — энергобаланс день/ночь, замкнутый цикл (verify.py §3-4)
    # -------------------------------------------------------------
    fig, (axp, axb) = plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True,
                                    gridspec_kw={"height_ratios": [2, 1]})
    axp.step(t_p, gen, where="post", color=BLUE, linewidth=2, label=T["fig2_gen"])
    axp.step(t_p, demand, where="post", color=ORANGE, linewidth=2, linestyle="--",
             label=T["fig2_demand"])
    axp.set_ylabel(T["fig2_ylabel_p"])
    axp.legend(frameon=False, fontsize=8, loc="upper right")
    axp.set_title(T["fig2_title_p"], fontsize=10, loc="left", color="#52514e")

    axb.plot(t_soc, soc, color=AQUA, linewidth=2)
    axb.fill_between(t_soc, soc, color=AQUA, alpha=0.15)
    axb.set_ylabel(T["fig2_ylabel_b"])
    axb.set_xlabel(T["fig2_xlabel_b"])
    axb.set_title(T["fig2_title_b"], fontsize=10, loc="left", color="#52514e")

    for ax in (axp, axb):
        ax.axvline(T_DAY, color=MUTED, linewidth=0.7, linestyle=":")
        ax.spines[["top", "right"]].set_visible(False)

    fig.suptitle(T["fig2_suptitle"], fontsize=11, x=0.02, ha="left")
    fig.tight_layout()
    save(fig, "energy-balance", lang)

    # -------------------------------------------------------------
    # Fig 3 — расходимость коэффициента k (verify.py §7)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(I_range, k_range, color=BLUE, linewidth=2)
    ax.axhline(1.0, color=ORANGE, linewidth=1.5, linestyle="--")
    ax.annotate(T["fig3_threshold"], (I_range[0], 1.03), color=ORANGE, fontsize=8)
    ax.fill_between(I_range, k_range, 1.0, where=[k > 1 for k in k_range],
                     color=ORANGE, alpha=0.08)
    ax.axvline(I_low, color=MUTED, linewidth=0.7, linestyle=":")
    ax.axvline(I_high, color=MUTED, linewidth=0.7, linestyle=":")
    ax.text(I_low, max(k_range) * 0.95, T["fig3_low"], fontsize=7, color=MUTED)
    ax.text(I_high, max(k_range) * 0.95, T["fig3_high"], fontsize=7, color=MUTED,
            ha="right")
    ax.set_xlabel(T["fig3_xlabel"])
    ax.set_ylabel(T["fig3_ylabel"])
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(T["fig3_suptitle"], fontsize=11, x=0.02, ha="left")
    fig.tight_layout()
    save(fig, "battery-divergence", lang)

    # -------------------------------------------------------------
    # Fig 4 — радиационное экранирование (verify.py §14)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    bars = ax.bar(T["fig4_labels"], values4, color=colors4, width=0.55)
    for b, v in zip(bars, values4):
        ax.annotate(f"{v:,.0f}".replace(",", " "), (b.get_x() + b.get_width() / 2, v),
                    xytext=(0, 4), textcoords="offset points", ha="center", fontsize=9)
    ax.set_ylabel(T["fig4_ylabel"])
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(T["fig4_suptitle"], fontsize=10.5, x=0.02, ha="left")
    fig.tight_layout()
    save(fig, "radiation-shielding", lang)

    # -------------------------------------------------------------
    # Fig 5 — разрез платформы: соты ячеек по функции
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    for coords, cls in HEXES:
        ax.add_patch(Polygon(coords, closed=True, facecolor=CELL_COLOR[cls],
                              edgecolor="white", linewidth=0.6, zorder=2))
    xs = [x for coords, _ in HEXES for x, y in coords]
    ys = [y for coords, _ in HEXES for x, y in coords]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)

    sky_y = y0 - 25
    ax.axhline(sky_y, color=MUTED, linewidth=0.7, linestyle=(0, (2, 4)), zorder=1)
    ax.text(x0, sky_y - 24, T["fig5_sky"], fontsize=7.5, color=MUTED, va="top")

    dim_y = y1 + 30
    ax.annotate("", xy=(x1, dim_y), xytext=(x0, dim_y),
                arrowprops=dict(arrowstyle="<->", color=MUTED, linewidth=0.8))
    ax.text((x0 + x1) / 2, dim_y + 24, T["fig5_width"], fontsize=8, color=MUTED, ha="center")

    dim_x = x1 + 30
    ax.annotate("", xy=(dim_x, y1), xytext=(dim_x, y0),
                arrowprops=dict(arrowstyle="<->", color=MUTED, linewidth=0.8))
    ax.text(dim_x + 8, (y0 + y1) / 2, T["fig5_height"], fontsize=8, color=MUTED,
            va="center", rotation=90)

    ax.set_xlim(x0 - 60, dim_x + 60)
    ax.set_ylim(dim_y + 55, sky_y - 55)
    ax.set_aspect("equal")
    ax.axis("off")

    handles5 = [Line2D([0], [0], marker="h", linestyle="", markersize=9,
                        markerfacecolor=CELL_COLOR[c], markeredgecolor="white",
                        label=labels[c])
                for c in ("cell-structural", "cell-airlock", "cell-float", "cell-panel",
                          "cell-habitat", "cell-production")]
    ax.legend(handles=handles5, loc="upper center", bbox_to_anchor=(0.5, -0.02),
              ncol=3, frameon=False, fontsize=7.5, handletextpad=0.4,
              columnspacing=1.2)

    fig.suptitle(T["fig5_suptitle"], fontsize=10.5, x=0.5, ha="center")
    fig.tight_layout()
    save(fig, "platform-cross-section", lang)

    # -------------------------------------------------------------
    # Fig 6 — топдаун-схема: план зон под панельной обшивкой
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(9.0, 9.0))
    for cx, cy, cls in TOP_CELLS:
        ax.add_patch(Polygon(hex_vertices(cx, cy, SIZE), closed=True,
                              facecolor=CELL_COLOR[cls], edgecolor="white",
                              linewidth=0.6, zorder=2))

    txs = [p[0] for p in TOP_CELLS]; tys = [p[1] for p in TOP_CELLS]
    tx0, tx1 = min(txs) - SIZE, max(txs) + SIZE
    ty0, ty1 = min(tys) - SIZE, max(tys) + SIZE

    ax.annotate("", xy=(tx1, ty1 + 25), xytext=(tx0, ty1 + 25),
                arrowprops=dict(arrowstyle="<->", color=MUTED, linewidth=0.8))
    ax.text((tx0 + tx1) / 2, ty1 + 45, T["fig6_width"], fontsize=8, color=MUTED, ha="center")

    ax.set_xlim(tx0 - 55, tx1 + 55)
    ax.set_ylim(ty1 + 55, ty0 - 55)
    ax.set_aspect("equal")
    ax.axis("off")

    handles6 = [Line2D([0], [0], marker="h", linestyle="", markersize=9,
                        markerfacecolor=CELL_COLOR[c], markeredgecolor="white",
                        label=labels[c])
                for c in ("cell-structural", "cell-airlock", "cell-float",
                          "cell-habitat", "cell-production")]
    ax.legend(handles=handles6, loc="upper center", bbox_to_anchor=(0.5, -0.02),
              ncol=3, frameon=False, fontsize=7.5, handletextpad=0.4,
              columnspacing=1.2)

    fig.suptitle(T["fig6_suptitle"], fontsize=10.5, x=0.5, ha="center")
    fig.tight_layout()
    save(fig, "platform-topdown", lang)

    # -------------------------------------------------------------
    # Fig 7 — стыковка отсеков: H2-ячейка / жилой / производственный
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(9.0, 2.8))
    for xa, xb, ya, yb, cls in DOCK_SEGMENTS:
        ax.add_patch(Rectangle((xa, ya), xb - xa, yb - ya, facecolor=CELL_COLOR[cls],
                                edgecolor="#52514e", linewidth=1.2, zorder=2))

    def doors(lock_x0, lock_x1, n):
        for i in range(n):
            door_x = lock_x0 + (lock_x1 - lock_x0) * i / (n - 1)
            ax.add_patch(Rectangle((door_x - DOCK_FLAP_W / 2, y0_l), DOCK_FLAP_W, H_LOCK,
                                    facecolor="white", edgecolor="#0b0b0b",
                                    linewidth=0.9, zorder=4))

    doors(LOCK_A_X0, LOCK_A_X1, 3)  # H2-ячейка <-> жилой: разные среды -- 3 створки
    doors(LOCK_B_X0, LOCK_B_X1, 2)  # жилой <-> производственный: общая среда -- 2 створки

    ax.annotate(T["fig7_h2"], (CELL_W / 2, y1_c + 8), ha="center", fontsize=8, color=MUTED)
    ax.annotate(T["fig7_o2"], ((LOCK_A_X1 + DOCK_X_FULL) / 2, y1_c + 8),
                ha="center", fontsize=8, color=MUTED)

    pad = 16
    ax.set_xlim(0 - pad, DOCK_X_FULL + pad)
    ax.set_ylim(y0_c - pad, y1_c + pad)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.patch.set_visible(False)  # иначе белый фон осей идёт в bbox_inches="tight"

    handles7 = [Line2D([0], [0], marker="s", linestyle="", markersize=9,
                        markerfacecolor=CELL_COLOR["cell-float"], markeredgecolor="#52514e",
                        label=labels["cell-float"]),
                Line2D([0], [0], marker="s", linestyle="", markersize=9,
                       markerfacecolor=CELL_COLOR["cell-airlock"], markeredgecolor="#52514e",
                       label=labels["cell-airlock"]),
                Line2D([0], [0], marker="s", linestyle="", markersize=9,
                       markerfacecolor="white", markeredgecolor="#0b0b0b",
                       label=T["fig7_leaf"])]
    for c in ("cell-habitat", "cell-production"):
        handles7.append(Line2D([0], [0], marker="s", linestyle="", markersize=9,
                                markerfacecolor=CELL_COLOR[c], markeredgecolor="#52514e",
                                label=labels[c]))
    ax.legend(handles=handles7, loc="upper center", bbox_to_anchor=(0.5, -0.05),
              ncol=5, frameon=False, fontsize=7.5, handletextpad=0.4,
              columnspacing=1.2)

    fig.suptitle(T["fig7_suptitle"], fontsize=10.5, x=0.5, ha="center")
    fig.tight_layout()
    save(fig, "airlock-docking", lang)


build("en")
build("ru")
print("ГОТОВО.")
