#!/usr/bin/env python

"""
This file is part of the 3D-ARD dataset python abstraction module

This example demonstrates how to browse the repository by downloading only the
metadata, and check that all files mentionned in metadata can be downloaded from
the server.

Project website: https://3dard.cnrs.fr/
Github repository: https://github.com/3D-ARD/python-module
"""

from ThreeDARD import *
import colored, os

dataset.init("./dataset")
dataset.verbose = False

forceSync = False
printFileContent = True

def printError(message):
    print(colored.stylize(message, colored.fg("red")))

def printFile(filename):
    print(colored.stylize(open(filename, 'r').read() , colored.bg("light_red")))


try:
    d = dataset.getDatasetMeta(forceSync)
except dataset.RemoteFileNotFountError:
    printError("FileNotFound: dataset metadata not available on remote.")
    quit()

for a in d["assets"]:
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
                print ("[{}] {} ".format(u, unit["name"]) + (colored.stylize("(process)", colored.fg("blue")) if unit["type"] == "process" else colored.stylize("(acquisition)", colored.fg("green"))))
                print("   Author: " + unit["author"])
                if unit["hardware"]: print ("   Hardware: " + str(unit["hardware"]) + ".")
                if unit["software"]: print ("   Software: " + str(unit["software"]) + ".")
                print("   Description: " + unit["description"])
                print(("   Details: " + unit["details"] if not unit["details"] else "   No details given"))


                # check file consistency
                for entry in unit["outputs"]:
                    filename = dataset.getUnitRelativeDirectory(a, u) + "/" + entry["filename"]
                    if not dataset.checkFileExistsOnRemote(filename):
                        printError("[{}] FileNotFound: {}".format(u, filename))

                # check input relationships consistency
                if unit["inputs"]:
                    print( "   Takes as input {}".format(unit["inputs"]))
                    for u2 in unit["inputs"]:
                        try:
                            unit = dataset.getUnitMeta(a, u2, forceSync)
                        except dataset.RemoteFileNotFountError:
                            printError("FileNotFound: unit {} takes as input unit {}, which does not exists in the dataset".format(u,u2))


                # check input relationships consistency
                if unit["related"]:
                    print( "   Is related to {}".format(unit["inputs"]))
                    for u2 in unit["related"]:
                        try:
                            unit = dataset.getUnitMeta(a, u2, forceSync)
                        except dataset.RemoteFileNotFountError:
                            printError("FileNotFound: unit {} is related to unit {}, which does not exists in the dataset".format(u,u2))











