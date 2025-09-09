import pygame
import random

# Inicializando o Pygame
pygame.init()

pygame.mixer.music.load("Spider.mp3")  # Carrega a música
pygame.mixer.music.play(-1)  # Toca em loop infinito (-1)
pygame.mixer.music.set_volume(1.0)  # Volume (0.0 a 1.0)




# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo 2D - Desvie dos obstáculos")

fundo = pygame.image.load("Spider.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))
  # Ajusta o tamanho da tela
# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Jogador
jogador_largura = 50
jogador_altura = 50
jogador_x = largura // 2 - jogador_largura // 2
jogador_y = altura - jogador_altura - 10
velocidade_jogador = 5

# Obstáculos
obstaculos = []
obstaculo_largura = 50
obstaculo_altura = 50
velocidade_obstaculo = 5
spawn_timer = 0

# Relógio para controlar FPS
clock = pygame.time.Clock()

# Pontuação
pontuacao = 0
fonte = pygame.font.SysFont(None, 36)

# Função para desenhar texto
def desenhar_texto(texto, cor, x, y):
    img = fonte.render(texto, True, cor)
    tela.blit(img, (x, y))

# Loop principal
rodando = True
while rodando:
    clock.tick(60)  # 60 FPS
    tela.blit(fundo, (0, 0))


    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_x < largura - jogador_largura:
        jogador_x += velocidade_jogador

    # Criar obstáculos
    spawn_timer += 1
    if spawn_timer > 30:  # A cada 0,5s aproximadamente
        x_obstaculo = random.randint(0, largura - obstaculo_largura)
        obstaculos.append([x_obstaculo, -obstaculo_altura])
        spawn_timer = 0

    # Movimentar obstáculos
    for obstaculo in obstaculos:
        obstaculo[1] += velocidade_obstaculo
        pygame.draw.rect(tela, VERMELHO, (obstaculo[0], obstaculo[1], obstaculo_largura, obstaculo_altura))

    # Remover obstáculos que saíram da tela
    obstaculos = [o for o in obstaculos if o[1] < altura]

    # Desenhar jogador
    pygame.draw.rect(tela, AZUL, (jogador_x, jogador_y, jogador_largura, jogador_altura))

    # Checar colisão
    for obstaculo in obstaculos:
        if (jogador_x < obstaculo[0] + obstaculo_largura and
            jogador_x + jogador_largura > obstaculo[0] and
            jogador_y < obstaculo[1] + obstaculo_altura and
            jogador_y + jogador_altura > obstaculo[1]):
            rodando = False

    # Atualizar pontuação
    pontuacao += 1
    desenhar_texto(f"Pontuação: {pontuacao}", PRETO, 10, 10)

    # Atualizar tela
    pygame.display.update()

# ... (restante do código igual)

# Inicializa as variáveis de dificuldade
velocidade_obstaculo = 5
spawn_interval = 30  # número de frames para spawnar um obstáculo (30 frames = 0.5s em 60 FPS)

def ajustar_dificuldade(pontuacao):
    global velocidade_obstaculo, spawn_interval
    # Aumenta a velocidade dos obstáculos a cada 100 pontos, até um limite
    velocidade_obstaculo = 5 + pontuacao // 100
    if velocidade_obstaculo > 15:
        velocidade_obstaculo = 15
    
    # Diminui o intervalo entre os obstáculos até um limite (mínimo 10 frames)
    spawn_interval = 30 - pontuacao // 100
    if spawn_interval < 10:
        spawn_interval = 10

# No loop principal, antes de criar obstáculos:
ajustar_dificuldade(pontuacao)

# Criar obstáculos
spawn_timer += 1
if spawn_timer > spawn_interval:  # usa o spawn_interval dinâmico
    x_obstaculo = random.randint(0, largura - obstaculo_largura)
    obstaculos.append([x_obstaculo, -obstaculo_altura])
    spawn_timer = 0

# ... (restante do código igual)
