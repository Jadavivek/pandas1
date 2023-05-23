
#   Create a pandas column using for loop
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
result=[]
for i in df['age'] :
    if i>=18 :
        result.append('eligible')
    else :
        result.append('not eligible')
df['voting eligibility ']=result
print(df)
#   How to get column names in Pandas dataframe
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=list(df.columns)
print(a)

#   How to rename columns in Pandas DataFrame
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
df.rename(columns={'name':'NAME'},inplace=True)
print(df)
#   Get unique values from a column in Pandas DataFrame
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df.age.unique
print(a)
#   Conditional operation on Pandas DataFrame columns
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,52,55],'lab':[25,22,24,23]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
if 'lab '  in df.columns :
    df['total ']=df['lab']+(df['theory'/2])
else :
    df['total']=df['lab']+(df['theory'])
print(df)
#   Return the Index label if some condition is satisfied over a column in Pandas Dataframe
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,52,55],'lab':[25,22,24,23]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
df.index=['m1','m2','m3','m4']
b=df[df['theory']>53].index.tolist()
print(b)

#   Formatting integer column of Dataframe in Pandas
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,52.5,55.8],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
pd.options.display.float_format = '{:,.2f}'.format
print (df)
#   Create a new column in Pandas DataFrame based on the existing columns
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,52.5,55.8],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
df['total']=df['theory']+df['lab']
print(df)
#   Python | Creating a Pandas dataframe column based on a given condition
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,52.5,55.8],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
grade=[]
for i in df['theory'] :
    if i>54:
        grade.append('s')
        
    elif i==54 :
        grade.append('a')
    else :
        grade.append('b')
df['grade']=grade
print(df)

#   Getting Unique values from a column in Pandas dataframe
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df.name.unique()
print("unique values of column name is :\n",a)
#   Split a String into columns using regex in pandas DataFrame
import pandas as pd

#   Getting frequency counts of a columns in Pandas DataFrame
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df['theory'].value_counts()
print(a)

#   Split a text column into two columns in Pandas DataFrame
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)

print("\nSplitting 'name' column into two different columns :\n",
                                  df.name.str.split(expand=True))
#   Get the index of minimum value in DataFrame column
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
print("index of minimum value of age in the given dataframe is :\n",df[['age']].idxmin())

#   Get the index of maximum value in DataFrame column
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'theory':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df[['age']].idxmax()
print("index of max value of the age in dataframe is :/n")

#   Difference of two columns in Pandas dataframe
import pandas as pd
data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'total':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
df['theory']=df['total']-df['lab']
print("dataframe after modificationo is :\n",df)

#   Get n-largest values from a particular column in Pandas DataFrame
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'total':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df.nlargest(2,['total'])
print('largest values in total column is :\n',a)

#   Get n-smallest values from a particular column in Pandas DataFrame
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'total':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df.nsmallest(2,['total'])
print('smallest values in total column is :\n',a)
#   How to drop one or multiple columns in Pandas Dataframe
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'total':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
df.drop(['lab'],axis=1)
print('dataframe after dropping lab column is :\n',df)
#   How to lowercase column names in Pandas dataframe
import pandas as pd

data={'NAME':['Vivek','Hari','Ajay','Pavan'],'AGE':[19,18,20,17],'TOTAL':[56,54,55,55],'LAB':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df.columns.str.lower()
print(a)
#   Capitalize first letter of a column in Pandas dataframe
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'total':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df['name'].str.capitalize()
print(a)
# Apply uppercase to a column in Pandas dataframe
import pandas as pd

data={'name':['vivek','hari','ajay','pavan'],'age':[19,18,20,17],'total':[56,54,55,55],'lab':[25,22.5,24.3,23.9]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
a=df['name']=df['name'].str.upper()
print(a)
