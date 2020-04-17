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
'''
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
'''
odbList=[fileN for fileN in os.listdir(".") if '.odb' in fileN]
for k in odbList:
    o1 = session.openOdb(name=os.getcwd()+"/"+k)
    h = k[0:len(k)-4]
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=376, farPlane=511, width=13, height=5, viewOffsetX=60, viewOffsetY=38)
    session.Path(name=h+'_'+'blt', type=NODE_LIST, expression=(('INFI_1-1', (131, )), ('INFI_2-1', (285, ))))
    session.Path(name=h+'_'+'sbt', type=NODE_LIST, expression=(('INFI_1-1', (193, )), ('INFI_2-1', (254, ))))
    session.Path(name=h+'_'+'sbg', type=NODE_LIST, expression=(('INFI_1-1', (198, )), ('INFI_2-1', (259, ))))

    sf = {0:'00' , 270:'025',423:'050',540:'075',648:'100',738:'125',810:'150',886:'175',990:'200'}
    for i in [h+'_'+'blt',h+'_'+'sbt',h+'_'+'sbg']:
        for j in [0,270,423,540,648,738,810,886,990]:
            session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=j)
            session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable( variableLabel='V', outputPosition=NODAL, refinement=(COMPONENT, 'V2'))
            pth = session.paths[i]
            session.XYDataFromPath(name=str(pth.name)+'_k'+sf[j], path=pth, includeIntersections=True, projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
            #abq_ExcelUtilities.excelUtilities.XYtoExcel(xyDataNames=str(pth.name)+'_ic_k'+sf[j], trueName='')
            x0 = session.xyDataObjects[str(pth.name)+'_k'+sf[j]]
            session.xyReportOptions.setValues(layout=SEPARATE_TABLES)
            session.writeXYReport(fileName=str(pth.name)+'_k'+sf[j]+'.txt', appendMode=OFF, xyData=(x0, ))





