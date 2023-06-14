def get_input():
    num = int(input())
    lst = list(map(int, input().split()))
    return num, lst


def bin_search(village, shelters):
    left = 0
    right = len(shelters) - 1
    while right - left > 1:
        middle = (left + right) // 2
        if village > shelters[middle]:
            left = middle
        else:
            right = middle

    shelter_idx = right if village > (shelters[left] + shelters[right]) // 2 else left
    return shelters[shelter_idx]

village_num, village_lst = get_input()
shelter_num, shelter_lst = get_input()
sorted_shelter_lst = sorted(shelter_lst)
original_shelter_indexes = {shltr_name : shltr_idx for shltr_idx, shltr_name in enumerate(shelter_lst, 1)}

for village in village_lst:
    shltr_name = bin_search(village, sorted_shelter_lst)
    print(original_shelter_indexes[shltr_name], end=' ')
print()