import pygame, random 
from pygame.locals import *


#PARA GERAR UMA POSIÇÃO ALEATÓRIA PARA MAÇÃ
def on_grid_random(): # Definindo a posição aleatória, para a maçã
    x = random.randint(0,590) # a posição em x vai de 0 a 590, pois se for até 600, a maçã pode sair da tela no 600 (usando quadros de 10 em 10px)
    y = random.randint(0,590) # a posição em y vai de 0 a 590, pois se for até 600, a maçã pode sair da tela no 600 (usando quadros de 10 em 10px)
    return (x//10 * 10, y//10 * 10) # Para pular em multiplos de 10 . De 10 em 10 pixels tanto em x como em y

#PARA COLISÃO ENTRE CABEÇA DA COBRA E A MAÇÃ.. para maçã aparecer em outro lugar...
def collision(c1, c2): # Para colisão entre 2 celulas.
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) # quando a posição da celula 1 estiver em 0 == celula 2 e posiçao celula1 estiver em 1 == celula2 na mesma posição.

#INSERINDO AS DIREÇÕES - sentido horário
UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

pygame.init() #Início
screen = pygame.display.set_mode((600,600)) #Tamanho da Tela 600 x 600 pixels
pygame.display.set_caption('Snake') #Nome que aparece no canto superior esquerdo da Tela

#DEFININDO A COBRA
snake = [(200,200),(210,200),(220,200)] #Modelo de cobra, em lista, tupla representado pelos valores de 'x' e 'y'
snake_skin = pygame.Surface((10,10)) #Define superficie(desenho) da cobra em uma tupla de 10 por 10... Outra opção é usar 'Sprites' = usar imagem para representar a cobra
snake_skin.fill((255,255,255)) #Define cor da cobra... Branco = RGB 255,255,255 

#DEFININDO A MAÇÃ
apple_pos = on_grid_random() #Define a posição da maçã, no caso aleatória.
apple = pygame.Surface((10,10))#Define superficie(desenho) da maçã em uma tupla de 10 por 10... Outra opção é usar 'Sprites' = usar imagem para representar a maçã
apple.fill((255,0,0)) #Define cor da maçã... Vermelho = RGB 255,0,0

my_direction = LEFT # Indica a direção que a cobra está indo no começo do jogo... Esquerda.

clock = pygame.time.Clock() # Para conseguir limitar o FPS, para cobra não correr tão rápido..

while True: # Laço infinito = loop
    clock.tick(20) #Define FPS. Velocidade da cobra..
    for event in pygame.event.get(): #Pega eventos de mudança.. Ex.: Ao apertar um botão, uma tecla, pega esses eventos..
        if event.type == QUIT: # Evento de Fechar Jogo = Quando apertar o botão X  = 'Quit'
            pygame.quit() # Vai sair do jogo

# PARA CONSEGUIR CONTROLAR A COBRA
        if event.type == KEYDOWN: # Lê um evento do tipo KEYDOWN
            if event.key == K_UP: # Se o evento for a tecla UP.. quando clicar na seta pra cima
                my_direction = UP # A direção da cobra vai ser UP
            if event.key == K_DOWN: # Se o evento for a tecla DOWN.. quando clicar na seta pra baixo
                my_direction = DOWN # A direção da cobra vai ser DOWN
            if event.key == K_RIGHT:# Se o evento for a tecla RIGHT.. quando clicar na seta pra direita
                my_direction = RIGHT # A direção da cobra vai ser RIGHT
            if event.key == K_LEFT: # Se o evento for a tecla LEFT.. quando clicar na seta pra esquerda
                my_direction = LEFT # A direção da cobra vai ser LEFT

#QUANDO ACONTECER A COLISÃO DA COBRA COM A MAÇÃ
    if collision(snake[0], apple_pos): # Se tiver colisão entre a cobra e a posição da maçã
        apple_pos = on_grid_random() #Gera nova posição da maçã que será aleatória
        snake.append((0,0)) #Para aumentar a cobra...Nova posição para cobra, que vai tomar a posição anterior, que a cauda tinha antes..

#PARA MECHER O CORPO DA COBRA
    for i in range(len(snake)-1,0,-1): #Começa pelo rabo. A ultima posição da cobra vai ocupar a posição '-1'. Vamos até o '0', e '-1' para ir ao contrário, decrementando.
        snake[i] = (snake[i-1][0], snake[i-1][1]) #Cada posição da cobra vai receber uma nova tupla, que é [i-1]'posição anterior' + [0] e [i-1][1] 

#PARA COBRA MOVIMENTAR - CABEÇA DA COBRA
    if my_direction == UP:
        snake[0] = (snake[0][0], snake [0][1] - 10) #snake[0] = cabeça da cobra, ela recebe nova tupla baseada na posição anterior e vai pra proxima posição . Posição 'x'[0][0]  e posição 'y' [0][1]  (como está indo pra cima, o y está diminuindo , então '- 10'.)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake [0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake [0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake [0][1])  

    screen.fill((0,0,0)) #Tela Inteira Limpa  
    screen.blit(apple, apple_pos)  #Para 'plotar'(mostrar) maçã na tela. Passando a superficie, o desenho da maçã (apple) e sua posição em (apple_pos)
    for pos in snake: #Para cada posição da cobra
        screen.blit(snake_skin, pos) #Para 'plotar'(mostrar) cobra na tela. Passando a superficie, o desenho da cobra (snake_skin) e sua posição em (pos)

   #PARA RODAR O JOGO 
    pygame.display.update() # Server para atualizar a tela a todo momento.   