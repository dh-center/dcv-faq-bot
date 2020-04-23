import pandas as pd

LANGUAGES = {'English': ['Admission', 'Program'],
             'Русский': ['Поступление', 'Программа']}

INTRO_QUESTION = {'English': 'Please, choose the question:',
                  'Русский': 'Выберите вопрос, пожалуйста:'}

MAIN_MENU = {'Admission': ['Required documents', 'How to apply?',
                           'Admission information'],
             'Program': ['Program information',
                         'Majors'],
             'Поступление': ['Список документов',
                             'Как поступить?',
                             'Информация о поступлении'],
             'Программа': ['Информация о программе',
                           'Специальности']
             }

SECOND_LEVEL = {'How to apply?': ['Portfolio Contest'],
                'Majors': ['Cultural analytics'],
                'Как поступить?': ['Вступительный экзамен',
                                   'Дистанционный экзамен',
                                   'Конкурс Портфолио',
                                   'Я - Профессионал',
                                   'КМУ'],
                'Специальности': ['Культурная аналитика',
                                  'Цифровые гуманитарные исследования']
                }

df_answers = pd.read_csv('answers/english_answers.csv', header=None)
ru_answers = pd.read_csv('answers/russian_answers.csv', header=None)
df_answers = df_answers.append(ru_answers)
df_answers.columns = ['name', 'answer']
df_answers = df_answers.replace(r'\\n', '\n', regex=True)
ANSWERS = df_answers.set_index('name').to_dict()['answer']
