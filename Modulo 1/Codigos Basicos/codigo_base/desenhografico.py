import turtle

t = turtle.Turtle()
t.speed(3)

def desenhar():
    encostar = t.pen()["pendown"]
    if encostar:
        t.penup()
        print("não encostando")
    else:
        t.pendown()
        print("encostando")

def mover_para_cima():
    y = t.ycor()
    t.sety(y + 10)

def mover_para_baixo():
    y = t.ycor()
    t.sety(y - 10)

def mover_para_direita():
    x=t.xcor()
    t.setx(x +  10)

def mover_para_esquerda():
    x=t.xcor()
    t.setx(x - 10)

def mover_diagonal_direita_cima():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x+10, y+10))

def mover_diagonal_esquerda_baixo():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x-10, y-10))

def mover_diagonal_esquerda_cima():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x-10, y+10))


def mover_diagonal_esquerda_lado():
    x = t.xcor()
    y = t.ycor()
    t.setposition( (x+10, y-10))
    
def engrossar_caneta(): 
    grossura_da_linha = t.pen()["pensize"]
    t.pensize(grossura_da_linha + 1)

def afinar_caneta():
    grossura_linha = t.pen()["pensize"]
    if  grossura_linha - 1 >=1:
        t.pensize(grossura_linha-1)

def borracha():
    cor_de_fundo = tela.bgcolor()
    cor_caneta = t.pen()["pencolor"]

    if cor_caneta == cor_de_fundo:
        t.color("black")
      
    else:
        t.color(cor_de_fundo,"gray")

seguidor = turtle.Turtle()
seguidor.color("purple")
seguidor.shape("turtle")
seguidor.speed(100)
velocidade_seguidor = 100

def mover_seguidor():
    player_x = t.xcor()
    player_y = t.ycor()

    seguidor_x = seguidor.xcor()
    seguidor_y = seguidor.ycor()

    if abs(player_x - seguidor_x)> velocidade_seguidor:
        if player_x > seguidor_x:
            seguidor_x = seguidor_x + velocidade_seguidor
        else:
            seguidor_x = seguidor_x - velocidade_seguidor       
    else:
        seguidor_x = player_x
        
        
    if abs (player_y - seguidor_y) > velocidade_seguidor:
        if player_y > seguidor_y:
            seguidor_y = seguidor_y + velocidade_seguidor
        else:
            seguidor_y = seguidor_y - velocidade_seguidor
    else:
        seguidor_y = player_y

    seguidor.setposition(seguidor_x,seguidor_y)
    tela.ontimer(mover_seguidor,100)

     
tela = turtle.Screen()
tela.listen()
tela.onkeypress(mover_para_cima, "w" )
tela.onkeypress(mover_para_baixo, "s")
tela.onkeypress(mover_para_direita, "d")
tela.onkeypress(mover_para_esquerda, "a")
tela.onkeypress(mover_diagonal_direita_cima, "8")
tela.onkeypress(mover_diagonal_esquerda_baixo,"2")
tela.onkeypress(mover_diagonal_esquerda_cima,"6")
tela.onkeypress(mover_diagonal_esquerda_lado,"4")
tela.mainloop
tela.onkeypress(desenhar,"e")
tela.onkeypress(borracha,"f")
tela.onkeypress(engrossar_caneta,"7")
tela.onkeypress(afinar_caneta,"9")
mover_seguidor()
turtle.done()