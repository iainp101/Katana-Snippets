import PackageSuperToolAPI
from Katana import Plugins

GafferThreeAPI = Plugins.GafferThreeAPI

def findChildren(groupPackage, packageClass):
    result = []
    for childPackage in groupPackage.getChildPackages():
        if isinstance(childPackage, packageClass):
            result.append(childPackage)
        elif isinstance(childPackage, PackageSuperToolAPI.Packages.GroupPackage):
            result.extend(findChildren(childPackage, packageClass))
    return result

upstreamGafferThreeNode = node

lightFilterReferencePackages = findChildren(upstreamGafferThreeNode.getRootPackage(), GafferThreeAPI.
PackageClasses.LightFilterReferencePackage)

print('Upstream light creation packages create the following light locations:')

for lightFilterReferencePackage in lightFilterReferencePackages:
    internalNode = lightFilterReferencePackage.getInternalNode()
    x = NodegraphAPI.GetNode(str(internalNode.getName()))
    refPath = x.getParameter('lightList.referencePath').getValue(0)
    refName = refPath.split('/')
    refName = refName[-1]
    packageNode = lightFilterReferencePackage.getPackageNode()
    y = NodegraphAPI.GetNode(str(packageNode.getName()))
    location = y.getParameter('__gaffer.location')#.getValue(0)
    newLocation = (location.getValue(0)).split('/')
    newLocation = ('/'.join(newLocation[:-1]))+'/LFR_'+refName
    location.setValue(newLocation,0)
