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


    i = fs["y"]*ft["z"]-ft["y"]*fs["z"]
    j = -fs["x"]*ft["z"]+ft["x"]*fs["z"]
    k = fs["x"]*ft["y"]-ft["x"]*fs["y"]

    area = 0.5*abs(sqrt(i*i + j*j + k*k))

    return area

f = open("face/face_cleaned.json", "r")
data_array = json.loads(json.dumps(json.load(f)))
f.close()

for i in range(len(data_array)):
    first = data_array[i]["vertices"][0]["vertice"]
    second = data_array[i]["vertices"][1]["vertice"]
    third = data_array[i]["vertices"][2]["vertice"]
    area = area_func(first, second, third)
    data_array[i]["area"] = area

f_w = open("face/face_area.json", "w")
f_w.write(json.dumps(data_array))
f_w.close()