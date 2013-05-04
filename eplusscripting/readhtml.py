"""read the html outputs"""

from bs4 import BeautifulSoup, NavigableString, Tag

class NotSimpleTable(Exception):
    pass
        

def is_simpletable(table):
    """test if the table has only strings in the cells"""
    tds = table('td')
    for td in tds:
        if td.contents != []:
            if len(td.contents) == 1:
                if not isinstance(td.contents[0], NavigableString):
                    return False
            else:
                return False
    return True

def table2matrix(table):
    """convert a table to a list of lists - a 2D matrix"""
    if not is_simpletable(table):
        raise NotSimpleTable, "Not able read a cell in the table as a string"
    rows = []
    for tr in table('tr'):
        row = []
        for td in tr('td'):
            try:
                row.append(td.contents[0])
            except IndexError, e:
                row.append('')
        rows.append(row)
    return rows

# fname = "../outputfiles/V_7_2/5ZoneCAVtoVAVWarmestTempFlowTable.html"
# html_doc = open(fname, 'r').read()

def titletable(html_doc):
    """return a list of [(title, table), .....]
    title = previous item with a <b> tab
    table = rows -> [[cell1, cell2, ..], [cell1, cell2, ..], ..]"""
    soup = BeautifulSoup(html_doc)
    btables = soup.find_all(['b', 'table']) # find all the <b> and <table> 
    titletables = []
    for i, item in enumerate(btables):
        if item.name == 'table':
            for j in range(i + 1):
                if btables[i-j].name == 'b':# step back to find a <b>
                    break
            titletables.append((btables[i-j], item))
    titlerows = [(tl.contents[0], table2matrix(tb)) for tl, tb in titletables]
    return titlerows