import json
import os

script_dir = os.path.dirname(__file__)

# coord_vertices
file_name = "coord_vertices.json"
cleaned_file = "coord_vertices_cleaned.json"
f = open("tojson/" + file_name)
data_array = json.loads(json.dumps(json.load(f)))
list_vertices = []
for i in range(0, len(data_array), 3):
    point_obj = {}
    point_obj["x"] = data_array[i]
    point_obj["y"] = data_array[i+1]
    point_obj["z"] = data_array[i+2]
    list_vertices.append(point_obj)
f.close()
f_w = open("cleanedjson/" + cleaned_file, "w")
f_w.write(json.dumps(list_vertices))
f_w.close()

# normais vertices
file_name = "normal_vertices.json"
cleaned_file = "normal_vertices_cleaned.json"
f = open("./tojson/" + file_name)
data_array = json.loads(json.dumps(json.load(f)))
list_vertices = []
for i in range(0, len(data_array), 3):
    point_obj = {}
    point_obj["x"] = data_array[i]
    point_obj["y"] = data_array[i+1]
    point_obj["z"] = data_array[i+2]
    list_vertices.append(point_obj)
f.close()
f_w = open("./cleanedjson/" + cleaned_file, "w")
f_w.write(json.dumps(list_vertices))
f_w.close()

# coord_textura
file_name = "coord_textura.json"
cleaned_file = "coord_textura_cleaned.json"
f = open("./tojson/" + file_name)
data_array = json.loads(json.dumps(json.load(f)))
list_vertices = []
for i in range(0, len(data_array), 2):
    point_obj = {}
    point_obj["s"] = data_array[i]
    point_obj["t"] = data_array[i+1]
    list_vertices.append(point_obj)
f.close()
f_w = open("./cleanedjson/" + cleaned_file, "w")
f_w.write(json.dumps(list_vertices))
f_w.close()

# cores
file_name = "colors_vertices.json"
cleaned_file = "colors_vertices_cleaned.json"
f = open("./tojson/" + file_name)
data_array = json.loads(json.dumps(json.load(f)))
list_vertices = []
for i in range(0, len(data_array), 4):
    point_obj = {}
    point_obj["r"] = data_array[i]
    point_obj["g"] = data_array[i+1]
    point_obj["b"] = data_array[i+2]
    point_obj["a"] = data_array[i+3]
    list_vertices.append(point_obj)
f.close()
f_w = open("./cleanedjson/" + cleaned_file, "w")
f_w.write(json.dumps(list_vertices))
f_w.close()

# faces
file_name = "faces.json"
cleaned_file = "faces_cleaned.json"
f = open("./tojson/" + file_name)
data_array = json.loads(json.dumps(json.load(f)))
list_vertices = []
for i in range(0, len(data_array), 12):
    list_face = []
    first_point = {}
    first_point["vertice"] = data_array[i]
    first_point["normal"] = data_array[i+1]
    first_point["textura"] = data_array[i+2]
    first_point["cor"] = data_array[i+3]
    second_point = {}
    second_point["vertice"] = data_array[i+4]
    second_point["normal"] = data_array[i+5]
    second_point["textura"] = data_array[i+6]
    second_point["cor"] = data_array[i+7]
    third_point = {}
    third_point["vertice"] = data_array[i+8]
    third_point["normal"] = data_array[i+9]
    third_point["textura"] = data_array[i+10]
    third_point["cor"] = data_array[i+11]
    list_face.append(first_point)
    list_face.append(second_point)
    list_face.append(third_point)
    
    list_vertices.append(list_face)
f.close()
f_w = open("./cleanedjson/" + cleaned_file, "w")
f_w.write(json.dumps(list_vertices))
f_w.close()