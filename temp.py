"""just playing around"""

from eppy import modeleditor
from eppy.modeleditor import IDF
iddfile = "./eppy/resources/iddfiles/Energy+V7_2_0.idd"
fname1 = "./eppy/resources/idffiles/V_7_2/box.idf"


IDF.setiddname(iddfile)
idf = IDF(fname1)


surfs = idf.idfobjects['BuildingSurface:Detailed'.upper()]
s0= surfs[0]
sl = surfs[-1]
print s0.area
