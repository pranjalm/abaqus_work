
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior


#mdb.models.changeKey(fromName='Model-1', toName='mgdd')
mdb.Model(name='mgdd', modelType=STANDARD_EXPLICIT)
a = mdb.models['mgdd']
s = a.ConstrainedSketch(name='bb_rail', sheetSize=1.0)
s.rectangle(point1=(0.0, 0.0), point2=(0.066, 0.132))
p = a.Part(name='bb_rail', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = a.ConstrainedSketch(name='pad', sheetSize=1.0)
s.Line(point1=(0.0, 0.083214), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.086, 0.0))
s.Line(point1=(0.086, 0.0), point2=(0.086, 0.065536))
s.Line(point1=(0.086, 0.065536), point2=(0.076, 0.065536))
s.Line(point1=(0.076, 0.065536), point2=(0.076, 0.01))
s.Line(point1=(0.076, 0.01), point2=(0.01, 0.01))
s.Line(point1=(0.01, 0.01), point2=(0.01, 0.083214))
s.Line(point1=(0.01, 0.083214), point2=(0.0, 0.083214))
p = a.Part(name='pad', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

p = a.parts['pad']
f, v, c, d = p.faces, p.vertices, p.cells, p.datums
p.DatumPlaneByOffset(plane=f[4], point=v[4])
p.DatumPlaneByOffset(plane=f[4], point=v[1])
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)

p.DatumPlaneByOffset(plane=f[9], flip=SIDE1, offset=0.0)
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=pickedCells)

s = a.ConstrainedSketch(name='grout', sheetSize=1.0)
s.Line(point1=(0.0, 0.108214), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.136, 0.0))
s.Line(point1=(0.136, 0.0), point2=(0.136, 0.090536))
s.Line(point1=(0.136, 0.090536), point2=(0.116, 0.090536))
s.Line(point1=(0.116, 0.090536), point2=(0.116, 0.02))
s.Line(point1=(0.116, 0.02), point2=(0.02, 0.02))
s.Line(point1=(0.02, 0.02), point2=(0.02, 0.108214))
s.Line(point1=(0.02, 0.108214), point2=(0.0, 0.108214))
p = a.Part(name='grout', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

p = a.parts['grout']
f, v, c, d = p.faces, p.vertices, p.cells, p.datums
p.DatumPlaneByOffset(plane=f[4], point=v[4])
p.DatumPlaneByOffset(plane=f[4], point=v[1])
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)

p.DatumPlaneByOffset(plane=f[9], flip=SIDE1, offset=0.0)
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=pickedCells)
	
s = a.ConstrainedSketch(name='shell', sheetSize=1.0)
s.Line(point1=(0.0, 0.088214), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.096, 0.0))
s.Line(point1=(0.096, 0.0), point2=(0.096, 0.070536))
s.Line(point1=(0.096, 0.070536), point2=(0.091, 0.070536))
s.Line(point1=(0.091, 0.070536), point2=(0.091, 0.005))
s.Line(point1=(0.091, 0.005), point2=(0.005, 0.005))
s.Line(point1=(0.005, 0.005), point2=(0.005, 0.088214))
s.Line(point1=(0.005, 0.088214), point2=(0.0, 0.088214))
p = a.Part(name='shell', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

p = a.parts['shell']
f, v, c, d = p.faces, p.vertices, p.cells, p.datums
p.DatumPlaneByOffset(plane=f[4], point=v[4])
p.DatumPlaneByOffset(plane=f[4], point=v[1])
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)

p.DatumPlaneByOffset(plane=f[9], flip=SIDE1, offset=0.0)
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=pickedCells)

s = a.ConstrainedSketch(name='infi_bottom', sheetSize=20.0)
s.rectangle(point1=(0.0, 0.0), point2=(8.0, 1.0))
p = a.Part(name='infi_bottom', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = a.ConstrainedSketch(name='infi_side', sheetSize=20.0)
s.rectangle(point1=(0.0, 0.0), point2=(1.0, 16.0))
p = a.Part(name='infi_side', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = a.ConstrainedSketch(name='wheel', sheetSize=1.0)
s.rectangle(point1=(0.0, 0.0), point2=(0.066, 0.1))
p = a.Part(name='wheel', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=0.2)

s = a.ConstrainedSketch(name='substructure', sheetSize=50.0)
s.Line(point1=(0.0, 0.0), point2=(0.0, 16.0))
s.Line(point1=(0.0, 16.0), point2=(5.5, 16.0))
s.Line(point1=(5.5, 16.0), point2=(5.5, 16.5))
s.Line(point1=(5.5, 16.5), point2=(6.2, 16.5))
s.Line(point1=(6.2, 16.5), point2=(6.2, 16.7))
s.Line(point1=(6.2, 16.7), point2=(8.0, 16.7))
s.Line(point1=(8.0, 16.7), point2=(8.0, 0.0))
s.Line(point1=(8.0, 0.0), point2=(0.0, 0.0))
p = a.Part(name='substructure', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

p = a.parts['substructure']
f, v, d, c = p.faces, p.vertices, p.datums, p.cells
p.DatumPlaneByOffset(plane=f[6], point=v[8])
p.DatumPlaneByOffset(plane=f[6], point=v[4])
p.DatumPlaneByOffset(plane=f[1], point=v[4])
p.DatumPlaneByOffset(plane=f[1], point=v[8])
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[4], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#7 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#12 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)


s = a.ConstrainedSketch(name='bb_layer', sheetSize=50.0)
s.Line(point1=(0.0, 0.643), point2=(0.2, 0.643))
s.Line(point1=(0.2, 0.643), point2=(0.2, 0.49009))
s.Line(point1=(0.2, 0.49009), point2=(0.3145, 0.49009))
s.Line(point1=(0.3145, 0.49009), point2=(0.3145, 0.381876))
s.Line(point1=(0.3145, 0.381876), point2=(0.4505, 0.381876))
s.Line(point1=(0.4505, 0.381876), point2=(0.4505, 0.472412))
s.Line(point1=(0.4505, 0.472412), point2=(0.85, 0.4))
s.Line(point1=(0.85, 0.4), point2=(1.1, 0.4))
s.Line(point1=(1.1, 0.4), point2=(1.1, 0.0))
s.Line(point1=(1.1, 0.0), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.0, 0.643))
p = a.Part(name='bb_layer', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

p = a.parts['bb_layer']
f, v, c, d = p.faces, p.vertices, p.cells, p.datums
p.DatumPlaneByOffset(plane=f[8], point=v[14])
p.DatumPlaneByOffset(plane=f[8], point=v[10])
p.DatumPlaneByOffset(plane=f[8], point=v[8])
p.DatumPlaneByOffset(plane=f[8], point=v[4])
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[4], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)

s = a.ConstrainedSketch(name='infi_1', sheetSize=50.0)
s.Line(point1=(0.55, -16.3785), point2=(0.55, 0.7215))
s.Line(point1=(0.55, 0.7215), point2=(0.3,0.7215))
s.Line(point1=(0.3, 0.7215), point2=(-0.0995, 0.793912))
s.Line(point1=(-0.0995, 0.793912), point2=(-0.0995, 0.703376))
s.Line(point1=(-0.0995, 0.703376), point2=(-0.2355, 0.703376))
s.Line(point1=(-0.2355, 0.703376), point2=(-0.2355, 0.81159))
s.Line(point1=(-0.2355, 0.81159), point2=(-0.35, 0.81159))
s.Line(point1=(-0.35, 0.81159), point2=(-0.35, 0.9645))
s.Line(point1=(-0.35, 0.9645), point2=(-0.55, 0.9645))
s.Line(point1=(-0.55, 0.9645), point2=(-0.55, 0.3215))
s.Line(point1=(-0.55, 0.3215), point2=(-1.25, 0.3215))
s.Line(point1=(-1.25, 0.3215), point2=(-1.25, 0.1215))
s.Line(point1=(-1.25, 0.1215), point2=(-1.95, 0.1215))
s.Line(point1=(-1.95, 0.1215), point2=(-1.95, -0.3785))
s.Line(point1=(-1.95, -0.3785), point2=(-7.45, -0.3785))
s.Line(point1=(-7.45, -0.3785), point2=(-7.45, -16.3785))
s.Line(point1=(-7.45, -16.3785), point2=(0.55, -16.3785))
p = a.Part(name='infi_1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=1.0)

p = a.parts['infi_1']
f, v, c, d = p.faces, p.vertices, p.cells, p.datums
p.DatumPlaneByOffset(plane=f[15], point=v[28])
p.DatumPlaneByOffset(plane=f[15], point=v[24])
p.DatumPlaneByOffset(plane=f[15], point=v[22])
p.DatumPlaneByOffset(plane=f[15], point=v[18])
p.DatumPlaneByOffset(plane=f[15], point=v[14])
p.DatumPlaneByOffset(plane=f[15], point=v[10])
p.DatumPlaneByOffset(plane=f[15], point=v[6])
p.DatumPlaneByOffset(plane=f[1], point=v[4])
p.DatumPlaneByOffset(plane=f[1], point=v[8])
p.DatumPlaneByOffset(plane=f[1], point=v[12])

pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[4], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#8 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#10 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#20 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[7], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#40 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[8], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#7e ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[11], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#a7a ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[10], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#69838 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[9], cells=pickedCells)
	
	

# materials and sections
mat_prop = {'cbl':[(2400.0,),(30000000000.0,0.2)],'fpl':[(2400.0,),(120000000.0,0.2)],'hbl':[(2400.0,),(5000000000.0,0.2)],'grout':[(2400.0,),(39000000000.0,0.45)], 'grp':[(2100.0,),(39000000000.0,0.45)], 'soil':[(2000.0,),(50000000.0,0.4)],
			'steel':[(7850.0,),(207000000000.0,0.28)],'elastic_pad':[(500.0,),(610000000000.0,0.3)]}
for i,j in mat_prop.items():
    a.Material(name=i)
    a.materials[i].Density(table=(j[0], ))
    a.materials[i].Elastic(table=(j[1], ))
    a.HomogeneousSolidSection(name=i+'_section', material=i, thickness=None)

all_parts1 = ['bb_layer', 'grout', 'pad', 'shell']
for i in all_parts1:
    p = a.parts[i]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1f ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p.SectionAssignment(region=region, sectionName='cbl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

all_parts2 = ['bb_rail', 'infi_bottom', 'infi_side', 'wheel']
for i in all_parts2:
    p = a.parts[i]
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p.SectionAssignment(region=region, sectionName='cbl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)


p = a.parts['infi_1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#34c0070 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#1c0f ]', ), )
region = p.Set(cells=cells, name='Set-2')
p.SectionAssignment(region=region, sectionName='fpl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#34380 ]', ), )
region = p.Set(cells=cells, name='Set-3')
p.SectionAssignment(region=region, sectionName='hbl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#b0a000 ]', ), )
region = p.Set(cells=cells, name='Set-4')
p.SectionAssignment(region=region, sectionName='cbl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

p = a.parts['substructure']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#23 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#c ]', ), )
region = p.Set(cells=cells, name='Set-2')
p.SectionAssignment(region=region, sectionName='fpl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
region = p.Set(cells=cells, name='Set-3')
p.SectionAssignment(region=region, sectionName='hbl_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

p = a.Part(name='infi_2', objectToCopy=a.parts['infi_1'])

p = a.parts['infi_2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#30c4980 #960924a4 #88888828 #480012 ]', ), )
p.Set(faces=faces, name='roller')
faces = f.getSequenceFromMask(mask=('[#0:2 #42222200 #100008 ]', ), )
p.Set(faces=faces, name='fixed')
	
p = a.parts['infi_1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4319280 #4c0c9248 #24444446 #280014 ]', ), )
p.Set(faces=faces, name='roller')
faces = f.getSequenceFromMask(mask=('[#0:2 #42222200 #100008 ]', ), )
p.Set(faces=faces, name='fixed')

p = a.parts['infi_bottom']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#35 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['infi_bottom']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#8 ]', ), )
p.Set(faces=faces, name='fixed')

p = a.parts['infi_side']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#31 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['infi_side']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#8 ]', ), )
p.Set(faces=faces, name='fixed')

p = a.parts['grout']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3006cb8 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['pad']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3006cb8 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['shell']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3006cb8 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['substructure']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4084000 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['bb_layer']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1000000 ]', ), )
p.Set(faces=faces, name='roller')

p = a.parts['bb_rail']
f = p.faces
p.Set(faces=f.getSequenceFromMask(mask=('[#30 ]', ), ), name='roller')
p.Surface(side1Faces=f.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')

p = a.parts['wheel']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#8 ]', ), ), name='bottom')

#assembly
a1 = a.rootAssembly
a1.DatumCsysByDefault(CARTESIAN)

for i in a.parts.keys():
    a1.Instance(name=i+'-1', part=a.parts[i], dependent=ON)

a1.translate(instanceList=('grout-1', ), vector=(0.3145, 0.381876, 0.0))
a1.translate(instanceList=('shell-1', ), vector=(0.3345, 0.401876, 0.0))
a1.translate(instanceList=('pad-1', ), vector=(0.3395, 0.406876, 0.0))
a1.translate(instanceList=('bb_rail-1', ), vector=(0.3495, 0.416876, 0.0))
a1.translate(instanceList=('bb_layer-1', 'bb_rail-1', 'grout-1', 'pad-1', 'shell-1'), vector=(6.9, 16.7, 0.0))
a1.translate(instanceList=('infi_side-1', ), vector=(-1.0, 0.0, 0.0))
a1.translate(instanceList=('infi_bottom-1', ), vector=(0.0, -1.0, 0.0))
a1.translate(instanceList=('infi_1-1', ), vector=(7.45, 16.3785, 200.0))
a1.translate(instanceList=('infi_2-1', ), vector=(7.45, 16.3785, -1.0))
a1.translate(instanceList=('wheel-1', ), vector=(7.2495, 17.248876, 199.8))
a1.translate(instanceList=tuple(a1.instances.keys()), vector=(-7.3155, -17.248876, -200.0))

# Step
a.ImplicitDynamicsStep(name='loading', previous='Initial', timePeriod=0.1, maxNumInc=10000, initialInc=0.001, minInc=1e-07, nlgeom=ON)
a.ImplicitDynamicsStep(name='moving', previous='loading', timePeriod=1.5, maxNumInc=10000, initialInc=0.001, minInc=1e-07)
a.fieldOutputRequests['F-Output-1'].setValues(variables=('A', 'S', 'U', 'V'), timeInterval=0.01)
a.historyOutputRequests['H-Output-1'].setValues(variables=('ALLAE', ), timeInterval=0.01)

#interaction

a.ContactProperty('smooth')
a.interactionProperties['smooth'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON, constraintEnforcementMethod=DEFAULT)
a.interactionProperties['smooth'].TangentialBehavior(formulation=FRICTIONLESS)

s1 =  a1.instances['bb_layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#80000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-1-bb_layer-1')
region1= a1.surfaces['CP-1-bb_layer-1']

s1 =  a1.instances['grout-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#400040 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-1-grout-1')
region2= a1.surfaces['CP-1-grout-1']

s1 =  a1.instances['bb_layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#100000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-2-bb_layer-1')
region3= a1.surfaces['CP-2-bb_layer-1']

s1 =  a1.instances['grout-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#208200 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-2-grout-1')
region4= a1.surfaces['CP-2-grout-1']

s1 =  a1.instances['bb_layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#200000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-3-bb_layer-1')
region5= a1.surfaces['CP-3-bb_layer-1']

s1 =  a1.instances['grout-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#100004 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-3-grout-1')
region6= a1.surfaces['CP-3-grout-1']

s1 =  a1.instances['infi_1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#30c4900 #920124a4 #88888828 #400002 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-4-infi_1-1')
region7= a1.surfaces['CP-4-infi_1-1']

s1 =  a1.instances['bb_layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#8004888 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-4-bb_layer-1')
region8= a1.surfaces['CP-4-bb_layer-1']

s1 =  a1.instances['infi_2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4319200 #48049248 #24444446 #200004 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-5-infi_2-1')
region9= a1.surfaces['CP-5-infi_2-1']

s1 =  a1.instances['bb_layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10002244 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-5-bb_layer-1')
region10= a1.surfaces['CP-5-bb_layer-1']

s1 =  a1.instances['substructure-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-6-substructure-1')
region11= a1.surfaces['CP-6-substructure-1']

s1 =  a1.instances['bb_layer-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2008422 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-6-bb_layer-1')
region12= a1.surfaces['CP-6-bb_layer-1']

s1 =  a1.instances['bb_rail-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-7-bb_rail-1')
region13= a1.surfaces['CP-7-bb_rail-1']

s1 =  a1.instances['pad-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-7-pad-1')
region14= a1.surfaces['CP-7-pad-1']

s1 =  a1.instances['bb_rail-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-8-bb_rail-1')
region15= a1.surfaces['CP-8-bb_rail-1']

s1 =  a1.instances['pad-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-8-pad-1')
region16= a1.surfaces['CP-8-pad-1']

s1 =  a1.instances['bb_rail-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#8 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-9-bb_rail-1')
region17= a1.surfaces['CP-9-bb_rail-1']

s1 =  a1.instances['pad-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-9-pad-1')
region18= a1.surfaces['CP-9-pad-1']

s1 =  a1.instances['bb_rail-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-10-bb_rail-1')
region19= a1.surfaces['CP-10-bb_rail-1']

s1 =  a1.instances['wheel-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#8 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-10-wheel-1')
region20= a1.surfaces['CP-10-wheel-1']

s1 =  a1.instances['grout-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-11-grout-1')
region21= a1.surfaces['CP-11-grout-1']

s1 =  a1.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#400040 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-11-shell-1')
region22= a1.surfaces['CP-11-shell-1']

s1 =  a1.instances['grout-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-12-grout-1')
region23= a1.surfaces['CP-12-grout-1']

s1 =  a1.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#208200 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-12-shell-1')
region24= a1.surfaces['CP-12-shell-1']

s1 =  a1.instances['grout-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-13-grout-1')
region25= a1.surfaces['CP-13-grout-1']

s1 =  a1.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#100004 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-13-shell-1')
region26= a1.surfaces['CP-13-shell-1']

s1 =  a1.instances['substructure-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10042304 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-14-substructure-1')
region27= a1.surfaces['CP-14-substructure-1']

s1 =  a1.instances['infi_1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#30c4900 #920124a4 #88888828 #400002 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-14-infi_1-1')
region28= a1.surfaces['CP-14-infi_1-1']

s1 =  a1.instances['substructure-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20028448 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-15-substructure-1')
region29= a1.surfaces['CP-15-substructure-1']

s1 =  a1.instances['infi_2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4319200 #48049248 #24444446 #200004 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-15-infi_2-1')
region30= a1.surfaces['CP-15-infi_2-1']

s1 =  a1.instances['infi_bottom-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-16-infi_bottom-1')
region31= a1.surfaces['CP-16-infi_bottom-1']

s1 =  a1.instances['substructure-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#8000082 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-16-substructure-1')
region32= a1.surfaces['CP-16-substructure-1']

s1 =  a1.instances['infi_side-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-17-infi_side-1')
region33= a1.surfaces['CP-17-infi_side-1']

s1 =  a1.instances['substructure-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#100000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-17-substructure-1')
region34= a1.surfaces['CP-17-substructure-1']

s1 =  a1.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-18-shell-1')
region35= a1.surfaces['CP-18-shell-1']

s1 =  a1.instances['pad-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#100004 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-18-pad-1')
region36= a1.surfaces['CP-18-pad-1']

s1 =  a1.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-19-shell-1')
region37= a1.surfaces['CP-19-shell-1']

s1 =  a1.instances['pad-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#400040 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-19-pad-1')
region38= a1.surfaces['CP-19-pad-1']

s1 =  a1.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20000 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-20-shell-1')
region39= a1.surfaces['CP-20-shell-1']

s1 =  a1.instances['pad-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#208200 ]', ), )
a1.Surface(side1Faces=side1Faces1, name='CP-20-pad-1')
region40= a1.surfaces['CP-20-pad-1']

a.Tie(name='CP-1-bb_layer-1-grout-1', master=region1, slave=region2, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-2-bb_layer-1-grout-1', master=region3, slave=region4, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-3-bb_layer-1-grout-1', master=region5, slave=region6, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-4-infi_1-1-bb_layer-1', master=region8, slave=region7, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-5-infi_2-1-bb_layer-1', master=region10, slave=region9, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-6-substructure-1-bb_layer-1', master=region11, slave=region12, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-7-bb_rail-1-pad-1', master=region13, slave=region14, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-8-bb_rail-1-pad-1', master=region15, slave=region16, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-9-bb_rail-1-pad-1', master=region17, slave=region18, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
#a.Tie(name='CP-10-bb_rail-1-wheel-1', master=region19, slave=region20, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-11-grout-1-shell-1', master=region21, slave=region22, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-12-grout-1-shell-1', master=region23, slave=region24, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-13-grout-1-shell-1', master=region25, slave=region26, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-14-substructure-1-infi_1-1', master=region27, slave=region28, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-15-substructure-1-infi_2-1', master=region29, slave=region30, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-16-infi_bottom-1-substructure-1', master=region32, slave=region31, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-17-infi_side-1-substructure-1', master=region33, slave=region34, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-18-shell-1-pad-1', master=region35, slave=region36, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-19-shell-1-pad-1', master=region37, slave=region38, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)
a.Tie(name='CP-20-shell-1-pad-1', master=region39, slave=region40, positionToleranceMethod=COMPUTED, adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE)

#mdb.models['mgdd'].constraints['CP-4-infi_1-1-bb_layer-1'].swapSurfaces()
#mdb.models['mgdd'].constraints['CP-5-infi_2-1-bb_layer-1'].swapSurfaces()
#mdb.models['mgdd'].constraints['CP-16-infi_bottom-1-substructure-1'].swapSurfaces()

region1= a1.surfaces['CP-10-bb_rail-1']
region2= a1.surfaces['CP-10-wheel-1']
a.SurfaceToSurfaceContactStd(name='wheel_rail', createStepName='Initial', master=region2, slave=region1, sliding=FINITE, thickness=ON, interactionProperty='smooth', 
	adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
		
		
#amplitude
import numpy as np
amp_move = tuple(zip([j for j in np.arange(0, 1.0+0.01,0.01)],[i for i in np.arange(0,1.5+0.015, 0.015)]))
amp_load = tuple(zip([j for j in np.arange(0, 0.1+0.01,0.01)],[i for i in np.arange(0,1.0+0.1, 0.1)]))
a.TabularAmplitude(name='load', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_load )
a.TabularAmplitude(name='motion', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_move )

#load and BC
s = a1.instances['wheel-1'].faces
side1Faces1 = s.getSequenceFromMask(mask=('[#2 ]', ), )
region = a1.Surface(side1Faces=side1Faces1, name='wheel_top')
a.Pressure(name='pressure_1', createStepName='loading', region=region, distributionType=UNIFORM, field='', magnitude=6314890.0, amplitude='load')

region = a1.instances['wheel-1'].sets['Set-1']
a.DisplacementBC(name='motion', createStepName='Initial', region=region, u1=SET, u2=UNSET, u3=SET, ur1=UNSET, ur2=SET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
a.boundaryConditions['motion'].setValuesInStep(stepName='moving', u2=-1.0, ur3=0.0, amplitude='motion')

a1.SetByBoolean(name='roller_all', sets=(
    a1.allInstances['substructure-1'].sets['roller'], 
    a1.allInstances['shell-1'].sets['roller'], 
    a1.allInstances['pad-1'].sets['roller'], 
    a1.allInstances['infi_side-1'].sets['roller'], 
    a1.allInstances['infi_bottom-1'].sets['roller'], 
    a1.allInstances['infi_2-1'].sets['roller'], 
    a1.allInstances['infi_1-1'].sets['roller'], 
    a1.allInstances['grout-1'].sets['roller'], 
    a1.allInstances['bb_rail-1'].sets['roller'], 
    a1.allInstances['bb_layer-1'].sets['roller'], ))

a1.SetByBoolean(name='fixed_all', sets=(
    a1.allInstances['infi_side-1'].sets['fixed'], 
    a1.allInstances['infi_bottom-1'].sets['fixed'], 
    a1.allInstances['infi_2-1'].sets['fixed'], 
    a1.allInstances['infi_1-1'].sets['fixed'], ))

region = a1.sets['roller_all']
a.YasymmBC(name='roller_bc', createStepName='Initial', region=region, localCsys=None)

region = a1.sets['fixed_all']
a.EncastreBC(name='fixed_bc', createStepName='Initial', region=region, localCsys=None)
	
#meshing
elemType1 = mesh.ElemType(elemCode=AC3D8, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=AC3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=AC3D4, elemLibrary=STANDARD)
infi_parts = {'infi_1':['[#3ffffff ]',74],'infi_2':['[#3ffffff ]',97],'infi_bottom':['[#1 ]',3],'infi_side':['[#1 ]',0]}
for i,j in infi_parts.items():
    p = a.parts[i]
    c, f = p.cells, p.faces
    pickedCells = c.getSequenceFromMask(mask=(j[0], ), )
    p.assignStackDirection(referenceRegion=f[j[1]], cells=pickedCells)
    pickedRegions = c.getSequenceFromMask(mask=(j[0], ), )
    p.setMeshControls(regions=pickedRegions, technique=SWEEP, algorithm=ADVANCING_FRONT)
    p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()
    cells = c.getSequenceFromMask(mask=(j[0], ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))

mesh_sizes = {'bb_layer':0.3, 'bb_rail':0.2, 'grout':0.2, 'pad':0.2, 'shell':0.2, 'substructure':2.0, 'wheel':0.1}
for i,j in mesh_sizes.items():
    p = a.parts[i]
    p.seedPart(size=j, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()

#job submission
mdb.Job(name='mgdd_job', model='mgdd', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['mgdd_job'].writeInput(consistencyChecking=OFF)
#mdb.ModelFromInputFile(name='mgdd_job', inputFileName='/home/pranjal/Desktop/data_anlys/abaqus_work/mgdd_job.inp')

#mdb.Job(name='tst', model='mgdd_job', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
#	memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
#	modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)