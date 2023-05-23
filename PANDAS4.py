# •	Pandas | Basic of Time Series Manipulation
import pandas as pd
import numpy as np
from datetime import datetime
range=pd.date_range(start='11/11/2003',end='12/11/2003',freq='Min')
print(range)

#	Using Timedelta and Period to create DateTime based indexes in Pandas
import pandas as pd
df=pd.DataFrame({'class':['AI','ML','DBMS'],'block':['AB1','AB2','CB']})
DATE=[pd.Timestamp('01-01-2022'),pd.Timestamp('01-01-2022'),pd.Timestamp('01-01-2022')]
df.index=DATE
print(df)

#	Convert the column type from string to datetime format in Pandas dataframe

import pandas as pd
df=pd.DataFrame({'Date':['01/01/2022','01/01/2022','01/01/2022'],'class':['AI','ML','DBMS'],'block':['AB1','AB2','CB']})
print(df)
df['Date']=pd.to_datetime(df['Date'])
df.info()

