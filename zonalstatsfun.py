#the aim of this code is to extract data from a raster for each polygon in a feature class where polygons overlap
#this will permit the user to aggregate raster data to overlapping subwatershed or serviceshed level

import arcpy
arcpy.env.workspace='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014'
import arcpy.sa
import arcpy.da
import os
arcpy.env.overwriteOutput = True

def zonalstatsfun(FID,start,end):
	value='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\invest_workspace\\sedimentretention1990\\output\\rkls_1990.tif' #XXXX = raster dataset holding values to be extracted
	table='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\zonaldata.gdb\\sshed_rkls90'
	FID="FID"
	arcpy.sa.ZonalStatisticsAsTable(fc, FID, value, statable,"DATA","ALL")
	arcpy.Append_management(statable,table,'NO_TEST')
	print 'appended'
statable=arcpy.CreateTable_management('C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\zonaldata.gdb','statable', 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\socioecon_settlements.gdb\\USLE_sshed90')
sshed_rkls90=arcpy.CreateTable_management('C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\zonaldata.gdb','sshed_rkls90', 'C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\zonaldata.gdb\\statable')
fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\servicesheds_2014-06-24\\servicesheds_v0.shp'
cursor=arcpy.da.SearchCursor(fc, "FID")
for FID in cursor:
	zonalstatsfun(FID,0,0) #til total 2896
