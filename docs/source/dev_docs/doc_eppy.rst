.. sectionauthor:: Leora Tanjuatco

Documenting Eppy
================

If you want to contribute to the Eppy documentation, you'll need to jump through a few hoops. Why? If it were simple, it wouldn't be fun.

If your documentation uses code examples to demonstrate what your XXXXX can do, it's best to start in the iPython notebook. This is because you can actually run the code and make sure your examples are correct. Then you will have to convert your iPython notebook to restructured text. After that, Sphinx will generate the HTML file. I'll walk you through this in the "Ipython notebook" section.

If you don't need to use code to explain yourself, you can simply write documentation in restructured text, and then use Sphinx to generate an HTML file. For example, this text was written directly into a restructured text document and the converted to an HTML file with Sphinx.

Let's get started. 

*This documentation is in progress.*


Ipython notebook
----------------

**START HERE IF YOU'D LIKE TO INCLUDE EXAMPLES OF CODE IN YOUR DOCUMENTATION**

If you'd like to see an example of documentation written in the Ipython notebook, visit `Eppy Tutorial <http://pythonhosted.org/eppy/Main_Tutorial.html>`_

Installing the notebook
^^^^^^^^^^^^^^^^^^^^^^^

Installing the Ipython notebook is easy. `Start here <http://ipython.org/install.html>`_

Using the notebook
^^^^^^^^^^^^^^^^^^

Once you have installed the notebook, open Terminal and enter your virtual environment. Then, type "Ipython notebook" into Terminal. This will bring up a page with a list of all the items we have already created.

Each item, which looks like a document, is composed of cells. Click through a few of the items already created to see how to make a header cell and how to run a code cell. It's very straightforward. I won't explain too much, so as not to insult your intelligence.

Converting the notebook to RST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Restructured text
-----------------

**START HERE IF YOUR DOCUMENTATION IS ONLY TEXT**

Basics of RST
^^^^^^^^^^^^^

RestructuredText is a very simple markup language. In fact, the RestructuredText documents look very similar to the HTML pages themselves. I'd recommend simply opening the .rst documents in the "source" file, which are in the "docs" file. It's easy to see how to markup your text.

If you'd like a more structured approach, Thomas Cokelaer has created a nice `RestructuredText cheat sheet <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_

Linking
^^^^^^^

If you want to create a link to a website, the syntax is: 
[Should I use ipython for this?]

Adding pictures
^^^^^^^^^^^^^^^

Sphinx
------