import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb'
import arcpy.sa
import arcpy.da
cost='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\settlements_draft.gdb\\costlayer'
def mergefun(row, start, end):
	FIDa=str(row.getValue("FID")) in range (start,end)
	FIDb=str(row.getValue("FID")) in range (start,end)
	#wherea ='"FID" =%s'%FIDa
	#whereb ='"FID" =%s'%FIDb
	out_fla='out_fl%i'%FIDa
	out_flab='out_fl%i'%FIDb
	overlap='overlapfile'
	extract='extractfile'
	minimum='minimumfile'
	threshold=50000
	#make the feature layers
	if int(FIDa)>=start and int(FIDa)<end: 
		arcpy.MakeFeatureLayer_management(fc,out_fla)#,wherea
	if int(FIDb)>=start and int(FIDb)<end: 
		arcpy.MakeFeatureLayer_management(fc,out_flab)#,whereb
	arcpy.sa.ZonalStatistics(out_flab, 'FID', 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\miyun_allvillages.gdb\\codist_%i'%FIDa,"MINIMUM").save(minimum) #find out if villages overlap with cost layers
	#if arcpy.Exists(overlap) is True: #select only thos which do overlap
	#	arcpy.sa.ExtractByMask('codist_{0}'.format(FIDa), out_flab).save(extract) #extract cost information for overlap
	#	print 'extract done {0} from {1}'.format(int(FIDa),int(FIDb)) 
	#	arcpy.GetRasterProperties_management("extract","MINIMUM").save(minimum) #get minimum values of costs
	if minimum <= threshold: #find out if distance fits within travel threshold
		arcpy.Merge_management(out_fla,out_flab,'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\mergedvillages.gdb\\mergedvillages') #merge villages
		t2=time.asctime()
		arcpy.Delete_management(minimum)
		print 'merge done at {0}'.format((t2))
	else:
		print 'minimum !< threshold'
	arcpy.Delete_management(FIDa)
	arcpy.Delete_management(FIDb)
	arcpy.Delete_management(out_fla)
	arcpy.Delete_management(out_flb)

fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\Miyun_everything_raw\\popcenters\\miyun_villages_poly.shp'
cursor=arcpy.SearchCursor(fc)
for row in cursor:
	mergefun(row, 0, 5)
