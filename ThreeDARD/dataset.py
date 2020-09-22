# 3D-ARD dataset abstraction module
import requests
import os
import json

__LOCAL_DATASET_PATH__ = None

class DatasetInitializationError(Exception):
    """Exception thrown when trying to access an uninitialized dataset"""
    pass


def projectName():
    """Name of the project on archeogrid"""
    return "3D-ARD"
    
def projectId():
    """Id of the project on archeogrid"""
    return "6302"

def init(localpath):
    """Initialize the dataset and link to the local filesystem
    :args: Local path where the dataset is stored.
    :raises: RuntimeError, OSError
    """
    global __LOCAL_DATASET_PATH__
    if __LOCAL_DATASET_PATH__ is None:
        __LOCAL_DATASET_PATH__ = localpath
        if not os.path.exists(localpath):
            os.makedirs(localpath)
    else:
        raise RuntimeError("Local path of the dataset has been already set.")

def isInitialized():
    return __LOCAL_DATASET_PATH__ is not None

def checkInitialized():
    """Check if the dataset has been correctly initialized
    :seealso: init().
    :raises: DatasetInitializationError
    """
    if not isInitialized():
        raise DatasetInitializationError("Local path of the dataset has not been set.")

def requestsFile(relativePath):
    """Use requests library to download file.
    It is not recommended to call this function directly, prefer openFile
    :seealso: openFile().
    """
    return requests.get("https://www-dev.archeogrid.fr/descaladen?type=E&idP=" + projectName() + "&path=" + relativePath, allow_redirects=True)

def openFile(relativePath):
    """Open a file of the dataset, and return its corresponding file object.
    If the file is not in the filesystem, it is downloaded first.
    :seealso: openFile, checkInitialized
    """
    checkInitialized()

    global __LOCAL_DATASET_PATH__
    localpath = __LOCAL_DATASET_PATH__ + "/" + relativePath

    # check if file needs to be downloaded
    if not os.path.exists(localpath):
        # download file
        print ("    Fetching " + relativePath + " from online dataset...")
        r = requestsFile(relativePath)

        # recursively create local path if needed
        dirname   = os.path.dirname(localpath)
        if not os.path.exists(dirname):
            print ("    Creating directory " + dirname)
            os.makedirs(dirname)

        open(localpath, 'wb').write(r.content)
    else:
        print("    Retrieve " + relativePath + " from cache")
    # return read only file descriptor
    return open(localpath, 'r')

def getAssetMeta(assetName):
    return json.load( openFile(assetName + "/asset.json") )

def getUnitMeta(assetName, unitName):
    return json.load( openFile(assetName + "/" + unitName + "/unit.json") )
