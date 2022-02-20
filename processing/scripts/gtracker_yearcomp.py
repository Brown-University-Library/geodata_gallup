# -*- coding: utf-8 -*-
"""
Loop through Gallup Analytics US Tracker files from 2008 to 2017
Generate files that show which variables are included over time

Frank Donnelly / GIS and Data Librarian / Brown University
"""

import openpyxl as xl, os

data_path='varlist_test'
fname='gtracker_vars_2008_2017'

gvars={}
years=[]
ystart=2008
yend=2018 # one yr beyond last file

# Generate dictionary of years available for each variable and write to text
for i in range (ystart,yend):
    years.append(i)

for item in os.listdir(data_path):
    if item [0:14] == 'gallup_tracker' and item [-5:] =='.xlsx':
        year=item[15:19]
        workbook = xl.load_workbook(os.path.join(data_path,item))
        ws = workbook['Sheet1']
        for cell in ws['B']:
            if cell.value in gvars:
                gvars[cell.value].append(year)      
            else:
                gvars[cell.value]=[year]
            
txtfile=fname+'.txt'
outfile=open(txtfile,'w')
for k in sorted(gvars):
    newtext=[k]
    for v in gvars[k]:
        newtext.append(v)
    outfile.writelines(",".join(newtext)+'\n')
outfile.close()

# Modify list to generate matrix of available years per variable and write to csv     
for v in gvars.values():
    for i,y in enumerate(years):
        if str(y) in v:
            pass
        else:
            v.insert(i,'') # Creates padded, un-ragged list
            
header=['y'+str(y) for y in years]
header.insert(0,'variable')

csvfile=fname+'.csv'
outfile=open(csvfile,'w')
outfile.writelines(",".join(header)+'\n')
for k in sorted(gvars):
    newline=[k]
    for v in gvars[k]:
        if v =='':
            newline.append(v)
        else:
            newline.append('x')
    outfile.writelines(",".join(newline)+'\n')
outfile.close()
