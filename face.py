import json

# coord_vertices
file_name = "faces_cleaned.json"
cleaned_file = "face.json"
f = open("cleanedjson/" + file_name)
data_array = json.loads(json.dumps(json.load(f)))
f.close()

f_aux = open("cleanedjson/coord_vertices_cleaned.json")
vertices = json.loads(json.dumps(json.load(f_aux)))
f_aux.close()

f_aux = open("cleanedjson/colors_vertices_cleaned.json")
colors = json.loads(json.dumps(json.load(f_aux)))
f_aux.close()

list_aux = []

for i in range(len(data_array)):
    face_obj = {}
    face_obj["vertices"] = data_array[i]
    face_obj["vertices"][0]["vertice"] = vertices[data_array[i][0]["vertice"]]
    face_obj["vertices"][0]["cor"] = colors[data_array[i][0]["cor"]]
    face_obj["vertices"][1]["vertice"] = vertices[data_array[i][1]["vertice"]]
    face_obj["vertices"][1]["cor"] = colors[data_array[i][1]["cor"]]
    face_obj["vertices"][2]["vertice"] = vertices[data_array[i][2]["vertice"]]
    face_obj["vertices"][2]["cor"] = colors[data_array[i][2]["cor"]]
    list_aux.append(face_obj)

f_w = open("face/" + cleaned_file, "w")
f_w.write(json.dumps(list_aux))
f_w.close()