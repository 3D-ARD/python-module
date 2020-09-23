from ThreeDARD import *
import colored, os

dataset.init("./dataset")
dataset.verbose = False

forceSync = False
printFileContent = True
fetch3D = False

def printError(message):
    print(colored.stylize(message, colored.fg("red")))

def printFile(filename):
    print(colored.stylize(open(filename, 'r').read() , colored.bg("light_red")))


d = dataset.getDatasetMeta(forceSync)
for a in d["units"]:
    print ("\nProcessing asset " + a)
    asset = None
    try:
        asset = dataset.getAssetMeta(a, forceSync)
    except ValueError:
        printError("Syntax error when parsing {} metadata".format(a))
        if printFileContent:
            relativePath = os.path.join(dataset.getAssetRelativeDirectory(a), "asset.json")
            printFile(dataset.getSynchronizedFilePath( relativePath ))
    except dataset.RemoteFileNotFountError:
        printError("FileNotFound: asset metadata not available on remote for asset {}".format(a))
    else:

        for u in asset["units"]:
            unit = None

            try:
                unit = dataset.getUnitMeta(a, u, forceSync)
            except (ValueError):
                printError ("[{}] Syntax error when parsing metadata".format(u))
                if printFileContent:
                    relativePath = os.path.join(dataset.getUnitRelativeDirectory(a,u), "unit.json")
                    printFile(dataset.getSynchronizedFilePath( relativePath ))
            except dataset.RemoteFileNotFountError:
                printError("[{}] FileNotFound: unit metadata not available on remote)".format(u))
            else:
#                print ( "[" + u + "] " + unit["name"] + " (software = " + str(unit["software"]) + "). Files: " + str(unit["outputs"]))
                print ( "[" + u + "] " + unit["name"] + " (software = " + str(unit["software"]) + ").")


                # check file consistency
                for entry in unit["outputs"]:
                    filename = dataset.getUnitRelativeDirectory(a, u) + "/" + entry["filename"]
                    if not dataset.checkFileExistsOnRemote(filename):
                        printError("[{}] FileNotFound: {}".format(u, filename))

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
