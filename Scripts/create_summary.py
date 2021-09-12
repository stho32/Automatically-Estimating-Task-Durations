import glob
import json
import tabulate

def load_json_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        print(data)
        return data

files = glob.glob("./output/*.json") 
files = sorted(files)

resulttable = [
        ["Algorithm", "Training on", "Estimating", "with params", "deviates by"]
    ]

for f in files:
    filecontent = load_json_data(f)
    resulttable.append([
        filecontent["algorithm"],
        filecontent["trainingOn"],
        filecontent["estimating"],
        filecontent["parameters"],
        "{:.3f}".format(filecontent["mean"]) + ' +/- ' + "{:.3f}".format(filecontent["standard_deviation"]) + ' hours'
        ])

with open("./output/summary-table.tex", "w") as summaryfile:
    summaryfile.write(tabulate.tabulate(resulttable, tablefmt="latex"))
