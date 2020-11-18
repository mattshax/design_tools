
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from scipy import stats
import sys
from collections import OrderedDict

def createSensitivity(csv_file,inputs,outputs):
        
    numDescriptors = len(inputs)
    # inputs = ['x','y']
    # outputs = ['z']
    
    f = open(csv_file)
    ptsraw = f.read()
    f.close()
    
    ptsraw = ptsraw.split('\n')
    pts = []
    labels = []
    for p in ptsraw:
        pp = p.split(',')
        pppp=[]
        for i,ppp in enumerate(pp):
            try:
                pppp.append(float(ppp))
            except:
                pass
        if len(pppp) > 0:
            pts.append(pppp)
     
    cols = []
    for i in inputs:
        cols.append(i)
    for i in outputs:
        cols.append(i.replace('--','_'))
    goodcols=[cols[c] for c in range(0,len(cols))]
    
    indexlabels=[cols[c] for c in range(0,1)]
    inputs=[cols[c] for c in range(0,numDescriptors)]
    outputs=[cols[c] for c in range(numDescriptors,len(cols))]
    
    # filter out errored results
    try:
        ptcheck= [ list(item) for item in pts ]
    except:
        print("Only one sample... cannot graph")
        exit(1)
    
    gg=[np.array(a) for a in zip(*pts)]
    
    print(labels)
    
    colmap={}
    for i,g in enumerate(gg):
        colmap[goodcols[i]]=g
    
    fig = plotly.tools.make_subplots(rows=len(outputs), cols=len(inputs), shared_yaxes=True, shared_xaxes=True)
    
    for i,out in enumerate(outputs):
        for j,inp in enumerate(inputs):
            
            slope, intercept, r_value, p_value, std_err = stats.linregress(colmap[inp],colmap[out])
            line = slope*colmap[inp]+intercept
        
            trace1 = go.Scatter(name=inputs[j],x = colmap[inp],y = colmap[out], text=labels,mode = 'markers',marker=go.Marker(size=3,color='rgb(0,0,255)'),showlegend=False)
            trace2 = go.Scatter(name='Fit',x = colmap[inp],y = line,mode = 'lines',line = dict(color = ('rgb(255, 0, 0)')),marker=go.Marker(color='rgba(255,0,0)'),showlegend=False)
            
            fig.append_trace(trace1, i+1, j+1)
            fig.append_trace(trace2, i+1, j+1)
    
    for lay in fig['layout']:
        if "xaxis" in lay:
            indy=lay.replace("xaxis","")
            if indy == "":
                indy="1"
            index=int(indy)-1
            fig['layout'][lay].update(title=inputs[index])
        if "yaxis" in lay:
            indy=lay.replace("yaxis","")
            if indy == "":
                indy="1"
            index=int(indy)-1
            fig['layout'][lay].update(title=outputs[index])
    
    fig['layout'].update(margin={'l': 60,'r': 20,'b': 60,'t': 20}) #title="Sensitivity Analysis Results"
            
    plot(fig, filename='outputs_sensitivity.html', auto_open=False,show_link=False)
    
    #add_custom_plotly_events('sensitivity.html')
