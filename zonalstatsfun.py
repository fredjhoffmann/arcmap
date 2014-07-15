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

stat_table = workdir + r'\zonaldata.gdb\statable1'
arcpy.CreateTable_management(workdir + r'\zonaldata.gdb','statable1', tab_template)

with arcpy.da.SearchCursor(zonal_shp, ['FID']) as rows:
    for row in rows:

        fid = row[0]

        expression = '"FID" = ' + str(fid)
        temp_shp = workdir + r'\tempshp.shp'
        arcpy.Select_analysis(zonal_shp, temp_shp, expression)

        temp_tab =  workdir + r'\temptab.dbf'
        arcpy.sa.ZonalStatisticsAsTable(temp_shp, 'FID', inraster, temp_tab, "DATA", "SUM")

        with arcpy.da.UpdateCursor(temp_tab, ['FID_']) as recs:
            try:
                for rec in recs:
                    rec[0] = fid
                    recs.updateRow(rec)
                    print 'updated rec{0}'.format(fid)
            except NameError, RuntimeError:
                print 'skipped for nameerror'
                pass
        del rec, recs

        arcpy.Append_management(temp_tab, stat_table, 'NO_TEST')

        arcpy.Delete_management(temp_tab)
        arcpy.Delete_management(temp_shp)

del row, rows
##what i'd like to make work
## much of what is hashed out does not function.
import arcpy
import arcpy.da
import arcpy.sa
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True

workdir = r'C:\Users\frederichoffmann\Desktop\ESRI_summer2014'
inraster = workdir + r'\invest_workspace\sedimentretention1990\output\rkls_1990.tif'
zonal_shp = workdir + r'\servicesheds_2014-06-24\servicesheds_v0.shp'
tab_template = workdir + r'\zonaldata.gdb\template_namesum'
# outside_extent = workdir + r'\zonaldata.gdb\outex_tab'

stat_table = workdir + r'\zonaldata.gdb\statable1'
arcpy.CreateTable_management(workdir + r'\zonaldata.gdb','statable1', tab_template)
# arcpy.CreateTable_management(workdir + r'\zonaldata.gdb','outex_tab', tab_template)

with arcpy.da.SearchCursor(zonal_shp, ['Name']) as rows:
    for row in rows:

        Name = row[0]

        expression = '"Name" = ' + str(Name)
        temp_shp = workdir + r'\tempshp.shp'
        arcpy.Select_analysis(zonal_shp, temp_shp, expression) #change "NAME" back to expression if doesnt work

        temp_tab =  workdir + r'\temptab.dbf'
        arcpy.sa.ZonalStatisticsAsTable(temp_shp, 'Name', inraster, temp_tab, "DATA")#, "SUM")
        # arcpy.CreateTable_management(workdir, 'tempout.dbf', temp_tab)
        with arcpy.da.UpdateCursor(temp_tab, ['Name']) as recs:
            for rec in recs:
                rec[0] = Name
                try:
                    recs.updateRow(rec)
                    print 'sum updated{0}'.format(rec[0])
                except NameError:
                    print 'out of extent'
                    pass
                    # with arcpy.da.UpdateCursor(temp_out) as outrows:
                    #     for outrow in outrows:
                    #     	outrow[0] = fid w
                    #     	outrows.updateRow(outrow)
                    #     	print 'out of extent'
        # with arcpy.da.UpdateCursor(temp_tab, 'OID') as names: ##change OID if names do not come up as different SSHED names
        #     for name in names:
        #         name[0] = fid
        #         names.updateRow(name)
        #         print 'FID updated{0}'.format(fid)
        del rec, recs#, outrow, outrows #name, names

        arcpy.Append_management(temp_tab, stat_table, 'NO_TEST')
        # arcpy.Append_management(temp_out, outside_extent, 'NO_TEST')

        arcpy.Delete_management(temp_tab)
        arcpy.Delete_management(temp_shp)
        # arcpy.Delete_management(temp_out)

del row, rows


##### simplest, most effective version below. most similar to orginal approach too. much faster than other approaches
## only issue is that I cannot get it to only run for a certain amount of rows (it repeats to infinity)
#output is good: a table with FID and SUM of all values within zone. would be nice to have a column called Name with the 
#sshed name, but not a problem because FID can be a proxy for that.


import arcpy
from arcpy import da, sa, os
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True

workdir = r'C:\Users\frederichoffmann\Desktop\ESRI_summer2014'
zonaldb = workdir + r'\zonaldata.gdb'
tab_template = workdir + r'\zonaldata.gdb\template_sum'

statable=arcpy.CreateTable_management(zonaldb,'statable', tab_template)
values=arcpy.CreateTable_management(zonaldb,'sshed_rkls90', statable)
fc='C:\\Users\\frederichoffmann\\Desktop\\ESRI_summer2014\\servicesheds_2014-06-24\\servicesheds_v0.shp'
cursor=arcpy.da.SearchCursor(fc, "FID")
# start = 0
# end = 15

for FID in cursor:
    0<=FID<=5 #this is useless!
    value=workdir + r'\invest_workspace\sedimentretention1990\output\rkls_1990.tif' #XXXX = raster dataset holding values to be extracted
    table= zonaldb + r'\sshed_rkls90'
    FID="FID"
    arcpy.sa.ZonalStatisticsAsTable(fc, FID, value, statable,"DATA","SUM")
    arcpy.Append_management(statable,table,'NO_TEST')
    print 'appended'
