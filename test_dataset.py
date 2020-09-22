from ThreeDARD import *

assets = ["Maitreya_Buddha", "Dame_d_Elche", "Os", "Jonque", "Guitare_tatou", "Annexe_Haut_Carre",  "Crane_mesange"]

dataset.init("./dataset")
dataset.verbose = False

def test_forcingAssetsMeta():
    for a in assets:
        print ("Processing asset " + a)
        asset = dataset.getAssetMeta(a, forceSync=True)

def test_browsingAssetsMeta():
    for a in assets:
        print ("Processing asset " + a)
        asset = dataset.getAssetMeta(a)

def test_browsingUnitsMeta():
    for a in assets:
        print ("Processing asset " + a)
        asset = dataset.getAssetMeta(a)

    for u in asset["units"]:
        unit   = dataset.getUnitMeta(a, u)
        print ( "[" + u + "] " + unit["name"])

