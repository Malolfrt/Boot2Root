from turtle import *


with open("../utils_writeup1/part3/turtle_dessin", "r") as f:
    for line in f:
        line = line.strip().lower()
        if not line:
            continue

        if line.startswith("avance"):
            value = int(line.split()[1])
            forward(value)
        elif line.startswith("recule"):
            value = int(line.split()[1])
            backward(value)
        elif "droite" in line:
            value = int(line.split("de")[1].split()[0])
            right(value)
        elif "gauche" in line:
            value = int(line.split("de")[1].split()[0])
            left(value)

done()
