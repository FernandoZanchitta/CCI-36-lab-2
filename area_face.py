from cmath import sqrt
import json

def area_func(vertice_1, vertice_2, vertice_3):

    fs = {
        "x": vertice_2["x"]-vertice_1["x"], 
        "y": vertice_2["y"]-vertice_1["y"], 
        "z": vertice_2["z"]-vertice_1["z"]
    }

    ft = {
        "x": vertice_3["x"]-vertice_1["x"], 
        "y": vertice_3["y"]-vertice_1["y"], 
        "z": vertice_3["z"]-vertice_1["z"]
    }

    print("1) ", fs, ft)

    i = fs["y"]*ft["z"]-ft["y"]*fs["z"]
    j = -fs["x"]*ft["z"]+ft["x"]*fs["z"]
    k = fs["x"]*ft["y"]-ft["x"]*fs["y"]

    print("2) ", i, j, k)

    area = 0.5*abs(sqrt(i*i + j*j + k*k))

    return area

first_point = {"x": -5, "y": 5, "z": -5}
second_point = {"x": 1, "y": -6, "z": 6}
third_point = {"x": 2, "y": -3, "z": 4}

area = area_func(first_point, second_point, third_point)
print(area)