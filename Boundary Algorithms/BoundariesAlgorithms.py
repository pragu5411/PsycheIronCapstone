


def graham_scan(list_of_points: "int[]") -> "int[]":
    """
    Module that computes the Convex hull using the Graham Scan O(NlogN)

    Parameter:
    list_of_points (int[]) : list of (x,y) tuples representing points
    
    Returns:
    int[] : list of (x,y) that define the convex hull.
    """
    pass

def jarvis_march(list_of_points: "int[]") -> "int[]":
    """
    Module that computes the Convex hull using the Jarvis March Algorithm O(N^2)

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

    if("jarvis" in algo.lower()):
        return jarvis_march(list_of_points)

    elif("graham" in algo.lower()):
        return graham_scan(list_of_points)

    else:
        raise ValueError