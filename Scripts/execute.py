#!/usr/bin/python3
"""
    This script executes all algorithms against their configured data combinations
    using the configured parameters.
"""
import analytics.grab_data
import analytics.exec_combinations as ec
import os

os.system('cls' if os.name=='nt' else 'clear')

directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(directory)
configuration = analytics.grab_data.load_json("./configuration.json")
data_root_dir = configuration["datarootdir"]
datacombinations = configuration["datacombinations"]
output_template = configuration["output_template"]

for algorithm_definition in configuration["algorithms"]:
    if not algorithm_definition["active"]:
        continue

    print("  - " + algorithm_definition["name"])
    for datacombination in datacombinations:
        learn = ec.derive_execution_combinations(algorithm_definition["learn"], algorithm_definition, datacombination, output_template)

        for combination in learn:
            print("    - " + combination)

        estimate = ec.derive_execution_combinations(algorithm_definition["estimate"], algorithm_definition, datacombination, output_template)

        for combination in estimate:
            print("    -> " + combination)
