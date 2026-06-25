def remove(l,word):
    n=[]
    for item in l :
        if not(item==word):
            n.append(item.strip(word))
    return n
l = ["harry","Dinesh","Rohini","Das"]
print(remove(l,"nesh"))