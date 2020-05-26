
def main():
    input = [1,2,3,1]
    print(containsDuplicate(input))

def containsDuplicate(nums: list) -> bool:
    hm ={}
    for index in range(len(nums)):
        if nums[index] not in hm:
            hm[index] = 0
        else:
            return True
    return False

main()