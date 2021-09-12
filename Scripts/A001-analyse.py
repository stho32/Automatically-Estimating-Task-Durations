#!/usr/bin/python3

import pandas as pd
import analytics.grab_data as gd
import analytics.high_level as hl

def analyse(filename):
    print("  - " + filename)
    df = gd.grab_prepared_data(filename)
    hl.create_image_boxplot(filename, df)
    hl.create_statistics(filename, df)


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
