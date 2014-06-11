arcmap
======

here is a selection of python snippets I am working on to process some GIS data using the python window in ESRI arcmap 10.2.

I have a set of settlement (shapefile) data, and the aim is to join some polygons that may be close enough to eachother. This is being done based on a set of costs calculated through arcmap. if the cost path between two settlements is low enough, the two polygons will be marked and joined. 


most of these are brainstorms/tests to see which methods work and which don't.
the most recent approach will rely on the 'disaggregation' method, by which the major shapefile is disaggregated, and each individual polygon tested for proximity to the next. 

The following files are currently regarded as part of the older methods, but may still be revisited:
- mergers.py
- movingvariable.py
- retabling.py
- disaggregation.py

dataextraction.py and costpath.py will be of use in future steps

master is the central file which will be updated to reflect the whole process once it is time 

costlayer.py defines how the cost layer was created

extractandcostdist.py is the first steps, until cost distance for each village has been decided
