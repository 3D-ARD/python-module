from ThreeDARD import *
import colored, os

dataset.init("./dataset")
dataset.verbose = True

forceSync = True
printFileContent = True
fetch3D = False

def printError(message):
    print(colored.stylize(message, colored.fg("red")))

def printFile(filename):
    print(colored.stylize(open(filename, 'r').read() , colored.bg("light_red")))


d = dataset.getDatasetMeta(forceSync)
for a in d["units"]:
    print ("Processing asset " + a)
    asset = None
    try:
        asset = dataset.getAssetMeta(a, forceSync)
    except (ValueError):
        printError("Error when loading {} metadata".format(a))
        if printFileContent:
            relativePath = os.path.join(dataset.getAssetRelativeDirectory(a), "asset.json")
            printFile(dataset.getSynchronizedFilePath( relativePath ))
    else:

        for u in asset["units"]:
            unit = None

            try:
                unit = dataset.getUnitMeta(a, u, forceSync)
            except (ValueError):
                printError ("Error when loading {} (unit {}) metadata".format(a, u))
                if printFileContent:
                    relativePath = os.path.join(dataset.getUnitRelativeDirectory(a,u), "unit.json")
                    printFile(dataset.getSynchronizedFilePath( relativePath ))
            else:
                print ( "[" + u + "] " + unit["name"])

                if fetch3D:
                    #check if any .xyz file can be found
                    for entry in unit["outputs"]:
                        if entry["filename"].endswith(".xyz"):

                            # 3d model found, getting relative path in the dataset
                            filename = dataset.getUnitRelativeDirectory(a, u) + "/" + entry["filename"]
                            print("3d model found in dataset: " + filename)

                            # download (if needed only) and get the 3d model
                            sfilename = dataset.getSynchronizedFilePath( filename)
                            print("3d model downloaded at " + sfilename)

