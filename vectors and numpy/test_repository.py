from repository import VectorRepository
from MyVector import MyVector

def test_add_vector():
    v_rep=VectorRepository()
    v1=MyVector('one','red',1,[1,2,3])
    v_rep.add_vector(v1)
    assert v_rep.get_vector_by_index(0).get_name_id()=='one'
    assert v_rep.get_vector_by_index(0).get_color()=='red'
    assert v_rep.get_vector_by_index(0).get_type()==1

def test_get_vector_by_index():
    v_rep = VectorRepository()
    v1=MyVector('one', 'red', 1, [1, 2,3])
    v2=MyVector('two','blue',1,[2,6,3])
    v3=MyVector('three','yellow',2,[5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    assert v_rep.get_vector_by_index(0).get_values()==[1,2,3]
    assert v_rep.get_vector_by_index(1).get_color()=='blue'
    assert v_rep.get_vector_by_index(2).get_name_id()=='three'

def test_update_vector_by_index():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1,2,3])
    v2 = MyVector('two', 'blue', 1, [2,6,3])
    v3 = MyVector('three', 'yellow', 2, [5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v4=MyVector('v4','red',2,[1,7,1])
    v5=MyVector('v5','blue',3,[7,9,10])
    v_rep.update_vector_by_index(2, v4)
    v_rep.update_vector_by_index(1, v5)
    assert v_rep.get_vector_by_index(1).get_color()=='blue'
    assert v_rep.get_vector_by_index(2).get_color()=='red'
    assert v_rep.get_vector_by_index(1).get_type()==3

def test_update_vector_name_id():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1,2,3])
    v2 = MyVector('two', 'blue', 1, [2,6,3])
    v3 = MyVector('three', 'yellow', 2, [5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v4 = MyVector('v4', 'red', 2, [1,7,1])
    v5 = MyVector('v5', 'blue', 3, [7,9,10])
    v_rep.update_vector_by_nameid('one',v4)
    v_rep.update_vector_by_nameid('two',v5)
    assert v_rep.get_vector_by_index(1).get_type()==3
    assert v_rep.get_vector_by_index(0).get_color()=='red'
    assert v_rep.get_vector_by_index(0).get_type()==2

def test_delete_vector_by_index():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1,2,3])
    v2 = MyVector('two', 'blue', 1, [2,6,3])
    v3 = MyVector('three', 'yellow', 2, [5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v_rep.delete_vector_by_index(0)
    v_rep.delete_vector_by_index(0)
    assert len(v_rep.get_all_vectors())==1

def test_delete_vector_name_id():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1,2,3])
    v2 = MyVector('two', 'blue', 1, [2,6,3])
    v3 = MyVector('three', 'yellow', 2, [5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v_rep.delete_vector_by_nameid('one')
    v_rep.delete_vector_by_nameid('two')
    assert len(v_rep.get_all_vectors())==1

def test_update_vector_add_given_scalar():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1,2,3])
    v2 = MyVector('two', 'blue', 1, [2,6,3])
    v3 = MyVector('three', 'yellow', 2, [5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v_rep.update_vector_add_given_scalar(4)
    assert v_rep.get_vector_by_index(0).get_values()==[5,6,7]
    assert v_rep.get_vector_by_index(1).get_values()==[6,10,7]
    assert v_rep.get_vector_by_index(2).get_values()==[9,10,6]

def test_get_sum_all_vectors():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1,2,3])
    v2 = MyVector('two', 'blue', 1, [2,6,3])
    v3 = MyVector('three', 'yellow', 2, [5,6,2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    assert v_rep.get_sum_all_vectors().get_values()==[8,14,8]

def test_delete_vec_product_greater():
    v_rep = VectorRepository()
    v1 = MyVector('one', 'red', 1, [1, 2, 3])
    v2 = MyVector('two', 'blue', 1, [2, 6, 3])
    v3 = MyVector('three', 'yellow', 2, [5, 6, 2])
    v_rep.add_vector(v1)
    v_rep.add_vector(v2)
    v_rep.add_vector(v3)
    v_rep.delete_vec_product_greater(7)
    assert len(v_rep.get_all_vectors())==1
def test_repo():
    test_add_vector()
    test_get_vector_by_index()
    test_update_vector_by_index()
    test_update_vector_name_id()
    test_update_vector_name_id()
    test_delete_vector_by_index()
    test_delete_vector_name_id()
    test_update_vector_add_given_scalar()
    test_get_sum_all_vectors()
    test_delete_vec_product_greater()

test_repo()