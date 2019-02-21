import pandas as pd

filename ='Inj_Prodbywell.xls'
df=pd.read_table(filename)
df_inj = pd.melt(df, id_vars=['Apino','Company','Inj_type','Field', 'Formation', 'Year'], 
              value_vars=['Jan_Inj', 'Feb_Inj', 'Mar_Inj', 'Apr_Inj', 'May_Inj', 'Jun_Inj', 
                          'Jul_Inj', 'Aug_Inj', 'Sep_Inj', 'Oct_Inj', 'Nov_Inj', 'Dec_Inj'],
              var_name="Month_val", value_name="Inj")
df_inj['Month_val']=df_inj['Month_val'].replace(to_replace='_Inj', value='', regex=True)
month_transform={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9,
                 'Oct':10, 'Nov':11, 'Dec':12}
df_inj['Month_val']=df_inj['Month_val'].map(month_transform)
df_inj['Date']=pd.to_datetime((df_inj.Year*10000+df_inj.Month_val*100+1).apply(str),format='%Y%m%d')
df_inj=df_inj.drop(['Month_val','Year'],axis=1)
df_inj=df_inj.reset_index().drop('index',axis=1)
df_inj.to_csv('injection.csv')
df_inj

