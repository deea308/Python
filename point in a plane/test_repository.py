from repository import PointRepository
from classs import MyPoint

def test_add_point():
    repo = PointRepository()
    p1 = MyPoint(1,2,'blue')
    repo.add_point(p1)
    assert  repo.get_point_given_index(0).get_coord_x()==1
    assert repo.get_point_given_index(0).get_coord_y()==2
    assert repo.get_point_given_index(0).get_color()=='blue'

def test_get_point_given_index():
    repo = PointRepository()
    p1=MyPoint(1,2,'blue')
    p2=MyPoint(2,3,'red')
    repo.add_point(p1)
    repo.add_point(p2)
    assert repo.get_point_given_index(0).get_coord_x()==1
    assert repo.get_point_given_index(1).get_color()=='red'
    assert repo.get_point_given_index(0).get_color()== 'blue'

def test_get_point_same_color():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    assert repo.get_point_by_color('red')== [p2]
    assert repo.get_point_by_color('blue')==[p1,p3,p4]
    assert len(repo.get_point_by_color('blue'))==3

def test_point_inside_square():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    assert len(repo.get_point_inside_square(1,2,4))==1
    assert len(repo.get_point_inside_square(3,7,7))==2
    assert len(repo.get_point_inside_square(4,6,2))==1

#def test_minim_distance_two_points():

def test_update_point():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    repo.update_point(p4,2)
    assert repo.get_point_given_index(2).get_color()=='blue'
    assert repo.get_point_given_index(2).get_coord_x()==4
    assert repo.get_point_given_index(2).get_coord_y()==5

def test_delete_point_index():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    assert len(repo.delete_point_index(0))== 3

def test_delete_points_inside_square():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    assert len(repo.delete_inside_square(1,2,4))== 3
    assert len(repo.delete_inside_square(5,2,6))== 3
    assert len(repo.delete_inside_square(3,7,7))== 1

def test_get_number_points_same_color():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    assert (repo.get_number_points_by_color("red"))== 1
    assert (repo.get_number_points_by_color("blue"))==3
    assert (repo.get_number_points_by_color('green'))==0

def test_shift_points_y_axis():
    repo = PointRepository()
    p1 = MyPoint(1, 2, 'blue')
    p2 = MyPoint(2, 3, 'red')
    p3 = MyPoint(3, 4, 'blue')
    p4 = MyPoint(4, 5, 'blue')
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    repo.add_point(p4)
    repo.shift_point_on_y_axis(10)
    assert p1.get_coord_y()==12
    assert p2.get_coord_y()==13
    assert p4.get_coord_y()==15

def test_repo():
    test_add_point()
    test_get_point_given_index()
    test_get_point_same_color()
    test_point_inside_square()
    test_update_point()
    test_delete_point_index()
    test_delete_points_inside_square()
    test_get_number_points_same_color()
    test_shift_points_y_axis()
test_repo()








