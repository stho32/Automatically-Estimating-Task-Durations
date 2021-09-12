def convert_to_seconds(column_name, row):
    """converts the value in the column to a value in seconds
    It will interpret the value as hours
    """
    value = float(row[column_name])*60*60
    return value

