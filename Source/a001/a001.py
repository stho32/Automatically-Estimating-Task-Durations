"""Implementation of estimation algorithm A001

learn the contents of an csv file:

    a001.py --learn --input input.csv --output model.json

estimate 1 task:

    a001.py --estimate --text "hello world" --model model.json --probabilityInPercent 80

estimate a csv file full of tasks (for algorithm validation purposes):

    a001.py --validation --input input.csv --output output.csv --model model.json --probabilityInPercent 80

"""

import argparse
import pandas as pd
import tools.conversions as conv
import tools.load_and_save as las
import json
import re
import random

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("--learn", action="store_true", help="learn from a csv file, write a model")
group.add_argument("--estimate", action="store_true", help="estimate one task described by the parameters")
group.add_argument("--validation", action="store_true", help="read a csv file and estimate all contained tasks, write an output that contains the input data and the new estimate, used for alorithm validation")

parser.add_argument("--input", type=str, help="the path to the input csv file for learning and validation")
parser.add_argument("--output", type=str, help="write the results of the execution to that file")
parser.add_argument("--model", type=str, help="path to the model.json file which has been created by the learn option")

parser.add_argument("--probabilityInPercent", type=int, help="probability/certainty of task completion (higher values estimate higher)")

args = parser.parse_args()

def splitToWords(value):
    words = re.split('[ :\(\)\.\?/]',value)
    words = list(filter(lambda x: len(x)>0, words))
    return words

def allWordsOf(listOfStrings):
    result = set()
    for value in listOfStrings:
        words = splitToWords(value)
        result.update(words)
    return result

def algorithm(toEstimate, model, probabilityInPercent):
    """the algorithm that performs the estimation"""

    words = splitToWords(toEstimate)
    
    sum_duration_in_seconds = 0

    for word in words:
        if word in model:
            randomSamples = list()
            for i in range(1,100):
                sample = random.choice(model[word])
                randomSamples.append(sample)
            randomSamples.sort()
            duration_in_seconds = randomSamples[probabilityInPercent]
            print("- found historic duration information for " + word + " : " + str(duration_in_seconds))
            sum_duration_in_seconds += duration_in_seconds

    return sum_duration_in_seconds

if args.learn:
    """learn from csv"""
    print ("Algorithm is learning from the presented data... one moment please")
    df = las.load_csv(args.input)

    word_values = dict()

    for index, row in df.iterrows():
        words = splitToWords(row["Name"])
        duration_per_word = row["DurationInSeconds"] / len(words)
        for word in words:
            if not word in word_values:
                word_values[word] = list()

            print("remember " + word + " as " + str(duration_per_word) + " seconds")
            word_values[word].append(duration_per_word)

    las.save_json(args.output, word_values)


if args.estimate:
    """estimate a new task"""
    
    model = las.load_json(args.model)
    print (algorithm(args.input, model, args.probabilityInPercent))

if args.validation:
    """estimate a bunch of tasks to validate algorithm"""
    print ("Estimating all tasks in " + args.input)
    model = las.load_json(args.model)
    tasksToEstimate = las.load_csv(args.input)
    tasksToEstimate["EstimateInSeconds"] = tasksToEstimate.apply(lambda row: algorithm(row["Name"], model, args.probabilityInPercent), axis=1)
    las.save_csv(args.output, tasksToEstimate)



