#!/usr/bin/env python
from ThreeDARD import *

assets = ["Maitreya_Buddha", "Dame_d_Elche", "Os", "Jonque", "Guitare_tatou", "Annexe_Haut_Carre",  "Great Tit Skull"]

dataset.init("./dataset")
dataset.verbose = True

forceSync = True

d = dataset.getDatasetMeta(forceSync)
assets = d["assets"]

def test_forcingAssetsMeta():
    for a in assets:
        print ("Processing asset " + a)
        asset = dataset.getAssetMeta(a, forceSync)

def test_browsingAssetsMeta():
    for a in assets:
        print ("Processing asset " + a)
        asset = dataset.getAssetMeta(a, forceSync)

def test_browsingUnitsMeta():
    for a in assets:
        print ("Processing asset " + a)
        asset = dataset.getAssetMeta(a, forceSync)

    for u in asset["units"]:
        unit   = dataset.getUnitMeta(a, u, forceSync)
        print ( "[" + u + "] " + unit["name"])

