#Estrella n lados
import turtle
t=turtle.Pen()
l=int(input("Ingrese el numero de lados:"))    
t.reset()
for x in range (l):
    t.forward(108)
    t.left((l-2)*180/l)
    t.left((l-2)*180/l)
