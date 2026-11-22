import pandas as pd
import csv
df =pd.read_csv("expenses.csv") #dataFrame created
df["amount"] = pd.to_numeric(df["amount"], errors="coerce") #due to bad value amount was assumed as str but to_numeric convert it back to numeral form
#print(df[df["amount"].isna()]) #shows which row do not have numeral value
#print(df["amount"].dtype)
#print(df.describe()) #count,unique elements,top value,highest frequency
#print(df.head()) #first five value,class,rangeindex,data columns
#print(df.info()) #column name,non_null constant, Dtype,memory usage
#(df.groupby("category")["amount"].sum())
#print(df["amount"].sum())                 
#print(df["amount"].max())                 
#print(df.loc[df["amount"].idxmax()])      
totals = df.groupby("category", as_index=False)["amount"].sum()
print(totals)
totals.to_csv("summary_pandas.csv", index=False)