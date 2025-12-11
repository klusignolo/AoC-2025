with open("test_input.txt", "r") as file:
    lines = file.read().splitlines()
device_ids = set()
for line in lines:
    left, right = line.split(":")
    device_ids.add(left.strip())
    for id in right.split():
        device_ids.add(id.strip())
device_connections = {device_id: ([],[]) for device_id in device_ids}
for line in lines:
    left, right = line.split(":")
    left_id = left.strip()
    for id in right.split():
        right_id = id.strip()
        device_connections[left_id][1].append(right_id) # child
        device_connections[right_id][0].append(left_id) # parent

target_device = "you"
paths_to_target_count = 0
parents_to_trace = device_connections["out"][0]

unique_visits = set()
while parents_to_trace:
    current_parent = parents_to_trace.pop()
    if current_parent == target_device:
        paths_to_target_count += 1
    else:
        for grandparent in device_connections[current_parent][0]:
            key = f"{current_parent}:{grandparent}"
            if key in unique_visits:
                continue
            unique_visits.add(key)
            parents_to_trace.append(grandparent)

print(paths_to_target_count)