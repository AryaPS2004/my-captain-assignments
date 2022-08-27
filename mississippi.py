def most_frequent(string):
    a=dict()
    for key in string:
        if key not in a:
            a[key]=1
        else:
            a[key]=a[key]+1
    return a
print(most_frequent('Mississippi'))
