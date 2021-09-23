#!/usr/bin/python3
"""
    This script executes all algorithms against their configured data combinations
    using the configured parameters.
"""
import analytics.grab_data
import analytics.exec_combinations as ec
import os
import pandas as pd
import analytics.high_level as hl

def analyse(algorithm, trainingOn, estimating, parameter, filename):
    print("   ANALYSE - " + filename + "...")
    
    df = analytics.grab_data.grab_prepared_data(filename)

    hl.create_image_scatterHours(filename, df)
    hl.create_image_boxplot(filename, df)
    hl.create_statistics(algorithm, trainingOn, estimating, parameter, filename, df)

os.system('cls' if os.name=='nt' else 'clear')

directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(directory)
print("I run in the following directory:")
os.system("pwd")
print("")

configuration = analytics.grab_data.load_json("./configuration.json")
data_root_dir = configuration["datarootdir"]
datacombinations = configuration["datacombinations"]
output_template = configuration["output_template"]

for algorithm_definition in configuration["algorithms"]:
    if not algorithm_definition["active"]:
        continue

    print("  - " + algorithm_definition["name"])
    for datacombination in datacombinations:
        executions = ec.derive_execution_combinations(algorithm_definition, datacombination, output_template, data_root_dir)

        for combination in executions:
            commandline = combination
            print("    - " + algorithm_definition["name"] + ": " + commandline["command"])

            if not os.system(commandline["command"]) == 0:
                print("There has been a problem. Stopping execution.")
                exit()

            if not commandline["output"] == None:
                analyse(
                    algorithm_definition["name"], 
                    commandline["trainOn"], 
                    commandline["estimate"], 
                    commandline["parameter"],
                    commandline["output"]
                )
