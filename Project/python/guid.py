from os import path
import xml.etree.ElementTree as ET

PROJECT_FILE="project.rs.xml"

"""

    When we link projects together we need to indicate if we are using a specific
    Version of a layer from another project. We do this by referencing the guid of the parent.

    Looking up a guid can be tedious though so here are 3 methods for doing it with
    various parameters based on what you know about a layer


"""


def getRealizationGuid(projectDir, realizationID, inputID):
    """
    Get a guid if I know the realizationID, the inputID and the project directory
    :param projectDir: Project directory containing the layer I want
    :param realizationID:
    :param inputID:
    :return:
    """
    dom = _getDomfromFile(projectDir)
    element = dom.find("Realizations/*[@id='{0}']//*[@id='{1}']".format(realizationID, inputID))
    if element is None:
        raise Exception("Could not find element with id: {1} inside realization: {0}".format(realizationID, inputID))
    if 'guid' not in element.attrib:
        raise Exception("Element did not have a guid")
    return element.attrib['guid']


def getRealizationGuidFromPath(projectDir, inputPath):
    """
    Get a guid if all I know is the project directory and the relative layer path
    :param projectDir: Project directory containing the layer I want
    :param inputPath: The relative path to the layer I want inside the directory
    :return:
    """
    element = None
    dom = _getDomfromFile(projectDir)
    for layer in dom.findall("Realizations//Path/.."):
        potentialpath = layer.find('Path').text.strip()
        if potentialpath == inputPath:
            element = layer
            break
    if element is None:
        raise Exception("Could not find element with path: {1} inside projectroot: {0}".format(projectDir, inputPath))
    if 'guid' not in element.attrib:
        raise Exception("Element did not have a guid")
    return element.attrib['guid']


def getRealizationGuidFromAbsPath(inputAbsPath):
    """
    Get a Guid if all I have is the raw path of the layer on disk.
    :param inputAbsPath: Absolute path to any layer on the hard drive
    :return:
    """
    # Walk up directories until we find a project file
    pathArr = inputAbsPath.split(path.sep)
    for idx in range(1, len(pathArr)):
        pathsplit = pathArr[:(-idx)]
        potentialDir = path.sep.join(pathsplit)
        if path.isfile(path.join(potentialDir, PROJECT_FILE)):
            projectDir = potentialDir
            break

    if not projectDir:
        raise Exception("Could not find a valid project that contains this layer")

    dom = _getDomfromFile(projectDir)
    relpath = path.relpath(inputAbsPath, projectDir)
    for layer in dom.findall("Realizations//Path/.."):
        potentialpath = layer.find('Path').text.strip()
        if potentialpath == relpath:
            element = layer
            continue

    if element is None:
        raise Exception("Could not find element with id: {1} inside realization: {0}".format(inputAbsPath))
    if 'guid' not in element.attrib:
        raise Exception("Element did not have a guid")
    return element.attrib['guid']


def _getDomfromFile(projDir):
    """
    Helper method for getting a dom from a file
    :param projDir:
    :return:
    """
    projXmlPath = path.join(projDir, PROJECT_FILE)
    if not path.isfile(projXmlPath):
        raise Exception("ERROR: could not find file called: {}".format(projXmlPath))

    DOM = ET.parse(projXmlPath).getroot()
    return DOM

# OK now let's test these out:
if __name__ == "__main__":
    print "getRealizationGuid: " + getRealizationGuid('./', 'run201703171512', 'SOL_RAS')
    print "getRealizationGuidFromPath: " + getRealizationGuidFromPath('./', 'Realizations\\run201703200952\\SolarRasterOutput\\solar_surface_BpS_2016-182-183.tif')

    print "getRealizationGuidFromAbsPath: " + getRealizationGuidFromAbsPath('/Users/work/Projects/RiverScapes/Data/CRB/MiddleForkJohnDay/Network/VBET/02_Analyses/Output_001/MFJD_VBET.shp')