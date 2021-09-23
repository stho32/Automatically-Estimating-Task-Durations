"""
    Depending on the configuration we need to flexibly
    build a lot of different combinations for each algorithm
    so we can create a test matrix more easily
"""
import os

def derive_model_combinations(model_template, algorithm_definition):
    """
        A model can have two formats:
        1. "model" : "./a001_model.json" : the result is simply one option with one possibility
        2. "model": "./a002_2_@@parameter@@_model.json"

        In the second case the template describes n models.
        In this case all learn and estimate command lines are cross-joined/matrix-multiplied
        by the possible combinations for the model.
    """
    result = list()
    
    # when the model_template is using the parameter definitions
    # then we multiply our model_template by all variants of the parameter
    if "@@parameter@@" in model_template:
        for parameter in algorithm_definition["parameters"]:
            template = model_template
            template = template.replace("@@parameter@@", parameter["filenameext"])
            result.append(template)
    else:
        # otherwise we return just one version
        result.append(model_template)

    return result


def derive_execution_combinations(algorithm_definition, datacombination, output_template, data_root_dir):
    """
        When an algorithm uses parameters, they are applied to either the learning,
        the execution, or both (e.g. by changing the model name for each combination).

        This means, all executions come in pairs: learning + estimating
        They may be multiplied by the parameters.
    """

    result = list()
    # when the commandline is using the parameter definitions
    # then we multiply our output by all variants of the parameter
    algorithm_has_parameters = len(algorithm_definition["parameters"]) > 0
    commands_to_complete = [algorithm_definition["learn"], algorithm_definition["estimate"]]

    if algorithm_has_parameters:
        for parameter in algorithm_definition["parameters"]:
            for command in commands_to_complete:
                result.append(complete_command(command, algorithm_definition, datacombination, parameter, output_template, data_root_dir))
    else:
        for command in commands_to_complete:
            result.append(complete_command(command, algorithm_definition, datacombination, None, output_template, data_root_dir))
    
    return result
        

def complete_command(command, algorithm_definition, datacombination, parameter, output_template, data_root_dir):
    """
        This function replaces all placeholders in one command
        using one data combination and one parameter.
    """
    result = command

    if "model" in algorithm_definition:
        result = result.replace("@@model@@", algorithm_definition["model"])
    if not parameter == None:
        if "model" in parameter:
            result = result.replace("@@model@@", parameter["model"])
        result = result.replace("@@parameter@@", parameter["value"])

    result = result.replace("@@trainOn@@", os.path.join(data_root_dir, datacombination["trainOn"]))
    result = result.replace("@@estimate@@", os.path.join(data_root_dir, datacombination["estimate"]))

    output = output_template
    output = output.replace("@@trainOn@@", datacombination["trainOn"])
    output = output.replace("@@estimate@@", datacombination["estimate"])
    if parameter != None:
        output = output.replace("@@filenameext@@", parameter["filenameext"])
    else:
        output = output.replace("@@filenameext@@", "")
    output = output.replace(".csv", "")
    output = output + ".csv"

    result = result.replace("@@output@@", output)

    return result