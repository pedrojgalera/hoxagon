from matplotlib.pyplot import scatter, show
import numpy as np
import networkx



class baseHexagon(object):
    """Add class description"""
    def __init__(self):
        self.__edges__ = self.build_edges()

    def build_edges(self):
        """Add comment"""
        res = []
        base_angle = np.pi / 3

        #origin = np.array((0,0))
        #res.append(origin)
        for i in range(6):
            x = np.cos(base_angle * i)
            y = np.sin(base_angle * i)
            res.append(np.array((x,y)))
        return res

    def plot(self):
        x_coord = [edge[0] for edge in self.__edges__]
        y_coord = [edge[1] for edge in self.__edges__]

        scatter(x_coord, y_coord)
        show()



