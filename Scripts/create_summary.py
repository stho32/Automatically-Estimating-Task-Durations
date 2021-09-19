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

resulttable = []

for f in files:
    print(f)
    filecontent = load_json_data(f)
    resulttable.append([
        filecontent["algorithm"].replace("_", "\\_"),
        filecontent["trainingOn"],
        filecontent["estimating"],
        filecontent["parameters"].replace("%", "\\%"),
        "{:.3f}".format(filecontent["mean"]) + ' $\pm$ ' + "{:.3f}".format(filecontent["standard_deviation"]) + ' hours',
        "{:.3f}".format(filecontent["mse"])
        ])

with open("./output/summary-table.tex", "w") as summaryfile:
    summaryfile.write(tabulate.tabulate(
        resulttable, 
        headers = ["Algorithm", "Training on", "Estimating", "with params", "deviation", "mse"],
        tablefmt="latex_raw",
        colalign=("left", "left", "left", "right", "right", "right")
        ).replace("tabular", "longtable"))
