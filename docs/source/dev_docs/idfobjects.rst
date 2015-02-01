
A list is not enough - Idf\_MSequence
=====================================


Some list operations
--------------------


Let us open an idf file

.. code:: python

    # you would normaly install eppy by doing
    # python setup.py install
    # or
    # pip install eppy
    # or
    # easy_install eppy
    
    # if you have not done so, uncomment the following three lines
    import sys
    # pathnameto_eppy = 'c:/eppy'
    pathnameto_eppy = '../../../'
    sys.path.append(pathnameto_eppy)
.. code:: python

    from eppy import modeleditor
    from eppy.modeleditor import IDF
    iddfile = "../../../eppy/resources/iddfiles/Energy+V7_2_0.idd"
    fname1 = "../../../eppy/resources/idffiles/V_7_2/dev1.idf"
    
    IDF.setiddname(iddfile)
    idf1 = IDF(fname1)
    idf1.printidf()

.. parsed-literal::

    
    VERSION,                  
        7.3;                      !- Version Identifier
    
    SIMULATIONCONTROL,        
        Yes,                      !- Do Zone Sizing Calculation
        Yes,                      !- Do System Sizing Calculation
        Yes,                      !- Do Plant Sizing Calculation
        No,                       !- Run Simulation for Sizing Periods
        Yes;                      !- Run Simulation for Weather File Run Periods
    
    BUILDING,                 
        Empire State Building,    !- Name
        30.0,                     !- North Axis
        City,                     !- Terrain
        0.04,                     !- Loads Convergence Tolerance Value
        0.4,                      !- Temperature Convergence Tolerance Value
        FullExterior,             !- Solar Distribution
        25,                       !- Maximum Number of Warmup Days
        6;                        !- Minimum Number of Warmup Days
    
    SITE:LOCATION,            
        CHICAGO_IL_USA TMY2-94846,    !- Name
        41.78,                    !- Latitude
        -87.75,                   !- Longitude
        -6.0,                     !- Time Zone
        190.0;                    !- Elevation
    
    MATERIAL:AIRGAP,          
        F04 Wall air space resistance,    !- Name
        0.15;                     !- Thermal Resistance
    
    MATERIAL:AIRGAP,          
        F05 Ceiling air space resistance,    !- Name
        0.18;                     !- Thermal Resistance
    


.. code:: python

    # we see that there are two MATERIAL:AIRGAP objects
    # let us take a look at them
    airgaps = idf1.idfobjects["MATERIAL:AIRGAP"]
    print airgaps

.. parsed-literal::

    [
    MATERIAL:AIRGAP,          
        F04 Wall air space resistance,    !- Name
        0.15;                     !- Thermal Resistance
    , 
    MATERIAL:AIRGAP,          
        F05 Ceiling air space resistance,    !- Name
        0.18;                     !- Thermal Resistance
    ]


-  We can see that there are two items in airgaps
-  each of these items are EpBunch objects
-  We know that EpBunch objects are really **syntactic sugar** for a
   simpler data structure. Earlier documentation explains how this
   happens
-  Just to review, let us dig a little deeper.


.. code:: python

    # looking at one of the airgaps, calling it airgap1
    airgap1 = airgaps[0]
    airgap1.obj



.. parsed-literal::

    ['MATERIAL:AIRGAP', 'F04 Wall air space resistance', 0.15]



.. code:: python

    # the underlying datasturcture we are working on is this one.
    idf1.model.dt["MATERIAL:AIRGAP"][0]



.. parsed-literal::

    ['MATERIAL:AIRGAP', 'F04 Wall air space resistance', 0.15]



Are these two lists really the same list. How can we check this. In
python we check the **id** of the objects. If they have the same **id**
then they are the same object

.. code:: python

    print id(airgap1.obj)
    print id(idf1.model.dt["MATERIAL:AIRGAP"][0])

.. parsed-literal::

    4438418640
    4438418640


Aha ! they are the same object. We know that ``airgap1`` is sysntactic
sugar for ``airgap.obj``, because that is how an EpBunch object works.

``airgap1`` was a single item in a list. We should start to look at the
entire list.

So we look at ``airgaps`` and compare it to
``idf1.model.dt["MATERIAL:AIRGAP"]``

.. code:: python

    print airgaps

.. parsed-literal::

    [
    MATERIAL:AIRGAP,          
        F04 Wall air space resistance,    !- Name
        0.15;                     !- Thermal Resistance
    , 
    MATERIAL:AIRGAP,          
        F05 Ceiling air space resistance,    !- Name
        0.18;                     !- Thermal Resistance
    ]


.. code:: python

    idf1.model.dt["MATERIAL:AIRGAP"]



.. parsed-literal::

    [['MATERIAL:AIRGAP', 'F04 Wall air space resistance', 0.15],
     ['MATERIAL:AIRGAP', 'F05 Ceiling air space resistance', 0.18]]



They don't quite look the same. At least they seem to print out
differently. Of course, both of them are lists.

-  We know that ``airgaps`` is a list of EpBunch objects.
-  ``idf1.model.dt["MATERIAL:AIRGAP"]`` looks like a list of lists

We know that any operation on ``airgaps[0]`` will access
``airgaps[0].obj`` which is the same as
``idf1.model.dt["MATERIAL:AIRGAP"][0]``. But how about an operation on
airgaps. if we delete an item in the ``airgaps``, will it remove an item
in ``idf1.model.dt["MATERIAL:AIRGAP"]``? As an example, let us look at a
specific operation.

-  for eppy to work correctly, poping a item in ``airgaps`` should pop
   an item in ``idf1.model.dt["MATERIAL:AIRGAP"]``
-  if ``airgaps`` is a list, ``airgaps.pop()`` will pop an item in
   airgaps. It will not pop an item in
   ``idf1.model.dt["MATERIAL:AIRGAP"]``
-  this is because, ``airgaps`` is a list. The list does not know that
   it is connected to another list 'idf1.model.dt["MATERIAL:AIRGAP"]'

How do we make this happen? How can we connect the two lists ?

In fact any list operation on ``airgaps``, should produce the same list
operation on ``idf1.model.dt["MATERIAL:AIRGAP"]``. Now, what are the
list operations ? In python, you can see all the functions of a object
by calling the function **dir** on it.

.. code:: python

    simplelist = [1,2,3,4]
    print dir(simplelist)

.. parsed-literal::

    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


You can see **pop** in the list, and many of the commonly used functions
like remove, reverse, insert.

Can we subclass the list object, so that any operation on ``airgaps``
will produce the same operation on ``idf1.model.dt["MATERIAL:AIRGAP"]``.
The subclassing strategy worked for us pretty well so far. ``Bunch`` is
a subclass of ``dict``. ``EpBunch`` is a subclass of ``Bunch``.

If we subclass ``list``, we will have to override all the functions of
``list`` and make sure that we do not break anything. This is getting
ugly very fast. The user may do many unexpected operations. For example,
the following operations are possible with list.

.. code:: python

    simplelist = simplelist + [11,22,33]
    print simplelist

.. parsed-literal::

    [1, 2, 3, 4, 11, 22, 33]


.. code:: python

    simplelist.insert(4, 104)
    print simplelist

.. parsed-literal::

    [1, 2, 3, 4, 104, 11, 22, 33]


.. code:: python

    simplelist.append(42)
    print simplelist

.. parsed-literal::

    [1, 2, 3, 4, 104, 11, 22, 33, 42]


.. code:: python

    simplelist.reverse()
    print simplelist

.. parsed-literal::

    [42, 33, 22, 11, 104, 4, 3, 2, 1]


.. code:: python

    print simplelist[2:5]

.. parsed-literal::

    [22, 11, 104]


We will be overriding all these functions. Can we be sure that they will
all work correctly. This is going to be difficult. There has to be an
easier way of doing this.

MutableSequence
---------------


The developers of python were expecting similar use cases and have given
us some built-in objects that will help us to get there. Specifically we
are importing the library ``collections`` and using a class called
``MutableSequence``.

The documentation for MutableSequence rather cryptic. It says that
MutableSequence is a subclass of Sequence and that List is a built-in
sequence. The end result is that MutableSequence has all the list
operations. But the real magic here is that we do not have to override
all the operations. We need to override only the follwoing operations:

-  ``__getitem__``
-  ``__setitem__``
-  ``__delitem__``
-  ``__len__``
-  ``insert``

If we override these operations, all the other operations will work as
expected. MutableSequence is an ``Abstract Base Class``. It cannot be
used directly. We have to subclass it and use the subclass.

Wow ! That is a lot of advanced stuff. It is hard to understand what it
all means. To be honest, I was not smart enough to understand that by
simply reading the standard python documentation. How would on even know
that such an object exists in the python documentation ?

Google to the rescue. I googled "subclassing lists in python", or
something to that effect. I found myself at:

http://stackoverflow.com/questions/3487434/overriding-append-method-after-inheriting-from-a-python-list

Here Alex Martelli makes an clearly described use case for using
MutableSequence and gives us the code for doing so. I have included this
code in the eppy source code (in eppy/idf\_msequence.py) as an example
of how to use MutableSequence and I have unit tested it.

Alex Martelli is one of the old time developers in python. He is also
one of the authors of "Python Cookbook". If you get a chance to a
BayPiggies meetup, you will probably meet him there. (Baypiggies is the
the python meetup in the south bay of the San Francisco Bay Area.)

Go take a look at the above link, spend some time reading it and then
return to reading this documentation.

Idf\_MSequence
--------------


Idf\_MSequence ? What is that ?

-  It is a sequence of idf objects
-  it is subclassed from MutableSequence
-  It could have been called ``Idf_MutableSequence``, but was shortened
   slightly to ``Idf_MSequence``

Let us take a look at the code for ``Idf_Msequence``

.. code:: python

    import collections
    # a code snippet from Idf_MSequence
    class Idf_MSequence(collections.MutableSequence):
        def __init__(self, list1, list2):
            super(Idf_MSequence, self).__init__()
            self.list1 = list1
            self.list2 = list2  
    # more below snipped off
From our example with airgaps above:

-  ``self.list1`` would be ``airgaps``
-  ``self.list2`` would be ``airgaps.obj``
-  we know that ``airgaps.obj`` is ``idf1.model.dt["MATERIAL:AIRGAP"]``


The rest of the code of ``Idf_MSequence`` simply overrides:

-  ``__getitem__``
-  ``__setitem__``
-  ``__delitem__``
-  ``__len__``
-  ``insert``

So that any operation on list1 will be duplicated in list2. Take a look
at the code in eppy/idf\_msequence.py and this will be clear.

``airgaps`` is of type ``Idf_MSequence``. Shall we check ?

.. code:: python

    print type(airgaps)

.. parsed-literal::

    <class 'eppy.idf_msequence.Idf_MSequence'>


Yup ! it is an Idf\_MSequence
