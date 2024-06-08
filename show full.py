node_type = hou.sopNodeTypeCategory().nodeType("file") # find the node type "file"
nodes = node_type.instances() # find nodes of this type

# for all nodes, switch the display mode to "All Geometry"
for node in nodes:
    node.parm("loadtype").set(0)
    
