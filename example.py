from ThreeDARD import *
import colored, os

assets = ["Maitreya_Buddha", "Dame_d_Elche", "Os", "Jonque", "Guitare_tatou", "Annexe_Haut_Carre",  "Crane_mesange"]

dataset.init("./dataset")
dataset.verbose = False

def printError(message):
    print(colored.stylize(message, colored.fg("red")))

def printFile(filename):
    print(colored.stylize(open(filename, 'r').read() , colored.bg("light_red")))

for a in assets:
    print ("Processing asset " + a)
    asset = None
    try:
        asset = dataset.getAssetMeta(a)
    except (ValueError):
        printError("Error when loading {} metadata".format(a))
        #relativePath = os.path.join(dataset.getAssetRelativeDirectory(a), "asset.json")
        #printFile(dataset.getSynchronizedFilePath( relativePath ))
    else:

        for u in asset["units"]:
            unit = None

            try:
                unit = dataset.getUnitMeta(a, u)
            except (ValueError):
                printError ("Error when loading {} (unit {}) metadata".format(a, u))
                #relativePath = os.path.join(dataset.getUnitRelativeDirectory(a,u), "unit.json")
                #printFile(dataset.getSynchronizedFilePath( relativePath ))
            else:
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

