# 3D-ARD dataset abstraction module
import requests


# Name of the project on archeogrid
def project_name(): 
    return "3D-ARD"
    
# Id of the project on archeogrid
def project_id(): 
    return "6302"

# Use requests library to download file
def requests_file(path):
    return requests.get("https://www-dev.archeogrid.fr/descaladen?type=E&idP=" + project_name() + "&path=" + path, allow_redirects=True)

