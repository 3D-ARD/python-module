from ThreeDARD import *
import json

assets = ["Crane_mesange"]

dataset.init("./dataset")

for a in assets:
    print ("Processing asset " + a)
    asset = dataset.getAssetMeta(a)

    for u in asset["units"]:
        unit   = dataset.getUnitMeta(a, u)
        print ( "[" + u + "] " + unit["name"])

