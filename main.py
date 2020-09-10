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
df = pandas.read_csv('/home/user/Загрузки/titanic.csv')

print(df.columns)
print(df.shape[0])

def Mans_on_board():return df[df['Sex'] == 'male'].shape[0]
print(Mans_on_board())

def alive_proc():
    alive = df[df['Survived'] == 1].shape[0]
    all = df.shape[0]
    return alive*100/all
print(alive_proc())

def mf():
    male = df[df['Sex'] == 'male'].shape[0]
    female = df[df['Sex'] == 'female'].shape[0]
    if male > female:
        return ('Male more')
    else:
        return ('Female more')

print(mf())

def surv_man():
    return (df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]/df[df['Survived'] == 1].shape[0])*100

print(surv_man())

def surv_class():
    var = {
        'First': (df[(df['Pclass'] == 1) & (df['Survived'] == 1)].shape[0] / df[df['Survived'] == 1].shape[0]) * 100,
        'Second': (df[(df['Pclass'] == 2) & (df['Survived'] == 1)].shape[0] / df[df['Survived'] == 1].shape[0]) * 100,
        'Third': (df[(df['Pclass'] == 3) & (df['Survived'] == 1)].shape[0] / df[df['Survived'] == 1].shape[0]) * 100
    }
    # min = min(var.values())
    min(var.values()) in var
    return (min(var()))

print(surv_class())