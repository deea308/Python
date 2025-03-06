class MyPoint:
    def __init__(self,coord_x,coord_y,color):
        self.__coord_x=coord_x
        self.__coord_y=coord_y
        self.__color =color

    def get_coord_x(self):
        return self.__coord_x

    def set_coord_x(self,coord_x):
        self.__coord_x=coord_x

    def get_coord_y(self):
        return self.__coord_y

    def set_coord_y(self,coord_y):
        self.__coord_y=coord_y

    def get_color(self):
        return self.__color

    def set_color(self,color):
        self.__color=color

    def update_y(self,y):
        self.__coord_y=y

    def __str__(self):
        return f"Point({self.__coord_x},{self.__coord_y}) of color {self.__color}."



