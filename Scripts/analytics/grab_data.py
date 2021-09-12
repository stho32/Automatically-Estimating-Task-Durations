import pandas as pd
import analytics.conversions as conv

def grab_prepared_data(filename):
    df = pd.read_csv(filename)
    df['HoursSpent'] = df.apply (lambda row: conv.convert_to_hours("DurationInSeconds", row), axis=1)
    df['HoursEstimated'] = df.apply (lambda row: conv.convert_to_hours("EstimateInSeconds", row), axis=1)
    df['HoursDifference'] = df.apply (lambda row: conv.difference_between("HoursEstimated", "HoursSpent", row), axis=1)
    df = df.sort_values('HoursSpent')
    df['Task'] = range(1,len(df)+1)
    return df
