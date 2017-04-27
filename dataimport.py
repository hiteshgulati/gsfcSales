import pandas as pd
print ("entered")
file_name = "dec20.xlsx"
sales = pd.read_excel (file_name, sheet_name="Sheet1")
print (file_name , " file read")
# new columns for Qty and Units in To/MT where ever available
sales['Qty']= sales['Qty in Base Unit']
sales['Unit']= sales['Base Unit']
print ("munging started")
# munging of file
# conversion to TO/MT
# and applying negative to S1 invoices
for i, record in sales.iterrows():
    if record ['Sales Unit'] == "TO":
        sales.loc[i, 'Qty']= record ['Qty in Sales Unit']
        sales.loc[i,'Unit']= record ['Sales Unit']
    if sales.loc[i,'Unit'] == "KG":
        sales.loc[i, 'Qty'] /= 1000
        sales.loc[i, 'Unit']= "TO"
    if sales.loc[i,'Bill Type'] == "S1":
        sales.loc[i,'Qty'] *= -1
        sales.loc[i,'Net Value'] *= -1
        sales.loc [i, 'Tax'] *= -1
    if sales.loc[i,'Sold to Party Name'] == "JCT LTD":
        sales.loc[i,'Mtl Grp Desc'] = "CaproJCT"
print (file_name , " file munged")
sales.to_excel ("munged_" + file_name, sheet_name="Sheet1")

print (("munged_" + file_name), " created")
print ("I am done now")