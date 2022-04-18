from cmath import nan
from numpy import NaN, greater
import pandas as pd

def drop_nan(df):
  for index, row in df.iterrows():
    if row.hasnans:
        df.drop(
            labels=index,
            axis=0,
            inplace=True
        )  
  df.reset_index(drop=True, inplace=True)

def drop_dupe(col_data, time_data):
  dupes = []
  # drop value if previous and next values are the same
  for i in range(1,len(col_data)-1,1):
    try:
      if pd.isna(col_data[i]):
        dupes.append(i)
      elif col_data[i] == col_data[i-1] and col_data[i] == col_data[i+1]:
        dupes.append(i)
    except:
      print(str(col_data[i]))
      print("couldn't eval dupe for index: " + str(i))

  out_col = col_data
  out_col.drop(index=dupes, inplace=True)
  out_time = time_data
  out_time.drop(index=dupes, inplace=True)

  return out_col, out_time