from cmath import sqrt
import json

def p_func(vertice_cor_1, vertice_cor_2, vertice_cor_3):

    p_r = (vertice_cor_1["r"] + vertice_cor_2["r"] + vertice_cor_3["r"])/3
    p_g = (vertice_cor_1["g"] + vertice_cor_2["g"] + vertice_cor_3["g"])/3
    p_b = (vertice_cor_1["b"] + vertice_cor_2["b"] + vertice_cor_3["b"])/3
    p_a = (vertice_cor_1["a"] + vertice_cor_2["a"] + vertice_cor_3["a"])/3

    return p_r, p_g, p_b, p_a

f = open("face/face_area.json", "r")
data_array = json.loads(json.dumps(json.load(f)))
f.close()

for i in range(len(data_array)):
    first = data_array[i]["vertices"][0]["cor"]
    second = data_array[i]["vertices"][1]["cor"]
    third = data_array[i]["vertices"][2]["cor"]
    p_r, p_g, p_b, p_a = p_func(first, second, third)
    data_array[i]["p"] = {
        "r": p_r,
        "g": p_g,
        "b": p_b,
        "a": p_a,
    }

f_w = open("face/face_p.json", "w")
f_w.write(json.dumps(data_array))
f_w.close()