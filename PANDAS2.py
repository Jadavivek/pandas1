
import pandas as pd
a=[["vivek",'jada',18],['hari','jada',28],['krishna','uyyala',23],['pavan','meesala',20]]
df=pd.DataFrame(a,columns=['name','surname','age'],dtype=float)
print("requied data frame is :\n",df)

#How to iterate over rows in Pandas Dataframe
import pandas as pd
a=[["vivek",'jada',18],['hari','jada',28],['krishna','uyyala',23],['pavan','meesala',20]]
df=pd.DataFrame(a,columns=['name','surname','age'],dtype=float)
print("requied data frame is :\n",df)

#Different ways to iterate over rows in Pandas Dataframe
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[19,18,20]}
df=pd.DataFrame(data)
print(df)

#Selecting rows in pandas DataFrame based on conditions
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print('the required data frame is :\n',df)
df1=df.loc[df['reg no']>9000]
print("persons who are from eapcet batch is :\n",df1)

#Select any row from a Dataframe using iloc[] and iat[] in Pandas
import pandas as pd
df=pd.DataFrame({'date':['1/1/23','14/1/23','15/1/23','16/1/23'],'FESTIVAL':['new year','bhogi','sankranthi','kanuma'],'special':['cake','kites','veg meals','non veg meals']})
print('req data frame is :\n',df)
row=[]
for i in range((df.shape[0])):
    row1=[]
    for j in range(df.shape[1]):
        row1.append(df.iat[i,j])
    row.append(row1)
print("desired output is :\n",row[:3])

#Limited rows selection with given column in Pandas | Python
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("printing first two rows of the data frame of columns of name and age is :\n",df.loc[1:2,['name','age']])
#Drop rows from the dataframe based on certain condition applied on a column
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("data frame is :\n",df)
df1=df[df['reg no']>=9000]
print("students from eapcet batch are :\n",df1)

#Insert row at given position in Pandas Dataframe
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("the actual data framme is :\n",df)

#Create a list from rows in Pandas dataframe
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("the actual data framme is :\n",df)
print(df.head())
list=df['name'].to_list()
print("the extracted list from the dataframe is :\n",list)

#Ranking Rows of Pandas DataFrame
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("the actual data framme is :\n",df)
df['set_reg no']=df['reg no'].rank(ascending=0)
df=df.set_index('set_reg no')
print(df)

#Sorting rows in pandas DataFrame
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("the actual data framme is :\n",df)
a=df.sort_values(by='reg no',ascending=0)
print("after sorting the data frame according to the reg no is :\n",a)

#Select row with maximum and minimum value in Pandas dataframe
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502]}
df=pd.DataFrame(data,columns=['name','age','reg no'])
print("the actual data framme is :\n",df)
print("person with max age is :\n",df.age.max())
print("person with min age  is :\n",df.age.min())

#Get all rows in a Pandas DataFrame containing given substring
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'age':[18,19,18,19,19],'reg no':[9858,7890,9007,8765,9502],'course':['cse','cse','ece','cse','mec']}
df=pd.DataFrame(data,columns=['name','age','reg no','course'])
print("the actual data framme is :\n",df)
df1=df['course'].str.contains('cse')
print("did he is persuing cse course",df1)

#Convert a column to row name/index in Pandas
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'reg no':[9858,7890,9007,8765,9502],'course':['cse','cse','ece','cse','mec']}
df=pd.DataFrame(data,columns=['name','reg no','course'])
print("the actual data framme is :\n",df)
df1=df.pivot(index='name',columns='course')
print("modified data frame is :\n",df1)

#How to randomly select rows from Pandas DataFrame
import pandas as pd
data={'name':['vivek','manish','nikhil','ajay','pavam'],'reg no':[9858,7890,9007,8765,9502],'course':['cse','cse','ece','cse','mec']}
df=pd.DataFrame(data,columns=['name','reg no','course'])
print("the actual data framme is :\n",df)
df.sample()
print(df.sample(n=2))
