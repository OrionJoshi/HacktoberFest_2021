#Program to check whether a number is Palindrome or not.
# Method: Using pointers

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

# Time Complexity:  O(n)
# Space Somplexity: O(1)
