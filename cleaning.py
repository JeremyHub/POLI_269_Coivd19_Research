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
print(type(questions))

# remove data in what_questions_are where "question" is not a string
questions = pd.DataFrame(questions[questions['question'] == questions['question'].astype(str)])
# print the question data in the fourth row from the "questions" clumn
print(questions)

# get unique countries
countries = data['Residency'].unique()

# get unique questions
questions = data['var'].unique()

# get unique groups
groups = questions['var_group'].unique()
print(groups)

# new dataframe:
# - one row per country
# - one column per question
# rows should be countries
# columns should be questions(vars)
# vaules will be lists of answers(codes)

# for each question there in "what_question_are" they are part of a group
# the first answer in the group is the intro statement

df = pd.DataFrame(columns=questions, index=countries)
print(df)