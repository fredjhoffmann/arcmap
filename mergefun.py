import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb'
import arcpy.sa
from arcpy.sa import CostPath
from arcpy.sa import CostDistance
import arcpy.da
cost='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\settlements_draft.gdb\\costlayer'

def mergefun(row, start, end):
	FIDa=str(row.getValue("FID"))
	FIDb=str(row.getValue("FID"))
	wherea = '"FID" =' + FIDa
	whereb = '"FID" =' + FIDb
	out_fla='out_fl{0}'.format(FIDa)
	out_flab='out_fl{0}'.format(FIDb)
	for FIDa in range (start,end): 
		arcpy.MakeFeatureLayer_management(fc,out_fla,wherea) #i want acodist_{0} to cycle through all the codist layers, while out_fl stays the same
	for FIDb in range (start,end): 
		arcpy.MakeFeatureLayer_management(fc,out_flab,whereb)
	for FIDb in range(start,end) and FIDa in range (start, end):
		arcpy.sa.ExtractByMask('C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb\\codist_{0}'.format(FIDb), out_fla)
		t1=time.asctime()
		print 'codist_{0}_extracted, time completed {1}'.format(FIDb, t1)
		if arcpy.GetRasterProperties_management('extractstat{0}'.format(FIDb), "MINIMUM") <= int(threshold):
			arcpy.Merge_management([out_flab, out_fla], 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\joinedtowns.gdb\\"merged_{0}".format(FIDb) "and" {0}.format(FIDa)') ##the format() should be the number of the codist_{0} which passed the condition, so that the out_fl is the one which is considered joinable 
			t2=time.asctime()
		else:
			continue
			print 'merged{0}{1}, time completed {2}'.format(FIDa,FIDb,t2)
	arcpy.Delete_management(FIDa)
	arcpy.Delete_management(FIDb)
	arcpy.Delete_management(out_fla)
	arcpy.Delete_management(out_flab)
	arcpy.Delete_management('C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\joinedtowns.gdb\\extract{0}'.format(FIDb))
	arcpy.Delete_management('C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\joinedtowns.gdb\\extractstat{0}'.format(FIDb))

fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\Miyun_everything_raw\\popcenters\\miyun_villages_poly.shp'
cursor=arcpy.SearchCursor(fc)
for row in cursor:
	threshold=50000
	mergefun(row, 0, 5)
