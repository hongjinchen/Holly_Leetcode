haystack = "sadbutsad"
needle = "sad"
if needle in haystack:
    for index in range(len(haystack)):
        if needle[0]==haystack[index]:
            if needle==haystack[index:index+len(needle)]:
                print(index)
