import time
import pandas as pd
import numpy as np

print("entered")
file_name = "indicators.xlsx"
zone_indicator = pd.read_excel (file_name, sheetname="zone",header=0, index_col = 0)
zone_dict = zone_indicator.to_dict(orient='dict')['Zone']

party_indicator = pd.read_excel (file_name, sheetname="party",header=0, index_col = 0)
party_exclusion_list = list(party_indicator.index.values)


print("file picking")
file_name = "munged_march26.xlsx"
all_sales_data = pd.read_excel (file_name, sheet_name="Sheet1",index_col=0)
sales = pd.DataFrame(data=None, columns= list(all_sales_data))
j = 1
for i, record in all_sales_data.iterrows():
  if zone_dict[record['Region Desc']] == 'North':
    if record['Payer Name'] not in party_exclusion_list:
      sales.loc[j] = record
      j +=1

# print(sales.describe())
# print(all_sales_data.describe())
print (sales['Qty'].sum)

