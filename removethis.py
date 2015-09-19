# from eppy import modeleditor
# from eppy.modeleditor import IDF


import eppy

iddfile = "/Applications/EnergyPlus-8-3-0/Energy+.idd"
fname = "../kauai_police_calib_v3_m12_HVAC_5.idf"
# fname = "/Volumes/Server/Active_Projects/HNEI_KauaiPoliceStation/Simulation/energyplus/EEMs/eem12/kauai_police_calib_v3_m12_HVAC_3.idf"

eppy.IDF.setiddname(iddfile)
idf = eppy.IDF()
idf.save()