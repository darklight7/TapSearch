def abcd(contents,word):
    iindex={}
    for i in range (len(contents)):
        for j in contents[i].split(" "):
            if(len(j)>0):
                if j not in iindex:
                    iindex[j]={i:1}
                    #print(iindex[j][i])
                else:
                    if(i not in iindex[j]):
                        iindex[j][i]=1
                    else:
                        iindex[j][i]+=1
    print("\n")
    print(iindex)
    print(type(word))
    ii=iindex[word]
    sorted_x=sorted(ii.items(),key=lambda kv:kv[1])
    print(sorted_x)
    rank=0
    for i in range(len(sorted_x)-1,-1,-1):
        rank+=1
        if(rank==11):
            break
        print(rank,"= Document",sorted_x[i][0])


