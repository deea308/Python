from classs import MyPoint
import matplotlib.pyplot as plt
from math import sqrt
from math import dist
class PointRepository:
    '''
    description: self.__points- a list of points
    '''
    def __init__(self):
        self.__points = []

    '''
    description:adds a point to the list
    input: the MyPoint type of point we want to add
    output:the final with the points
    '''
    def add_point(self,point):
        return self.__points.append(point)

    '''
    description:gets all points from self.__points
    output: a list with all the points
    '''
    def get_all_points(self):
        return self.__points

    '''
    description:gets a point at a given index
    input: self.__points[i]-the point at the index we want
    output: the point we search for
    '''
    def get_point_given_index(self,i):
       if 0<=i and i<len(self.__points):
            return self.__points[i]
       else:
            return "Invalid index"

    '''
    description:gets all points of a given color
    input: the color we search for in the points
    output:the final list with all the points at the specific color
    '''
    def get_point_by_color(self,color):
        colorlst=[]
        for i in self.__points:
            if color==i.get_color():
                colorlst.append(i)
        if len(colorlst)>=0:
            return colorlst
        else:
            return 0

    '''
    description:gets all points that are inside a given square
    input: 2 indices for the corners: corner_x and corner_y and a length tor the slides of the square
    output:the exact points that are inside the square
    '''
    def get_point_inside_square(self,corner_x, corner_y, length):
        inside_square=[]
        for i in self.__points:
            if corner_x <= i.get_coord_x() <= corner_x+length:
                if corner_y >= i.get_coord_y() >= corner_y-length:
                    inside_square.append(i)
        return inside_square

    '''
    description:the minimum distance between two points
    output:the minimum distance
    '''
    def get_min_distance(self):
        minim=10000000000
        if len(self.__points) < 2:
            return None
        for p1 in range(len(self.__points)-1):
            for p2 in range(p1+1,len(self.__points)):
                distance=sqrt( (self.__points[p1].get_coord_x()-self.__points[p2].get_coord_x()) **2 + (self.__points[p1].get_coord_y()-self.__points[p2].get_coord_y()) **2)
                if distance<minim:
                    minim=distance
        return minim

    '''
    description:updates a point at a given index
    input: the point we want to update the point from the given index with
    output:it shows the updated point
    '''
    def update_point(self,point,index):
        self.__points[index]=point

    '''
    description:this function deletes a point by index
    input: the i indece we search for to delete the number
    output: the new list without the point of i indece that we deleted
    '''
    def delete_point_index(self,i):
        new_list=[]
        for j in range(len(self.__points)):
            if i!=j:
                new_list.append(self.__points[i])
            else:
                del self.__points[i] #it deletes the wanted point
        return new_list

    '''
    description:this function deletes the points that are inside a square
    input: the corner corner_x and corner_y of the square we want and the length of the slices of the square
    output: the final list without the points inside the square
    '''
    def delete_inside_square(self,corner_x,corner_y,length):
        pInsideSquare=self.get_point_inside_square(corner_x,corner_y,length)
        for p in pInsideSquare:
            self.__points.pop(self.__points.index(p))
        return self.__points

    '''
    description: we want to see the points with th colors of them in a chart
    '''
    def plot_all_points(self):
        x=[]
        y=[]
        color=[]
        for p in self.__points:
            x.append(p.get_coord_x())
            y.append(p.get_coord_y())
            color.append(p.get_color())
        plt.scatter(x,y,c=color)
        plt.show()
    #pb14 EXTRA
    '''
    description: numbers the point of a given color
    input: the color we search for
    output:return the final numbers of points of a color
    '''
    def get_number_points_by_color(self,color):
        k=0
        for elem in self.__points:
            if color==elem.get_color():
                k=k+1
        return k
    #pb17 EXTRA
    '''
    description:this function shifts all the points on the Y axis with a value
    input: a given value
    output: the shifted points
    '''
    def shift_point_on_y_axis(self,value):
        for i in range(len(self.__points)):
           self.__points[i].update_y(self.__points[i].get_coord_y()+value)
    #pb20 EXTRA
    '''
    description:this function delete the points within a certain distance from a given point
    input:distance- the distance we want to serch through for the points
            coord_x, coord_y- the coordonate from where we start looking
            color- the color of the point
    output:the list without the points
    '''
    def get_within_distance(self,coord_x,coord_y,distance):
        new_list = []
        for i in range(len(self.__points)):
            new_distance = dist((self.__points[i].get_coord_x(), self.__points[i].get_coord_y()), (coord_x, coord_y))
            if new_distance <= distance:
                new_list.append(self.__points[i])
        return new_list

    def delete_points_certain_distance(self,coord_x,coord_y,distance):
        points_within_distance = self.get_within_distance(coord_x,coord_y,distance)
        for elem in points_within_distance:
            if elem in self.__points:
                self.__points.pop(self.__points.index(elem))

