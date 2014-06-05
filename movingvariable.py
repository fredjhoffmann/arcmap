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

n={0}.format(u)
m={0}.format(v)

#n and m will then be run in a CostPath analysis, with n as the ID of the source poligon and m that of the destination.
