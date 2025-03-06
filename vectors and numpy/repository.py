from MyVector import MyVector
import matplotlib.pyplot as plt
class VectorRepository:
    '''
    description: self.__vector- a list of vectors
    '''
    def __init__(self):
        self.__vector=[]

    '''
    description:adds a vector to the list of vectors
    input: the MyVector type of vector we want to add
    output:the final with the vectors
    '''
    def add_vector(self,vector):
        self.__vector.append(vector)

    '''
    description:gets all vectors from self.__vector
    output: a list with all the vectores
    '''
    def get_all_vectors(self):
        return self.__vector

    '''
    description:gets a vector at a given index
    input: self.__vector[i]-the vector at the index we want
    output: the vector we search for
    '''
    def get_vector_by_index(self,i):
        if 0 <= i and i < len(self.__vector):
            return self.__vector[i]
        else:
            return "Invalid index"

    '''
    description:updates a vector at a given index
    input: the vector we want to update and the index of the old vector we update
    output:it shows the updated vector
    '''
    def update_vector_by_index(self,i,new_vec):
        for j in range(len(self.__vector)):
            if i==j:
                self.__vector[i]=new_vec

    '''
    description:updates a vector at a given name
    input: the vector we want to update and the name of the old vector we update
    output:it shows the updated vector
    '''
    def update_vector_by_nameid(self,name,vec):
        for i in range(len(self.__vector)):
            if name== self.__vector[i].get_name_id():
                self.__vector[i]=vec

    '''
    description:this function deletes the vectors that are on the i'th position in the list of vectors
    input: the index we want to delete the vector
    output: the final list without the i'th vector
    '''
    def delete_vector_by_index(self,i):
        for j in range(len(self.__vector)):
            if i==j:
                del self.__vector[i]
        self.__vector

    '''
    description:this function deletes the vectors that has an exactly name
    input: the name of the vector we want to delete
    output: the final list without the vector with the specified name
    '''
    def delete_vector_by_nameid(self,name_id):
        i=0
        ok=0
        while i<len(self.__vector):
            if name_id==self.__vector[i].get_name_id():
                self.__vector.pop(i)
                i=i-1
                ok=1
            i=i+1
        if ok==0:
            print("there doesn't exist any vector witch that name_id")
        return self.__vector

    def plot_vec(self):
        for vectors in self.__vector:
            marker=vectors.get_type()
            if marker==1:
                marker='o'
            elif marker==2:
                marker='s'
            elif marker==3:
                marker='^'
            else:
                marker='d'

            color = vectors.get_color()
            x = vectors.get_values()[0]
            y = vectors.get_values()[1]

            plt.scatter(x, y, marker=marker, c=color, label=vectors.get_name_id())
        plt.legend()
        plt.show()
    #Pb21 EXTRA
    '''
    description: i add a scalar to the value of the vectors 
    input: the scalar i add to every values of every vector
    output: the final list with the vectors
    '''
    def update_vector_add_given_scalar(self,scalar):
        for vec in self.__vector:
            for i in range(len(vec.get_values())):
                vec.get_values()[i]+=scalar

    #PB10 EXTRA
    '''
    description: a vector that has the sum of all integer numbers of the vectors
    output: a new vector with the name "new", color "x"(we are not interested in the color but the numbers), the final type is the sum of alll number types and the final list 
            the final list contains the sum of all the elements of all the values from the vactors
    '''
    def get_sum_all_vectors(self):
        type=0
        num_values=0
        s=[0,0,0]
        for i in self.__vector:
            type+=i.get_type()
        for vector in range(len(self.__vector)):
            v1=self.__vector[vector].get_values()
            for i in range(len(s)):
                 s[i] += v1[i]
        #return s
        vector=MyVector('new','x',type,s)
        return vector

    '''
        description: a new vector that doesn't have the vector of which the product of the elements of the vector is greater then a given value 
        output: the final list of vector without the vectors which has the product of the elemts greater then a given value
        '''
    #PB18 EXTRA
    def delete_vec_product_greater(self,value):
        i=0
        while i<len(self.__vector):
            product=self.calculate_product(self.__vector[i].get_values())
            if product > value:
                self.__vector.pop(i)
                i=i-1
            i=i+1
        return self.__vector

    def calculate_product(self,values):
        product=1
        for v in values:
            product*=v
        return product

