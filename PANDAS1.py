#     Make a Pandas DataFrame with two-dimensional list | Python
import pandas as pd
a=[["vivek",'jada',18],['hari','jada',28],['krishna','uyyala',23],['pavan','meesala',20]]
df=pd.DataFrame(a)
print("requied data frame is :\n",df)

#     Python | Creating DataFrame from dict of narray/lists
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[19,18,20]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)

#     Creating Pandas dataframe using list of lists
import pandas as pd
a=[["vivek",'jada',18],['hari','jada',28],['krishna','uyyala',23],['pavan','meesala',20]]
df=pd.DataFrame(a,columns=['name','surname','age'],dtype=float)
print("requied data frame is :\n",df)

#     Creating a Pandas dataframe using list of tuples
import pandas as pd
list=[("vivek",18,97),('ajay',19,98),('pavan',20,97)]
df=pd.DataFrame.from_records(list,columns=['name','age','marks'])
print("requied data frame is :\n",df)

#     Create a Pandas DataFrame from List of Dicts
import pandas as pd
data=[{'name':'vivek','age':19},
      {'name':'hari','age':18}]
df=pd.DataFrame.from_records(data,index=['1','2'])
print("requied data frame is :\n",df)

#     Python | Convert list of nested dictionary into Pandas dataframe
import pandas as pd
list=[{"python":[{'marks':97,'grade':'s'},{'marks':95,'grade':"a"},{'marks':93,'grade':'b'}],'name':'vivek'},{'java':[{'marks':92,'grade':'s'},{'marks':90,'grade':'a','marks':85,'grade':'b'}],"name":'jada vivek'}]
print("converted dictionary is :\n",list)
#     Creating a dataframe from Pandas series
import pandas as pd
a=['vivek','ajay','pavan','upendra']
b=pd.Series(a)
print("required dataframe series is :\n",b)
#     Construct a DataFrame in Pandas using string data
import pandas as pd
from io import StringIO
strdata=StringIO("""name;age;marks
           vivek;18;97
           ajay;18;98
           pavan;20;97""")
df=pd.read_csv(strdata,sep=';')
print(df)

#     Clean the string data in the given Pandas Dataframe
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[18,18,20],'course':['cse','cse','ece']}
df=pd.DataFrame(data,columns=['name','age','course'],index=['1','2','3'])
print("original dataframe is",df)
df['name']=df['name'].apply(lambda x  :x.strip().capitalize())
print("updated dataframe is :\n",df)
#     Replace values in Pandas dataframe using regex
import pandas as pd
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[18,18,20]}
df=pd.DataFrame(data)
print("required data frame is :\n",df)
df1=df.replace(to_replace=18, value=20,regex=True)
print("updated dataframe is :\n",df1)
#     Reindexing in Pandas DataFrame
import pandas as pd
import numpy as np
column=['A','B','C','D']
index=['A1','B1','C1','D1']
df=pd.DataFrame(np.random.rand(4,4),columns=column,index=index)
index=['E','F','G','H']
print(df.reindex(column,axis='columns'))

#     Mapping external values to dataframe values in Pandas
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[18,18,20],'course':['cse','cse','ece']}
df=pd.DataFrame(data,columns=['name','age','course'])
data1={'vivek':9.8,'hari':9.0,'ajay':9.8}
df['cgpa']=df['name'].map(data1)
print(df)

#     Reset Index in Pandas Dataframe
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[18,18,20],'course':['cse','cse','ece']}
df=pd.DataFrame(data,columns=['name','age','course'])
index=['a','b','c']
df=pd.DataFrame(data,index)
df.reset_index(inplace=True)
print(df)
#     Python | Change column names and row indexes in Pandas DataFrame
import pandas as pd
data={'name':['vivek','hari','ajay'],'age':[18,18,20],'course':['cse','cse','ece']}
df=pd.DataFrame(data,columns=['name','age','course'],index=['1','2','3'])
print(df)
df=df.rename(index={'1':'R1','2':'R2','3':'R3'})
print(df)
