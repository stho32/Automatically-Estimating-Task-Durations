"""Tools for task estimation algorithms
"""
import pandas as pd
import tools.conversions as conv
import json

def load_csv(filename):
    df = pd.read_csv(filename)
    df.rename(columns={"Name": "Text"})
    df["DurationInSeconds"] = df.apply (lambda row: conv.convert_to_seconds("Time spent",     row), axis=1)
    return df

def save_csv(filename, dataframe):
    dataframe.to_csv(filename, index = False, header=True)

def save_json(filename, data):
    with open(filename, "w") as output:
        json.dump(data, output)

def load_json(filename):
    with open(filename) as inputfile:
        return json.load(inputfile)


