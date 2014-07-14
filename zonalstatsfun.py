#the aim of this code is to extract data from a raster for each polygon in a feature class where polygons overlap
#this will permit the user to aggregate raster data to overlapping subwatershed or serviceshed level
### SEE BELOW FOR MORE RECENT CODE
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


##### DOING THIS WITHOUT DEFINING A FUNCTION
### idea curtesy of @nonpenso from GIS SE. code updated/altered by fredjhoffmann
 ##source : http://gis.stackexchange.com/questions/106839/calculating-zonal-statistics-of-raster-data-in-multiple-overlapping-zones-and-co/107076#107076 link

import arcpy
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True

workdir = r'C:\Users\frederichoffmann\Desktop\ESRI_summer2014'
inraster = workdir + r'\invest_workspace\sedimentretention1990\output\rkls_1990.tif'
zonal_shp = workdir + r'\servicesheds_2014-06-24\servicesheds_v0.shp'
tab_template = workdir + r'\zonaldata.gdb\template_fidsum'

stat_table = workdir + r'\zonaldata.gdb\statable'
arcpy.CreateTable_management(workdir + r'\zonaldata.gdb','statable', tab_template)

with arcpy.da.SearchCursor(zonal_shp, ['FID']) as rows:
    for row in rows:

        fid = row[0]

        expression = '"FID" = ' + str(fid)
        temp_shp = workdir + r'\tempshp.shp'
        arcpy.Select_analysis(zonal_shp, temp_shp, expression)

        temp_tab =  workdir + r'\temptab.dbf'
        arcpy.sa.ZonalStatisticsAsTable(temp_shp, 'FID', inraster, temp_tab, "DATA", "SUM")

        with arcpy.da.UpdateCursor(temp_tab, ['FID_']) as recs:
            for rec in recs:
                rec[0] = fid
                recs.updateRow(rec)
                print 'row updated{0}'.format(fid)
        with arcpy.da.UpdateCursor(temp_shp, 'Name') as FIDs:
            for FID in FIDs:
            	FID[0] = fid
                FIDs.updateRow(FID)
                print 'FID updated{0}'.format(fid)
        del rec, recs, FID, FIDs

        arcpy.Append_management(temp_tab, stat_table, 'NO_TEST')

        arcpy.Delete_management(temp_tab)
        arcpy.Delete_management(temp_shp)

del row, rows
