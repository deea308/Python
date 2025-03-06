from repository import PointRepository
from classs import MyPoint

def printMenu(): #it prints the menu
    menu= ( '\tMenu:\n'
        '\t1. Add a point to the repository\n'
        '\t2. Get all points\n'
        '\t3.Get a point at a given index\n'
        '\t4.Get all points at a given color\n'
        '\t5.Get all points that are inside a given square\n'
        '\t6.Get the minimum distance between two points\n'
        '\t7.Update a point at a given index\n'
        '\t8.Delete a point bu index\n'
        '\t9.Delete all points that are inside a given square\n'
        '\t10.Plot all points in a chart\n'
        '\t11.Get the number of points of a given color\n'
        '\t12.Shift all point on the y axis\n'
        '\t13.Delete all points within a certain distance from a given point\n'
        '\t0.Quit\n')
    print(menu)

def start():
    point_rep=PointRepository()
    point_rep.add_point(MyPoint(1,6,'yellow'))
    point_rep.add_point(MyPoint(1, 3, 'red'))
    point_rep.add_point(MyPoint(2,4,'green'))
    point_rep.add_point(MyPoint(6,8,'blue'))
    point_rep.add_point(MyPoint(5,7,'magenta'))
    point_rep.add_point(MyPoint(4,4,'magenta'))
    point_rep.add_point(MyPoint(3,7,'red'))
    point_rep.add_point(MyPoint(1,5,'yellow'))
    point_rep.add_point(MyPoint(7,4,'magenta'))
    point_rep.add_point(MyPoint(6,3,'red'))
    printMenu()
    stop=False
    while stop==False:
        option=input("Give an option: ")
        if option=='1':
            coord_x = int(input("Give the x coordinate: "))
            coord_y = int(input("Give the y coordinate: "))
            color = input("Give the color: ")
            ok=1
            while ok==1:
                if color!='red' and color!='blue' and color!='green' and color!='yellow' and color!='magenta':
                    color=input("give another color:")
                    ok=1
                else:
                    ok=0
            point_rep.add_point(MyPoint(coord_x,coord_y,color))
        elif option=='2':
            for points in point_rep.get_all_points():
                print(str(points))
        elif option=='3':
            i=int(input("Give an index:"))
            print(str(point_rep.get_point_given_index(i)))
        elif option=='4':
            color=input("give a color:")
            ok=1
            while ok==1:
                if color!='red' and color!='blue' and color!='green' and color!='yellow' and color!='magenta':
                    color=input("give another color:")
                else:
                    ok=0
            for points in point_rep.get_point_by_color(color):
                print(str(points))
        elif option=='5':
            corner_x=int(input("Give an x coordinate:"))
            corner_y=int(input("Give an y coordinate:"))
            length=int(input("give a length:"))
            for i in point_rep.get_point_inside_square(corner_x,corner_y,length):
                print(i)
        elif option=='6':
            print(point_rep.get_min_distance())
        elif option=='7':
            coord_x=int(input("give a x coordinate:"))
            coord_y=int(input("give a y coordinate:"))
            color=input("give a color:")
            ok=1
            while ok==1:
                if color!='red' and color!='blue' and color!='green' and color!='yellow' and color!='magenta':
                    color=input("give another color")
                else:
                    ok=0
            i=int(input("give an index:"))
            point_rep.update_point(MyPoint(coord_x,coord_y,color),i)
        elif option=='8':
            i=int(input("Give an index"))
            if i<0 or i>len(point_rep.get_all_points())-1:
                i=int(input("give another index"))
            point_rep.delete_point_index(i)
        elif option=='9':
            corner_x=int(input("give a x coordinate:"))
            corner_y=int(input("give a y coordinate:"))
            length=int(input("give a length:"))
            point_rep.delete_inside_square(corner_x,corner_y,length)
        elif option=='10':
            point_rep.plot_all_points()
        elif option=='11':
            color=input("give a color:")
            ok=1
            while ok==1:
                if color!='red' and color!='yellow' and color!='blue' and color!='green' and color!='magenta':
                    color=input("give another color:")
                else:
                     ok=0
            print(point_rep.get_number_points_by_color(color))
        elif option=='12':
            value=int(input("give a value to shift y by:"))
            point_rep.shift_point_on_y_axis(value)
        elif option=='13':
            distance=int(input("give a distance:"))
            coord_x=int(input("give a x coordinate:"))
            coord_y=int(input("give a y coordinate"))
            point_rep.delete_points_certain_distance(distance,coord_x,coord_y)
        elif option=='0':
            stop=True
            print("Quit")
        else:
            print("the option does not exist")

start()
