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
python3 py/lecture.py post --date 2023-02-04 lectures/l04_afe.md


#- Slides
test -d slides || mkdir slides; 
test -d docs/assets/slides || mkdir docs/assets/slides;
python3 py/lecture.py slide lectures/l01_intro.md
python3 py/lecture.py slide lectures/l02_esd.md
python3 py/lecture.py slide lectures/l03_refbias.md
python3 py/lecture.py slide lectures/l04_afe.md
