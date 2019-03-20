from BoundariesAlgorithms import convex_hull
import graphics as gp


def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def main():

    win = gp.GraphWin("Boundary Demo", 600, 400)
    win.setCoords(0,0,600, 400)
    win.setBackground("black")
    

    point_set = set()
    list_of_points = []
    all_drawn_objects = []

    while True:
        # check for new points and updated needed structures
        point = win.checkMouse()
        
        if( point and point not in point_set):
            point_set.add(point)
            list_of_points.append(point)

            #draw that point
            point.setOutline("white")
            point.draw(win)
           

            convex_list = convex_hull([(pt.getX(), pt.getY()) for pt in list_of_points])
            if(convex_list):
                clear(win)
                for pt in list_of_points:
                    point.setOutline("white")
                    pt.draw(win)
                poly = gp.Polygon(convex_list)
                poly.setOutline("white")
                poly.draw(win)

        key = win.checkKey()
        if(key and key == 'q'):
            
            win.close()
            break 

        
                      
        
        




    
if __name__ == "__main__":
    main()

