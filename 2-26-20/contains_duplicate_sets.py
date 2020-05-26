def main():
    input = [1, 2, 3, 1]
    print(containsDuplicate(input))

def containsDuplicate(nums: list) -> bool:
    set_of_nums = set()
    oopsie_doopsie = False
    for index in range(len(nums)):
        if nums[index] not in set_of_nums:
            set_of_nums.add(nums[index])
        else:
            oopsie_doopsie = True

    return oopsie_doopsie

main()