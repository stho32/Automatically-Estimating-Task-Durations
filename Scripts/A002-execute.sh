#!/bin/bash

rm a002_1_model.json

python3 ../Source/a002_1/a002_1.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a002_1_model.json

#python3 ../Source/a002_1/a002_1.py --estimate --input "Ticketsystem: neuer Antrag für Ingo" --model ./a002_1_model.json

python3 ../Source/a002_1/a002_1.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A002_1_swearchiv2020_swearchiv2020.csv --model ./a002_1_model.json

python3 ../Source/a002_1/a002_1.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A002_1_swearchiv2020_swearchiv2021.csv --model ./a002_1_model.json


rm a002_2_model*.json

python3 ../Source/a002_2/a002_2.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a002_2_model_095.json --middlepercent 95

python3 ../Source/a002_2/a002_2.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a002_2_model_085.json --middlepercent 85

python3 ../Source/a002_2/a002_2.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a002_2_model_075.json --middlepercent 75

python3 ../Source/a002_2/a002_2.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a002_2_model_050.json --middlepercent 50

python3 ../Source/a002_2/a002_2.py --learn --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./a002_2_model_025.json --middlepercent 25

python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A002_2_swearchiv2020_swearchiv2020_095.csv --model ./a002_2_model_095.json

python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A002_2_swearchiv2020_swearchiv2021_095.csv --model ./a002_2_model_095.json


python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A002_2_swearchiv2020_swearchiv2020_085.csv --model ./a002_2_model_085.json

python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A002_2_swearchiv2020_swearchiv2021_085.csv --model ./a002_2_model_085.json


python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A002_2_swearchiv2020_swearchiv2020_075.csv --model ./a002_2_model_075.json

python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A002_2_swearchiv2020_swearchiv2021_075.csv --model ./a002_2_model_075.json


python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A002_2_swearchiv2020_swearchiv2020_050.csv --model ./a002_2_model_050.json

python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A002_2_swearchiv2020_swearchiv2021_050.csv --model ./a002_2_model_050.json


python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv --output ./output/A002_2_swearchiv2020_swearchiv2020_025.csv --model ./a002_2_model_025.json

python3 ../Source/a002_2/a002_2.py --validation --input ../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv --output ./output/A002_2_swearchiv2020_swearchiv2021_025.csv --model ./a002_2_model_025.json

