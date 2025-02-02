def spy_game(nums):
    result = ''
    for i in nums:
        if(i == str(0) or i == str(7)):
            result += i
    if(result == '007'):
        return True
    return False

nums = list(input().split())
print(spy_game(nums))