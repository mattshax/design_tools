#!/usr/bin/python3
import sys
import json

import cufflinks as cf
import plotly as py
from plotly.graph_objs import *

from doe_functions import *
from collections import OrderedDict
import seaborn as sns
import os
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

def run_doe(params, num_samples, method, out_csv, out_png):

    if method == "lhs-spacefill":
        df=build_space_filling_lhs(params,num_samples=num_samples)
    elif method == "random":
        df=build_uniform_random(params,num_samples=num_samples)
    elif method == "k-means":
        df=build_random_k_means(params,num_samples=num_samples)
    elif method == "lhs-simple":
        df=build_lhs(params,num_samples=num_samples)
    elif method == "maximin":
        df=build_maximin(params,num_samples=num_samples)
    elif method == "halton":
        df=build_halton(params,num_samples=num_samples)

    df.to_csv(out_csv,index=False)
    
    nunique = df.apply(pd.Series.nunique)
    cols_to_drop = nunique[nunique == 1].index
    df = df.drop(cols_to_drop, axis=1)
    
    genImage=True
    if genImage ==True:
        
        # dirty output but fast
        # axs = scatter_matrix(df, alpha=1, figsize=(12, 12)) # diagonal='kde'
        # plt.savefig(out_png)
        
        # nicest output but very slow
        g = sns.pairplot(df, height=3,aspect=1)
        g.savefig(out_png)
        
        # web based output - very slow with large datasets
        # fig = df.scatter_matrix(asFigure=True)
        # fig['layout']['paper_bgcolor'] = 'rgba(0,0,0,0)'
        # fig['layout']['plot_bgcolor'] = 'rgba(0,0,0,0)'
        # fig['layout']['margin'] = {
        #     'l': 25,
        #     'r': 20,
        #     'b': 20,
        #     't': 20,
        #     'pad': 0
        # }
        # plotly.offline.plot(fig, filename = 'tmp.html', auto_open=False)
        # f = open('tmp.html','r')
        # content = f.read()
        # f.close()

        # print("")
        # print("result:")
        # print('')

 
dspace_f = str(sys.argv[1])
num_samples = int(sys.argv[2]) # 50
method = str(sys.argv[3]) # lhs-spacefill
out_csv = str(sys.argv[4])
out_png = str(sys.argv[5])

for o in [out_csv, out_png]:
    odir = os.path.dirname(o)
    if odir:
        os.makedirs(odir, exist_ok=True)

with open(dspace_f) as json_file:
    params = json.load(json_file, object_pairs_hook=OrderedDict)
print(params)

run_doe(params, num_samples, method, out_csv, out_png)
