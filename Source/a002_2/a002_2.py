"""Implementation of estimation algorithm A002_2

The goal of this algorithm is to provide "simply an average".

learn the contents of an csv file:

    a002_2.py --learn --input input.csv --output model.json

estimate 1 task:

    a002_2.py --estimate --text "hello world" --model model.json

estimate a csv file full of tasks (for algorithm validation purposes):

    a002_2.py --validation --input input.csv --output output.csv --model model.json

"""

import argparse
import pandas as pd
import tools.conversions as conv
import tools.load_and_save as las
import json

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("--learn", action="store_true", help="learn from a csv file, write a model")
group.add_argument("--estimate", action="store_true", help="estimate one task described by the parameters")
group.add_argument("--validation", action="store_true", help="read a csv file and estimate all contained tasks, write an output that contains the input data and the new estimate, used for alorithm validation")

parser.add_argument("--input", type=str, help="the path to the input csv file for learning and validation")
parser.add_argument("--output", type=str, help="write the results of the execution to that file")
parser.add_argument("--model", type=str, help="path to the model.json file which has been created by the learn option")
parser.add_argument("--middlepercent", type=int, help="learn from the middle percent percent of the data")

parser.add_argument("--verbose", action="store_true", help="verbose output")

args = parser.parse_args()

def verbose(value):
    if args.verbose:
        print(value)

def algorithm(toEstimate, model):
    """the algorithm that performs the estimation"""
    return model["mean"]

if args.learn:
    """learn from csv"""
    verbose ("Algorithm is learning from " + str(args.middlepercent) + " middle % of presented data... one moment please")
    df = las.load_csv(args.input)

    count = len(df.index) # this is how many entries there are
    margin = int(round(count*1.0*args.middlepercent/100.0)/2)

    df = df[margin:(count-margin)] # remove extreme points

    mean = df.DurationInSeconds.mean()
    las.save_json(args.output, dict(mean = mean))

    verbose ("learned that the mean of the middle " + str(args.middlepercent) + "% is:" + str(mean)) 

if args.estimate:
    """estimate a new task"""
    
    model = las.load_json(args.model)
    
    verbose (model["mean"])

if args.validation:
    """estimate a bunch of tasks to validate algorithm"""
    verbose ("Estimating all tasks in " + args.input)
    model = las.load_json(args.model)
    tasksToEstimate = las.load_csv(args.input)
    tasksToEstimate["EstimateInSeconds"] = tasksToEstimate.apply(lambda row: algorithm(row["Name"], model), axis=1)
    las.save_csv(args.output, tasksToEstimate)



