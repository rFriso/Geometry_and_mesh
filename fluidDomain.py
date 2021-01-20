## Calculation of the parameterised coordinates
x, y = CST.CST(wl, wu, dz, N, yte)

# Interpolation of the parameterised points to construct the airfoil
ptList = []

for i in range(len(x)//2):
        pt = geompy.MakeVertex(x[i], y[i], 0)
        ptList.append(pt)
        #geompy.addToStudy(pt, "Pt_%s"%(i))
        pass

for i in range(len(x)//2+1, N):
        pt = geompy.MakeVertex(x[i], y[i], 0)
        ptList.append(pt)
        #geompy.addToStudy(pt, "Pt_%s"%(i))
        pass

## Find the line to create the blade-to-blade domain
meanPtList = []

import numpy as np

for i in range(len(ptList)//2+1):
        meanPtx = (geompy.PointCoordinates(ptList[i])[0]+geompy.PointCoordinates(ptList[len(ptList)-1-i])[0])/2
        meanPty = (geompy.PointCoordinates(ptList[i])[1]+geompy.PointCoordinates(ptList[len(ptList)-1-i])[1])/2
        meanPtz = (geompy.PointCoordinates(ptList[i])[2]+geompy.PointCoordinates(ptList[len(ptList)-1-i])[2])/2
        meanPt = geompy.MakeVertex(meanPtx, meanPty, meanPtz)
        meanPtList.append(meanPt)
        #geompy.addToStudy(meanPt, "Pt_Mean%s"%(i))
        pass

meanLine = geompy.MakeInterpol(meanPtList)

vector1 = geompy.MakeVector(ptList[-2], ptList[-1])
extrPoint = geompy.MakeTranslationVectorDistance(ptList[-1], vector1, 0.075)
TE = geompy.MakeArc(ptList[14], ptList[13], extrPoint)

ptList = ptList[14:]

for i in range(0, 100, 10):
        ptTE = geompy.MakeVertexOnCurve(TE, 1-(i/100))
        ptList.append(ptTE)
        #geompy.addToStudy(ptTE, "Pt_%s"%(i))

airfoil = geompy.MakeInterpol(ptList, True, False)

tangentBack = geompy.MakeVector(meanPtList[1], meanPtList[0])
tangentFront = geompy.MakeVectorDXDYDZ(-1, 0, 0) #(meanPtList[len(meanPtList)-2], meanPtList[len(meanPtList)-1])

extrudedFront = geompy.MakePrismVecH(meanPtList[len(meanPtList)-1], tangentFront, c)
extrudedBack = geompy.MakePrismVecH(meanPtList[0], tangentBack, c)

wireMwanLine = geompy.MakeWire([extrudedFront, meanLine, extrudedBack], 1e-07)
edgeMeanLine = geompy.MakeEdgeWire(wireMwanLine, 1e-1, 1e-12)

upperMeanLine = geompy.MakeTranslation(edgeMeanLine, 0, s/2, 0)
lowerMeanLine = geompy.MakeTranslation(edgeMeanLine, 0, -s/2, 0)

inletUpperVertex = geompy.MakeVertexOnCurve(upperMeanLine, 1)
inletLowerVertex = geompy.MakeVertexOnCurve(lowerMeanLine, 1)
outletUpperVertex = geompy.MakeVertexOnCurve(upperMeanLine, 0)
outletLowerVertex = geompy.MakeVertexOnCurve(lowerMeanLine, 0)

inlet = geompy.MakeLineTwoPnt(inletUpperVertex, inletLowerVertex)
outlet = geompy.MakeLineTwoPnt(outletUpperVertex, outletLowerVertex)

## Creation of the 2D fluid domain
faceFront = geompy.MakeFaceWires([inlet, upperMeanLine, outlet, lowerMeanLine, airfoil], True)
