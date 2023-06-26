def twoSum(nums, target):
    dictionary = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in dictionary:
            return [dictionary[diff], i]
        dictionary[n] = i
    return


def main():
    nums = [2, 7, 11, 15]

    print(twoSum(nums, 9))


if __name__ == '__main__':
    main()
