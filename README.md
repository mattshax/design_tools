# Design Exploration Tools

This repository contains a number of utility scripts for exploring design spaces. It draws upon many open source projects and common design exploration methods across disciplines. 

More specifically this repo allows a user to provide a JSON input file containing keys with min/max values describing the design space. With this input data, a Design of Experiment is run to generate input samples across the design space. A modular wrapper script allows the user to specify a model to evaluate with each DOE case, and a resulting csv and sensitivity plot is produced. With the resulting csv file, a design explorer visualization is started to interact with and parse through the results.

The specific open-source tools featured in this repo are outlined below (all MIT license):

* doepy - https://github.com/tirthajyoti/doepy
* Plotly - https://github.com/plotly/plotly.py
* DesignExplorer - https://github.com/tt-acm/DesignExplorer

#### Installation & Run Instructions

These tools use docker for portability. Install docker using the below command:

```
apt-get install git curl

curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

Now you should be able to run the design explorer tools using the commands below:

```

# install DesignExplorer with custom patches
./DesignExplorer_patch/install.sh

# run the design exploration a docker container
./exploreDesign.sh

# you should now have the below files in your run directory:
    # inputs_doe.csv - doe input samples
    # inputs_doe.png - doe input image
    # outputs_doe.csv - doe case evaluations
    # outputs_sensitivity.html - doe sensitivity plot

# run the visualizer
PORT=3000
./runDesignExplorer.sh $PORT

# navigate to http://localhost:3000 to explore results

```
