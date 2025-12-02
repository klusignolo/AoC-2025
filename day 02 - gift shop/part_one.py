with open("input.txt","r") as file_contents:
    id_list = file_contents.read().split(",")

invalid_ids = []
for id_range in id_list:
    bottom_and_top = id_range.split("-")
    bottom = int(bottom_and_top[0])
    top = int(bottom_and_top[1])
    for i in range(bottom, top+1):
        possible_id = str(i)
        id_length = len(possible_id)
        
        if id_length % 2 == 1: continue

        half_length = int(id_length / 2)
        left = possible_id[:half_length]
        right = possible_id[half_length:]
        if left == right:
            invalid_ids.append(i)
answer = sum(invalid_ids)
print(answer)