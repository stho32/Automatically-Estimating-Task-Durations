#!/usr/bin/python3

import pandas as pd
import analytics.grab_data as gd
import analytics.high_level as hl

def analyse(algorithm, trainingOn, estimating, parameters, filename):
    print("  - " + filename)
    df = gd.grab_prepared_data(filename)
    hl.create_image_boxplot(filename, df)
    hl.create_statistics(algorithm, trainingOn, estimating, parameters, filename, df)


analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '25%P', './output/A001_swearchiv2020_swearchiv2020_025.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '50%P', './output/A001_swearchiv2020_swearchiv2020_050.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '75%P', './output/A001_swearchiv2020_swearchiv2020_075.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '80%P', './output/A001_swearchiv2020_swearchiv2020_080.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '90%P', './output/A001_swearchiv2020_swearchiv2020_090.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2020', '100%P', './output/A001_swearchiv2020_swearchiv2020_100.csv')

analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '25%P', './output/A001_swearchiv2020_swearchiv2021_025.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '50%P', './output/A001_swearchiv2020_swearchiv2021_050.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '75%P', './output/A001_swearchiv2020_swearchiv2021_075.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '80%P', './output/A001_swearchiv2020_swearchiv2021_080.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '90%P', './output/A001_swearchiv2020_swearchiv2021_090.csv')
analyse('A001', 'SWEArchiv2020', 'SWEArchiv2021', '100%P', './output/A001_swearchiv2020_swearchiv2021_100.csv')

analyse('A002_1', 'SWEArchiv2020', 'SWEArchiv2020', '', './output/A002_1_swearchiv2020_swearchiv2020.csv')
analyse('A002_1', 'SWEArchiv2020', 'SWEArchiv2021', '', './output/A002_1_swearchiv2020_swearchiv2021.csv')

analyse('A002_2', 'SWEArchiv2020', 'SWEArchiv2020', 'L95%M', './output/A002_2_swearchiv2020_swearchiv2020_095.csv')
analyse('A002_2', 'SWEArchiv2020', 'SWEArchiv2021', 'L95%M', './output/A002_2_swearchiv2020_swearchiv2021_095.csv')

analyse('A002_2', 'SWEArchiv2020', 'SWEArchiv2020', 'L85%M', './output/A002_2_swearchiv2020_swearchiv2020_085.csv')
analyse('A002_2', 'SWEArchiv2020', 'SWEArchiv2021', 'L85%M', './output/A002_2_swearchiv2020_swearchiv2021_085.csv')

analyse('A002_2', 'SWEArchiv2020', 'SWEArchiv2020', 'L75%M', './output/A002_2_swearchiv2020_swearchiv2020_075.csv')
analyse('A002_2', 'SWEArchiv2020', 'SWEArchiv2021', 'L75%M', './output/A002_2_swearchiv2020_swearchiv2021_075.csv')








