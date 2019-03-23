

def crossProduct(a: "tuple(x,y)",b: "tuple(x,y)",c: "tuple(x,y)") -> "int":
    """
    Module that returns the relative orientation of c with respect to ab

    Parameters:
    a,b,c: tuples of the form (x,y) repreenating points

    Returns:
    int : if result > 0 then c is left to ab else if result < 0 c is right of ab else a, b, and c are colinear
    """
    dy_ab = a[1] - b[1]
    dy_ac = a[1] - c[1]
    dx_ab = a[0] - b[0]
    dx_ac = a[0] - c[0]
    return (dy_ac * dx_ab) - (dy_ab * dx_ac)

def relative_distance(a: "tuple(x,y)",b: "tuple(x,y)",c: "tuple(x,y)") -> "int":
    """
    Module that returns the relative distance of c and b with respect to a

    Parameters:
    a,b,c: tuples of the form (x,y) repreenating points

    Returns:
    int : if result < 0 then b is closer to a than c else if result > 0 then c is closer to a than b else b and c are the same distance from a
    """
    dy_ab = a[1] - b[1]
    dy_ac = a[1] - c[1]
    dx_ab = a[0] - b[0]
    dx_ac = a[0] - c[0]
    
    rel_ab = (dy_ab **2) + (dx_ab **2)
    rel_ac = (dy_ab **2) + (dx_ab **2)

    return  (-1 if rel_ab < rel_ac else (1 if rel_ab > rel_ac else 0))


def jarvis_march(list_of_points: "int[]") -> "int[]":
    """
    Module that computes the Convex hull using the Jarvis March Algorithm O(N^2) O(N*H)

    Parameter:
    list_of_points (int[]) : list of (x,y) tuples representing points
    
    Returns:
    int[] : list of (x,y) that define the convex hull.
    """
    # Start the march at the left most point
    start = min(list_of_points, key = lambda point : point[0])
    # The first pivot point is the start
    current = start
    # There maybe repeated points for use a set to store the results
    result = []
    result.append(start)
    #colinear points -> Something to deal with as they occur...
    co_points = []
    #Loop that should terminate if the current point being considered is the start point
    while True:
        # For all points in the convex exculding the current
        # find the left most point using rel_or then set add that point to results
        # Set that point to current and continue until current is start
        
        for line_point in list_of_points:
            if(line_point == current):
                continue
            else:

                is_left_most = True                
                for point in list_of_points:
                    
                    rel_or = crossProduct(current,line_point,point)
                    if(rel_or > 0):
                        is_left_most = False
                
                if(is_left_most):
                    result.append(line_point)
                    current = line_point
                    break
                


        if(current == start):
            break
    return result


def graham_scan(list_of_points: "int[]") -> "int[]":
    """
    Module that computes the Convex hull using the Graham Scan O(NlogN)

    Parameter:
    list_of_points (int[]) : list of (x,y) tuples representing points
    
    Returns:
    int[] : list of (x,y) that define the convex hull.
    """
    pass



def convex_hull(list_of_points : "int[]", algo : "str" = "jarvis") -> "int[]":
    """
    Routing module that can route a request for the Convex hull to the apporiate algorithm

    Parameter:
    list_of_points (int[]) : list of (x,y) tuples representing points
    algo (str): string that should contain the name of a valid algorithm if not raises ValueError

    Returns:
    int[] : list of (x,y) that define the convex hull using the requested algorithm
    """
    if(len(list_of_points) < 3):
        return None

    elif("jarvis" in algo.lower()):
        return jarvis_march(list_of_points)

    elif("graham" in algo.lower()):
        return graham_scan(list_of_points)

    else:
        raise ValueError