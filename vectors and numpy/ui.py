from repository import VectorRepository
from MyVector import MyVector
from MyVector_numpy import MyVector_np
def print_menu():
    menu = ('\tMenu:\n'
            '\t1.Add a vector to the repository\n'
            '\t2.Get all vectors\n'
            '\t3.Get a vector at a given index\n'
            '\t4.Update a vector at a given index\n'
            '\t5.Update a vector identified by name_id\n'
            '\t6.Delete a vector by index\n'
            '\t7.Delete a vector by name_id\n'
            '\t8.Plot all vectors in a chart based on the type and colour of ech other\n'
            '\t9.Get the vector that represents the sum of all vectors\n'
            '\t10.Delete all vectors for which the product of elements is greater then a given value\n'
            '\t11.Update all vectors by adding a given scalar to each element\n'
            '\t     Applications with numpy: \n'
            '\t     12.Add a scalar to the vector\n'
            '\t     13.Add a vector to the old vector\n'
            '\t     14.Subtract vectors\n'
            '\t     15.Multiply vector\n'
            '\t     16.Sum of elements of the vector\n'
            '\t     17.Product of elements of the vector\n'
            '\t     18.Average element of the vector\n'
            '\t     19.Minimum element of the vector\n'
            '\t     20.Maximum element of the vector\n'
            '\t0.Quit\n')
    print(menu)

def start():
    v_rep=VectorRepository()
    v1=MyVector('one','r',1,[1,2,3])
    v2=MyVector('two','b',2,[2,3,4])
    v3=MyVector('three','g',3,[3,4,5])
    v4=MyVector('four','y',4,[4,5,6])
    v5=MyVector('five','r',2,[5,6,7])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v_rep.add_vector(v4)
    v_rep.add_vector(v5)
    v1_rep=VectorRepository()
    v11 = MyVector_np('one', 'r', 1, [1,1,2])
    v12 = MyVector_np('two', 'b', 2, [2,2,3])
    v13 = MyVector_np('three', 'g', 3, [3,3,4])
    v14 = MyVector_np('four', 'y', 4, [4,4,5])
    v15 = MyVector_np('five', 'r', 2, [5,5,6])
    v1_rep.add_vector(v11)
    v1_rep.add_vector(v12)
    v1_rep.add_vector(v13)
    v1_rep.add_vector(v14)
    v1_rep.add_vector(v15)

    print_menu()
    stop=False
    while stop==False:
        option=input("give an option:")
        if option=='1':
            ok=1
            name_id=input("give a name id:")
            color=input("give the first letter of the color")
            while ok==1:
                if color!='r' and color!='b' and color!='g' and color!='y' and color!='m':
                    color=input("give another color:")
                else:
                    ok=0
            type=int(input("give a type:"))
            value1=int(input("give the first value of the vector: "))
            value2=int(input("give the second value of the vector: "))
            value3=int(input("give the third value of the vector: "))
            values=[value1,value2,value3]
            new=MyVector(name_id,color,type,values)
            v_rep.add_vector(new)

        elif option=='2':
            for vec in v_rep.get_all_vectors():
                print(str(vec))

        elif option=='3':
            i = int(input("Give an index:"))
            if i<0 or i>len(v_rep.get_all_vectors())-1:
                i=int(input("give another index"))
            print(str(v_rep.get_vector_by_index(i)))

        elif option=='4':
            name_id = input("give a name id:")
            color = input("give the first letter of the color")
            ok=1
            while ok==1:
                if color!='r' and color!='b' and color!='g' and color!='y' and color!='m':
                    color=input("give another color:")
                else:
                    ok=0
            type = int(input("give a type:"))
            index=int(input("give the index where you update the vector"))
            if index<0 or index>len(v_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            value1 = int(input("give the first value of the vector: "))
            value2 = int(input("give the second value of the vector: "))
            value3 = int(input("give the third value of the vector: "))
            values = [value1, value2, value3]
            v=MyVector(name_id,color,type,values)
            v_rep.update_vector_by_index(index,v)

        elif option=='5':
            name_id = input("give a name id:")
            color = input("give the first letter of the color")
            ok=1
            while ok==1:
                if color!='r' and color!='b' and color!='g' and color!='y' and color!='m':
                    color=input("give another color:")
                else:
                    ok=0
            type = int(input("give a type:"))
            nameid = input("give the name where you update the vector")
            value1 = int(input("give the first value of the vector: "))
            value2 = int(input("give the second value of the vector: "))
            value3 = int(input("give the third value of the vector: "))
            values = [value1, value2, value3]
            v = MyVector(name_id, color, type, values)
            v_rep.update_vector_by_nameid(nameid,v)

        elif option=='6':
            index=int(input("give the index:"))
            if index<0 or index>len(v_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            v_rep.delete_vector_by_index(index)

        elif option=='7':
            nameid=input("give the name: ")
            v_rep.delete_vector_by_nameid(nameid)

        elif option=='8':
            v_rep.plot_vec()

        elif option=='9':
            print(v_rep.get_sum_all_vectors())

        elif option=='10':
            value=int(input("give a value: "))
            v_rep.delete_vec_product_greater(value)

        elif option=='11':
            scalar=int(input("give a scalar: "))
            v_rep.update_vector_add_given_scalar(scalar)

        elif option=='12':
            scalar=int(input("give a scalar"))
            v11.add_scalar_np(scalar)
            v12.add_scalar_np(scalar)
            v13.add_scalar_np(scalar)
            v14.add_scalar_np(scalar)
            v15.add_scalar_np(scalar)
            for vec in v1_rep.get_all_vectors():
                print(str(vec))

        elif option=='13':
            type=int(input("give the type for the new vector"))
            value1 = int(input("give the first value of the vector: "))
            value2 = int(input("give the second value of the vector: "))
            value3 = int(input("give the third value of the vector: "))
            values = [value1, value2, value3]
            new_vector=MyVector_np('name','color',type,values)
            index=int(input("give the index where you want to add the new-vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            v1_rep.get_vector_by_index(index).add_vectors(new_vector)
            for vec in v1_rep.get_all_vectors():
                print(str(vec))

        elif option=='14':
            type = int(input("give the type for the new vector"))
            value1 = int(input("give the first value of the vector: "))
            value2 = int(input("give the second value of the vector: "))
            value3 = int(input("give the third value of the vector: "))
            values = [value1, value2, value3]
            new_vector = MyVector_np('name', 'color',type,values)
            index = int(input("give the index where you want to substract the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            v1_rep.get_vector_by_index(index).substract_vectors(new_vector)
            for vec in v1_rep.get_all_vectors():
                print(str(vec))

        elif option=='15':
            type = int(input("give the type for the new vector"))
            value1 = int(input("give the first value of the vector: "))
            value2 = int(input("give the second value of the vector: "))
            value3 = int(input("give the third value of the vector: "))
            values = [value1, value2, value3]
            new_vector = MyVector_np('name', 'color', type, values)
            index = int(input("give the index where you want to multiply the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            v1_rep.get_vector_by_index(index).multiply_vectors(new_vector)
            for vec in v1_rep.get_all_vectors():
                print(str(vec))


        elif option=='16':
            index = int(input("give the index where you want to sum the elements of the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            print(v1_rep.get_vector_by_index(index).sum_elements())

        elif option=='17':
            index = int(input("give the index where you want to product the elements of the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            print(v1_rep.get_vector_by_index(index).product_elements())

        elif option=='18':
            index = int(input("give the index where you want the average element of the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            print(v1_rep.get_vector_by_index(index).average_element())

        elif option=='19':
            index = int(input("give the index where you want the minimum element of the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            print(v1_rep.get_vector_by_index(index).min_elements())

        elif option=='20':
            index = int(input("give the index where you want the maximum element of the vector"))
            if index<0 or index>len(v1_rep.get_all_vectors())-1:
                index=int(input("give another index"))
            print(v1_rep.get_vector_by_index(index).max_elements())

        elif option=='0':
            stop=True

        else:
            print("the option does not exist")

start()