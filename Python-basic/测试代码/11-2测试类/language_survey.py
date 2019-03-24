#!/usr/bin/env python
# @Time : 2019/3/24 11:41 
__author__ = 'Boaz'

from survey import AnoymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymouSurvey对象

question = "What language did you first learn to speak?"
my_survey = AnoymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print('Enter 1 at any time to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print('\n Thankk you to everyone who participated in the survey!')

my_survey.show_results()
