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

#creating a model
mdb.Model(name='test', modelType=STANDARD_EXPLICIT)

#mohr-coulamb materials
mc_mat = {'ballast':[(2400.0, ), (140000000.0, 0.37), (51.0, 0), (1000.0, 0.0), (800.0, 0.0), 2.609, 0.000434],'subballast':[(2400.0, ), (70000000.0, 0.37), (40.5, 0), (1000.0, 0.0), (1170.0, 0.0), 2.609, 0.000434],
		  'soil':[(2000.0, ), (10000000.0, 0.49), (35.0, 0), (1000.0, 0.0), (1420.0, 0.0), 2.609, 0.000434]}
for i,j in mc_mat.items():
	#soil material
    mdb.models['test'].Material(name=i)
    mdb.models['test'].materials[i].Density(table=(j[0], ))
    mdb.models['test'].materials[i].Elastic(table=(j[1], ))
    mdb.models['test'].materials[i].MohrCoulombPlasticity(table=(j[2], ), useTensionCutoff=True)
    mdb.models['test'].materials[i].mohrCoulombPlasticity.MohrCoulombHardening( table=(j[3], ))
    mdb.models['test'].materials[i].mohrCoulombPlasticity.TensionCutOff(table=(j[4], ))
    mdb.models['test'].materials[i].Damping(alpha=j[5], beta=j[6])

#elastic materials	
el_mat = {'steel':[(7850.0, ), (200000000000.0, 0.2)], 'sleeper':[(2400.0, ), (30000000000.0, 0.2)]}
for i,j in el_mat.items():
	#soil material
    mdb.models['test'].Material(name=i)
    mdb.models['test'].materials[i].Density(table=(j[0], ))
    mdb.models['test'].materials[i].Elastic(table=(j[1], ))

#soil sketch
s = mdb.models['test'].ConstrainedSketch(name='soil', sheetSize=10.0)
s.rectangle(point1=(0.0, 0.0), point2=(9.875, 10.0))

#soil part
p = mdb.models['test'].Part(name='soil', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=300.0)
       
#ballast sketch
s = mdb.models['test'].ConstrainedSketch(name='ballast', sheetSize=10.0)
s.Line(point1=(-0.7, 0.0), point2=(0.0, 0.35))
s.Line(point1=(0.0, 0.35), point2=(1.775, 0.35))
s.Line(point1=(1.775, 0.35), point2=(1.775, 0.0))
s.Line(point1=(1.775, 0.0), point2=(-0.7, 0.0))

#ballast part
p = mdb.models['test'].Part(name='ballast', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=300.0)


#subballast sketch
s = mdb.models['test'].ConstrainedSketch(name='subballast', sheetSize=10.0)
s.Line(point1=(-2.0, 0.0), point2=(0.0, 1.0))
s.Line(point1=(0.0, 1.0), point2=(3.875, 1.0))
s.Line(point1=(3.875, 1.0), point2=(3.875, 0.0))
s.Line(point1=(3.875, 0.0), point2=(-2.0, 0.0))

#subballast part
p = mdb.models['test'].Part(name='subballast', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=300.0)

#sleeper sketch
s = mdb.models['test'].ConstrainedSketch(name='sleeper', sheetSize=10.0)
s.Line(point1=(0.0, 0.0), point2=(0.25, 0.0))
s.Line(point1=(0.25, 0.0), point2=(0.2, 0.21))
s.Line(point1=(0.2, 0.21), point2=(0.05, 0.21))
s.Line(point1=(0.05, 0.21), point2=(0.0,0.0))

#sleeper part
p = mdb.models['test'].Part(name='sleeper', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=1.375)

#sleeper1 sketch
s = mdb.models['test'].ConstrainedSketch(name='sleeper1', sheetSize=10.0)
s.Line(point1=(0.0, 0.0), point2=(0.125, 0.0))
s.Line(point1=(0.125, 0.0), point2=(0.075, 0.21))
s.Line(point1=(0.075, 0.21), point2=(0.0, 0.21))
s.Line(point1=(0.0, 0.21), point2=(0.0,0.0))

#sleeper1 part
p = mdb.models['test'].Part(name='sleeper1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=1.375)


#sleeper2 sketch
s = mdb.models['test'].ConstrainedSketch(name='sleeper2', sheetSize=10.0)
s.Line(point1=(0.0, 0.0), point2=(-0.125, 0.0))
s.Line(point1=(-0.125, 0.0), point2=(-0.075, 0.21))
s.Line(point1=(-0.075, 0.21), point2=(0.0, 0.21))
s.Line(point1=(0.0, 0.21), point2=(0.0,0.0))

#sleeper2 part
p = mdb.models['test'].Part(name='sleeper2', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=1.375)


#rail sketch
s = mdb.models['test'].ConstrainedSketch(name='rail', sheetSize=10.0)
s.Line(point1=(0.0, 0.0), point2=(0.0, 0.10))
s.Line(point1=(0.0, 0.10), point2=(0.0715, 0.1))
s.Line(point1=(0.0715, 0.1), point2=(0.0715, 0.0))
s.Line(point1=(0.0715, 0.0), point2=(0.10775,0.0))
s.Line(point1=(0.10775,0.0), point2=(0.10775,-0.053))
s.Line(point1=(0.10775,-0.053), point2=(-0.04225,-0.053))
s.Line(point1=(-0.04225,-0.053), point2=(-0.04225,0.0))
s.Line(point1=(-0.04225,0.0), point2=(0.0,0.0))

#rail part
p = mdb.models['test'].Part(name='rail', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=300.0)

#wheel sketch
s = mdb.models['test'].ConstrainedSketch(name='wheel', sheetSize=2.0)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.5))

#wheel part
p = mdb.models['test'].Part(name='wheel', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=0.0715)

#subballast section assignment
mdb.models['test'].HomogeneousSolidSection(name='subballast_section', material='subballast', thickness=None)
p = mdb.models['test'].parts['subballast']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['subballast']
p.SectionAssignment(region=region, sectionName='subballast_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#ballast section assignment
mdb.models['test'].HomogeneousSolidSection(name='ballast_section', material='ballast', thickness=None)
p = mdb.models['test'].parts['ballast']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['ballast']
p.SectionAssignment(region=region, sectionName='ballast_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
 
#soil section assignment
mdb.models['test'].HomogeneousSolidSection(name='soil_section', material='soil', thickness=None)
p = mdb.models['test'].parts['soil']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['soil']
p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)


#infinite sketch
s1 = mdb.models['test'].ConstrainedSketch(name='infi_part', sheetSize=50.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Line(point1=(9.875, 0.0), point2=(9.875, 11.35))
s1.Line(point1=(9.875, 11.35), point2=(8.1, 11.35))
s1.Line(point1=(8.1, 11.35), point2=(7.4, 11.0))
s1.Line(point1=(7.4, 11.0), point2=(6.0, 11.0))
s1.Line(point1=(6.0, 11.0), point2=(4.0, 10.0))
s1.Line(point1=(4.0, 10.0), point2=(0.0, 10.0))
s1.Line(point1=(0.0, 10.0), point2=(0.0, 0.0))
s1.Line(point1=(0.0, 0.0), point2=(9.875, 0.0))

#infinite part
p = mdb.models['test'].Part(name='infi_1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['infi_1']
p.BaseSolidExtrude(sketch=s1, depth=1.0)

#infinite part cut and section assignment
#side_1
p = mdb.models['test'].parts['infi_1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v1[4], normal=e[0], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[9], normal=e1[8], cells=pickedCells)
cells = c.getSequenceFromMask(mask=('[#4 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['infi_1']
p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region = p.Set(cells=cells, name='Set-2')
p.SectionAssignment(region=region, sectionName='subballast_section', 
    offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-3')
p.SectionAssignment(region=region, sectionName='ballast_section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#side_2
p1 = mdb.models['test'].parts['infi_1']
p = mdb.models['test'].Part(name='infi_2', objectToCopy=mdb.models['test'].parts['infi_1'])

#infi_1 surface assignment
p = mdb.models['test'].parts['infi_1']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#2 ]', ), ), name='blst')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#20000 ]', ), ), name='sbblst')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#20 ]', ), ), name='soil')
p.Set(faces=s.getSequenceFromMask(mask=('[#141cc ]', ), ), name='roller')
p.Set(faces=s.getSequenceFromMask(mask=('[#8000 ]', ), ), name='fixed')

#infi_1 partitioning
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#7 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e1[32], cells=pickedCells, 
    point=p.InterestingPoint(edge=e1[32], rule=MIDDLE))
 
#infi_2 surface assignment
p = mdb.models['test'].parts['infi_2']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#40 ]', ), ), name='blst')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#8 ]', ), ), name='sbblst')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#10000 ]', ), ), name='soil')
p.Set(faces=s.getSequenceFromMask(mask=('[#241a6 ]', ), ), name='roller')
p.Set(faces=s.getSequenceFromMask(mask=('[#8000 ]', ), ), name='fixed')

#infi_2 partitioning
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#7 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e[32], cells=pickedCells, 
    point=p.InterestingPoint(edge=e[32], rule=MIDDLE))
    
#infi_long part creation
s = mdb.models['test'].ConstrainedSketch(name='infi_long', sheetSize=50.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(1.0, 10.0))
p = mdb.models['test'].Part(name='infi_long', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['infi_long']
p.BaseSolidExtrude(sketch=s, depth=300.0)
p = mdb.models['test'].parts['infi_long']
f = p.faces
p.Set(faces=f.getSequenceFromMask(mask=('[#31 ]', ), ), name='roller')
p.Surface(side1Faces=f.getSequenceFromMask(mask=('[#4 ]', ), ), name='side')
p.Set(faces=f.getSequenceFromMask(mask=('[#8 ]', ), ), name='fixed')

#infi_long section assignment
c = p.cells
region = p.Set(cells=c.getSequenceFromMask(mask=('[#1 ]', ), ), name='Set-3')
p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

#infi_long partitioning
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e[4], cells=pickedCells, 
    point=p.InterestingPoint(edge=e[4], rule=MIDDLE))       
    
#infi_bottom part creation
s1 = mdb.models['test'].ConstrainedSketch(name='infi_bottom', sheetSize=50.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(9.875, 1.0))
p = mdb.models['test'].Part(name='infi_bottom', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['infi_bottom']
p.BaseSolidExtrude(sketch=s1, depth=300.0)

#infi_bottom section assignment
c = p.cells
region = p.Set(cells=c.getSequenceFromMask(mask=('[#1 ]', ), ), name='Set-3')
p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)   

#infi_bottom surfaces and sets
s = p.faces 
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')
p.Set(faces=s.getSequenceFromMask(mask=('[#35 ]', ), ), name='roller')
p.Set(faces=s.getSequenceFromMask(mask=('[#8 ]', ), ), name='fixed')

#infi_bottom partitioning
p.DatumPlaneByOffset(plane=s[3], flip=SIDE2, offset=0.5)
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))


#rail section assignment
mdb.models['test'].HomogeneousSolidSection(name='steel_section', material='steel', thickness=None)
p = mdb.models['test'].parts['rail']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['rail']
p.SectionAssignment(region=region, sectionName='steel_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#wheel section assignment
p = mdb.models['test'].parts['wheel']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['wheel']
p.SectionAssignment(region=region, sectionName='steel_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#wheel surface assignment
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#1 ]', ), ), name='rim')

p = mdb.models['test'].parts['wheel']
v, e, c, d = p.vertices, p.edges, p.cells, p.datums

p.DatumPlaneByTwoPoint(point1=v[0], point2=v[1])#, isDependent=False)
p.DatumPlaneByTwoPoint(point2=v[0], point1=p.InterestingPoint(edge=e[0], 
    rule=MIDDLE))#, isDependent=False)
p.DatumPlaneByThreePoints(point2=v[0], point3=v[1], 
    point1=p.InterestingPoint(edge=e[0], rule=MIDDLE))


p.PartitionCellByDatumPlane(datumPlane=d[4], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=c.getSequenceFromMask(mask=('[#3 ]', ), )) 
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=c.getSequenceFromMask(mask=('[#f ]', ), ))

#sleeper section assignment
mdb.models['test'].HomogeneousSolidSection(name='sleeper_section', material='sleeper', thickness=None)
p = mdb.models['test'].parts['sleeper']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['sleeper']
p.SectionAssignment(region=region, sectionName='sleeper_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#sleeper roller boundary and surfaces
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#4 ]', ), ), name='bottom')
p.Set(faces=s.getSequenceFromMask(mask=('[#20 ]', ), ), name='roller')

#partitioning sleeper for mesh
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.763)#, isDependent=False)
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.913)#, isDependent=False)
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#400 ]', ), ), name='rail_cont')

#sleeper1 section assignment
p = mdb.models['test'].parts['sleeper1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p.SectionAssignment(region=region, sectionName='sleeper_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#sleeper1 roller boundary and surfaces
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#4 ]', ), ), name='bottom')
p.Set(faces=s.getSequenceFromMask(mask=('[#28 ]', ), ), name='roller')

#partitioning sleeper1 for mesh
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.763)#, isDependent=False)
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.913)#, isDependent=False)
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#400 ]', ), ), name='rail_cont')

#sleeper2 section assignment
p = mdb.models['test'].parts['sleeper2']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p.SectionAssignment(region=region, sectionName='sleeper_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

#sleeper2 roller boundary and surfaces
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#4 ]', ), ), name='bottom')
p.Set(faces=s.getSequenceFromMask(mask=('[#28 ]', ), ), name='roller')


#partitioning sleeper2 for mesh
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.763)#, isDependent=False)
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.913)#, isDependent=False)
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[6], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#400 ]', ), ), name='rail_cont')


#partitioning rail for mesh
p = mdb.models['test'].parts['rail']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e[16], cells=pickedCells, point=p.InterestingPoint(edge=e[16], rule=MIDDLE))
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[6], normal=e1[7], cells=pickedCells)


#rail surfaces
p = mdb.models['test'].parts['rail']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#20 ]', ), ), name='bottom')

# surface assignments of substructure
for i in ['soil','ballast','subballast']:
    p = mdb.models['test'].parts[i]
    s = p.faces
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#8 ]', ), ), name='bottom')
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#10 ]', ), ), name='side_1')
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#20 ]', ), ), name='side_2')
    #p.Set(faces=s.getSequenceFromMask(mask=('[#4 ]', ), ), name='roller')
	
p = mdb.models['test'].parts['soil']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#1 ]', ), ), name='long')

#partitioning ballast 
p = mdb.models['test'].parts['ballast']
f = p.faces
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.913)#, isDependent=False)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.763)#, isDependent=False)
c = p.cells
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[8], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[7], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
e, v, d = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v[8], normal=e[10], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))

#partitioning subballast
p = mdb.models['test'].parts['subballast']
f = p.faces
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.763)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.913)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=1.775)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=2.475)
c = p.cells
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[7], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[8], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[9], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[10], cells=c.getSequenceFromMask(mask=('[#2 ]', ), ))
e, v, d = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v[8], normal=e[10], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
    
#partitioning soil
p = mdb.models['test'].parts['soil']
f = p.faces
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.763)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.913)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=1.775)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=2.475)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=3.875)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=5.875)
c = p.cells
d = p.datums
p.PartitionCellByDatumPlane(datumPlane=d[8], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[9], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[10], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[11], cells=c.getSequenceFromMask(mask=('[#2 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[12], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=d[13], cells=c.getSequenceFromMask(mask=('[#2 ]', ), ))

#roller for substructure and rail
p = mdb.models['test'].parts['ballast']
s = p.faces
p.Set(faces=s.getSequenceFromMask(mask=('[#10000 ]', ), ), name='roller')

p = mdb.models['test'].parts['soil']
s = p.faces
p.Set(faces=s.getSequenceFromMask(mask=('[#0 #1 ]', ), ), name='roller')

p = mdb.models['test'].parts['subballast']
s = p.faces
p.Set(faces=s.getSequenceFromMask(mask=('[#4000000 ]', ), ), name='roller')

p = mdb.models['test'].parts['rail']
s = p.faces
p.Set(faces=s.getSequenceFromMask(mask=('[#30053c ]', ), ), name='roller')


# assembly building 
a = mdb.models['test'].rootAssembly
for i in mdb.models['test'].parts.values():
    a.Instance(name=i.name+'-1', part=i, dependent=ON)

a.translate(instanceList=('subballast-1', ), vector=(6.0, 10.0, 0.0))
a.translate(instanceList=('ballast-1', ), vector=(8.1, 11.0, 0.0))
a.translate(instanceList=('sleeper-1', 'sleeper1-1', 'sleeper2-1'), vector=(9.75, 11.35, 298.625))
a.rotate(instanceList=('sleeper-1', 'sleeper1-1', 'sleeper2-1'), axisPoint=(9.875, 11.0, 300.0), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a.translate(instanceList=('sleeper-1', ), vector=(-1.375, 0.0, 0.0))
a.translate(instanceList=('sleeper2-1', ), vector=(-1.375, 0.0, 0.125))
a.translate(instanceList=('sleeper1-1', ), vector=(-1.375, 0.0, -299.875))
a.LinearInstancePattern(instanceList=('sleeper-1', ), direction1=(0.0, 0.0,-1.0), direction2=(0.0, 1.0, 0.0), number1=501, number2=1,spacing1=0.6, spacing2=0.21)
del a.features['sleeper-1']
del a.features['sleeper-1-lin-501-1'] 

a.translate(instanceList=('infi_long-1', ), vector=(-1.0, 0.0, 0.0))
a.translate(instanceList=('infi_bottom-1', ), vector=(0.0, -1.0, 0.0))
a.translate(instanceList=('infi_1-1', ), vector=(0.0, 0.0, 300.0))
a.translate(instanceList=('infi_2-1', ), vector=(0.0, 0.0, -1.0))

#situating wheel
a.translate(instanceList=('rail-1', 'wheel-1'), vector=(9.00425, 11.613, 0.0))
a.translate(instanceList=('wheel-1', ), vector=(0.0715, 0.6, 299.9285))
a.rotate(instanceList=('wheel-1', ), axisPoint=(9.07575, 12.213, 300.0), axisDirection=(0.0, -0.25, 0.0), angle=270.0)
a.translate(instanceList=('wheel-1', ), vector=(0.0, 0.0, -1.0))
a.LinearInstancePattern(instanceList=('wheel-1', ), direction1=(0.0, 0.0,-1.0), direction2=(0.0, 1.0, 0.0), number1=2, number2=1,spacing1=2.0, spacing2=0.21)
a.features.changeKey(fromName='wheel-1-lin-2-1', toName='wheel-2')
a.LinearInstancePattern(instanceList=('wheel-1', 'wheel-2'), direction1=(0.0, 0.0, -1.0), direction2=(0.0, 1.0, 0.0), number1=2, number2=1, spacing1=4.2, spacing2=1.0)
a.features.changeKey(fromName='wheel-1-lin-2-1', toName='wheel-3')
a.features.changeKey(fromName='wheel-2-lin-2-1', toName='wheel-4')
#merging sleepers
a.InstanceFromBooleanMerge(name='all_sleeper', instances=tuple([i for i in a.instances.values() if 'sleeper' in i.name]), keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)   


# step module (analysis definition)

mdb.models['test'].ImplicitDynamicsStep(name='loading', previous='Initial', nlgeom=ON, timePeriod=0.1, maxNumInc=100000, initialInc=0.001, minInc=1e-06)
mdb.models['test'].ImplicitDynamicsStep(name='moving', previous='loading', nlgeom=ON, timePeriod=0.1, maxNumInc=100000, initialInc=0.001, minInc=1e-06)
#mdb.models['test'].ExplicitDynamicsStep(name='loading', previous='Initial', timePeriod=0.1)
#mdb.models['test'].ExplicitDynamicsStep(name='moving', previous='loading', timePeriod=1.44)
mdb.models['test'].fieldOutputRequests['F-Output-1'].setValues(variables=('U','V', 'A', 'S'), timeInterval=0.01, timeMarks=ON)
mdb.models['test'].historyOutputRequests['H-Output-1'].setValues(variables=('ETOTAL', ), timeInterval=0.01)


# interaction TIE and FRICTION
mdb.models['test'].Tie(name='blst_sbblst', master=a.instances['ballast-1'].surfaces['bottom'], slave=a.instances['subballast-1'].surfaces['top'], 
	positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
	
mdb.models['test'].Tie(name='sbblst_soil', master=a.instances['subballast-1'].surfaces['bottom'], slave=a.instances['soil-1'].surfaces['top'], 
	positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='slpr_blst', master=a.instances['all_sleeper-1'].surfaces['bottom'], slave=a.instances['ballast-1'].surfaces['top'], 
	positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='blst_side_1', master=a.instances['ballast-1'].surfaces['side_1'], slave=a.instances['infi_1-1'].surfaces['blst'], 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='blst_side_2', master=a.instances['ballast-1'].surfaces['side_2'], slave=a.instances['infi_2-1'].surfaces['blst'], 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='sbblst_side_1', master=a.instances['subballast-1'].surfaces['side_1'], slave=a.instances['infi_1-1'].surfaces['sbblst'], 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='sbblst_side_2', master=a.instances['subballast-1'].surfaces['side_2'], slave=a.instances['infi_2-1'].surfaces['sbblst'], 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='soil_side_1', master=a.instances['soil-1'].surfaces['side_1'], slave=a.instances['infi_1-1'].surfaces['soil'], 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='soil_side_2', master=a.instances['soil-1'].surfaces['side_2'], slave=a.instances['infi_2-1'].surfaces['soil'], 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='soil_bottom', master=a.instances['soil-1'].surfaces['bottom'], slave=a.instances['infi_bottom-1'].surfaces['top'], 
	positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='soil_long', master=a.instances['soil-1'].surfaces['long'], slave=a.instances['infi_long-1'].surfaces['side'], 
	positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].Tie(name='rail_slpr', master=a.instances['rail-1'].surfaces['bottom'], slave=a.instances['all_sleeper-1'].surfaces['rail_cont'], 
	positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)

mdb.models['test'].ContactProperty('friction')
mdb.models['test'].interactionProperties['friction'].TangentialBehavior(formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
	pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((0.3, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
	fraction=0.005, elasticSlipStiffness=None)
mdb.models['test'].interactionProperties['friction'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON,constraintEnforcementMethod=DEFAULT)
mdb.models['test'].ContactStd(name='whl_rl', createStepName='Initial')
r11=a.instances['wheel-1'].surfaces['rim']
r12=a.instances['rail-1'].surfaces['top']
r21=a.instances['wheel-2'].surfaces['rim']
r22=a.instances['rail-1'].surfaces['top']
r31=a.instances['wheel-3'].surfaces['rim']
r32=a.instances['rail-1'].surfaces['top']
r41=a.instances['wheel-4'].surfaces['rim']
r42=a.instances['rail-1'].surfaces['top']
mdb.models['test'].interactions['whl_rl'].includedPairs.setValuesInStep(stepName='Initial', useAllstar=OFF, addPairs=((r11, r12), (r21, r22), (r31, r32), (r41, r42)))
mdb.models['test'].interactions['whl_rl'].contactPropertyAssignments.appendInStep(stepName='Initial', assignments=((GLOBAL, SELF, 'friction'), ))
	
# setting boundary conditions roller and fixed
a.SetByBoolean(name='roller', sets=(a.allInstances['all_sleeper-1'].sets['roller'],	a.allInstances['infi_1-1'].sets['roller'], 
	a.allInstances['infi_2-1'].sets['roller'], a.allInstances['infi_bottom-1'].sets['roller'], a.allInstances['infi_long-1'].sets['roller'],
	a.allInstances['soil-1'].sets['roller'],a.allInstances['ballast-1'].sets['roller'], a.allInstances['subballast-1'].sets['roller'], a.allInstances['rail-1'].sets['roller'],))

a.SetByBoolean(name='fixed', sets=(	a.allInstances['infi_1-1'].sets['fixed'], a.allInstances['infi_2-1'].sets['fixed'], 
	a.allInstances['infi_bottom-1'].sets['fixed'], a.allInstances['infi_long-1'].sets['fixed'], ))
	
mdb.models['test'].DisplacementBC(name='roller', createStepName='Initial', 
        region=a.sets['roller'], u1=SET, u2=UNSET, u3=SET, ur1=UNSET, ur2=SET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.models['test'].EncastreBC(name='fixed', createStepName='Initial', region=a.sets['fixed'], localCsys=None)

#amplitute definition
import numpy as np
movr = []
amp = [ [[0,2.7,0.045],[0,18.75,0.3125 ]],[[2.7,4.23,0.045],[18.75,40,0.625 ]],
       [[4.23,5.4,0.045],[40,64.375,0.9375]],[[5.4,6.48,0.045],[64.375,94.375,1.25]],
       [[6.48,7.38,0.045],[94.375,125.625,1.5625]] ,[[7.38,8.1,0.045],[125.625,155.625,1.875]],
       [[8.1,8.865,0.045],[155.625,192.8125,2.1875]],[[8.865,9.9,0.045],[192.8125,250.3125,2.5]]] 
for i in amp:
    a,b,c = i[0][0],i[0][1],i[0][2] #0,2.7,0.045
    d,e,f = i[1][0],i[1][1],i[1][2] #0,18.75,0.3125 
    #print(a,b,c)
    #print(d,e,f)             
    movr.extend(list(zip([j for j in np.arange(a, b,c)],[i for i in np.arange(d,e, f)])))
#print(ampl)  
loadr = tuple(zip([j for j in np.arange(0, 0.1+0.01,0.01)],[i for i in np.arange(0,1+0.1, 0.1)]))

mdb.models['test'].TabularAmplitude(name='loading', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=loadr)
mdb.models['test'].TabularAmplitude(name='motion', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=tuple(movr))

#rigid wheel
a = mdb.models['test'].rootAssembly
frst_rp = 1036
wheels = ['wheel-1','wheel-2','wheel-3','wheel-4']
for i in wheels:
    v = a.instances[i].vertices
    a.ReferencePoint(point=v[1])
    print(i)
    print(a.referencePoints.items())

for i in wheels:
    region2=a.instances[i].sets['Set-1']
    r = a.referencePoints
    print(frst_rp)
    refPoints1=(r[frst_rp], )
    frst_rp = frst_rp+1
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['test'].RigidBody(name='rigid_'+i, refPointRegion=region1, bodyRegion=region2)
	
#setting wheel motion
for i in wheels:
    mdb.models['test'].DisplacementBC(name='disp'+i, createStepName='Initial', region=a.instances[i].sets['Set-1'], u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=SET, ur3=SET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['test'].boundaryConditions['disp'+i].setValuesInStep(stepName='loading', u3=0.0, amplitude='loading')
    mdb.models['test'].boundaryConditions['disp'+i].setValuesInStep( stepName='moving', u3=-1.0, amplitude='motion')

#applying load on wheel and gravity
mdb.models['test'].Gravity(name='gravity', createStepName='loading', comp2=-9.8, distributionType=UNIFORM, field='')
for i in wheels:
    v1 = a.instances[i].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
    mdb.models['test'].ConcentratedForce(name='load'+i, createStepName='loading', region=a.Set(vertices=verts1, name='centr'+i), cf2=-100000.0, amplitude='loading', distributionType=UNIFORM, field='', localCsys=None)

#meshing  are 50 mm, 50 mm, 500 mm, 250 mm, 500 mm and 1000 mm
mesh_sizes = {'wheel':0.05, 'rail':0.05, 'all_sleeper':0.5, 'ballast':0.25, 'subballast':0.5,'subgrade':1.0 }
for i in mdb.models['test'].parts.keys():
    p = mdb.models['test'].parts[i]
    if(i in list(mesh_sizes.keys())):
        size=mesh_sizes[i]
    else:
        size=1.0
    p.seedPart(size=size, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()

elemType1 = mesh.ElemType(elemCode=AC3D8, elemLibrary=EXPLICIT)
elemType2 = mesh.ElemType(elemCode=AC3D6, elemLibrary=EXPLICIT)
elemType3 = mesh.ElemType(elemCode=AC3D4, elemLibrary=EXPLICIT)
infi_parts = ['infi_long','infi_bottom','infi_1','infi_2']
infi_layers = ['[#1 ]','[#1 ]','[#b ]','[#34 ]']
infi_all = ['[#3 ]','[#3 ]','[#3f ]','[#3f ]']
infi_direction = [5,8,31,20]
for i in range(4):
    p = mdb.models['test'].parts[infi_parts[i]]
    p.deleteMesh()
    c = p.cells
    cells = c.getSequenceFromMask(mask=(infi_layers[i], ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,elemType3))
    pickedCells = c.getSequenceFromMask(mask=(infi_all[i], ), )
    f = p.faces
    p.assignStackDirection(referenceRegion=f[infi_direction[i]], cells=pickedCells)
    pickedRegions = c.getSequenceFromMask(mask=(infi_all[i], ), )
    p.setMeshControls(regions=pickedRegions, technique=SWEEP, algorithm=ADVANCING_FRONT)
    p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
    p.generateMesh()

	
mdb.Job(name='test_job_impl', model='test', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
        nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
        contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
        resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
        activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
mdb.jobs['test_job_impl'].writeInput(consistencyChecking=OFF)

#import fileinput
#with fileinput.FileInput('test_job.inp', inplace=True, backup='.bak') as file:
#    for line in file:
#        line.replace('AC3D8R', 'CIN3D8')
#mdb.jobs['test_job'].submit(consistencyChecking=OFF, datacheckJob=True)

#mdb.jobs['test_job'].submit(consistencyChecking=OFF)	
