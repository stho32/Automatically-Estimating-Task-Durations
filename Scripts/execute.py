#!/usr/bin/python3
"""
    This script executes all algorithms against their configured data combinations
    using the configured parameters.
"""
from genericpath import exists
import analytics.grab_data
import analytics.exec_combinations as ec
import os
import pandas as pd
import analytics.high_level as hl

def analyse(algorithm, trainingOn, estimating, parameter, filename):
    """
        Execute analysis
    """
    print("   analysing the result - " + filename + "...")
    
    df = analytics.grab_data.grab_prepared_data(filename)

    hl.create_image_scatterHours(filename, df)
    hl.create_image_boxplot(filename, df)
    hl.create_statistics(algorithm, trainingOn, estimating, parameter, filename, df)

def execute_combination(algorithm_definition, commandline):
    """
        Execute combination
        Should there be an output generated, then we start the analysis
    """
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

            # If an output is defined we check if there is a file like that 
            # already on the disk. If it is we do not need to repeat the execution
            # and analysis - unless it is explicitly requested.
            # This way we save time when developing new algorithms.
            if not commandline["output"] == None:
                if (os.path.exists(commandline["output"])):
                    # ... and the repeat is not requested
                    if algorithm_definition["force_run"]:
                        execute_combination(algorithm_definition, commandline)
                    else:
                        print("      -> execution not needed, output already there")
                else:
                    execute_combination(algorithm_definition, commandline)

