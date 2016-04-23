# PyPy Package Index

This is a test visualization to map PyPi package dependencies using [graphistry](https://labs.graphistry.com).

### 1. Download PyPi

Run [1.get_pypi.py](1.get_pypi.py) to produce pypi.tsv (included in the repo, so optional). This is a tab separated file with package names, description, and version.

### 2. Get Package MetaData

Run [2.get_meta.py](2.get_meta.py) to download meta data (a json file) for each package. Optionally, you can filter down to packages to ones that have meta data. This should be all of them, but I haven't finished parsing at the time of writing this README, so there may be some bugs with the PyPi API to be missing package data. Note that this was originally part of my [repofish](http://www.github.com/vsoch/repofish) project (and will continue to be :O) )

### 3. Generate graph input

The input is a simple csv file with target,source, and value column headers. For value, I'll first try using the package monthly downloads. This is generated with [3.map_dependencies.py](3.map_depencies.py)

### 4. Generate graph

The code to generate the graph is in the ipython notebook [pypi.ipynb](pypi.ipynb). It's so ridiculously easy I just-can't-even! 

I'm still running step 2 myself, so I only have about 4000 links in my graph. The small (incomplete) version is [here](https://labs.graphistry.com/graph/graph.html?type=vgraph&viztoken=a469101e3b93976edf84204a37c664150a0d9afd&usertag=72805b68-pygraphistry-0.9.27&splashAfter=1461369066&info=true&dataset=Users%2F5RXJD0BWP7_9unt4jk56xjguzo20529&play=0
)

Super looking forward to trying out more advanced features for this library. For pypi, when my meta data finishes downloading, I will update the visualization soon!

