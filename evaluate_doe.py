import sys,json
import subprocess

import sys
sys.path.append("models")
from model_simple import f_xy

sys.path.append("utils")
from radar import createRadar
from sensitivity import createSensitivity

f = open('inputs_doe.csv')
inputs = f.readlines()
f.close()

input_labels=['x','y']
output_labels=['z']

allInputs=[]
allOutputs=[]
headers=[]
for i,input in enumerate(inputs):
    
    if i==0:    
        headers=[xx.strip() for xx in input.split(',')]
        continue
    
    print(i,'/',len(inputs)-1)
    
    idata = [xx.strip() for xx in input.split(',')]
    for ii,id in enumerate(idata):
        exec("{}={}".format(headers[ii],float(id)))
    
    # evalute the model
    z = f_xy(x,y)
    
    inp=[x,y]
    outp=[z]
    print('inputs',inp)
    print('outputs',outp)
    
    allInputs.append(inp)
    allOutputs.append(outp)
    
# postprocessing of the results
allData = []
row=[]
for i in input_labels:
    row.append('in:'+i)
for o in output_labels:
    row.append('out:'+o)
row.append('img:plot')
allData.append(",".join(row))

# get all the data organized for min/max values
allDataHash={}
for ir,r in enumerate(allInputs):
    for ii,i in enumerate(allInputs[ir]):
        try:
            allDataHash[input_labels[ii]].append(i)
        except:
            allDataHash[input_labels[ii]] = []
            allDataHash[input_labels[ii]].append(i)
    for io,o in enumerate(allOutputs[ir]):
        try:
            allDataHash[output_labels[io]].append(o)
        except:
            allDataHash[output_labels[io]] = []
            allDataHash[output_labels[io]].append(o)

# create the rows
print("")
for ir,r in enumerate(allInputs):
    
    print("plotting",ir+1,'/',len(allInputs)-1)
    
    row=[]    
    headers=[]
    for ii,i in enumerate(allInputs[ir]):
        row.append((i))
        headers.append(input_labels[ii])
    for io,o in enumerate(allOutputs[ir]):
        row.append((o))
        headers.append(output_labels[io])
    
    # make the radar plots
    plot = createRadar(str(ir),row,headers,allDataHash)
    #plot = 'plots/case_'+str(ir)+'.png'
    
    row.append(plot)
    allData.append(",".join([str(x) for x in row]))

# generate the output csv data
f = open('outputs_doe.csv','w')
f.write("\n".join(allData))
f.close()

# generate the sensitivity plot
createSensitivity('outputs_doe.csv',input_labels,output_labels)
