# cheackIfWordIsPalindrom
# return True if a single word is a palindrom
# otherwise return False
def cheackIfWordIsPalindrom(str):
    if len(str) == 1:
        return True
    mid = len(str)//2+1
    for idx in range(mid):
        if str[idx] != str[-(idx+1)]:
            return False
    return True

# get_palindrom_dict
# return a dictionary
# key = the length of valuse words 
# valus = list of all sub words of given stirng that are palindrom
def get_palindrom_dict(str):
    palindrom_dict = {}
    for length in range(1, len(str)+1):
        for start_idx in range(len(str)+1-length):
            if cheackIfWordIsPalindrom(str[start_idx:start_idx + length]):
                if not length in palindrom_dict:
                    palindrom_dict[length] = []
                palindrom_dict[length].append(str[start_idx:start_idx + length])
    print("palindrom=",palindrom_dict)
    return palindrom_dict

# checkIfTwoStringsAreMatchmatch
# check if to string are simillar the following requirements:
# If all instances of a character int the first string can only be replaced with another single character in the second string.
# the order of the characters must be maintained
# return False if the strings length is different or requirement not maintained
# return True two string are simillar
def checkIfTwoStringsAreMatchmatch(str1, str2):
    if len(str1) != len(str2):
        return False
    if not str1:
        return True
    change_caracters = {}
    for idx in range(len(str1)):
        if not str1[idx] in change_caracters:
            change_caracters[str1[idx]] = str2[idx]
            continue
        else:
            if not change_caracters[str1[idx]] == str2[idx]:
                return False
    return True

# check_match
# check if the sub word in the even and odd indexes are simillar
# return True if two sub string are simillar, otherwise False
def check_match(str):
    if checkIfTwoStringsAreMatchmatch(str[:len(str):2], str[1:len(str):2]):
        return True
    return False
    
