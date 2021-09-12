import glob
import json
import tabulate

def load_json_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        print(data)
        return data

files = glob.glob("./output/*.png") 
files = sorted(files)

result = ""

for f in files:
    f = f.replace("./output", "Scripts/output")
    result += "\\includegraphics[width=\\textwidth]{" + f + "}\n"

with open("./output/summary-graphs.tex", "w") as summaryfile:
    summaryfile.write(result)
