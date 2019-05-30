import sys, pygame, os
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
black = 0, 0, 0

class Bouncer(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        #direcao: 1=direita, -1=esquerda
        self.direction = 1
        #carrega a imagem e a posiciona na tela
        self.image, self.rect = load_image("imagemteste.jpg")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    def update(self):
        #multiplicamos x por 3 pro bouncer mover-se um pouco mais rápido!
        self.rect.move_ip((self.direction*3,0))
        #se o bouncer atingir os limites da tela, invertemos a sua direcao
        if self.rect.left < 0:
            self.direction = 1
        elif self.rect.right > width:
            self.direction = 1

class Ball(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [2,2]
        #carrega a imagem e a posiciona na tela
        self.image, self.rect = load_image("imagemteste.jpg")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        #salva a posicao inicial para ser reutilizada quando a bola sair da tela pelo fundo
        self.init_pos = startpos

    def update(self):
        self.rect.move_ip(self.speed)
        #se a bola atingir os lados da tela, inverte a direcao horizontal (x)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            #se a bola atingir o topo da tela, inverte a posicao vertical (y)
            if self.rect.top < 0:
                self.speed[1] = -self.speed[1]
                #se a bola atingir o fundo da tela, reseta #a sua posicao
                if self.rect.bottom > height:
                    self.rect.centerx = self.init_pos[0]
                    self.rect.centery = self.init_pos[1]

def load_image(name):
    """carrega uma imagem na memoria"""
    fullname = os.path.join("Imagens", name)
    try:
        image = pygame.image.load(fullname)
    except (pygame.error, message):
        print ("Cannot load image:" + fullname)
        raise (SystemExit, message)
    return image, image.get_rect()

def main():
    #cria os nossos objetos (bola e bouncer)
    ball = Ball([1,1])
    bouncer = Bouncer([400,395])
    playSurface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("Teste")
    clock = pygame.time.Clock()
    while 1:
        #garante que o programa nao vai rodar a mais que 120fps
        clock.tick(120)
        #checa eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bouncer.direction = -1
                if event.key == pygame.K_RIGHT:
                    bouncer.direction = 1
                #checa se a bola colidiu no bouncer, e caso sim inverte a direcao vertical da bola
        if bouncer.rect.colliderect(ball.rect):
            if ball.speed[1] > 0:
                ball.speed[1] = -ball.speed[1]

        #atualiza os objetos
        ball.update()
        bouncer.update()
        #redesenha a tela
        screen.fill(black)
        screen.blit(ball.image, ball.rect)
        screen.blit(bouncer.image, bouncer.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()

