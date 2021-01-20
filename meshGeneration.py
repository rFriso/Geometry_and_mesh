import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(faceFront)
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( maxSizeElem )
NETGEN_2D_Parameters_1.SetMinSize( minSizeElem )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 80 )
Viscous_Layers_2D_1 = NETGEN_1D_2D.ViscousLayers2D(BLthick, nLayers, growthRatio, airfoilLine, 0)
isDone = Mesh_1.Compute()
airfoil_2 = Mesh_1.GroupOnGeom(airfoilLine,'airfoil',SMESH.EDGE)
periodicUp_1 = Mesh_1.GroupOnGeom(upperLine,'periodicUp',SMESH.EDGE)
PeriodicDown_1 = Mesh_1.GroupOnGeom(lowerLine,'PeriodicDown',SMESH.EDGE)
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.EDGE)
outlet_1 = Mesh_1.GroupOnGeom(outlet,'outlet',SMESH.EDGE)
[ airfoil_extruded, periodicUp_extruded, PeriodicDown_extruded, inlet_extruded, outlet_extruded, airfoil_top, periodicUp_top, PeriodicDown_top, inlet_top, outlet_top ] = Mesh_1.ExtrusionSweepObjects( [ Mesh_1 ], [ Mesh_1 ], [ Mesh_1 ], [ 0, 0, 0.001 ], 1, 1, [  ], 0, [  ], [  ], 0 )

try:
  Mesh_1.ExportUNV( r'/home/riccardo/OpenFOAM/riccardo-v1906/run/PhD/parameterisation/Mesh_1.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(airfoil_extruded, 'airfoil_extruded')
smesh.SetName(periodicUp_extruded, 'periodicUp_extruded')
smesh.SetName(PeriodicDown_extruded, 'PeriodicDown_extruded')
smesh.SetName(inlet_extruded, 'inlet_extruded')
smesh.SetName(outlet_extruded, 'outlet_extruded')
smesh.SetName(outlet_top, 'outlet_top')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(inlet_top, 'inlet_top')
smesh.SetName(PeriodicDown_top, 'PeriodicDown_top')
smesh.SetName(airfoil_2, 'airfoil')
smesh.SetName(PeriodicDown_1, 'PeriodicDown')
smesh.SetName(periodicUp_1, 'periodicUp')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(periodicUp_top, 'periodicUp_top')
smesh.SetName(airfoil_top, 'airfoil_top')
