from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashMap = {}
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return res.values()

def main():
    test_input1 = ["act","pots","tops","cat","stop","hat"]
    test_input2 = ["x"] 
    print(groupAnagrams(test_input1))
    print(groupAnagrams(test_input2))
    
if __name__ == '__main__':
    main()