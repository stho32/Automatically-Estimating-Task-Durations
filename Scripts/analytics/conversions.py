def convert_to_hours(columnName, row):    
    if row[columnName] == 0:    
        return 0.0    
    numberAsString = row[columnName].replace(",", ".")    
    number = float(numberAsString)    
    hours = number / 60 / 60    
    return hours

def difference_between(columnNameA, columnNameB, row):    
    return row[columnNameA] - row[columnNameB];


