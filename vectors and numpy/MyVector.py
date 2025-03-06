import numpy as np

class MyVector:
    def __init__(self,name_id,color,type,values):
        self.__name_id=name_id
        self.__color=color
        self.__type=type
        self.__values=values

    def get_name_id(self):
        return self.__name_id
    def set_name_id(self,name_id):
        self.__name_id=name_id

    def get_color(self):
        return self.__color
    def set_color1(self,color):
        self.__color=color

    def get_type(self):
        return self.__type
    def set_type(self,type):
        self.__type=type

    def get_values(self):
        return self.__values
    def set_values(self,values):
        self.__values=values

    def scalarOperation(self,scalar):
        new_list=[]
        for i in range(len(self.__values)):
            new_list.append(self.__values[i]+scalar)
        return new_list



    def add_vectors(self,vector1,vector2):
        np.array(vector1)+np.array(vector2)

    def substract_vectors(self,vector1,vector2):
        return np.array(vector1)-np.array(vector2)

    def multiply_vectors(self,vector1,vector2):
        return np.dot(vector1, vector2)

    def sum_elements(self,vector):
        return np.sum(vector)

    def product_elements(self,vector):
        return np.prod(vector)

    def average_element(self,vector):
        return np.mean(vector)

    def min_elements(self,vector):
        return np.min(vector)

    def max_elements(self,vector):
        return np.max(vector)


    def __str__(self):
        return f"vector of name:{self.__name_id}, color:{self.__color}, type:{self.__type}, values:{self.__values}"


