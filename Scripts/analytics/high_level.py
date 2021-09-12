import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
import numpy as np

def create_image_boxplot(filename, df):
    boxdf = df.copy()
    boxdf=boxdf[boxdf.HoursSpent < boxdf.HoursSpent.quantile(.90)]

    fig = go.Figure()

    fig.add_box(y=boxdf["HoursSpent"], name="HoursSpent")
    fig.add_box(y=boxdf["HoursEstimated"], name="HoursEstimated")

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

    fig.write_image(filename + ".png", width=1200, height=700, scale=1)
    fig.show()

def create_image_scatterHours(filename, df):
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

def create_statistics(filename, df):
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

