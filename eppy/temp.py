iddfile = "./eppy/resources/iddfiles/Energy+V7_2_0.idd"
fname1 = "./eppy/resources/idffiles/V_7_2/smallfile.idf"

fname1 = "./eppy/resources/idffiles/V_7_2/box.idf"


BuildingSurface:Detailed, 
    E_Wall,                   !- Name
    Wall,                     !- Surface Type
    Exterior Wall,            !- Construction Name
    Box,                      !- Zone Name
    Outdoors,                 !- Outside Boundary Condition
    ,                         !- Outside Boundary Condition Object
    SunExposed,               !- Sun Exposure
    WindExposed,              !- Wind Exposure
    ,                         !- View Factor to Ground
    4,                        !- Number of Vertices
    5.0,                      !- Vertex 1 Xcoordinate
    0.0,                      !- Vertex 1 Ycoordinate
    3.0,                      !- Vertex 1 Zcoordinate
    5.0,                      !- Vertex 2 Xcoordinate
    0.0,                      !- Vertex 2 Ycoordinate
    0.0,                      !- Vertex 2 Zcoordinate
    5.0,                      !- Vertex 3 Xcoordinate
    6.0,                      !- Vertex 3 Ycoordinate
    0.0,                      !- Vertex 3 Zcoordinate
    5.0,                      !- Vertex 4 Xcoordinate
    6.0,                      !- Vertex 4 Ycoordinate
    3.0;                      !- Vertex 4 Zcoordinate
]

funnywall = idf1.newidfobject('BuildingSurface:Detailed'.upper(), 
                            Name="funnywall",
                            Surface_Type="Wall",
                            Number_of_Vertices=4,
                            Vertex_1_Xcoordinate=5,
                            Vertex_1_Ycoordinate=0,
                            Vertex_1_Zcoordinate=3,
                            Vertex_2_Xcoordinate=5,
                            Vertex_2_Ycoordinate=0,
                            Vertex_2_Zcoordinate=0,
                            Vertex_3_Xcoordinate=5,
                            Vertex_3_Ycoordinate=6,
                            Vertex_3_Zcoordinate=0,
                            Vertex_4_Xcoordinate=5,
                            Vertex_4_Ycoordinate=6,
                            Vertex_4_Zcoordinate=3,
                            )




from eppy import modeleditor
from eppy.modeleditor import IDF
iddfile = "./eppy/resources/iddfiles/Energy+V7_2_0.idd"
fname1 = "./eppy/resources/idffiles/V_7_2/smallfile.idf"
IDF.setiddname(iddfile)
idf1 = IDF(fname1)
fname1 = "./eppy/resources/idffiles/V_7_2/box.idf"
idf1 = IDF(fname1)

surfs = idf1.idfobjects["BuildingSurface:Detailed".upper()]
funnywall = idf1.newidfobject('BuildingSurface:Detailed'.upper(), 
                            Name="funnywall",
                            Surface_Type="Wall",
                            Number_of_Vertices=4,
                            Vertex_1_Xcoordinate=5,
                            Vertex_1_Ycoordinate=0,
                            Vertex_1_Zcoordinate=3,
                            Vertex_2_Xcoordinate=5,
                            Vertex_2_Ycoordinate=0,
                            Vertex_2_Zcoordinate=0,
                            Vertex_3_Xcoordinate=5,
                            Vertex_3_Ycoordinate=6,
                            Vertex_3_Zcoordinate=0,
                            Vertex_4_Xcoordinate=5,
                            Vertex_4_Ycoordinate=6,
                            Vertex_4_Zcoordinate=3,
                            )

fs = surfs[0]
ls = surfs[-1]
