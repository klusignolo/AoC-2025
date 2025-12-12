with open("input.txt", "r") as file:
    lines = file.read().splitlines()
device_connections: dict[str,set] = {}
for line in lines:
    left, right = line.split(":")
    source_id = left.strip()
    if source_id not in device_connections:
        device_connections[source_id] = set()
    for id in right.split():
        destination_id = id.strip()
        if destination_id not in device_connections:
            device_connections[destination_id] = set()
            device_connections[destination_id].add(source_id)
        else:
            device_connections[destination_id].add(source_id)

def get_count_of_possible_paths(from_id: str, to_id: str, avoid_id: str) -> int:
    to_parents = device_connections[to_id]
    if from_id in to_parents:
        return 1
    else:
        path_count = 0
        for parent in to_parents:
            if parent == avoid_id:
                continue
            path_count += get_count_of_possible_paths(from_id=from_id, to_id=parent, avoid_id=avoid_id)
        return path_count

# calculate all of these on different threads

fft_to_out = get_count_of_possible_paths(from_id="fft", to_id="out", avoid_id="dac")
print(f"fft_to_out: {fft_to_out}")
svr_to_dac = get_count_of_possible_paths(from_id="svr", to_id="dac", avoid_id="fft")
print(f"svr_to_dac: {svr_to_dac}")
svr_to_fft = get_count_of_possible_paths(from_id="svr", to_id="fft", avoid_id="dac")
print(f"svr_to_fft: {svr_to_fft}")
dac_to_fft = get_count_of_possible_paths(from_id="dac", to_id="fft", avoid_id="out")
print(f"dac_to_fft: {dac_to_fft}")
fft_to_dac = get_count_of_possible_paths(from_id="fft", to_id="dac", avoid_id="out")
print(f"fft_to_dac: {fft_to_dac}")
dac_to_out = get_count_of_possible_paths(from_id="dac", to_id="out", avoid_id="fft")
print(f"dac_to_out: {dac_to_out}")

svr_dac_fft_out_paths = fft_to_out
svr_dac_fft_out_paths *= dac_to_fft
svr_dac_fft_out_paths *= svr_to_dac

svr_fft_dac_out_paths = dac_to_out
svr_fft_dac_out_paths *= fft_to_dac
svr_fft_dac_out_paths *= svr_to_fft


answer = svr_dac_fft_out_paths + svr_fft_dac_out_paths
print(f"Answer: {answer}")