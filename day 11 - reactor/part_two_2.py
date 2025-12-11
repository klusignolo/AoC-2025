with open("input.txt", "r") as file:
    lines = file.read().splitlines()
CONNECTIONS: dict[str,set] = {}
for line in lines:
    left, right = line.split(":")
    source_id = left.strip()
    destination_ids = set()
    for id in right.split():
        destination_ids.add(id.strip())
    CONNECTIONS[source_id] = destination_ids

def find_possible_path_count(start_device: str, target_device: str, avoid_device: str):
    global CONNECTIONS

    dead_ends = set() # This will be a list of all devices that lead to the target device
    dead_ends.add(target_device)
    for k,v in CONNECTIONS.items():
        if target_device in v and avoid_device not in v:
            dead_ends.add(k)
    prev_dead_ends_length = 0
    while len(dead_ends) != prev_dead_ends_length:
        prev_dead_ends_length = len(dead_ends)
        for path_key,path_children in CONNECTIONS.items():
            if path_key == avoid_device: continue # do not add these "waypoints"

            # A device leads to the target if all of its children would lead to at least one "dead end"
            if path_children.issubset(dead_ends) and path_key not in dead_ends:
                dead_ends.add(path_key)
    paths_to_target_count = 0
    possible_paths = []
    paths_in_progress = [[start_device]]
    while paths_in_progress:
        current_path = paths_in_progress.pop()
        last_node = current_path[-1]
        if last_node == 'out': continue
        for child in CONNECTIONS[last_node]:
            if child in current_path: # check if path already visited
                continue
            elif child in dead_ends: # check if path leads to 'out'
                if avoid_device not in current_path:
                    current_path.append(child)
                    possible_paths.append(current_path)
                    paths_to_target_count += len(CONNECTIONS[child])
            else:
                next_path = current_path.copy()
                next_path.append(child)
                paths_in_progress.append(next_path)
    return paths_to_target_count

svr_to_dac = find_possible_path_count(start_device="svr", target_device="dac", avoid_device="fft")
print("svr_to_dac: " + svr_to_dac)
svr_to_fft = find_possible_path_count(start_device="svr", target_device="fft", avoid_device="dac")
print("svr_to_fft: " + svr_to_fft)
dac_to_fft = find_possible_path_count(start_device="dac", target_device="fft", avoid_device="out")
print("dac_to_fft: " + dac_to_fft)
fft_to_dac = find_possible_path_count(start_device="fft", target_device="dac", avoid_device="out")
print("fft_to_dac: " + fft_to_dac)
fft_to_out = find_possible_path_count(start_device="dac", target_device="out", avoid_device="fft")
print("fft_to_out: " + fft_to_out)
fft_to_out = find_possible_path_count(start_device="fft", target_device="out", avoid_device="dac")
print("fft_to_out: " + fft_to_out)