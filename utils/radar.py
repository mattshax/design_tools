import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import os
 

def createRadar(caseindex,indata,headers,allDataHash):
    
    fig = plt.figure(figsize=(8,8))
    fig.clear()
    
    # normalized data
    #indata = allInputs[0]
    normalized_data = []
    for ii,id in enumerate(indata):
        mini=min(allDataHash[headers[ii]])
        maxi=max(allDataHash[headers[ii]])
        #print(mini,maxi,headers[ii])
        dd = ( id - mini ) / ( maxi - mini )
        normalized_data.append(dd)
    
    data={}
    data['group']=['case']
    
    for ii,id in enumerate(normalized_data):
        data[headers[ii]] = id
    
    # Set data
    df = pd.DataFrame(data)
     
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
     
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    values
     
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
     
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
     
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
     
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.5,0.75], ["0.25","0.5","0.75"], color="grey", size=7)
    plt.ylim(0,1)
     
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
     
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    
    try:
        os.makedirs('plots')
    except OSError as e:
        pass
    
    file='plots/case_'+caseindex+'.png'
    plt.savefig(file)
    
    return file
