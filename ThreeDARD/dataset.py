# 3D-ARD dataset abstraction module
import requests
import os
import json

__LOCAL_DATASET_PATH__ = None
verbose = True

class DatasetInitializationError(Exception):
    """Exception thrown when trying to access an uninitialized dataset"""
    pass

################################################################################
# Utilities
################################################################################
def verboseLog(message):
    if verbose: print ("    " + message)

def projectName():
    """Name of the project on archeogrid"""
    return "3D-ARD"
    
def projectId():
    """Id of the project on archeogrid"""
    return "6302"

def init(localpath):
    """Initialize the dataset and link to the local filesystem
    :args: Local path where the dataset is stored. Can be retrieved using getLocalPath()
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


################################################################################
# Internals
################################################################################
def __checkInitialized__():
    """Check if the dataset has been correctly initialized
    :seealso: init().
    :raises: DatasetInitializationError
    """
    if not isInitialized():
        raise DatasetInitializationError("Local path of the dataset has not been set.")

def __fetchFile__(relativePath):
    """Use requests library to download file.
    It is not recommended to call this function directly, prefer getSynchronizedFilePath
    :seealso: getSynchronizedFilePath().
    """
    return requests.get("https://www-dev.archeogrid.fr/descaladen?type=E&idP=" + projectName() + "&path=" + relativePath, allow_redirects=True)


################################################################################
# Getters
################################################################################
def getLocalPath():
    __checkInitialized__()
    return __LOCAL_DATASET_PATH__

def getAssetRelativeDirectory(assetName):
    """Relative path of a given asset.
    Relative paths are expressed relatively to getLocalPath().
    :seealso: init().
    """
    return assetName

def getUnitRelativeDirectory(assetName, unitName):
    """Relative path of the unit of a given asset.
    Relative paths are expressed relatively to getLocalPath().
    :seealso: init().
    """
    return getAssetRelativeDirectory(assetName) + "/" + unitName


################################################################################
# Fetching and loading data
################################################################################
def getSynchronizedFilePath(relativePath, forceSync = False):
    """Get the path on the current filesystem from a file in the dataset.
    If the file is not in the filesystem, it is downloaded first.

    This function is used to download and synchronise data from online dataset.
    To access metadata, it is recommended to use getAssetMeta and getUnitMeta
    directly.

    :seealso: getAssetMeta, getUnitMeta
    """
    __checkInitialized__()

    global __LOCAL_DATASET_PATH__
    localpath = os.path.join(__LOCAL_DATASET_PATH__, relativePath)

    # check if file needs to be downloaded
    if not os.path.exists(localpath) or forceSync:
        # download file
        verboseLog ("Fetching " + relativePath + " from online dataset...")
        r = __fetchFile__(relativePath)

        # recursively create local path if needed
        dirname   = os.path.dirname(localpath)
        if not os.path.exists(dirname):
            verboseLog ("Creating directory " + dirname)
            os.makedirs(dirname)

        open(localpath, 'wb').write(r.content)
    else:
        verboseLog("Retrieve " + relativePath + " from cache")
    # return read only file descriptor
    return localpath

def getAssetMeta(assetName, forceSync = False):
    """Get the metadata of a given asset. The metadata file is fetched if needed.
    :seealso: getSynchronizedFilePath()
    """
    relativePath = os.path.join(getAssetRelativeDirectory(assetName), "asset.json")
    localpath = getSynchronizedFilePath( relativePath, forceSync )
    return json.load( open(localpath, 'r') )

def getUnitMeta(assetName, unitName, forceSync = False):
    """Get the metadata of a given unit. The metadata file is fetched if needed.
    :seealso: getSynchronizedFilePath()
    """
    relativePath = os.path.join(getUnitRelativeDirectory(assetName, unitName), "unit.json")
    localpath = getSynchronizedFilePath( relativePath, forceSync )
    return json.load( open(localpath, 'r') )
