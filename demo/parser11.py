def abc(contents, word):  # content is paragraph , word is word to be searched
    iindex = {}  # it will become a dictionary inside a dictionary
    contents = contents.split("\n")
    #   print("_______________")
    #   print(len(contents))
    #    for i in contents:
    #      print(i,"\n")
    #   print("_______________")
    for i in range(len(contents)):
        for j in contents[i].strip().replace(".", " ").replace(",", " ").lower().split(" "):
            if (len(j) > 0):
                if j not in iindex:
                    iindex[j] = {i: 1}
                    # print(iindex[j][i])
                else:
                    if (i not in iindex[j]):
                        iindex[j][i] = 1
                    else:
                        iindex[j][i] += 1
    print("\n")

    # print(iindex)
    # print(type(word))
    ii = iindex[word]
    sorted_x = sorted(ii.items(), key=lambda kv: kv[1])
    # print(sorted_x)
    lis = []
    for i in range(len(sorted_x) - 1, -1, -1):
        lis.append([sorted_x[i][0], contents[sorted_x[i][0]]])
    print(lis)
    return lis
