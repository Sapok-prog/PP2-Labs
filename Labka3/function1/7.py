
def has_33(nums):
    for i in range(len(nums)):
        if(nums[i] == str(3) and i + 1 < len(nums)):
            if(nums[i + 1] == str(3)):
                continue
            return False
    return True 

my_list = list(input().split())
print(has_33(my_list))
