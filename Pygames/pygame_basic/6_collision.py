import pygame

pygame.init() #초기화(반드시)

screen_width = 480 #화면 가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#배경 불러오기 
background = pygame.image.load("/Users/Jiung/coding/coding_learn/python/pygame_basic/assets/background.png")

#캐릭터 불러오기
character = pygame.image.load("/Users/Jiung/coding/coding_learn/python/pygame_basic/assets/character.png")
character_size = character.get_rect().size #크기
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width / 2) - (character_width / 2) #가로 화면 절반
character_y_pos = screen_height - character_height#화면 세로 가장 아래

#이동할 좌표
to_x = 0
to_y = 0

#이속
character_speed = 0.6

#적 캐릭
enemy = pygame.image.load("/Users/Jiung/coding/coding_learn/python/pygame_basic/assets/enemy.png")
enemy_size = enemy.get_rect().size #크기
enemy_width = enemy_size[0] #가로
enemy_height = enemy_size[1] #세로
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #가로 화면 절반
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)#화면 세로 가장 아래

#이벤트 루프    
running = True #게임 진행중?
while running:
    dt = clock.tick(60) #게임 화면의 초당 프레임 수 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는가?
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        # 키가 때져있는가?
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                 
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("출동했어요")
        running = False

    screen.blit(background, (0, 0)) #배경 그리기 
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    pygame.display.update() # 게임 화면 다시 그리기

#게임 종료
pygame.quit()