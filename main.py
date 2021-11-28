# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
def draw():

    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    #g.graph_attr(labelloc="t")
    #g.graph_attr(label="My Diagram")
    #g.attr(size='6,6')
    g.graph_attr['rankdir'] = 'LR'

    g.node('001', label='Key to Nematoda\nin the Kootenay Area',fillcolor='red',style="filled")
    g.node('001.1', 'Cephalic setae',fillcolor='aqua',style="filled" )
    g.edge('001','001.1')
    g.edge('001.1','002', label='Indistinct')
    g.edge('001.1','064', label='Setae-like\nhead appendages')
    g.edge('001.1','069', label='Visible')
    g.node('', '',fillcolor='aqua',style="filled" )
    g.node('', '',fillcolor='aqua',style="filled" )
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')
    g.edge('','', label='')

    g.node('', '',fillcolor='aqua',style="filled" )
    g.node('', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")

    g.render('NematodaKey.gv', format='svg', view=True)
    #g.render('NematodaKey.gv', format='jpg', view=False)
    #g.render('NematodaKey.gv', format='pdf', view=False)

def main():
    # Use a breakpoint in the code line below to debug your script.
    draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
