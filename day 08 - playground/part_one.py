import math
import re


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    junction_boxes = []
    for line in lines:
        split_line = line.split(",")
        junction_boxes.append((int(split_line[0]), int(split_line[1]), int(split_line[2])))

distances = {}
for i in range(len(junction_boxes)):
    for j in range(len(junction_boxes)):
        if i == j: continue
        key = f"<{i}>;<{j}>" if i < j else f"<{j}>;<{i}>"
        if key in distances: continue
        distance = math.dist(junction_boxes[i], junction_boxes[j])
        distances[key] = distance
connections = ""
total_connections = 1000
current_connection = 0
while current_connection < total_connections:
    current_connection += 1
    smallest_connection = min(distances, key=distances.get)
    distances.pop(smallest_connection)
    junction_a, junction_b = smallest_connection.split(";")
    box_a_name = junction_boxes[int(junction_a[1:-1])]
    box_b_name = junction_boxes[int(junction_b[1:-1])]
    print(f"Total connections: {current_connection}/{total_connections}")

    if junction_a in connections and junction_b in connections:
        index_of_a = connections.index(junction_a)
        index_of_b = connections.index(junction_b)
        slice = connections[index_of_a:index_of_b] if index_of_a < index_of_b else connections[index_of_b:index_of_a]
        if ";" in slice:
            split_circuits = connections.split(";")
            circuit_a = None
            circuit_b = None
            loop_i = 0
            while not circuit_a or not circuit_b:
                c_i = split_circuits[loop_i]
                loop_i += 1
                if junction_a in c_i:
                    circuit_a = c_i
                elif junction_b in c_i:
                    circuit_b = c_i
            connections = connections.replace(f";{circuit_a}", "").replace(f";{circuit_b}", "")
            connections += f";{circuit_a}-{circuit_b}"

    # add junction b to the existing chain
    elif junction_a in connections:
        index_of_a = connections.index(junction_a)
        connections = connections[:index_of_a] + f"{junction_b}-" + connections[index_of_a:]
 
    # add junction a to the existing chain
    elif junction_b in connections:
        index_of_b = connections.index(junction_b)
        connections = connections[:index_of_b] + f"{junction_a}-" + connections[index_of_b:]
    
    # add new connections to the chain
    else:
        connections += f";{junction_a}-{junction_b}"
circuits = [re.findall(r"<(\d+)>", connection) for connection in connections.split(";")]
circuits.sort(key=lambda x: len(x))
a,b,c = len(circuits[-1]), len(circuits[-2]), len(circuits[-3])
answer = a*b*c
print(answer)
# 7866 too low :(