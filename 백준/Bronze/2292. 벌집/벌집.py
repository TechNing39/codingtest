N=int(input())

layer=1
max_room=1

while N>max_room:
    max_room+=6*layer
    layer+=1

print(layer)


    