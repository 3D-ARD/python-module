from ThreeDARD import * 

r = dataset.requests_file("Crane_mesange/asset.json")
open('assets.json', 'wb').write(r.content)
