hit = 'hit.mp3'
fire = 'fire.mp3'
bg = 'bg.png'
p1 = 'fb.png'
p2 = 'ig.png'

import pygame
pygame.font.init()
pygame.mixer.init()

Gamedispley = pygame.display.set_mode((900,500))
pygame.display.set_caption('Social Media War')

white = (255,255,255)
black = (0,0,0)
blueco =  (0, 0, 255)
pinkco = (255, 20, 147)

FPS = 60
velocity = 5
bullvel = 10
max_bullets = 3

HitSound = pygame.mixer.Sound(hit)
FireSound = pygame.mixer.music.load(fire)

Healthfont = pygame.font.SysFont('comicsans', 20)
Winnerfont = pygame.font.SysFont('comicsans', 100)
BG9 = pygame.transform.scale(pygame.image.load(bg), (900,500))

bluehit = pygame.USEREVENT + 1
pinkhit = pygame.USEREVENT + 2

Border = pygame.Rect(445, 0, 10, 500)       #Used to create rectangular blocks (code)

Player1 = pygame.image.load(p1)
Player2 = pygame.image.load(p2)

Facebok = pygame.transform.scale(Player1, (40, 40))
Facebook = pygame.transform.rotate(Facebok, 90)
Instagram = pygame.transform.scale(Player2, (40,40))

def drawkaro(blue, pink, bluebullets, pinkbullets, hpfb, hpig): #called the draw window
    #Gamedispley.fill(white)
    Gamedispley.blit(BG9, (0,0))
    pygame.draw.rect(Gamedispley, black, Border)    #Used to create rectangular surfaces (code)

    fbhelthtext = Healthfont.render("Health: " + str(hpfb), 1, black)
    ighelthtext = Healthfont.render("Health: " + str(hpig), 1, black)
    Gamedispley.blit(fbhelthtext, (10,10))
    Gamedispley.blit(ighelthtext, (900-ighelthtext.get_width() -10,10))

    Gamedispley.blit(Facebook, (blue.x, blue.y))
    Gamedispley.blit(Instagram, (pink.x, pink.y))

    for b in bluebullets:
        pygame.draw.rect(Gamedispley, blueco, b)
    for b in pinkbullets:
        pygame.draw.rect(Gamedispley, pinkco, b)

    pygame.display.update()

def movementsblue(keysthatarepressedrn, blue):
    if keysthatarepressedrn[pygame.K_a] and blue.x >0:
        blue.x -= velocity
    if keysthatarepressedrn[pygame.K_d] and blue.x <400 :
        blue.x += velocity
    if keysthatarepressedrn[pygame.K_w] and blue.y >0:
        blue.y -= velocity
    if keysthatarepressedrn[pygame.K_s]and blue.y <460:
        blue.y += velocity

def movementspink(keysthatarepressedrn, pink):
    if keysthatarepressedrn[pygame.K_LEFT] and pink.x > 460:
        pink.x -= velocity
    if keysthatarepressedrn[pygame.K_RIGHT] and pink.x <860:
        pink.x += velocity
    if keysthatarepressedrn[pygame.K_UP] and pink.y >0:
        pink.y -= velocity
    if keysthatarepressedrn[pygame.K_DOWN] and pink.y <460:
        pink.y += velocity

def handlebullets(bluebullets, pinkbullets, blue, pink):
    for bullet in bluebullets:
        bullet.x += bullvel
        if pink.colliderect(bullet):
            pygame.event.post(pygame.event.Event(pinkhit))
            bluebullets.remove(bullet)
        elif bullet.x > 900:
            bluebullets.remove(bullet)

    for bullet in pinkbullets:
        bullet.x -= bullvel
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(bluehit))
            pinkbullets.remove(bullet)
        elif bullet.x <0:
            pinkbullets.remove(bullet)

def winner(text):
    draw = Winnerfont.render(text, 1, white)
    Gamedispley.blit(draw, (450-draw.get_width()//2, 250 - draw.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    blue = pygame.Rect(280,230, 40, 40)
    pink = pygame.Rect(580, 230, 40 ,40)
    hpfb =10
    hpig = 10
    bluebullets = []
    pinkbullets =[]

    clockk = pygame.time.Clock()
    run =True
    while run:
        clockk.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_LCTRL and len(bluebullets) <max_bullets:
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + 20 -2, 6,4)
                    bluebullets.append(bullet)
                    pygame.mixer.music.play()
                if event.key == pygame.K_RCTRL and len(pinkbullets) <max_bullets:
                    bullet = pygame.Rect(pink.x, pink.y + 20 - 2, 6, 4)
                    pinkbullets.append(bullet)
                    pygame.mixer.music.play()
            if event.type == bluehit:
                hpfb -= 1
                HitSound.play()
            if event.type == pinkhit:
                hpig -= 1
                HitSound.play()

        wintext = ""
        if hpfb<=0:
            wintext = 'Instagram Wins!'
        if hpig<=0:
            wintext = 'Facebook Wins!'
        if wintext != "":
            winner(str(wintext))
            break

        #print(bluebullets, pinkbullets)
        keysthatarepressedrn = pygame.key.get_pressed()
        movementspink(keysthatarepressedrn, pink)
        movementsblue(keysthatarepressedrn, blue)

        handlebullets(bluebullets, pinkbullets, blue, pink)

        drawkaro(blue, pink, bluebullets, pinkbullets, hpfb, hpig)

    main()

main()