import bpy
import json
import os
from pathlib import Path

# Delete All Existance Elements
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

my_areas = bpy.context.workspace.screens[0].areas
my_shading = 'MATERIAL'  # 'WIREFRAME' 'SOLID' 'MATERIAL' 'RENDERED'

Drct    = open(os.getcwd()+'/app/link/script.dir', "r" ).read()
Methods = open(os.getcwd()+'/app/link/script00.py', "r" ).read()

FileName = (Path(Drct).stem)

assm = []
zpln = []

if Methods == 'NEM':
    with open(Drct) as json_data:
        data = json.load(json_data)
        mode = data['Data']['Parameters']['Calculation Mode']
        nmat = data['Data']['Parameters']['Number of Materials']
        np  = data['Data']['Parameters']['Number of Planar'] 
        nx = len( data['Data']['Assemblies'][0]['Assembly'][0])
        ny = len( data['Data']['Assemblies'][0]['Assembly'])
        zplan = data['Data']['Parameters']['Planar Assignement to Z']
        assm = data['Data']['XY_Assembly']

# Transform Z-Plannar of Numbers to Z-Plannar of Materials
for i in zplan : 
    for j in range(np):
        if i == j+1:
            zpln.append(assm[j])

# Number of Axial Planes
nz = len(zpln)

# Reverse Assemblies Order in Planes
#for o in range(nz):

if FileName == 'IAEA_2D' :
    zpln[0].reverse()

# Set Colors
Red      = [0.715694,0.006995,0.045186,1]
Blue     = [0.033105,0.3564,0.584079,1]
Green    = [0,0.571125,0.262251,1]
Yellow   = [1,0.838799,0.258183,1]
SkyBlue  = [0,1,1,1]
Brown    = [0.955974,0.21586,0.168269,1]
Pink     = [1,0.533276,0.533277,1]
SkyGreen = [0.412543,1,0.571125,1]

Colors = [Blue,Red,Green,Yellow,SkyBlue,Brown,Pink,SkyGreen]

# Initialize Positions
xpos = 0
ypos = 0
zpos = 0

#Initialize Axial Variable
v_zp = 0

#Initialize Assembly Variable
v_cube = 0

#Initialize Total Number of Assemblies in Plane
TotAsm = 0

# Total Number of Assemblies in Whole Core Reactor
for k in range(nz):
    for j in range(ny):
        for i in range(nx):
            if zpln[k][j][i] != 0:
                TotAsm += 1

# Set of Axial Planes
for s in range(nz):

    # Set Number of Assemblies
    for m in range(ny):

        # Select Specific Plane by Order
        for i in zpln[v_zp][m]:
                
            # Set Materials
            for n in range(nmat):
                if i == n+1:
                                
                    # Create Cubes at locations
                    bpy.ops.mesh.primitive_cube_add(size=2, location=(xpos,ypos+2*m,zpos*2))
                            
                    # Ennhance The Edges of the Cube
                    bpy.ops.object.modifier_add(type='BEVEL')
                    bpy.context.object.modifiers["Bevel"].segments = 10
                    bpy.context.object.modifiers["Bevel"].width = 0.2
                    bpy.ops.object.shade_smooth()
                            
                    obj = bpy.context.object
                    obj.color = (1,1,0,1)
                                
                    # Create a material
                    mat = bpy.data.materials.new("Color : "+ str(i))

                    # Activate its nodes
                    mat.use_nodes = True

                    # Get the principled BSDF (created by default)
                    principled = mat.node_tree.nodes['Principled BSDF']

                    # Assign the color
                    principled.inputs['Base Color'].default_value = Colors[i-1]

                    # Assign the material to the object
                    obj.data.materials.append(mat)

                    v_cube += 1
                    print ( '  Plotting Progression ......', int((v_cube/TotAsm)*100),'%')

                    #print('v_cube=',v_cube)

                    #if i == 0:
                        #bpy.ops.mesh.primitive_uv_sphere_add(radius=0, location=(xpos,ypos+2*m,zpos))
                        #bpy.ops.object.delete(use_global=False)
            xpos += 2
        xpos=0
        ypos=0

    v_zp +=1
    
    if s < nz-1 :
        if zplan[s+1]  == zplan[s]:
            zpos += 1
        else : 
            zpos += 6        

print( '     ---------------------')
print( 'Plotting Finished, Geometry is Preparing...')

# bpy.ops.object.select_all(action='SELECT')
# Duplicate 1/4 of Core & Symmetrisize it
# bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-(ny*2-2), -0, -0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(True, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
# bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False))


# bpy.ops.object.select_all(action='SELECT')
# Duplicate 1/2 of Core & Symmetrisize it
# bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, (ny*2-2), 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, True, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
# bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False))

# Reallocate to Center
bpy.ops.object.select_all(action='SELECT')
bpy.ops.transform.translate(value=(-0, -(ny*2-2), -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

bpy.ops.object.select_all(action='DESELECT')
print( '     ---------------------')

# Set keys
zpos = 0
for i in range(nmat):
        def createObject():
            
            bpy.ops.mesh.primitive_cube_add(size=2, location=(nx*2+5,0,zpos*6))
                            
            # Ennhance The Edges of the Cube
            bpy.ops.object.modifier_add(type='BEVEL')
            bpy.context.object.modifiers["Bevel"].segments = 10
            bpy.context.object.modifiers["Bevel"].width = 0.2
            bpy.ops.object.shade_smooth()
                            
            obj = bpy.context.object
            obj.color = (1,1,0,1)
                                
            # Create a material
            mat = bpy.data.materials.new("Color : "+ str(i))

            # Activate its nodes
            mat.use_nodes = True

            # Get the principled BSDF (created by default)
            principled = mat.node_tree.nodes['Principled BSDF']

            # Assign the color
            principled.inputs['Base Color'].default_value = Colors[i]

            # Assign the material to the object
            obj.data.materials.append(mat)
            # Create and name TextCurve object
            bpy.ops.object.text_add(
            location=(nx*2+10,0,i*6),
            rotation=(3.141592653589793/2,0,0))
            ob = bpy.context.object
            ob.name = 'MyObjectName'
            tcu = ob.data
            tcu.name = 'MyTextCurveName'
            tcu.body = "Material_"+ str(i+1)
            tcu.font = bpy.data.fonts[0]
            tcu.offset_x = -3
            tcu.offset_y = -0.25
            tcu.shear = 0.3
            tcu.size = 3
            tcu.space_character = 1
            tcu.space_word = 4
             
            # Inherited Curve attributes
            tcu.extrude = 0.2
            tcu.fill_mode="FRONT"
            tcu.use_fill_deform = True
            tcu.fill_mode="FRONT"

            return ob
            
        # if __name__ == "__main__":
            
        createObject()
        zpos += 1

for area in my_areas:
    for space in area.spaces:
        if space.type == 'VIEW_3D':
            space.shading.type = my_shading

bpy.ops.wm.save_mainfile(filepath=FileName+'.blend')