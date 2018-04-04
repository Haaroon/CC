import pandas as pd
import os
files = os.listdir(".")
umpires = []
for filex in files:
	if '.xl' not in filex:
		continue
	print(filex)
	xl = pd.ExcelFile(filex)
	df = xl.parse('Results')
	for row in df.iterrows():
		rowdata = row[1]
		if(not pd.isna(rowdata['Umpire 1'])):
			print(rowdata['Umpire 1'])
			umpires.append(str(rowdata['Umpire 1']))
		if(not pd.isna(rowdata['Umpire 2'])):
			print(rowdata['Umpire 2'])
			umpires.append(str(rowdata['Umpire 2']))

umpires = list(set(umpires))
print(umpires)
	
