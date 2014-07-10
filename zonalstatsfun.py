#the aim of this code is to extract data from a raster for each polygon in a feature class where polygons overlap

import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014'
import arcpy.sa
import arcpy.da
import os
arcpy.env.overwriteOutput = True
arcpy.CreateTable_management('C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\zonaldata.gdb', 'sshed_nxport90')
sattable = 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\zonaldata.gdb\\sattable'
def zonalstatsfun(row,start,end):
	zone_field="FID"
	value = 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\invest_workspace\\nut_ret_1990\\output\\n_export_1990.tif' #XXXX = raster dataset holding values to be extracted
	arcpy.sa.ZonalStatisticsAsTable(row, zone_field, value, sattable)
	arcpy.Append_management(stattable,sshednutret90)
	#insert line clearing content of sattable but not deleting the file
	print 'done serviceshed FID {0}'.format(int(in_zone))

fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\servicesheds_2014-06-24\\servicesheds_v0.shp'
cursor=arcpy.da.SearchCursor(fc, "FID")
for row in cursor:
	zonalstatsfun(row,0,3896)
