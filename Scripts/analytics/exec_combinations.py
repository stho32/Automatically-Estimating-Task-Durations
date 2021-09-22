"""
    Depending on the configuration we need to flexibly
    build a lot of different combinations for each algorithm
    so we can create a test matrix more easily
"""

def derive_execution_combinations(commandline, algorithm_definition, datacombination, output_template):
    result = list()
    # when the commandline is using the parameter definitions
    # then we multiply our output by all variants of the parameter
    if "@@parameter@@" in commandline:
        for parameter in algorithm_definition["parameters"]:
            template = commandline
            template = template.replace("@@parameter@@", parameter["value"])
            result.append(dict(
                template = template,
                parameter = parameter
            ))
    else:
        # otherwise we return just one version
        result.append(dict(
                template = commandline,
                parameter = None
            ))

    finalresult = list()
    for element in result:

        output = output_template
        output = output.replace("@@trainOn@@", datacombination["trainOn"])
        output = output.replace("@@estimate@@", datacombination["estimate"])
        if element["parameter"] != None:
            output = output.replace("@@filenameext@@", element["parameter"]["filenameext"])
        else:
            output = output.replace("@@filenameext@@", "")
        output = output.replace(".csv", "")
        output = output + ".csv"

        final_command = element["template"]
        final_command = final_command.replace("@@output@@", output)
        final_command = final_command.replace("@@model@@", algorithm_definition["model"])
        final_command = final_command.replace("@@trainOn@@", datacombination["trainOn"])
        final_command = final_command.replace("@@estimate@@", datacombination["estimate"])
        
        finalresult.append(final_command)

    return finalresult