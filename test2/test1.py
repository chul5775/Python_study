#도수 분포표
import pandas as pd
from pandas import DataFrame

frame = pd.read_csv("../testdata/ex_studentlist.csv")
print(frame.head(3))
print(frame.shape)
print(frame.info())
print(frame.describe())


# 혈행형 빈도수
data1 = frame.groupby(['bloodtype'])['bloodtype'].count()
print(data1)

data2 = pd.crosstab(index=frame['bloodtype'], columns = ["count"])
print(data2)

#성별 혈액형 빈도수
data3 = pd.crosstab(index=frame['bloodtype'], columns = frame['sex'])
print(data3)




