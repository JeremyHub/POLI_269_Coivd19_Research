import pandas as pd
import numpy as np

data_file_name = 'data.csv'
labels_file_name = 'what_answer_codes_mean.csv'
questions_file_name = 'what_questions_are.csv'

data = pd.read_csv(data_file_name)
print(data)

headings = pd.read_csv('headings.csv')
headings.dropna()
headings.dropna(subset=['txt_en'], inplace=True)
print(headings)

# new dataframe:
# rows should be countries
# columns should be questions(vars)
# vaules will be lists of answers(codes)