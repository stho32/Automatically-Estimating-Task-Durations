"""Implementation of estimation algorithm A007

learn the contents of an csv file:

    a007.py --learn --input input.csv --output model.json

estimate 1 task:

    a007.py --estimate --text "hello world" --model model.json 

start the "testing environment":
    a007.py --test --model model.json

estimate a csv file full of tasks (for algorithm validation purposes):

    a007.py --validation --input input.csv --output output.csv --model model.json 

use --verbose in case you want to see some output
"""

import argparse
import pandas as pd
import tools.conversions as conv
import tools.load_and_save as las
import json
import re
import random
import statistics
import os
import uuid

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("--learn", action="store_true", help="learn from a csv file, write a model")
group.add_argument("--estimate", action="store_true", help="estimate one task described by the parameters")
group.add_argument("--validation", action="store_true", help="read a csv file and estimate all contained tasks, write an output that contains the input data and the new estimate, used for alorithm validation")
group.add_argument("--test", action="store_true", help="test environment")

parser.add_argument("--input", type=str, help="the path to the input csv file for learning and validation")
parser.add_argument("--output", type=str, help="write the results of the execution to that file")
parser.add_argument("--model", type=str, help="path to the model.json file which has been created by the learn option")
parser.add_argument("--top", type=int, help="use top n search results for the average in the estimation")

parser.add_argument("--verbose", action="store_true", help="more output")

args = parser.parse_args()

def verbose(value):
    """
        Print to screen in case verbose is set
    """
    if (args.verbose):
        print(value)

def splitToWords(value):
    """
        Use a regular expression to split the given string into
        acceptable "words".
    """
    words = re.split('[ :\(\)\.\?/]',value)
    words = list(filter(lambda x: len(x)>0, words))
    return words

def allWordsOf(listOfStrings):
    """
        Creates a set of words in wich all words
        that can be collected from the list of given strings
        are represented exactly once.
    """
    result = set()
    for value in listOfStrings:
        words = splitToWords(value)
        result.update(words)
    return result

def add_document_for_estimation(document, word, relevant_documents):
    """
        we need to transform the given information to 
        a new representation so we can tell the user
        very specifically why a task is seen as relevant
        for the estimation request
    """
    key = document["document"]["text"]

    if not key in relevant_documents:
        verbose("The document " + key + " was noted as relevant.")
        relevant_documents[key] = dict()
        relevant_documents[key]["words"] = list()
        relevant_documents[key]["duration_in_seconds"] = document["document"]["durationInSeconds"]

    verbose("  -> " + word + " found in " + key)
    relevant_documents[key]["words"].append(
        dict(
            word = word,
            relevance_for_the_document = document["relevanceForTheDocument"]
        )
    )

def sum_relevance(document):
    sum = 0
    for word in document["words"]:
        sum += word["relevance_for_the_document"]
    return sum

def get_total_relevance(obj):
    return obj["total_relevance"]

def algorithm(toEstimate, model):
    """
        the algorithm that performs the estimation
    """
    words = splitToWords(toEstimate)
    
    relevant_documents = dict()

    for word in words:
        if word in model:
            for document in model[word]["documents"]:
                add_document_for_estimation(document, word, relevant_documents)

    next_level = list()

    for document in relevant_documents:
        next_level.append(dict(
            text = document,
            duration_in_seconds = relevant_documents[document]["duration_in_seconds"],
            total_relevance = sum_relevance(relevant_documents[document])
        ))

    next_level.sort(key=get_total_relevance, reverse=True)

    count = 0
    sum = 0
    # Top n hits
    for i in range(0, min(len(next_level), args.top)):
        print(next_level[i])
        count += 1
        sum += next_level[i]["duration_in_seconds"]

    if count > 0:
        return (sum/count)
    return 0


def add_document_to_index(indexEntryForWord, documentContent, word, words):
    """
        Since we think that we will not process a document more than one
        time this function just has the task to calculate the word relevance
        for the words given and save them with the documentContent as reference.
    """
    relevanceForTheDocument = words.count(word) / len(words) 
    indexEntryForWord["documents"].append(
        dict(
            document = documentContent,
            relevanceForTheDocument = relevanceForTheDocument
        )
    )

if args.learn:
    """
        learn from csv
    """
    verbose("Algorithm is learning from the presented data... one moment please")
    df = las.load_csv(args.input)
    df['Name'] = df.apply (lambda row: row["Name"] + " " + str(uuid.uuid4()), axis=1)

    searchindex = dict()

    for index, row in df.iterrows():
        words = splitToWords(row["Name"])
        for word in words:
            if not word in searchindex:
                verbose("  - found new word " + word)
                searchindex[word] = dict()
                searchindex[word]["documents"] = list()
                 
            add_document_to_index(searchindex[word], 
                dict(
                    text = row["Name"], 
                    durationInSeconds = row["DurationInSeconds"]
                ),
            word, words)
    
    las.save_json(args.output, searchindex)

if args.test:
    """
        just a loop so you can start the application once
        and test estimating out
    """

    model = las.load_json(args.model)

    while 1==1:
        os.system('clear')
        print("What do you wish to estimate (empty to stop): ")
        testInput = input()
        if testInput == "":
            break
        resultInSeconds = algorithm(testInput, model)
        print("I estimate: " + str(resultInSeconds) + " seconds.")
        print("That is " + str((round(resultInSeconds/60/60, 2))) + " in hours.")
        input()

if args.estimate:
    """estimate a new task"""
    
    model = las.load_json(args.model)
    print (algorithm(args.input, model))

if args.validation:
    """estimate a bunch of tasks to validate algorithm"""
    verbose ("Estimating all tasks in " + args.input)
    model = las.load_json(args.model)
    tasksToEstimate = las.load_csv(args.input)
    tasksToEstimate["EstimateInSeconds"] = tasksToEstimate.apply(lambda row: algorithm(row["Name"], model), axis=1)
    las.save_csv(args.output, tasksToEstimate)



