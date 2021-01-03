import os
import pandas as pd
import numpy as np

pdf_folder = "pdf_files/"
xml_folder = "xml_files/"
excel = "Sample Comparison 2020_10_05.xlsx"
checked="checked_Sample Comparison 2020_10_05.xlsx"
name_col="name"
link_col="link"
pdf_col="pdf"
xml_col="xml"

pdf_dict = {}
xml_dict = {}

for _, _, files in os.walk(pdf_folder):
    for pdf_f in files:
        pdf_dict[pdf_f[:-4]] = True

for _, _, files in os.walk(xml_folder):
    for xml_f in files:
        xml_dict[xml_f[:-4]] = True

df = pd.read_excel(excel, sheet_name="check")
df[name_col] = df[name_col].astype(str)
df[link_col] = df[link_col].astype(str)
df[pdf_col] = df[pdf_col].astype(str)
df[xml_col] = df[xml_col].astype(str)
df = df.replace('nan', '', regex=True)

for index, row in df.iterrows():
   pdf_name = row[name_col]
   for col,dic in [(pdf_col,pdf_dict), (xml_col,xml_dict)]:
    if pdf_name in dic:
        df.at[index,col] = 1
        dic.pop(pdf_name, None)
    elif row[link_col]=='.' or row[link_col]=="0":
        df.at[index,col] = row[link_col]
    else:
        df.at[index,col] = 0 

print("PDF dictionary:"+str(pdf_dict))
print("XML dictionary:"+str(xml_dict))

df.to_excel(checked)
print("Done!")
