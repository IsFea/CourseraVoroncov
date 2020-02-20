import pandas
import re
data = pandas.read_csv ( 'csv/titanic.csv' , index_col='PassengerId' )

#Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
cntSex = data['Sex'].value_counts()
print(str(cntSex.to_dict()['male'])+' '+str(cntSex.to_dict()['female']))

# Какой части пассажиров удалось выжить?
# Посчитайте долю выживших пассажиров. 
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.
cntSurv = data['Survived'].value_counts()
prSurv = round(( int(cntSurv.to_dict()[1]) /data['Survived'].count() ) * 100,2)
print(prSurv)

# Какую долю пассажиры первого класса составляли среди всех пассажиров? 
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.
cntPrimeClass = data['Pclass'].value_counts()
prPrimeClass = round(( int(cntPrimeClass.to_dict()[1]) / data['Pclass'].count() ) * 100 , 2)
print(prPrimeClass)

# Какого возраста были пассажиры? 
# Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел.
mean = data['Age'].mean()
median = data['Age'].median()
print(str(mean)+' '+str(median))

# Коррелируют ли число братьев/сестер/супругов с числом родителей/детей?
# Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
dataCorr = data[['SibSp','Parch']]
print(dataCorr.corr(method='pearson')['Parch'].to_dict()['SibSp'])

# Какое самое популярное женское имя на корабле? 
# Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name). 
# Это задание — типичный пример того, с чем сталкивается специалист по анализу данных. 
# Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию. 
# Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для извлечения имен, 
# а также разделения их на женские и мужские.
dataNames = data[['Name','Sex']]
dataNames = dataNames[dataNames['Sex'] == 'female']
def regName(x):
    if(re.search(r'[.]\s\w+',x)):
        return re.search(r'[.]\s\w+',x).group()[2:]
    else:
        return x
print (dataNames['Name'].apply(regName).value_counts().head())
# print(dataNames['Name'].apply(regName).value_counts().head(1).index.tolist().pop())