#!/bin/bash

infile="../inputs.json"
samples="300"
method="lhs-spacefill" # 

python3 doe.py $infile $samples $method ../doe.csv ../doe.png
