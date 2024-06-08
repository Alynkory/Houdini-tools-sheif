obj = hou.node("/obj/") # turning to the obj context

# creating a geocontainer, it is created by calling a method on its parent node, its parent node is the obj context
geo_container = obj.createNode("geo") 

file_path = hou.ui.selectFile() # open a window to select a file

file_node = geo_container.createNode("file") # creating file node
file_parm = file_node.parm("file") # refer to the Geometry File parameter of the new file node
file_parm.set(file_path) # setting the path of the selected file as the parameter value
splitted_path = file_path.split("/") # splitting the path into sections
file_name = splitted_path[-1] # we take the last part as the file name
geo_container.setName(file_name) # rename the geo node with the name obtained above

# creating additional nodes
unpack_node = geo_container.createNode("unpack")  
unpack_node.setInput(0,file_node) # connecting file node with unpack
unpack_node.moveToGoodPosition() # align the nodes vertically

transform_node = geo_container.createNode("xform")
transform_node.setInput(0,unpack_node) 
transform_node.moveToGoodPosition() 

null_node = geo_container.createNode("null") 
null_node.setInput(0,transform_node) 
null_node.moveToGoodPosition() 

# repainting the null node in red
red = hou.Color((1.0, 0 , 0)) 
null_node.setColor(red) 

# renaming the node null 
null_name = file_name.split(".")[-2]  
null_node.setName("OUT_" + null_name) 
