"""Implementation of estimation algorithm A003_1

we categorize:
    class 1: tasks below half an hour
    class 2: tasks above half an hour and below 1 hour
    class 3: tasks ... and below 2 hours
    class 4: tasks ... and below 3 hours
    class 5: tasks ... and below 4 hours
    class 6: tasks ... and below 5 hours
    class 7: tasks ... and below 6 hours
    class 8: tasks ... and below 7 hours
    class 9: tasks ... and below 8 hours
    class 10: tasks above 8 hours

learn the contents of an csv file:

    a003_1.py --learn --input input.csv --output model.json

estimate 1 task:

    a003_1.py --estimate --text "hello world" --model model.json

estimate a csv file full of tasks (for algorithm validation purposes):

    a003_1.py --validation --input input.csv --output output.csv --model model.json

"""

import argparse
import pandas as pd
import tools.conversions as conv
import tools.load_and_save as las
import json
import re

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("--learn", action="store_true", help="learn from a csv file, write a model")
group.add_argument("--estimate", action="store_true", help="estimate one task described by the parameters")
group.add_argument("--validation", action="store_true", help="read a csv file and estimate all contained tasks, write an output that contains the input data and the new estimate, used for alorithm validation")

parser.add_argument("--input", type=str, help="the path to the input csv file for learning and validation")
parser.add_argument("--output", type=str, help="write the results of the execution to that file")
parser.add_argument("--model", type=str, help="path to the model.json file which has been created by the learn option")

args = parser.parse_args()

def categorizeTasksByTimeSpent(durationInSeconds):
    durationInHours = durationInSeconds / 60 / 60  
    if durationInHours < 0.5:
        return 1
    if durationInHours < 1:
        return 2
    if durationInHours < 2:
        return 3
    if durationInHours < 3:
        return 4
    if durationInHours < 4:
        return 5
    if durationInHours < 5:
        return 6
    if durationInHours < 6:
        return 7
    if durationInHours < 7:
        return 8
    if durationInHours < 8:
        return 9
    return 10

def splitToWords(value):
    return re.split('[ :\(\)\.\?/]',value)

def allWordsOf(listOfStrings):
    result = set()
    for value in listOfStrings:
        words = splitToWords(value)
        result.update(words)
    return result

def algorithm(toEstimate, model):
    """the algorithm that performs the estimation"""

    words = splitToWords(toEstimate)
    
    highest_category = 0
    average_duration_of_that_category = 0
    for category in model:
        for word in words:
            if ((word in category["words"]) and (category["category"] > highest_category)):
                print("found " + word + " in category " + str(category["category"]))
                highest_category = category["category"]
                average_duration_of_that_category = category["avg_duration_in_seconds"]

    return average_duration_of_that_category

if args.learn:
    """learn from csv"""
    print ("Algorithm is learning from the presented data... one moment please")
    df = las.load_csv(args.input)
    df["Category"] = df.apply (lambda row: categorizeTasksByTimeSpent(row["DurationInSeconds"]), axis = 1)

    information_per_category = []

    for category in range(1,11):
        in_this_category = df[df["Category"]==category]
        the_other_categories = df[df["Category"]!=category]

        specific_words = set()
        specific_words = allWordsOf(in_this_category["Name"])
        unspecific_words = allWordsOf(the_other_categories["Name"])
        specific_words.difference_update(unspecific_words)
        print("category " + str(category) + " has " + str(len(specific_words)))

        information_per_category.append(
            dict(
                category = category,
                words = list(specific_words), 
                task_count = len(in_this_category),
                avg_duration_in_seconds = in_this_category["DurationInSeconds"].mean()
            ))

    las.save_json(args.output, information_per_category)


if args.estimate:
    """estimate a new task"""
    
    model = las.load_json(args.model)
    print (algorithm(args.input, model))

if args.validation:
    """estimate a bunch of tasks to validate algorithm"""
    print ("Estimating all tasks in " + args.input)
    model = las.load_json(args.model)
    tasksToEstimate = las.load_csv(args.input)
    tasksToEstimate["EstimateInSeconds"] = tasksToEstimate.apply(lambda row: algorithm(row["Name"], model), axis=1)
    las.save_csv(args.output, tasksToEstimate)



