with open("input.txt", "r") as file:
    lines = file.read().splitlines()
device_connections: dict[str,set] = {}
for line in lines:
    left, right = line.split(":")
    source_id = left.strip()
    destination_ids = set()
    for id in right.split():
        destination_ids.add(id.strip())
    device_connections[source_id] = destination_ids

target_device = "out" # The last part of the path we want to hit


dead_ends = set() # This will be a list of all devices that lead to the target device
dead_ends.add(target_device)
prev_dead_ends_length = 0
while len(dead_ends) != prev_dead_ends_length:
    prev_dead_ends_length = len(dead_ends)
    for path_key,path_children in device_connections.items():
        if path_key == "fft" or path_key == "dac": continue # do not add these "waypoints"

        # A device leads to the target if all of its children would lead to at least one "dead end"
        if path_children.issubset(dead_ends) and path_key not in dead_ends:
            dead_ends.add(path_key)

def print_progress(pip: list[list[str]]):
    sorted_pop = sorted(pip, key=lambda x: len(x), reverse=True)
    print(f"Biggest Path: {len(sorted_pop[0])}. Last element: {sorted_pop[0][-1]}")
            
paths_to_target_count = 0
attempts = 0
paths_in_progress = [["svr"]]
while paths_in_progress:
    attempts += 1
    if attempts == 100000:
        print_progress(paths_in_progress)
        attempts = 0
    current_path = paths_in_progress.pop()
    last_node = current_path[-1]
    for child in device_connections[last_node]:
        if child in current_path: # check if path already visited
            continue
        elif child in dead_ends: # check if path leads to 'out'
            if "fft" in current_path and "dac" in current_path:
                paths_to_target_count += len(device_connections[child])
        else:
            next_path = current_path.copy()
            next_path.append(child)
            paths_in_progress.append(next_path)

print(paths_to_target_count)