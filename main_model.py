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
a1 = mdb.models['test'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a1)

#soil material
mdb.models['test'].Material(name='soil')
mdb.models['test'].materials['soil'].Density(table=((2000.0, ), ))
mdb.models['test'].materials['soil'].Elastic(table=((10000000.0, 0.49), ))
mdb.models['test'].materials['soil'].MohrCoulombPlasticity(table=((35.0, 0), ), useTensionCutoff=True)
mdb.models['test'].materials['soil'].mohrCoulombPlasticity.MohrCoulombHardening( table=((1000.0, 0.0), ))
mdb.models['test'].materials['soil'].mohrCoulombPlasticity.TensionCutOff(table=((1420.0, 0.0), ))
mdb.models['test'].materials['soil'].Damping(alpha=2.609, beta=0.000434)

#subballast material
mdb.models['test'].Material(name='subballast')
mdb.models['test'].materials['subballast'].Density(table=((2400.0, ), ))
mdb.models['test'].materials['subballast'].Elastic(table=((70000000.0, 0.37), ))
mdb.models['test'].materials['subballast'].MohrCoulombPlasticity(table=((40.5, 0), ), useTensionCutoff=True)
mdb.models['test'].materials['subballast'].mohrCoulombPlasticity.MohrCoulombHardening( table=((1000.0, 0.0), ))
mdb.models['test'].materials['subballast'].mohrCoulombPlasticity.TensionCutOff(table=((1170.0, 0.0), ))
mdb.models['test'].materials['subballast'].Damping(alpha=2.609, beta=0.000434)

#ballast material
mdb.models['test'].Material(name='ballast')
mdb.models['test'].materials['ballast'].Density(table=((2400.0, ), ))
mdb.models['test'].materials['ballast'].Elastic(table=((140000000.0, 0.37), ))
mdb.models['test'].materials['ballast'].MohrCoulombPlasticity(table=((51, 0), ), useTensionCutoff=True)
mdb.models['test'].materials['ballast'].mohrCoulombPlasticity.MohrCoulombHardening( table=((1000.0, 0.0), ))
mdb.models['test'].materials['ballast'].mohrCoulombPlasticity.TensionCutOff(table=((800.0, 0.0), ))
mdb.models['test'].materials['ballast'].Damping(alpha=2.609, beta=0.000434)

#sleeper material
mdb.models['test'].Material(name='sleeper')
mdb.models['test'].materials['sleeper'].Density(table=((2400.0, ), ))
mdb.models['test'].materials['sleeper'].Elastic(table=((30000000000.0, 0.2), ))

#steel material
mdb.models['test'].Material(name='steel')
mdb.models['test'].materials['steel'].Density(table=((7850.0, ), ))
mdb.models['test'].materials['steel'].Elastic(table=((200000000000.0, 0.3), ))


#soil sketch
s = mdb.models['test'].ConstrainedSketch(name='soil', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(9.875, 10.0))

#soil part
p = mdb.models['test'].Part(name='soil', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['soil']
p.BaseSolidExtrude(sketch=s, depth=300.0)
       
#ballast sketch
s = mdb.models['test'].ConstrainedSketch(name='ballast', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(-0.7, 0.0), point2=(0.0, 0.35))
s.Line(point1=(0.0, 0.35), point2=(1.775, 0.35))
s.Line(point1=(1.775, 0.35), point2=(1.775, 0.0))
s.Line(point1=(1.775, 0.0), point2=(-0.7, 0.0))

#ballast part
p = mdb.models['test'].Part(name='ballast', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['ballast']
p.BaseSolidExtrude(sketch=s, depth=300.0)


#subballast sketch
s = mdb.models['test'].ConstrainedSketch(name='subballast', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(-2.0, 0.0), point2=(0.0, 1.0))
s.Line(point1=(0.0, 1.0), point2=(3.875, 1.0))
s.Line(point1=(3.875, 1.0), point2=(3.875, 0.0))
s.Line(point1=(3.875, 0.0), point2=(-2.0, 0.0))

#subballast part
p = mdb.models['test'].Part(name='subballast', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['subballast']
p.BaseSolidExtrude(sketch=s, depth=300.0)

#sleeper sketch
s = mdb.models['test'].ConstrainedSketch(name='sleeper', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(0.0, 0.0), point2=(0.25, 0.0))
s.Line(point1=(0.25, 0.0), point2=(0.2, 0.21))
s.Line(point1=(0.2, 0.21), point2=(0.05, 0.21))
s.Line(point1=(0.05, 0.21), point2=(0.0,0.0))

#sleeper part
p = mdb.models['test'].Part(name='sleeper', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['sleeper']
p.BaseSolidExtrude(sketch=s, depth=1.375)


#rail sketch
s = mdb.models['test'].ConstrainedSketch(name='rail', sheetSize=10.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
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
p = mdb.models['test'].parts['rail']
p.BaseSolidExtrude(sketch=s, depth=300.0)

#wheel sketch
s = mdb.models['test'].ConstrainedSketch(name='wheel', sheetSize=2.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.5))

#wheel part
p = mdb.models['test'].Part(name='wheel', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['test'].parts['wheel']
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
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region = p.Set(cells=cells, name='Set-2')
p.SectionAssignment(region=region, sectionName='subballast_section', 
    offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-3')
p.SectionAssignment(region=region, sectionName='ballast_section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

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
 
#infi_bottom partitioning
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e1[7], cells=pickedCells, 
    point=p.InterestingPoint(edge=e1[7], rule=MIDDLE)) 
        
#infi_bottom surfaces and sets
p = mdb.models['test'].parts['infi_bottom']
f = p.faces
p.Set(faces=f.getSequenceFromMask(mask=('[#35 ]', ), ), name='roller')
p.Surface(side1Faces=f.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')
p.Set(faces=f.getSequenceFromMask(mask=('[#8 ]', ), ), name='fixed')

     
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
v, e, c = p.vertices, p.edges, p.cells
p.DatumPlaneByTwoPoint(point1=v[0], point2=v[1], isDependent=False)
p.DatumPlaneByTwoPoint(point2=v[0], point1=p.InterestingPoint(edge=e[0], 
    rule=MIDDLE), isDependent=False)
p.DatumPlaneByThreePoints(point2=v[0], point3=v[1], 
    point1=p.InterestingPoint(edge=e[0], rule=MIDDLE))
f, e, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[1], sketchUpEdge=e[0], 
    sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 0.0715))
s1 = mdb.models['test'].ConstrainedSketch(name='wheel_cut', sheetSize=2.82, 
    gridSpacing=0.07, transform=t)
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, -0.3))

pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.PartitionFaceBySketch(sketchUpEdge=e[0], faces=pickedFaces, sketch=s1)

pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[4], cells=pickedCells)
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )

p.PartitionCellByDatumPlane(datumPlane=d[6], cells=pickedCells)

pickedCells = c.getSequenceFromMask(mask=('[#f ]', ), )
p.PartitionCellByDatumPlane(datumPlane=d[5], cells=pickedCells)

pickedCells = c.getSequenceFromMask(mask=('[#ff ]', ), )

pickedEdges =(e[14], e[27], e[39], e[41])
p.PartitionCellByExtrudeEdge(line=e[4], cells=pickedCells, edges=pickedEdges, 
    sense=FORWARD)   

#sleeper section assignment
mdb.models['test'].HomogeneousSolidSection(name='sleeper_section', material='sleeper', thickness=None)
p = mdb.models['test'].parts['sleeper']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['test'].parts['sleeper']
p.SectionAssignment(region=region, sectionName='sleeper_section', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)


#partitioning rail for mesh
p = mdb.models['test'].parts['rail']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e[16], cells=pickedCells, point=p.InterestingPoint(edge=e[16], rule=MIDDLE))
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[6], normal=e1[7], cells=pickedCells)

# surface assignments of substructure
for i in ['soil','ballast','subballast']:
    p = mdb.models['test'].parts[i]
    s = p.faces
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#8 ]', ), ), name='bottom')
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#10 ]', ), ), name='side_1')
    p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#20 ]', ), ), name='side_2')
p = mdb.models['test'].parts['soil']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#1 ]', ), ), name='long')

#rail surfaces
p = mdb.models['test'].parts['rail']
s = p.faces
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#2 ]', ), ), name='top')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#20 ]', ), ), name='bottom')


#partitioning sleeper for mesh
p = mdb.models['test'].parts['sleeper']
f = p.faces
c = p.cells
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.763, isDependent=False)
p.DatumPlaneByOffset(plane=p.faces[5], flip=SIDE2, offset=0.913, isDependent=False)
p.PartitionCellByDatumPlane(datumPlane=p.datums[3], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))
p.PartitionCellByDatumPlane(datumPlane=p.datums[4], cells=c.getSequenceFromMask(mask=('[#1 ]', ), ))


#sleeper roller boundary and surfaces
p = mdb.models['test'].parts['sleeper']
s = p.faces
p.Set(faces=s.getSequenceFromMask(mask=('[#8000 ]', ), ), name='roller_bc')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#400 ]', ), ), name='rail_cont')
p.Surface(side1Faces=s.getSequenceFromMask(mask=('[#10 ]', ), ), name='bottom')

#partitioning ballast 
p = mdb.models['test'].parts['ballast']
f = p.faces
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.913, isDependent=False)
p.DatumPlaneByOffset(plane=f[2], flip=SIDE2, offset=0.763, isDependent=False)
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

# assembly building 
a1 = mdb.models['test'].rootAssembly
for i in mdb.models['test'].parts.values():
    a1.Instance(name=i.name+'-1', part=i, dependent=ON)

a1.translate(instanceList=('subballast-1', ), vector=(6.0, 10.0, 0.0))
a1.translate(instanceList=('ballast-1', ), vector=(8.1, 11.0, 0.0))
a1.translate(instanceList=('soil-1', 'subballast-1', 'ballast-1', 'rail-1', 'sleeper-1', 'wheel-1'), vector=(-9.875, -11.35, -300.0))

a1.rotate(instanceList=('sleeper-1', ), axisPoint=(-9.75, -11.14, -297.25), axisDirection=(0.0, -0.21, 0.0), angle=90.0)
a1.translate(instanceList=('sleeper-1', ), vector=(7.0, 11.35, 297.25))
a1.LinearInstancePattern(instanceList=('sleeper-1', ), direction1=(0.0, 0.0,-1.0), direction2=(0.0, 1.0, 0.0), number1=501, number2=1,spacing1=0.6, spacing2=0.21)
a1.translate(instanceList=('rail-1', ), vector=(9.00425, 11.613, 0.0))

a1.translate(instanceList=('wheel-1', ), vector=(9.07575, 12.213, 299.9285))
a1.rotate(instanceList=('wheel-1', ), axisPoint=(-0.79925, 0.363, 0.0), axisDirection=(0.0, 0.5, 0.0), angle=90.0)
a1.translate(instanceList=('wheel-1', ), vector=(0.0, 0.0, -1.0))
a1.translate(instanceList=('infi_long-1', ), vector=(-10.875, -11.35, -300.0))
a1.translate(instanceList=('infi_bottom-1', ), vector=(-9.875, -12.35, -300.0))
a1.translate(instanceList=('infi_2-1', ), vector=(-9.875, -11.35, -301.0))
a1.translate(instanceList=('infi_1-1', ), vector=(-9.875, -11.35, 0.0))

#merging sleepers
'''
a1 = mdb.models['test'].rootAssembly
a1.InstanceFromBooleanMerge(name='all_sleeper', instances=tuple([i for i in a1.instances.values() if 'sleeper' in i.name]), keepIntersections=ON, 
       originalInstances=DELETE, domain=GEOMETRY)   

#cutting sleepers from side

p = mdb.models['test'].parts['all_sleeper']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#0:23 #1c000 ]', ), )
e1, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e1[7027], cells=pickedCells, 
    point=p.InterestingPoint(edge=e1[7027], rule=MIDDLE))
p = mdb.models['test'].parts['all_sleeper']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#0:46 #80000000 #3 ]', ), )
e, v, d = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(normal=e[14045], cells=pickedCells, 
    point=p.InterestingPoint(edge=e[14045], rule=MIDDLE))

p = mdb.models['test'].parts['all_sleeper']
f1 = p.faces
p.RemoveFaces(faceList = f1[4003:4004]+f1[4006:4008]+f1[4009:4010]+\
    f1[4013:4016]+f1[4017:4018]+f1[4021:4022]+f1[4024:4026]+f1[4027:4029]+\
    f1[8016:8017]+f1[8018:8019]+f1[8022:8026]+f1[8029:8030]+f1[8031:8034]+\
    f1[8035:8037]+f1[8039:8040], deleteCells=False)
'''
# step module (analysis definition)
mdb.models['test'].ExplicitDynamicsStep(name='loading', previous='Initial', timePeriod=0.1)
mdb.models['test'].ExplicitDynamicsStep(name='moving', previous='loading', timePeriod=1.44)
mdb.models['test'].fieldOutputRequests['F-Output-1'].setValues(variables=('U', 
    'V', 'A', 'S'), timeInterval=0.01, timeMarks=ON)
mdb.models['test'].historyOutputRequests['H-Output-1'].setValues(variables=(
    'ETOTAL', ), timeInterval=0.01)


