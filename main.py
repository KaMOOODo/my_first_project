# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
lambda x:x*2
print('It is first branch')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


import pandas
titanic = pandas.read_csv('C:/Users/User/PycharmProjects/my_first_project/titanic.csv')

print(titanic.columns)
print(titanic.shape[0])

def Mans_on_board():return titanic[titanic['Sex'] == 'male'].shape[0]
print(Mans_on_board())

def alive_proc():
    alive = titanic[titanic['Survived'] == 1].shape[0]
    all = titanic.shape[0]
    return alive*100/all
print(alive_proc())

def mf():
    male = titanic[titanic['Sex'] == 'male'].shape[0]
    female = titanic[titanic['Sex'] == 'female'].shape[0]
    if male > female:
        return ('Male more')
    else:
        return ('Female more')

print(mf())

def surv_man():
    return (titanic[(titanic['Sex'] == 'male') & (titanic['Survived'] == 1)].shape[0] / titanic[titanic['Survived'] == 1].shape[0]) * 100

print(surv_man())

def surv_class():
    var = {
        (titanic[(titanic['Pclass'] == 1) & (titanic['Survived'] == 1)].shape[0] / titanic[titanic['Survived'] == 1].shape[0]) * 100 : 'First',
        (titanic[(titanic['Pclass'] == 2) & (titanic['Survived'] == 1)].shape[0] / titanic[titanic['Survived'] == 1].shape[0]) * 100 : 'Second',
        (titanic[(titanic['Pclass'] == 3) & (titanic['Survived'] == 1)].shape[0] / titanic[titanic['Survived'] == 1].shape[0]) * 100 : 'Third'
    }
    return (var.get(min(var.keys())) + ' class most likely did not survive')

print(surv_class())

info = pandas.read_csv('C:/Users/User/PycharmProjects/my_first_project/info.csv')
marks = pandas.read_csv('C:/Users/User/PycharmProjects/my_first_project/marks.csv')

# 1. Узнайте для скольких людей из датафрейма info неизвестны оценки.
def task38_1():
    comb = info.merge(marks, left_on='id', right_on='id2', how='left') #combined DataFrame
    result = comb[(comb['math'].isnull()) | (comb['reading'].isnull()) | (comb['writing'].isnull())].shape[0]
    return result


print('У', task38_1(),'неизвестны оценки.')


# 2. Узнайте для скольких людей из датафрейма marks неизвестны расса\пол\...
def task38_2():
    comb = marks.merge(info, left_on='id2', right_on='id', how='left') #combined DataFrame
    result = comb[(comb['gender'].isnull()) | (comb['race'].isnull()) | (comb['parents_education'].isnull())].shape[0]
    return result


print('У', task38_2(),'неизвестны пол/раса/образование родителей.')


# 3. Узнайте среднюю оценку по математике рассы "group A".
def task38_3():
    comb = info.merge(marks, left_on='id', right_on='id2') #combined DataFrame
    print(comb[(comb['race'] == 'group A') & comb['math']])

task38_3()