#datastructures
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}
#operation
union = E | N
intersection = E & N
difference = E - N
symmetric_diff = E ^ N
#printing
print("Union of E and N is", union)
print("Intersection of E and N is", intersection)
print("Difference of E and N is", difference)
print("Symmetric difference of E and N is", symmetric_diff)