f = open("distancias_cidades.txt", 'w')
for i in range(0, 99):
    for j in range(0, 99):
        f.write("De: " + str(i) + " Para: " + str(j) + " -> " + str(distancia(nodeX[i], nodeY[j])) + "\n")
f.close()