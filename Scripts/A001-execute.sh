#!/bin/bash

rm a001*_model.json

python3 ../Source/a001/a001.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a001_model.json

#python3 ../Source/a003_1/a003_1.py --estimate --input "Ticketsystem: neuer Antrag für Ingo" --model ./a003_1_model.json

python3 ../Source/a001/a001.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A001_swearchiv2020_swearchiv2020_025.csv --model ./a001_model.json --probabilityInPercent 25


