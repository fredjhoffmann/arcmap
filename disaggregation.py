#the following code is used in a new attempt at the problem
#here, the original shapefile, which contains poligons for each village, will be broken into individual feature classes. 
#these will then be used to run a costdistance analysis

fc='C:\\Users\\xxxxxx\\miyun_villages_poly.shp'

cursor=arcpy.SearchCursor(fc)
for row in cursor:
	FID = str(row.getValue("FID"))
	where = '"FID" =' + FID
	out_fl='C:\\Users\\xxxxx\\miyun_allvillages.gdb\\allvillages_miyun\\fl_{0}'.format(FID)
	arcpy.MakeFeatureLayer_management(fc,out_fl,where)
	
#the result (processing at the time of writing) will be a database (miyun_allvillages.gdb) containing one shapefile
#for each polygon
