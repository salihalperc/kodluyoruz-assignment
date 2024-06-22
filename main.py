def euclideanDistance(x, y): #defintion for the function which obtain oklid distance
    oklid = ( (x**2) + (y**2) ) ** (1/2) #obtain oklid distance
    return oklid


points = [(1,2), (3, 7), (4, 9)]  #initialize list 'points' which includes (x,y) pairs.


distances = []  #initialize list 'distances' which inclues oklid distances


for data in points:  #for loop to add oklid distances

    distances.append(euclideanDistance(data[0], data[1]))


print(min(distances))  #print minimum distance value