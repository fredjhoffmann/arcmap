import arcpy
arcpy.env.workspace = arcpy.scratchWorkspace = 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb\\miyun_allvillages'
import arcpy.sa
from arcpy.sa import CostPath
from arcpy.sa import CostDistance
import arcpy.da
import time
cost='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\settlements_draft.gdb\\costlayer'
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
def myfun(row, start, end):
	t1 = time.time() #for the print statement later which will help estimate remaining time
	FID = str(row.getValue("FID"))
	where = '"FID" =' + FID
	out_fl='fl_{0}'.format(FID) 
	if int(FID)>=start and int(FID)<end: 
		arcpy.MakeFeatureLayer_management(fc,out_fl,where)
		arcpy.sa.CostDistance(out_fl,cost,100000).save('codist_{0}'.format(FID))
		arcpy.Delete_management(out_fl)
		t2 = time.time()
		print 'done_{0}: time completed {1} ms: {2} rows remain'.format(FID,t2*1000,(end - int(FID)))

fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\Miyun_everything_raw\\popcenters\\miyun_villages_poly.shp'
cursor=arcpy.SearchCursor(fc)
for row in cursor:
	myfun(row, 600, 602) #change the range, needsto be done 300 at a time or arcmap crashes..
