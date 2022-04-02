original_list = [int(element) for element in input().split()]
# Também poderia ser feito com list(map(int, input().split()))

copied_list = original_list.copy()  # Sempre dê nomes que indiquem propósito das variáveis!
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
