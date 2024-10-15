def isAnagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    for val in count:
        if val != 0:
            return False
    
    return True

def main():
    test_s1 = 'racecar'
    test_t1 = 'carrace'
    test_s2 = 'jar'
    test_t2 = 'jam'
    print(isAnagram(test_s1, test_t1))
    print(isAnagram(test_s2, test_t2))

if __name__ == '__main__':
    main()