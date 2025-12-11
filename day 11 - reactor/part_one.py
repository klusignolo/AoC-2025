with open("input.txt", "r") as file:
    lines = file.read().splitlines()
dead_ends = set()
dead_ends.add("out")
device_connections: dict[str,set] = {}
for line in lines:
    left, right = line.split(":")
    source_id = left.strip()
    destination_ids = set()
    for id in right.split():
        destination_ids.add(id.strip())
    device_connections[source_id] = destination_ids

last_count = 1
current_count = 0
while current_count != last_count:
    last_count = current_count
    current_count = 0
    for k,v in device_connections.items():
        if v.issubset(dead_ends) and k not in dead_ends:
            current_count += 1
            dead_ends.add(k)
target_device = "out"
paths_to_target_count = 0

paths_in_progress = [["you"]]
while paths_in_progress:
    print(f"Paths found: {paths_to_target_count}; Length of path checks: {len(paths_in_progress)}")
    current_path = paths_in_progress.pop()
    last_node = current_path[-1]
    for parent in device_connections[last_node]:
        if parent in current_path:
            continue
        elif parent == target_device:
            paths_to_target_count += 1
        else:
            next_path = current_path.copy()
            next_path.append(parent)
            paths_in_progress.append(next_path)

print(paths_to_target_count)