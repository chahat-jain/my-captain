import operator
def most_frequenct(string):
    d= dict()
    for x in string:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_d

print(most_frequenct('Mississippi'))
