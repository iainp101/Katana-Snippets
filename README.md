# Katana-Snippets

### Set_LightFilterReference_Names.py
Sets the names of any lightFilterReference objects listed in the GafferThree node to the name of the filter they are referencing with "LFR_" as a prefix.

### Enable Common InteractiveRenderFilters
```
irfs = ['PLOs', 'Asset_AOVs', 'Moblur_Off', 'Half_Res', 'Hair_Off', 'Overscan_Off'] # Edit this list to your preferred render filters
rfList = []

for i in irfs:
    rfnode = NodegraphAPI.GetNode(i)
    rfList.append(rfnode)
    
rfDelegate = RenderManager.InteractiveRenderDelegateManager.GetRenderFiltersDelegate()
rfDelegate.setActiveRenderFilterNodes(rfList)
```
