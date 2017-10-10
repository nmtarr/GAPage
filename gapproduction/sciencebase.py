## Functions to use for connecting to and interacting with ScienceBase
##
##
import gapconfig

# The top level ScienceBase Item ID for the GAP habitat maps
habMapCollectionItem = "527d0a83e4b0850ea0518326"

#### Function to establish a connection to ScienceBase
def ConnectToSB(username=gapconfig.sbUserName):
    """
    (string) -> connection to ScienceBase
    
    Creats a connection to ScienceBase. You will have to enter your password.
    
    Arguments:
    username -- your ScienceBase user name.
    
    Example:
    >> connection = ConnectToSB(username="ntarr@usgs.gov")
    """
    import pysb
    sb = pysb.SbSession()
    sb.loginc(str(username))
    return sb

#### Function to get list of habitat map child items
def HabitatMapIDs():
    """
    () -> list
    
    Returns a list of habitat map IDs by listing child items of the top
    level ScienceBase item for the GAP habitat maps.
    
    Example:
    >> mapIDs = HabitatMapIDs()
    """
    sb = ConnectToSB()
    global habMapCollectionItem
    habitatMapIDs = sb.get_child_ids(habMapCollectionItem)
    return habitatMapIDs

#### Function to get a list of strUCs loaded to ScienceBase
def ListUCs():
    """
    () -> list
    
    Returns a list of all the strUC species codes for species that have been
    uploaded onto ScienceBase.  
    
    NOTE:
    This is very slow.
    
    Example:
    >> UCs = ListUCs()
    """
    sb = ConnectToSB()
    habitatMapIDs = HabitatMapIDs()
    UCs = [sb.get_item(x)["identifiers"][0]["key"] for x in habitatMapIDs[:]]
    return UCs
