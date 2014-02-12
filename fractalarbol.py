#! /usr/local/bin/python3

import turtle
import random

ANG = 20    #ángulo de inclinación para las ramas
REL = 4/5   #relación entre la rama y las sub ramas
RAND = 20   #factor de aleatoriedad del ángulo de inclinación (grados)
RANDT = 60  #factor de aleatoriedad en el tamaño de las ramas (%)
CTRONCO = (111,0,255)  #color del tronco. tres números entre 0 y 255
CTRONCOVAR = 20         #factor de aletoriedad en el color del tronco
CHOJAS =  (64,224,208) #color de las hojas
CHOJASVAR = 50          #factor de aleatoriedad en el color de las hojas
CFONDO = (0,0,0)        #color de fondo
TAMINIC = 90            #tamaño del tronco inicial en pixeles
TAMHOJA = 10    #tamaño de la hoja
ANGHOJA = 100    #ángulo de las puntas de las hojas (180 = círculos)
PROF = 10       #cantidad de niveles en el árbol (más de 10 puede durar mucho dibujándose)

def arbol(t, d):
    if d==0:
        turtle.fd(t)
        hoja(TAMHOJA, ANGHOJA)
        turtle.back(t)
        return
    else:
        angulo1 = ANG + random.randrange(-RAND, RAND+1)
        angulo2 = ANG + random.randrange(-RAND, RAND+1)
        tamano = t + t*random.randrange(-RANDT, RANDT+1)/100
        colortronco = variacioncolor(CTRONCO, CTRONCOVAR)
        turtle.color(colortronco)
        turtle.pensize(d)
        turtle.fd(tamano)
        turtle.left(angulo1)
        arbol(t*REL, d-1)
        turtle.right(angulo1+angulo2)
        arbol(t*REL, d-1)
        turtle.color(colortronco)
        turtle.left(angulo2)
        turtle.back(tamano)

def hoja(t, a):
    turtle.color(variacioncolor(CHOJAS, CHOJASVAR))
    turtle.begin_fill()
    turtle.right(a/2)
    turtle.circle(t, a)
    turtle.left(180-a)
    turtle.circle(t, a)
    turtle.left(180-a/2)
    turtle.end_fill()


def variacioncolor(color, var):
    Rd = random.randrange(-var, var+1)
    Gd = random.randrange(-var, var+1)
    Bd = random.randrange(-var, var+1)
    R, G, B = color
    R += Rd
    G += Gd
    B += Bd
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return R, G, B
        
        
turtle.speed(0)
turtle.colormode(255)
turtle.penup()
turtle.left(90)
turtle.back(200)
turtle.pendown()
turtle.hideturtle()
turtle.color(CTRONCO)
turtle.bgcolor(CFONDO)

arbol(TAMINIC, PROF)

turtle.done()
