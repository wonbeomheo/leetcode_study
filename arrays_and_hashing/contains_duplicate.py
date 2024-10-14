from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

def main():
    test_case = [1,2,3,4]
    test_case2 = [1,2,3,3]
    
    print(hasDuplicate(test_case))
    print(hasDuplicate(test_case2))

if __name__ == '__main__':
    main()
