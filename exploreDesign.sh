#!/bin/bash

infile="inputs.json"
samples="30"
method="lhs-spacefill" # random

runcmd="docker run -it --rm -v $PWD:/scratch -w /scratch mattshax/design_tools"

# RUN THE DOE AND GENERATE INPUT CASES
echo "Generating DOE..."
echo $runcmd python3 ./doe/doe.py $infile $samples $method inputs_doe.csv inputs_doe.png
$runcmd python3 ./doe/doe.py $infile $samples $method inputs_doe.csv inputs_doe.png

# EVALUATE THE DOE
echo "Evaluating DOE..."
echo $runcmd python3 evaluate_doe.py
$runcmd python3 evaluate_doe.py

# VIEW THE RESULTS
echo "Results Generated."

echo "http://localhost:3000"
