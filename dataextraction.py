##used to get informations stored in columns out of the tables and into a new one

#gets the in_fid and near_fid from the villagesnear table
villages = []
for row in arcpy.da.SearchCursor(villagesnear,['IN_FID','NEAR_FID']):
	villages.append(row)

#gets all the information in miyun_vilalges_poly
miyun_villages_poly_set = []
for row in arcpy.da.SearchCursor(miyun_villages_poly,'*'):
	miyun_villages_poly_set.append(row)

#sort set by fid
miyun_villages_poly_set.sort()
