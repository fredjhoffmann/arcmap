import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb'
import arcpy.sa
from arcpy.sa import CostPath
from arcpy.sa import CostDistance
import arcpy.da
cost='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\settlements_draft.gdb\\costlayer'
def mergefun(row, start, end):
	FIDa=str(row.getValue("FID")) in range (start,end)
	FIDb=str(row.getValue("FID")) in range (start,end)
	wherea ='"FID" =' + FIDa
	whereb ='"FID" =' + FIDb
	out_fla='out_fl%i'%FIDa
	out_flab='out_fl%i'%FIDb
	threshold=50000
	arcpy.SelectFeatureLayerByLocation_manager('codist_{0}'.format(FIDa), INTERSECT, out_flab).save(overlap)
	if arcpy.Exists(overlap) is True:
		arcpy.sa.ExtractByMask('codist_{0}'.format(FIDa), out_flab).save(extract)
		print 'extract done {0} from {1}'.format(int(FIDa),int(FIDb))
		arcpy.GetRasterProperties_management("extract","MINIMUM").save('minimum')
		if int(getValue(minimum)) <= int(threshold):
			arcpy.Merge_management(out_fla,out_flab,'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\joinedtowns.gdb\\"merged_towns')
			t2=time.asctime()
			arcpy.Delete_management(minimum)
			print 'merge done at {0}'.format((t2))
	arcpy.Delete_management(FIDa)
	arcpy.Delete_management(FIDb)
	arcpy.Delete_management(out_fla)
	arcpy.Delete_management(out_flb)

fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\Miyun_everything_raw\\popcenters\\miyun_villages_poly.shp'
cursor=arcpy.SearchCursor(fc)
for row in cursor:
	mergefun(row, 0, 5)
