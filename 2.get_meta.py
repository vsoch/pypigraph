# get_meta will use pypi API to get meta data about packages

import requests
import pandas
import json
import time
import os

# Function to save pretty json
def save_json(json_obj,output_file):
    filey = open(output_file,'wb')
    filey.write(json.dumps(json_obj, sort_keys=True,indent=4, separators=(',', ': ')))
    filey.close()
    return output_file


url = "https://pypi.python.org/pypi/%s/json"

# Load functions
folder = os.getcwd()
packages = pandas.read_csv("%s/pypi.tsv" %folder,sep="\t",index_col=0)

meta_folder = "%s/packages" %(folder)

if not os.path.exists(meta_folder):
    os.mkdir(meta_folder)

# We will keep track of rows to drop
drop = []

for row in packages.iterrows():
    package_name = row[1].package
    output_file = "%s/%s.json" %(meta_folder,package_name)
    if not os.path.exists(output_file):
        time.sleep(1)
        print "parsing %s of %s" %(row[0],packages.shape[0])
        response = requests.get(url %package_name)
        if response.status_code == 200:
            save_json(response.json(),output_file)
        else:
            print "Error getting meta data for package %s" %(package_name)
            drop.append(row[0])

# Remove the functions we don't have meta data for
packages = packages.drop(drop)
packages.to_csv("%s/pypi_filtered.tsv"%folder,sep="\t",encoding="utf-8")
