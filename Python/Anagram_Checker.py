# anagram -> A word or phrase that is made by arranging the letters of another word or phrase in a different order

# Example 1:- cat & act are anagrams
# Example 2:- listen & silent are anagrams
# Example 3:- fried & fired are anagrams

String_1 = input()
String_2 = input()

Sorted_String_1 = sorted(String_1)
Sorted_String_2 = sorted(String_2)

if (Sorted_String_1 == Sorted_String_2):
    print("String 1 & String 2 are ANAGRAMS")
else:
    print("String 1 & String 2 are **NOT** ANAGRAMS")
