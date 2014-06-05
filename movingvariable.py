#this code is designed to assign a value from a list to a variable, and have this value cycle through the list 
#as the variable is used in subsequent operations

##folowing two blocks creat strings u and v, which are the lists (strings, sets, easily changeable) which will be the source
##of the value for variables n and m
fc=villagesnear
field='IN_FID'
values = [row[0] for row in arcpy.da.SearchCursor(fc,(field))]
u=str(values)
print(u) ##prints a list of the ID  of every village with another within 500m

fc=villagesnear
field='NEAR_FID'
values = [row[0] for row in arcpy.da.SearchCursor(fc,(field))]
v=str(values)
print(v) ##essentially prints the same list of numbers as IN_FID, but to be used as destination data

#find an expression where n will be a revolving value in u, same for m in v

n=
m=

#n and m will then be run in a CostPath analysis, with n as the ID of the source poligon and m that of the destination.
costpath=arcpy.sa.CostPath('n' in 'miyun_villages_poly', 'costD', 'costB','EACH_ZONE','m' in 'miyun_villages_poly')
##find proper synthax for n to make sure it keeps the spatial data related to it in miyun villages poly. 
cursor=arcpy.da.InsertCursor('output','n','m')

threshhold_cost=1000
while (n<=4909):
	if n == m:
		skip
	if 'costpath'<='threshhold_cost':
		cursor.insertRow([n],[m])
		del cursor
	else:
 		print "done"
 		n+=1
