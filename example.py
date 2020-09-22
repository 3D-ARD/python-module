from ThreeDARD import *

assets = ["Crane_mesange"]

dataset.init("./dataset")
dataset.verbose = False

for a in assets:
    print ("Processing asset " + a)
    asset = dataset.getAssetMeta(a)

    for u in asset["units"]:
        unit   = dataset.getUnitMeta(a, u)
        print ( "[" + u + "] " + unit["name"])

        #check if any .xyz file can be found
        for entry in unit["outputs"]:
            if entry["filename"].endswith(".xyz"):

                # 3d model found, getting relative path in the dataset
                filename = dataset.getUnitRelativeDirectory(a, u) + "/" + entry["filename"]
                print("3d model found in dataset: " + filename)

                # download (if needed only) and get the 3d model
                sfilename = dataset.getSynchronizedFilePath( filename)
                print("3d model downloaded at " + sfilename)

