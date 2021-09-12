#!/usr/bin/python3

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy

def convert_to_hours(columnName, row):
    numberAsString = row[columnName].replace(",", ".")
    number = float(numberAsString)
    hours = number / 60 / 60
    #print("convert", numberAsString, "to", number, "=", hours, "h")
    return hours

def create_image(filename):
    df = pd.read_csv(filename)
    df['HoursSpent'] = df.apply (lambda row: convert_to_hours("DurationInSeconds", row), axis=1)
    df['HoursEstimated'] = df.apply (lambda row: convert_to_hours("EstimateInSeconds", row), axis=1)
    df = df.sort_values('HoursSpent')
    df['Task'] = range(1,len(df)+1)

    fig = px.scatter(df, y="HoursSpent", x="Task")
    fig.add_scatter(x=df["Task"], y=df["HoursEstimated"], mode="markers", name="Hours estimated")

    fig.update_layout(
        title='Hours spent per task and hours estimated (2020)',
        plot_bgcolor='rgb(230, 230,230)',
        showlegend=True)

    fig.update_traces(marker_size=5)
    #fig.update_xaxes(visible=False, showticklabels=False)

    fig.write_image(filename + ".png", width=1200, height=700, scale=1)
    fig.show()

def analyse(filename):
    create_image(filename)


analyse('./output/A001_swearchiv2020_swearchiv2020_25.csv');

