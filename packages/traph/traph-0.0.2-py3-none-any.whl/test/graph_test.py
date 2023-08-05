from traph.ui.ui import TERMINAL as term
from traph.ui.shapes import MessageBox
from traph.graph import Graph
from traph.algorithms import load, bfs

def test_bfs():
    with term.fullscreen():
            y1 = term.height // 3 
            x1 = term.width // 3 
            pos = [ (x1, y1), (2*x1, y1 + 5), (x1, 2*y1), (2*x1, 2*y1 + 5), (term.width // 2, term.height // 2),
            (term.width // 2, term.height // 6), (x1*2, term.height // 6)]
            verts = [ 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
            e = [ ('v1', 'v2'), ('v1', 'v3'), ('v3', 'v4'), ('v4', 'v2'), ('v3', 'v5'), ('v5', 'v6'),
            ('v5', 'v7')]
            g = Graph(verts, e, pos)
            le, vc = load(g)
            bfs(le, vc, g)
            while True:
                pass

def test_boxes():
    with term.fullscreen():
        # box1 = MessageBox('tl', 'Hello world!\nFuck You!')
        msg = """
Hello, whats your name?
My name is Max!"""
        box2 = MessageBox('c', msg)
        box2.draw()
        while True:
            pass 

if __name__ == '__main__':
    test_boxes()