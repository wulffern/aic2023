#!/usr/bin/env bash


rm images.txt
cp syllabus.md docs/syllabus.md
cp plan.md docs/plan.md
python3 py/lecture.py post --date 2021-07-08 memos/2021-07-08_diodes/memo.md
python3 py/lecture.py post --date 2022-12-03 lectures/l00_my_thoughts.md
#python3 py/lecture.py post --date 2022-12-13 lectures/l00_analog_paradigm.md
python3 py/lecture.py post --date 2023-01-01 lectures/l01_need_to_know.md
python3 py/lecture.py post --date 2023-01-02 lectures/l01_ad.md
python3 py/lecture.py post --date 2023-01-12 lectures/l01_intro.md
python3 py/lecture.py post --date 2023-01-19 lectures/l02_esd.md
python3 py/lecture.py post --date 2023-01-26 lectures/l03_refbias.md
python3 py/lecture.py post --date 2023-02-02 lectures/l04_afe.md
python3 py/lecture.py post --date 2023-02-09 lectures/l05_sc.md
python3 py/lecture.py post --date 2023-02-16 lectures/l06_adc.md
python3 py/lecture.py post --date 2023-03-09 lectures/l07_vreg.md
python3 py/lecture.py post --date 2023-03-16 lectures/l08_pll.md
python3 py/lecture.py post --date 2023-03-23 lectures/l09_osc.md
python3 py/lecture.py post --date 2023-03-30 lectures/l10_lpradio.md
python3 py/lecture.py post --date 2023-04-20 lectures/lx_energysrc.md
