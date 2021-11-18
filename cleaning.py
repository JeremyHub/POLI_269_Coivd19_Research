import pandas as pd
import numpy as np

data_file_name = 'data.csv'
labels_file_name = 'what_answer_codes_mean.csv'
questions_file_name = 'what_questsions_are.csv'

data = pd.read_csv(data_file_name)
labels = pd.read_csv(labels_file_name)
questions = pd.read_csv(questions_file_name)

# remove data where country is Nan
data = data[data['Residency'] != 'Nan']

# remove data in what_questions_are where "question" is not a string
questions = questions[questions['question'] == questions['question'].astype(str)]
# get and remove the question data where [var] is NA
group_header_statements = questions[questions['row_id'] == 0]
questions = questions[questions['row_id'] != 0]

# get unique countries
countries = data['Residency'].unique()
# get unique questions
unique_questions = data['var'].unique()
# get unique questions in the data

# new dataframe:
# - one row per country
# - one column per question
# rows should be countries
# columns should be questions(vars)
# vaules will be lists of answers(codes)

# for each question there in "what_question_are" they are part of a group
# the first answer in the group is the intro statement


country_dict = {}

for index, row in data.iterrows():
    country_dict[row['Residency']] = country_dict.get(row['Residency'], {})
    country_dict[row['Residency']][row['var']] = country_dict[row['Residency']].get(row['var'], [])
    country_dict[row['Residency']][row['DemGen']] = country_dict[row['Residency']].get(row['DemGen'], [])
    country_dict[row['Residency']][row['quota_age']] = country_dict[row['Residency']].get(row['quota_age'], [])
    country_dict[row['Residency']][row['var']].append(row['code'])
    country_dict[row['Residency']][row['DemGen']].append(row['DemGen'])
    country_dict[row['Residency']][row['quota_age']].append(row['quota_age'])

df = pd.DataFrame.from_dict(country_dict, orient='index')
# remove columns where the column name is NaN
df = df.dropna(axis=1, how='all')
print(df)
df.to_json('cleaned_data.json', orient='columns')
