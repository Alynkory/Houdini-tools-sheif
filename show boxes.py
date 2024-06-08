# find the camera
camera_node_type = hou.objNodeTypeCategory().nodeType("cam") # find the node Type "Camera"
cameras = camera_node_type.instances() # find nodes of the type "Camera"
camera = cameras[0] # take the first camera found

# finding the camera position
t = camera.parmTuple("t").eval() # find the value of the parameter "translate"
camera_pos = hou.Vector3(t) #creating a vector
print("camera_pos", camera_pos) # displaying the camera position in the console

# we ask the user for the maximum distance in the dialog box
max_distance = float(hou.ui.readInput(message="Max distance")[1]) 
print("Max distance:", max_distance) 

# finding files
file_node_type = hou.sopNodeTypeCategory().nodeType("file")
files = file_node_type.instances()

# perform further actions for each file
for file in files:#
    parent = file.parent() # find the geonode that contains the file
    if parent.name() == "cam1": # if it's a camera, then skip it
        continue

    t = parent.parmTuple("t").eval() # turn to the translate parameter of the geonode and take its value
    parent_pos = hou.Vector3(t) # creating a vector
    print("Geo node name:", parent.name()) # output the name of the parent node 
    print("position:", parent_pos) # output the position of the parent node
    
    pos_diff = camera_pos - parent_pos # find the difference of vectors, the difference of positions
    distance = pos_diff.length() # find the length of this difference
    print("Distance:", distance) # output the result
    
    if distance > max_distance: # if the length of the difference is greater than the value entered by the user
        file.parm("loadtype").set(1) # the object is displayed as a box
