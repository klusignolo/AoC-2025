with open("input.txt","r") as file_contents:
    id_list = file_contents.read().split(",")

def is_valid(possible_id: str) -> bool:
    id_length = len(possible_id)
    test_length = 0
    while test_length <= len(possible_id) / 2:
        test_length += 1
        test_chunk = possible_id[:test_length]

        if id_length % len(test_chunk) != 0:
            continue # The possible id must divide into equal parts of the test chunk's length

        start_index = test_length
        while start_index <= id_length - test_length:
            next_chunk = possible_id[start_index:start_index+test_length]
            if next_chunk != test_chunk:
                break # At least one chunk is not the same
            else:
                start_index += test_length
                if start_index == id_length:
                    return False # All chunks were the same
    return True
        

invalid_ids = []
for id_range in id_list:
    bottom_and_top = id_range.split("-")
    bottom = int(bottom_and_top[0])
    top = int(bottom_and_top[1])
    for i in range(bottom, top+1):
        possible_id = str(i)
        if not is_valid(possible_id):
            invalid_ids.append(i)

answer = sum(invalid_ids)
print(answer)