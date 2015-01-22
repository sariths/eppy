"""py.tests for idfobjects.py"""

import pytest
import copy
import eppy.idf_msequence as idfobjects
from eppy import modeleditor
from eppy.modeleditor import IDF
from eppy import bunchhelpers
from eppy.bunch_subclass import EpBunch

# idd is read only once in this test
# if it has already been read from some other test, it will continue with the old reading
from StringIO import StringIO
from eppy.iddcurrent import iddcurrent
iddfhandle = StringIO(iddcurrent.iddtxt)
if IDF.getiddname() == None:
    IDF.setiddname(iddfhandle)

def test_TypedList():
    """py.test for TypedList
    not used by eppy"""
    tl = idfobjects.TypedList((str, unicode), 'foo', 'bar')
    assert list(tl) == ['foo', 'bar']
    tl.append('zap')
    assert list(tl) == ['foo', 'bar', 'zap']
    with pytest.raises(TypeError):
            tl.append(23)

def test_TwoLists():
    """py.test for TwoLists
    Not used by eppy"""
    tl = idfobjects.TwoLists()
    tl.append(5)
    assert tl.list1 == [5]
    assert tl.list2 == ["r_5"]
    tl.extend([2,3,4])
    assert tl.list1 == [5, 2, 3, 4]
    assert tl.list2 == ["r_%s" % (i, ) for i in [5, 2, 3, 4]]
    tl.pop()
    assert tl.list1 == [5, 2, 3]
    assert tl.list2 == ["r_%s" % (i, ) for i in [5, 2, 3]]
    tl.pop(1)
    assert tl.list1 == [5, 3]
    assert tl.list2 == ["r_%s" % (i, ) for i in [5, 3]]
        
def test_FakeEpBunch():
    """py.test for FakeEpBunch"""
    fb = idfobjects.FakeEpBunch('jumpy')
    assert fb.Name == 'jumpy'
    assert fb.obj == ['jumpy', 'r_jumpy']
    
def test_Idf_MSequence_FakeEpBunch():
    """py.test for Idf_MSequence with FakeEpBunch"""
    idfobjs = idfobjects.Idf_MSequence_old()    
    fobj = idfobjects.FakeEpBunch('jumpy')
    idfobjs.append(fobj)
    assert list(idfobjs) == [fobj]
    assert idfobjs[0].obj == ['jumpy', 'r_jumpy']
    # ----
    fobj1 = idfobjects.FakeEpBunch('fatty')
    idfobjs.append(fobj1)
    assert list(idfobjs) == [fobj, fobj1]
    assert idfobjs[0].obj == ['jumpy', 'r_jumpy']
    assert idfobjs[1].obj == ['fatty', 'r_fatty']
    # ----
    idfobjs.pop()
    assert list(idfobjs) == [fobj]
    assert idfobjs[0].obj == ['jumpy', 'r_jumpy']
    assert len(idfobjs) == 1
    # ----
    idfobjs.remove(fobj)
    assert list(idfobjs) == []
    assert len(idfobjs) == 0

def test_Idf_MSequence_old():
    """py.test for Idf_MSequence_old suing an actual idf file"""
    def makeabunch(commdct, obj, obj_i):
        """make a bunch from the object"""
        objidd = commdct[obj_i]
        objfields = [comm.get('field') for comm in commdct[obj_i]]
        objfields[0] = ['key']
        objfields = [field[0] for field in objfields]
        obj_fields = [bunchhelpers.makefieldname(field) 
            for field in objfields]
        bobj = EpBunch(obj, obj_fields, objidd)
        return bobj
    abldg = ['BUILDING', 'Taj Mahal', 0.0, 'Suburbs', 0.04, 0.4, 
                            'FullExterior', 25, 6]
    idftxt = "" # empty string
    from StringIO import StringIO
    fhandle = StringIO(idftxt) # we can make a file handle of a string
    idf = IDF(fhandle) # initialize the IDF object with the file handle
    commdct = idf.idd_info
    obj_i = idf.model.dtls.index("BUILDING")
    idfobjs = idfobjects.Idf_MSequence_old()

    bobj = makeabunch(commdct, abldg, obj_i)
    idfobjs.append(bobj)
    assert idfobjs.list2 == [abldg]
    assert idfobjs[0].Name == 'Taj Mahal'

    abldg1 = copy.copy(abldg)
    abldg1[1] = 'Qoit tower'
    bobj1 = makeabunch(commdct, abldg1, obj_i)
    idfobjs.append(bobj1)
    assert idfobjs.list2 == [abldg, abldg1]
    assert idfobjs[0].Name == 'Taj Mahal'
    assert idfobjs[1].Name == 'Qoit tower'
    
    idfobjs.remove(bobj)
    assert idfobjs.list2 == [abldg1]
    assert idfobjs[0].Name == 'Qoit tower'
    
    idfobjs[0].Name = 'Karamba'
    assert idfobjs.list2[0][1] == 'Karamba'
