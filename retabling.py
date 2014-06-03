#working on some python code to try to pull information from an attribute table, run it through the arcmap's cost path 
#tool to select only certain data
#needs to be run through cost distance first
#synthax for cost distance tool:
#    CostDistance (in_source_data, in_cost_raster, {maximum_distance}, {out_backlink_raster})
#synthax for cost path tool:
#    CostPath (in_destination_data, in_cost_distance_raster, in_cost_backlink_raster, {path_type}, {destination_field})

arcpy.ImportToolbox("Toolboxes\System Toolboxes\Spatial Analyst Tools.tbx\Distance\Cost Distance")
arcpy.ImportToolbox("Toolboxes\System Toolboxes\Spatial Analyst Tools.tbx\Distance\Cost Path")

import arcpy
arcpy.env.workspace=r'C:\Users\frederichoffmann\Desktop\ESRI_summer2014\settlements_draft.gdb'
from arcpy.sa import *
import arcpy.da

#cost raster created formerly 
cost='C:\Users\frederichoffmann\Desktop\ESRI_summer2014\settlements_draft.gdb\costlayer'
#table with two columns: one of n and one of m, destination for data that meets criteria
output='C:\Users\frederichoffmann\Desktop\ESRI_summer2014\settlements_draft.gdb\joinabletowns'
# costdistance raster 
costD='C:\Users\frederichoffmann\Desktop\ESRI_summer2014\settlements_draft.gdb\cost_dist' 
#costbacklink raster 
costB='C:\Users\frederichoffmann\Desktop\ESRI_summer2014\settlements_draft.gdb\cost_backlink'

threshhold_cost=1000

#of shapefile attribute table (so theidentifier of each polygon) a variable that will move a 
n ='arcpy.da.SearchCursor(in_table, field_names)'
 #list of all values for n
m ='1+[arcpy.da.SearchCursor(in_table, field_names)]'

costpath=CostPath('n', 'costD', 'costB','EACH_ZONE','m')
cursor=arcpy.da.InsertCursor(output,n,m)

while (n<=m):
	if 'costpath'<='threshhold_cost':
		cursor.insertRow([n,m])
	else:
 		print "done"
 		n+=1
