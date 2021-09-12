#!/usr/bin/python3

import pandas as pd
import analytics.grab_data as gd
import analytics.high_level as hl

def analyse(algorithm, trainingOn, estimating, parameters, filename):
    print("  - " + filename)
    df = gd.grab_prepared_data(filename)
    hl.create_image_boxplot(filename, df)
    hl.create_statistics(algorithm, trainingOn, estimating, parameters, filename, df)


analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '25%P', './output/A001_swearchiv2020_swearchiv2020_25.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '50%P', './output/A001_swearchiv2020_swearchiv2020_50.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '75%P', './output/A001_swearchiv2020_swearchiv2020_75.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '80%P', './output/A001_swearchiv2020_swearchiv2020_80.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '90%P', './output/A001_swearchiv2020_swearchiv2020_90.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '100%P', './output/A001_swearchiv2020_swearchiv2020_100.csv')

analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '25%P', './output/A001_swearchiv2020_swearchiv2021_25.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '50%P', './output/A001_swearchiv2020_swearchiv2021_50.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '75%P', './output/A001_swearchiv2020_swearchiv2021_75.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '80%P', './output/A001_swearchiv2020_swearchiv2021_80.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '90%P', './output/A001_swearchiv2020_swearchiv2021_90.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '100%P', './output/A001_swearchiv2020_swearchiv2021_100.csv')
