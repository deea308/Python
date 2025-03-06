import numpy as np

class MyVector_np:
    def __init__(self,name_id,color,type,values):
        self.__name_id=name_id
        self.__color=color
        self.__type=type
        self.__values=np.array(values)

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
    '''
    description:the function adds a scalar to each element of the vector
    input: the scalar we add to each element
    output: the list with the new vectors
    '''
    def add_scalar_np(self,scalar):
        self.__values +=scalar

    '''
    description:the function adds a vector to another vector
    input: the final vector after the sum of the vectors
    output: the list with the new vectors
    '''
    def add_vectors(self,vector1):
        self.__values+=vector1.__values

    '''
    description:the function subtract a vector from another vector
    input: the new vector we want to subtract with
    output: the list with the new vectors
    '''
    def subtract_vectors(self,vector1):
        self.__values-=vector1.__values

    '''
    description:the function multiply a vector with another vector
    input: the vector we want to multiply with 
    output: the list with the new vectors
    '''
    def multiply_vectors(self,vector1):
        self.__values*=vector1.__values

    '''
    description:the function sums the elements of the vectors
    output: the sum
    '''
    def sum_elements(self):
        return np.sum(self.__values)

    '''
    description:the function wants to calculate the product of the values of the vector
    output: the product
    '''
    def product_elements(self):
        return np.prod(self.__values)

    '''
    description:the function give the average element of the vector
    output: the average number
    '''
    def average_element(self):
        return np.mean(self.__values)

    '''
    description:the function give the minimum element of the vector
    output: the minimum number
    '''
    def min_elements(self):
        return np.min(self.__values)

    '''
    description:the function give the maximum element of the vector
    output: the maximum number
    '''
    def max_elements(self):
        return np.max(self.__values)


    def __str__(self):
        return f"vector of name:{self.__name_id}, color:{self.__color}, type:{self.__type}, values:{self.__values}"


