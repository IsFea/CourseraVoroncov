import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier

# В библиотеке scikit-learn решающие деревья реализованы в классах:
#   sklearn.tree.DecisionTreeСlassifier (для классификации);
#   sklearn.tree.DecisionTreeRegressor (для регрессии).
# Обучение модели производится с помощью функции fit.

    # X = np.array([[1, 2], [3, 4], [5, 6]])
    # y = np.array([0, 1, 0])
    # clf = DecisionTreeClassifier()
    # clf.fit(X, y)

# importances = clf.feature_importances_ #Нахождение важности признаков используя обученный классификатор
# Переменная importances будет содержать массив "важностей" признаков. Индекс в этом массиве соответствует индексу признака в данных.

# np.isnan(X) - проверка на NaN

data = pandas.read_csv ( './csv/titanic.csv' , index_col='PassengerId' )[['Pclass','Fare','Age','Sex','Survived']]
def strSexToInt(sex):
    if(sex == 'male'):
        return 1
    else:
        return 0
data['Sex'] = data['Sex'].apply(strSexToInt)
dataTrain = data.drop(data[np.isnan(data.Age)].index)[['Pclass','Fare','Age','Sex']] # Убираем NaN значения
dataTarget = data.drop(data[np.isnan(data.Age)].index)[['Survived']]
clf = DecisionTreeClassifier(random_state=241)
clf.fit(dataTrain,dataTarget)
importances = clf.feature_importances_ 
print(importances)
# print(data)
# data = data.drop(data[np.isnan(data.Age).index],inplace = True)
