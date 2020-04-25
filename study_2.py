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
import os

print(os.getcwd())
#change path to where this file is at
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# get list of files with .odb extension
odbList=[fileN for fileN in os.listdir(".") if '.odb' in fileN]
#iterating over the list
for k in odbList:
	#opeing the ODB file
    o1 = session.openOdb(name=os.getcwd()+"/"+k)
    h = k[0:len(k)-4]
	#Creating paths and naming them 
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.Path(name=h+'_'+'blt', type=NODE_LIST, expression=(('INFI_1-1', (131, )), ('INFI_2-1', (285, ))))
    session.Path(name=h+'_'+'sbt', type=NODE_LIST, expression=(('INFI_1-1', (193, )), ('INFI_2-1', (254, ))))
    session.Path(name=h+'_'+'sbg', type=NODE_LIST, expression=(('INFI_1-1', (198, )), ('INFI_2-1', (259, ))))
    # Time frame and speeds
    sf = {0:'00' , 270:'025',423:'050',540:'075',648:'100',738:'125',810:'150',886:'175',990:'200'}
	#getting the data in report files
    for i in [h+'_'+'blt',h+'_'+'sbt',h+'_'+'sbg']:
        for k,v in sf.items():
        #for j in [0,270,423,540,648,738,810,886,990]:
            session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=k)
            session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable( variableLabel='V', outputPosition=NODAL, refinement=(COMPONENT, 'V2'))
            pth = session.paths[i]
            session.XYDataFromPath(name=str(pth.name)+'_k'+v, path=pth, includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
        #abq_ExcelUtilities.excelUtilities.XYtoExcel(xyDataNames=str(pth.name)+'_ic_k'+sf[j], trueName='')
            x0 = session.xyDataObjects[str(pth.name)+'_k'+v]
            session.xyReportOptions.setValues(layout=SEPARATE_TABLES)
            session.writeXYReport(fileName=str(pth.name)+'_k'+v+'.txt', appendMode=OFF, xyData=(x0, ))