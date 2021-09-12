#!/usr/bin/python3

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json

def convert_to_hours(columnName, row):
    if row[columnName] == 0:
        return 0.0
    numberAsString = row[columnName].replace(",", ".")
    number = float(numberAsString)
    hours = number / 60 / 60
    return hours

def difference_between(columnNameA, columnNameB, row):
    return row[columnNameA] - row[columnNameB];

def grab_prepared_data(filename):
    df = pd.read_csv(filename)
    
    df['HoursSpent'] = df.apply (lambda row: convert_to_hours("DurationInSeconds", row), axis=1)
    df['HoursEstimated'] = df.apply (lambda row: convert_to_hours("EstimateInSeconds", row), axis=1)
    df['HoursDifference'] = df.apply (lambda row: difference_between("HoursEstimated", "HoursSpent", row), axis=1)

    df = df.sort_values('HoursSpent')
    df['Task'] = range(1,len(df)+1)
    return df

def create_image(filename):
    df = grab_prepared_data(filename)

    fig = go.Figure() 

    fig.add_scatter(y=df["HoursSpent"], x=df["Task"], name="Hours spent")
    fig.add_scatter(x=df["Task"], y=df["HoursEstimated"], mode="markers", name="Hours estimated")

    fig.update_layout(
        title = filename,
        plot_bgcolor='rgb(230, 230,230)',
        showlegend=True)

    fig.update_layout(
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))

    fig.update_traces(marker_size=5)

    fig.write_image(filename + ".png", width=1200, height=700, scale=1)
    #fig.show()

def create_statistics(filename):
    df = grab_prepared_data(filename)
    
    mean = df["HoursDifference"].mean()
    standard_deviation = df["HoursDifference"].std()

    data = dict(
            mean=mean,
            standard_deviation=standard_deviation
        )

    with open(filename + ".json", 'w') as outfile:
        json.dump(data, outfile)

    print("    mean:", mean)
    print("    std:", standard_deviation)


def analyse(filename):
    print("  - " + filename)
    create_image(filename)
    create_statistics(filename)


analyse('./output/A001_swearchiv2020_swearchiv2020_25.csv')
analyse('./output/A001_swearchiv2020_swearchiv2020_50.csv')
analyse('./output/A001_swearchiv2020_swearchiv2020_75.csv')
analyse('./output/A001_swearchiv2020_swearchiv2020_80.csv')
analyse('./output/A001_swearchiv2020_swearchiv2020_90.csv')
analyse('./output/A001_swearchiv2020_swearchiv2020_100.csv')

analyse('./output/A001_swearchiv2020_swearchiv2021_25.csv')
analyse('./output/A001_swearchiv2020_swearchiv2021_50.csv')
analyse('./output/A001_swearchiv2020_swearchiv2021_75.csv')
analyse('./output/A001_swearchiv2020_swearchiv2021_80.csv')
analyse('./output/A001_swearchiv2020_swearchiv2021_90.csv')
analyse('./output/A001_swearchiv2020_swearchiv2021_100.csv')
