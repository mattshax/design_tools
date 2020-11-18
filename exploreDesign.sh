#!/bin/bash

infile="inputs.json"
samples="50"
method="lhs-spacefill" # random

# RUN THE DOE AND GENERATE INPUT CASES
echo "Generating DOE..."
python3 ./doe/doe.py $infile $samples $method inputs_doe.csv inputs_doe.png

# EVALUATE THE DOE
echo "Evaluating DOE..."
python3 evaluate_doe.py

# VIEW THE RESULTS
echo "Results Generated."

echo "http://localhost:3000"
