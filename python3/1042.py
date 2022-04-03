original_list = [int(element) for element in input().split()]

copied_list = original_list.copy()  # Needed to avoid reference copy.
result = list()

for _ in range(len(original_list)):
    minimum = min(copied_list)
    result.append(minimum)
    copied_list.remove(minimum)

for element in result:
    print(element)

print()

for element in original_list:
    print(element)
