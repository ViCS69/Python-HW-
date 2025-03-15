import sys
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

string1, string2 = sys.argv[1], sys.argv[2]


if are_anagrams(string1, string2):
    print("Anagrams")
else:
    print("Not anagrams")