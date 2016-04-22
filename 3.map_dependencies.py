from repofish.utils import save_json
import numpy
import pandas
import json
import os 

folder = os.getcwd()
packages = pandas.read_csv("%s/pypi.tsv" %folder,sep="\t",index_col=0)

# NODEJS VISUALIZATIOn #########################################################
df = pandas.DataFrame(columns=["source","target","value"])

count=1
for row in packages.iterrows():
    package_name = row[1].package
    meta_file = "%s/%s.json" %(meta_folder,package_name)
    if os.path.exists(meta_file):
        meta = json.load(open(meta_file,"r"))
        if "requires_dist" in meta["info"]:
            dependencies = meta["info"]["requires_dist"]
            dependencies = [x.split(" ")[0].strip() for x in dependencies]
            for dep in dependencies:
                downloads = meta["info"]["downloads"]["last_month"]
                df.loc[count] = [package_name,dep,downloads] 
                count+=1

# Save to file
df.to_csv("pypi.csv",inde=False)
