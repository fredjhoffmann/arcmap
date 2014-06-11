#method devised to extract polygons from a shapefile, and calculate cost distance from each individual one

import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb\\miyun_allvillages'
import arcpy.sa
from arcpy.sa import CostPath
from arcpy.sa import CostDistance
import arcpy.da
cost='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\settlements_draft.gdb\\costlayer' #define cost layer

fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\Miyun_everything_raw\\popcenters\\miyun_villages_poly.shp'
cursor=arcpy.SearchCursor(fc)
for row in cursor:
	FID = str(row.getValue("FID"))
	where = '"FID" =' + FID
	out_fl='fl_{0}'.format(FID)
	for FID in range(0,1000): #need to break into segments because of unexpected crashing
		arcpy.MakeFeatureLayer_management(fc,out_fl,where)
		arcpy.sa.CostDistance(out_fl,cost,100000).save('codist_{0}'.format(FID))
		arcpy.Delete_management(out_fl) #delete useless files in process, clears up space and runs smoother
		print 'done_{0}'.format(FID) #printing this helps keep track of how much has been run
	else:
		print 'rangedone'
		break
