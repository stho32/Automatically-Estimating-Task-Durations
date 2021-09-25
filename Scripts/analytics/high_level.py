import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
import numpy as np
from sklearn.metrics import mean_squared_error

def create_image_boxplot(filename, df):
    boxdf = df.copy()
    boxdf=boxdf[boxdf.HoursSpent < boxdf.HoursSpent.quantile(.90)]

    fig = go.Figure()

    fig.add_box(y=boxdf["HoursSpent"], name="HoursSpent (INPUT)")
    fig.add_box(y=boxdf["HoursEstimated"], name="HoursEstimated (OUTPUT)")

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
    #fig.show()

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

    fig.write_image(filename + ".scatter.png", width=1200, height=700, scale=1)
    #fig.show()

def create_image_error_distribution(filename, df):
    mydf = df.copy()
    mydf['EstimationErrorInSeconds'] = mydf.apply (lambda row: row["EstimateInSeconds"] - row["DurationInSeconds"], axis=1)
    mydf['DurationInHours'] = mydf.apply (lambda row: row["DurationInSeconds"]/60/60, axis=1)
    mydf['DurationAsHour'] = mydf.apply (lambda row: round(row["DurationInSeconds"]/60/60,0), axis=1)
    mydf['EstimationErrorInHours'] = mydf.apply (lambda row: row["EstimateInSeconds"]/60/60, axis=1)

    result = list()

    for i in range(0,40):
        taskCount=len(mydf[mydf["DurationAsHour"]==i])
        mean = mydf[mydf["DurationAsHour"]==i]["EstimationErrorInHours"].mean()
        standard_deviation = mydf[mydf["DurationAsHour"]==i]["EstimationErrorInHours"].std()
        standard_deviation_minus = mean - standard_deviation
        standard_deviation_plus = mean + standard_deviation
        result.append(dict (
            task_duration_in_about_hours = i,
            taskCount = taskCount,
            mean = mean,
            standard_deviation = standard_deviation,
            standard_deviation_minus = standard_deviation_minus,
            standard_deviation_plus = standard_deviation_plus
        ))

    error_distribution = pd.DataFrame(result)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=error_distribution["task_duration_in_about_hours"], y=error_distribution["mean"], mode='lines',name='mean error'))
    fig.add_trace(go.Scatter(x=error_distribution["task_duration_in_about_hours"], y=error_distribution["standard_deviation_plus"], mode='lines',name='+'))
    fig.add_trace(go.Scatter(x=error_distribution["task_duration_in_about_hours"], y=error_distribution["standard_deviation_minus"], mode='lines',name='-'))

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

    fig.update(layout_yaxis_range = [-1,40])

    fig.write_image(filename + ".error_distribution.png", width=1200, height=700, scale=1)

def create_statistics(algorithm, trainingOn, estimating, parameters, filename, df):
    mean = df["HoursDifference"].mean()
    standard_deviation = df["HoursDifference"].std()
    mse = mean_squared_error(df["HoursSpent"], df["HoursEstimated"])

    if parameters == None:
        parameters = ""

    data = dict(
            algorithm          = algorithm,
            trainingOn         = trainingOn,
            estimating         = estimating,
            parameters         = parameters,
            mean               = mean,
            standard_deviation = standard_deviation,
            mse                = mse
        )

    with open(filename + ".json", 'w') as outfile:
        json.dump(data, outfile)

    print("    mean:", mean)
    print("    std:", standard_deviation)
    print("    mse:", mse)

