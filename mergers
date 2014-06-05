#to join the polygons into one:
#either merge
arcpy.Merge_management(["shapes represented by m", "shapes represented by n"], "C:/output/Output.gdb/")
#source http://resources.arcgis.com/en/help/main/10.2/index.html#/Merge/001700000055000000/
#or, but less sure about:
import arcmap
target_features =c:/Users... #the values for n 
join_features = c:/sers... #the values for m
out_feature_class = c:/users... #joined polygons -> the settlements which will now be considered as one in_source_data

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
#source http://resources.arcgis.com/en/help/main/10.1/index.html#//00080000000q000000

#joined polygons then need to be added to miyun_villages_poly to get a poligon set of all settlements in miyun.
#use append tool http://resources.arcgis.com/en/help/main/10.2/index.html#//001700000050000000
#synthax: import arcpy
#arcpy.env.workspace = "C:/data/"
#arcpy.Append_management(["north.shp", "south.shp", "east.shp", "west.shp"], "wholecity.shp", "TEST","","")
