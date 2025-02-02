def unique(list):
    unique_list = []
    for i in list:
        if(i in unique_list):
            continue
        unique_list.append(i)
    return unique_list

list = list(input().split())
print("unique list :" , *unique(list))