# PyPi Package Index

This is a test visualization to map PyPi package dependencies using [graphistry](https://labs.graphistry.com).

### 1. Download PyPi

Run [1.get_pypi.py](1.get_pypi.py) to produce pypi.tsv (included in the repo, so optional). This is a tab separated file with package names, description, and version.

### 2. Get Package MetaData

Run [2.get_meta.py](2.get_meta.py) to download meta data (a json file) for each package. Optionally, you can filter down to packages to ones that have meta data. This should be all of them, but I haven't finished parsing at the time of writing this README, so there may be some bugs with the PyPi API to be missing package data. Note that this was originally part of my [repofish](http://www.github.com/vsoch/repofish) project (and will continue to be :O) )

### 3. Generate graph input

The input is a simple csv file with target,source, and value column headers. For value, I'll first try using the package monthly downloads. This is generated with [3.map_dependencies.py](3.map_dependencies.py)

### 4. Generate graph

The code to generate the graph is in the ipython notebook [pypi.ipynb](pypi.ipynb). It's so ridiculously easy I just-can't-even! 

You can see the visualization [here](https://labs.graphistry.com/graph/graph.html?type=vgraph&viztoken=fcc371749aa7182d19cbe6d017652f7e95d272e6&usertag=72805b68-pygraphistry-0.9.27&info=true&dataset=Users%2FWWEM9C9GP6_srcjav2l6d69sgfzuxr&play=0)

Note that this only includes packages with links, which reduces the subset down quite a bit.
