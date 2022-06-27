import numpy as np
import skfuzzy
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Входные переменные
users_student = ctrl.Antecedent(np.arange(0, 80.1, 1.), 'Пользователи-студенты')
users_interested = ctrl.Antecedent(np.arange(0, 75.1, 1.), 'Заинтересованные пользователи')
users_not_interested = ctrl.Antecedent(np.arange(0, 75.1, 1.), 'Не заинтересованные пользователи')
users_course_graduates = ctrl.Antecedent(np.arange(0, 80.1, 1.), 'Прошли весь курс')
users_not_course_graduates = ctrl.Antecedent(np.arange(0, 75.1, 1.), 'Отчислились')

# Выходные переменные
course_relevance = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'Актуальность курса')
interest_in_course = ctrl.Consequent(np.arange(0, 80.1, 1.), 'Заинтересованность в курсе')

# ФП для 'Пользователи-студенты'
users_student['very few'] = fuzz.trapmf(users_student.universe, [-1, 0, 0, 15])
users_student['few'] = fuzz.trapmf(users_student.universe, [10, 23, 23, 35])
users_student['medium'] = fuzz.trapmf(users_student.universe, [30, 47, 47, 65])
users_student['many'] = fuzz.trapmf(users_student.universe, [60, 80, 80, 100])
users_student.view()
print()

# ФП для 'Заинтересованые пользователи'
users_interested['very few'] = fuzz.trapmf(users_interested.universe, [-1, 0, 0, 15])
users_interested['few'] = fuzz.trapmf(users_interested.universe, [10, 23, 23, 35])
users_interested['medium'] = fuzz.trapmf(users_interested.universe, [30, 43, 43, 55])
users_interested['many'] = fuzz.trapmf(users_interested.universe, [50, 75, 75, 100])
users_interested.view()
print()

# ФП для 'Не заинтересованые пользователи'
users_not_interested['very few'] = fuzz.trapmf(users_not_interested.universe, [-1, 0, 0, 15])
users_not_interested['few'] = fuzz.trapmf(users_not_interested.universe, [10, 23, 23, 35])
users_not_interested['medium'] = fuzz.trapmf(users_not_interested.universe, [30, 43, 43, 55])
users_not_interested['many'] = fuzz.trapmf(users_not_interested.universe, [50, 75, 75, 100])
users_not_interested.view()
print()

# ФП для 'Прошли весь курс'
users_course_graduates['very few'] = fuzz.trapmf(users_course_graduates.universe, [-1, 0, 0, 25])
users_course_graduates['few'] = fuzz.trapmf(users_course_graduates.universe, [20, 33, 33, 45])
users_course_graduates['medium'] = fuzz.trapmf(users_course_graduates.universe, [40, 53, 53, 65])
users_course_graduates['many'] = fuzz.trapmf(users_course_graduates.universe, [60, 80, 80, 100])
users_course_graduates.view()
print()

# ФП для 'Отчислились'
users_not_course_graduates['very few'] = fuzz.trapmf(users_not_course_graduates.universe, [-1, 0, 0, 15])
users_not_course_graduates['few'] = fuzz.trapmf(users_not_course_graduates.universe, [10, 23, 23, 35])
users_not_course_graduates['medium'] = fuzz.trapmf(users_not_course_graduates.universe, [30, 43, 43, 55])
users_not_course_graduates['many'] = fuzz.trapmf(users_not_course_graduates.universe, [50, 75, 75, 100])
users_not_course_graduates.view()
print()

# ФП для 'Актуальность курса'
course_relevance['not_relevant'] = fuzz.trapmf(course_relevance.universe, [-1, 0, 0, 0.6])
course_relevance['relevant'] = fuzz.trapmf(course_relevance.universe, [0.4, 1, 1, 2])
course_relevance.view()
print()

# ФП для 'Заинтересованность в курсе'
interest_in_course['low'] = fuzz.trapmf(interest_in_course.universe, [-1, 0, 0, 25])
interest_in_course['medium'] = fuzz.trapmf(interest_in_course.universe, [20, 43, 43, 66])
interest_in_course['high'] = fuzz.trapmf(interest_in_course.universe, [60, 80, 80, 100])
interest_in_course.view()
print()

# База правил
rule1 = ctrl.Rule(users_student['many'] & users_interested['many'] & users_not_interested['few'] & users_course_graduates['many'] & users_not_course_graduates['few'], [course_relevance['relevant'], interest_in_course['high']])
rule2 = ctrl.Rule(users_student['many'] & users_interested['medium'] & users_not_interested['very few'] & users_course_graduates['medium'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['high']])
rule3 = ctrl.Rule(users_student['medium'] & users_interested['many'] & users_not_interested['few'] & users_course_graduates['many'] & users_not_course_graduates['few'], [course_relevance['relevant'], interest_in_course['high']])
rule4 = ctrl.Rule(users_student['medium'] & users_interested['medium'] & users_not_interested['very few'] & users_course_graduates['medium'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['high']])
rule5 = ctrl.Rule(users_student['many'] & users_interested['many'] & users_not_interested['very few'] & users_course_graduates['many'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['high']])
rule6 = ctrl.Rule(users_student['medium'] & users_interested['many'] & users_not_interested['very few'] & users_course_graduates['many'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['high']])
rule7 = ctrl.Rule(users_student['few'] & users_interested['many'] & users_not_interested['few'] & users_course_graduates['many'] & users_not_course_graduates['few'], [course_relevance['relevant'], interest_in_course['medium']])
rule8 = ctrl.Rule(users_student['few'] & users_interested['medium'] & users_not_interested['very few'] & users_course_graduates['medium'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['medium']])
rule9 = ctrl.Rule(users_student['many'] & users_interested['medium'] & users_not_interested['few'] & users_course_graduates['medium'] & users_not_course_graduates['few'], [course_relevance['relevant'], interest_in_course['medium']])
rule10 = ctrl.Rule(users_student['few'] & users_interested['many'] & users_not_interested['very few'] & users_course_graduates['many'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['medium']])
rule11 = ctrl.Rule(users_student['very few'] & users_interested['many'] & users_not_interested['very few'] & users_course_graduates['very few'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['medium']])
rule12 = ctrl.Rule(users_student['many'] & users_interested['many'] & users_not_interested['many'] & users_course_graduates['many'] & users_not_course_graduates['few'], [course_relevance['relevant'], interest_in_course['medium']])
rule13 = ctrl.Rule(users_student['many'] & users_interested['few'] & users_not_interested['few'] & users_course_graduates['many'] & users_not_course_graduates['very few'], [course_relevance['relevant'], interest_in_course['medium']])
rule14 = ctrl.Rule(users_student['many'] & users_interested['few'] & users_not_interested['medium'] & users_course_graduates['medium'] & users_not_course_graduates['medium'], [course_relevance['relevant'], interest_in_course['low']])
rule15 = ctrl.Rule(users_student['medium'] & users_interested['medium'] & users_not_interested['few'] & users_course_graduates['medium'] & users_not_course_graduates['few'], [course_relevance['not_relevant'], interest_in_course['medium']])
rule16 = ctrl.Rule(users_student['few'] & users_interested['medium'] & users_not_interested['few'] & users_course_graduates['medium'] & users_not_course_graduates['few'], [course_relevance['not_relevant'], interest_in_course['medium']])
rule17 = ctrl.Rule(users_student['many'] & users_interested['medium'] & users_not_interested['medium'] & users_course_graduates['medium'] & users_not_course_graduates['very few'], [course_relevance['not_relevant'], interest_in_course['medium']])
rule18 = ctrl.Rule(users_student['many'] & users_interested['many'] & users_not_interested['many'] & users_course_graduates['few'] & users_not_course_graduates['few'], [course_relevance['not_relevant'], interest_in_course['medium']])
rule19 = ctrl.Rule(users_student['many'] & users_interested['few'] & users_not_interested['many'] & users_course_graduates['medium'] & users_not_course_graduates['many'], [course_relevance['not_relevant'], interest_in_course['low']])
rule20 = ctrl.Rule(users_student['many'] & users_interested['very few'] & users_not_interested['medium'] & users_course_graduates['few'] & users_not_course_graduates['medium'], [course_relevance['not_relevant'], interest_in_course['low']])
rule21 = ctrl.Rule(users_student['medium'] & users_interested['few'] & users_not_interested['many'] & users_course_graduates['medium'] & users_not_course_graduates['many'], [course_relevance['not_relevant'], interest_in_course['low']])
rule22 = ctrl.Rule(users_student['medium'] & users_interested['very few'] & users_not_interested['medium'] & users_course_graduates['few'] & users_not_course_graduates['medium'], [course_relevance['not_relevant'], interest_in_course['low']])
rule23 = ctrl.Rule(users_student['few'] & users_interested['few'] & users_not_interested['many'] & users_course_graduates['medium'] & users_not_course_graduates['many'], [course_relevance['not_relevant'], interest_in_course['low']])
rule24 = ctrl.Rule(users_student['few'] & users_interested['very few'] & users_not_interested['medium'] & users_course_graduates['few'] & users_not_course_graduates['medium'], [course_relevance['not_relevant'], interest_in_course['low']])
rule25 = ctrl.Rule(users_student['many'] & users_interested['very few'] & users_not_interested['many'] & users_course_graduates['few'] & users_not_course_graduates['many'], [course_relevance['not_relevant'], interest_in_course['low']])
rule26 = ctrl.Rule(users_student['medium'] & users_interested['few'] & users_not_interested['medium'] & users_course_graduates['medium'] & users_not_course_graduates['medium'], [course_relevance['not_relevant'], interest_in_course['low']])
rule27 = ctrl.Rule(users_student['medium'] & users_interested['very few'] & users_not_interested['many'] & users_course_graduates['few'] & users_not_course_graduates['many'], [course_relevance['not_relevant'], interest_in_course['low']])
rule28 = ctrl.Rule(users_student['few'] & users_interested['few'] & users_not_interested['medium'] & users_course_graduates['medium'] & users_not_course_graduates['medium'], [course_relevance['not_relevant'], interest_in_course['low']])
rule29 = ctrl.Rule(users_student['few'] & users_interested['very few'] & users_not_interested['many'] & users_course_graduates['few'] & users_not_course_graduates['many'], [course_relevance['not_relevant'], interest_in_course['low']])
rule30 = ctrl.Rule(users_student['very few'] & users_interested['medium'] & users_not_interested['few'] & users_course_graduates['very few'] & users_not_course_graduates['very few'], [course_relevance['not_relevant'], interest_in_course['low']])
rule31 = ctrl.Rule(users_student['very few'] & users_interested['few'] & users_not_interested['medium'] & users_course_graduates['very few'] & users_not_course_graduates['very few'], [course_relevance['not_relevant'], interest_in_course['low']])
rule32 = ctrl.Rule(users_student['very few'] & users_interested['very few'] & users_not_interested['many'] & users_course_graduates['very few'] & users_not_course_graduates['very few'], [course_relevance['not_relevant'], interest_in_course['low']])

rules_base = [ rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16,
               rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32 ]

mark_ctrl = ctrl.ControlSystem(rules_base)

marking = ctrl.ControlSystemSimulation(mark_ctrl)

# Пример 1
inputs = {'Пользователи-студенты': 65, 'Заинтересованные пользователи': 73, 'Не заинтересованные пользователи': 27, 'Прошли весь курс': 68, 'Отчислились': 32}
marking.inputs(inputs)
marking.compute()

print(marking.output['Актуальность курса'])
course_relevance.view(sim = marking)

# Пример 2
inputs = {'Пользователи-студенты': 65, 'Заинтересованные пользователи': 73, 'Не заинтересованные пользователи': 27, 'Прошли весь курс': 68, 'Отчислились': 32}
marking.inputs(inputs)
marking.compute()

print(marking.output['Заинтересованность в курсе'])
interest_in_course.view(sim = marking)

# Пример 3
inputs = {'Пользователи-студенты': 72, 'Заинтересованные пользователи': 12, 'Не заинтересованные пользователи': 55, 'Прошли весь курс': 28, 'Отчислились': 72}
marking.inputs(inputs)
marking.compute()

print(marking.output['Актуальность курса'])
course_relevance.view(sim = marking)

# Пример 4
inputs = {'Пользователи-студенты': 72, 'Заинтересованные пользователи': 12, 'Не заинтересованные пользователи': 55, 'Прошли весь курс': 28, 'Отчислились': 72}
marking.inputs(inputs)
marking.compute()

print(marking.output['Заинтересованность в курсе'])
interest_in_course.view(sim = marking)

# Пример 5
inputs = {'Пользователи-студенты': 63, 'Заинтересованные пользователи': 39, 'Не заинтересованные пользователи': 46, 'Прошли весь курс': 41, 'Отчислились': 12}
marking.inputs(inputs)
marking.compute()

print(marking.output['Актуальность курса'])
course_relevance.view(sim = marking)

# Пример 6
inputs = {'Пользователи-студенты': 63, 'Заинтересованные пользователи': 39, 'Не заинтересованные пользователи': 46, 'Прошли весь курс': 41, 'Отчислились': 12}
marking.inputs(inputs)
marking.compute()

print(marking.output['Заинтересованность в курсе'])
interest_in_course.view(sim = marking)

# Пример 7
inputs = {'Пользователи-студенты': 68, 'Заинтересованные пользователи': 46, 'Не заинтересованные пользователи': 24, 'Прошли весь курс': 53, 'Отчислились': 31}
marking.inputs(inputs)
marking.compute()

print(marking.output['Актуальность курса'])
course_relevance.view(sim = marking)

# Пример 8
inputs = {'Пользователи-студенты': 68, 'Заинтересованные пользователи': 46, 'Не заинтересованные пользователи': 24, 'Прошли весь курс': 53, 'Отчислились': 31}
marking.inputs(inputs)
marking.compute()

print(marking.output['Заинтересованность в курсе'])
interest_in_course.view(sim = marking)

# Пример 9
inputs = {'Пользователи-студенты': 51, 'Заинтересованные пользователи': 73, 'Не заинтересованные пользователи': 28, 'Прошли весь курс': 64, 'Отчислились': 25}
marking.inputs(inputs)
marking.compute()

print(marking.output['Актуальность курса'])
course_relevance.view(sim = marking)

# Пример 10
inputs = {'Пользователи-студенты': 51, 'Заинтересованные пользователи': 73, 'Не заинтересованные пользователи': 28, 'Прошли весь курс': 64, 'Отчислились': 25}
marking.inputs(inputs)
marking.compute()

print(marking.output['Заинтересованность в курсе'])
interest_in_course.view(sim = marking)
