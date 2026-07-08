#u have list of roll nos w u when iterating to search a particular roll no, if the roll no no found in the list: print roll no not present in the list
#if the roll no is fount in the list print roll no found and immediately stop searchin further

l=[1,72,11,22,24,33,44,55]
for i in l:
    if i==22:
        print("roll no found")
        break
else:
    print("roll no not found")

