#!/usr/bin/env python

## Description: airfoil geometry and mesh generator code based on salome library

import CST ## Parameterisation technique

## Geometry generation inputs
wl = [-0.17, 0.5, 0.5, 1.3, 1.4] ## CST weights of lower surface
wu = [0.8, 1.8, 2, 3.3, 2.9]     ## CST weights of upper surface
dz = 0.08                        ## half trailing edge thickness
N = 1000                         ## number of points discretizing the surfaces
c = 1                            ## airfoil chord
yte = -1.4                       ## y-coordinate of TE
s = 1                            ## pitch of the cascade

## Mesh generation inputs
maxSizeElem = 0.01      	 ## Element max size
minSizeElem = 0.003      	 ## Element min size
BLthick = 0.003         	 ## Prism layer thickness (structured O-Grid)
nLayers = 3             	 ## number of layers in the structured grid
growthRatio = 1.2       	 ## layers growth ratio in the structured grid

## Advices:
##      - keep the ratio maxSizeElem/minSizeElem approximately equal to 3 
##      - a large BLthick could lead to blows-up the process
##      - use a growthRatio value between 1.1 - 1.2

## Execute Salome library
exec(open("./salomeFiles.py").read())

## Airfoil geometry generation
exec(open("./fluidDomain.py").read())

## Name selection
exec(open("./salomeGeomGroups.py").read())

## Mesh generation
exec(open("./meshGeneration.py").read())

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
