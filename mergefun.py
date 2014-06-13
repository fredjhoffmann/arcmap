import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb'
import arcpy.sa
from arcpy.sa import CostPath
from arcpy.sa import CostDistance
import arcpy.da
cost='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\settlements_draft.gdb\\costlayer'

def mergefun(row, start, end):
	FIDa=str(row.getValue("FID"))
	where = '"FID" =' + FIDa
	out_fla='out_fl{0}'.format(FIDa)
	for FIDa in range (start,finish): 
		arcpy.MakeFeatureLayer_management(fc,out_fla,where) #i want acodist_{0} to cycle through all the codist layers, while out_fl stays the same
		FIDb=str(row.getValue("FID"))
		out_flab='out_fl{0}'.format(FIDb)
		for FIDb in range (start, finish):
			arcpy.sa.ExtractByMask('codist_{0}'.format(FIDb), out_fla).save(extract)
		if arcpy.GetRasterProperties_management(extract, "MINIMUM") <= threshold:
			arcpy.Merge_management([out_flab, out_fla], '"joined_{0}".format(FIDb) "and" {0}.format(FIDa)') ##the format() should be the number of the codist_{0} which passed the condition, so that the out_fl is the one which is considered joinable 
		arcpy.Delete_management(FIDa)
		arcpy.Delete_management(FIDb)



fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\Miyun_everything_raw\\popcenters\\miyun_villages_poly.shp'
cursor=arcpy.SearchCursor(fc)
for row in cursor:
	threshold=50000
	mergefun(row, 0, 2)
