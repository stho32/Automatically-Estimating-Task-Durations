#!/bin/bash

rm a003_1_model.json

python3 ../Source/a003_1/a003_1.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a003_1_model.json

#python3 ../Source/a003_1/a003_1.py --estimate --input "Ticketsystem: neuer Antrag für Ingo" --model ./a003_1_model.json

python3 ../Source/a003_1/a003_1.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A003_1_swearchiv2020_swearchiv2020.csv --model ./a003_1_model.json

python3 ../Source/a003_1/a003_1.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A003_1_swearchiv2020_swearchiv2021.csv --model ./a003_1_model.json

