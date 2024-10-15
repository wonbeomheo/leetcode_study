from typing import List

def twoIntegerSum(nums: List[int], target: int) -> List[int]:
    hashMap = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        else:
            hashMap[n] = i
    return []


def main():
    test_nums1 = [3,4,5,6]
    test_target1 = 7
    print(twoIntegerSum(test_nums1, test_target1))

if __name__ == '__main__':
    main()