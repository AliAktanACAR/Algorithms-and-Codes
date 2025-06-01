def ortalama(liste):
    i=0
    for a in liste:
        i+=a
    orta = i/len(liste)
    print(orta) 
    for b in liste:
        if b > orta:
            print(b)
          
liste = [1,2,3,4,5,6,7,8]
print(ortalama(liste))
