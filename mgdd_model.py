
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

mdb.Model(name='mgdd', modelType=STANDARD_EXPLICIT)
s = mdb.models['mgdd'].ConstrainedSketch(name='bb_rail', sheetSize=1.0)
s.rectangle(point1=(0.0, 0.0), point2=(0.066, 0.132))
p = mdb.models['mgdd'].Part(name='bb_rail', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='pad', sheetSize=1.0)
s.Line(point1=(0.0, 0.083214), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.086, 0.0))
s.Line(point1=(0.086, 0.0), point2=(0.086, 0.065536))
s.Line(point1=(0.086, 0.065536), point2=(0.076, 0.065536))
s.Line(point1=(0.076, 0.065536), point2=(0.076, 0.01))
s.Line(point1=(0.076, 0.01), point2=(0.01, 0.01))
s.Line(point1=(0.01, 0.01), point2=(0.01, 0.083214))
s.Line(point1=(0.01, 0.083214), point2=(0.0, 0.083214))
p = mdb.models['mgdd'].Part(name='pad', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='grout', sheetSize=1.0)
s.Line(point1=(0.0, 0.108214), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.136, 0.0))
s.Line(point1=(0.136, 0.0), point2=(0.136, 0.090536))
s.Line(point1=(0.136, 0.090536), point2=(0.116, 0.090536))
s.Line(point1=(0.116, 0.090536), point2=(0.116, 0.02))
s.Line(point1=(0.116, 0.02), point2=(0.02, 0.02))
s.Line(point1=(0.02, 0.02), point2=(0.02, 0.108214))
s.Line(point1=(0.02, 0.108214), point2=(0.0, 0.108214))
p = mdb.models['mgdd'].Part(name='grout', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='shell', sheetSize=1.0)
s.Line(point1=(0.0, 0.088214), point2=(0.0, 0.0))
s.Line(point1=(0.0, 0.0), point2=(0.096, 0.0))
s.Line(point1=(0.096, 0.0), point2=(0.096, 0.070536))
s.Line(point1=(0.096, 0.070536), point2=(0.091, 0.070536))
s.Line(point1=(0.091, 0.070536), point2=(0.091, 0.005))
s.Line(point1=(0.091, 0.005), point2=(0.005, 0.005))
s.Line(point1=(0.005, 0.005), point2=(0.005, 0.088214))
s.Line(point1=(0.005, 0.088214), point2=(0.0, 0.088214))
p = mdb.models['mgdd'].Part(name='shell', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='infi_bottom', sheetSize=20.0)
s.rectangle(point1=(0.0, 0.0), point2=(8.0, 1.0))
p = mdb.models['mgdd'].Part(name='infi_bottom', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='infi_side', sheetSize=20.0)
s.rectangle(point1=(0.0, 0.0), point2=(1.0, 16.0))
p = mdb.models['mgdd'].Part(name='infi_side', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='wheel', sheetSize=1.0)
s.rectangle(point1=(0.0, 0.0), point2=(0.066, 0.1))
p = mdb.models['mgdd'].Part(name='wheel', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=0.2)

s = mdb.models['mgdd'].ConstrainedSketch(name='substructure', sheetSize=50.0)
s.Line(point1=(0.0, 0.0), point2=(0.0, 16.0))
s.Line(point1=(0.0, 16.0), point2=(5.5, 16.0))
s.Line(point1=(5.5, 16.0), point2=(5.5, 16.5))
s.Line(point1=(5.5, 16.5), point2=(6.2, 16.5))
s.Line(point1=(6.2, 16.5), point2=(6.2, 16.7))
s.Line(point1=(6.2, 16.7), point2=(8.0, 16.7))
s.Line(point1=(8.0, 16.7), point2=(8.0, 0.0))
s.Line(point1=(8.0, 0.0), point2=(0.0, 0.0))
p = mdb.models['mgdd'].Part(name='substructure', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='bb_layer', sheetSize=50.0)
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
p = mdb.models['mgdd'].Part(name='bb_layer', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=200.0)

s = mdb.models['mgdd'].ConstrainedSketch(name='infi_1', sheetSize=50.0)
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
p = mdb.models['mgdd'].Part(name='infi_1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=1.0)

# materials
mat_prop = {'cbl':[(2400.0,),(30000000000.0,0.2)],'fpl':[(2400.0,),(120000000.0,0.2)],'hbl':[(2400.0,),(5000000000.0,0.2)],'grout':[(2400.0,),(39000000000.0,0.45)], 'grp':[(2100.0,),(39000000000.0,0.45)], 'soil':[(2000.0,),(50000000.0,0.4)],
			'steel':[(7850.0,),(207000000000.0,0.28)],'elastic_pad':[(500.0,),(610000000000.0,0.3)]}
for i,j in mat_prop.items():
    mdb.models['mgdd'].Material(name=i)
    mdb.models['mgdd'].materials[i].Density(table=(j[0], ))
    mdb.models['mgdd'].materials[i].Elastic(table=(j[1], ))

#section
