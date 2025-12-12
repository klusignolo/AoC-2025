with open("test_input.txt", "r") as file:
    sections = file.read().split("\n\n")

class Present:
    def __init__(self, shape_matrix: list[list[str]]):
        self.shape_matrix = shape_matrix

    def smallest_shape_from_other_present(self, other_present: "Present") -> list[list[str]]:
        # Given another present, find the smallest shape that can contain both presents
        return []

class Tree:
    def __init__(self, input_str):
        left, right = input_str.split(":")
        self.width, self.height = map(int, left.split("x"))
        self.required_presents = [int(p) for p in right.strip().split(" ")]

    def can_hold_presents(self, presents: list[Present]) -> bool:
        # Check if the tree can hold the given presents
        # Given the required presents, grab the corresponding presents and check if they fit
        # T
        presents_to_fit = []
        for i in range(len(self.required_presents)):
            for _ in range(self.required_presents[i]):
                presents_to_fit.append(presents[i])
        return True

presents = [Present(present.splitlines()[1:]) for present in sections[:-2]]
trees = [Tree(tree_string) for tree_string in sections[-1].splitlines()]

valid_trees = [tree for tree in trees if tree.can_hold_presents(presents)]
print(f"Total valid trees: {len(valid_trees)}")