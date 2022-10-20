import pygame
import random
# 0 기본 설정들
################################################
pygame.init() #값 초기화

# 화면 크기
screen_width=480 #가로크기
screen_hight =640 #세로크기
screen=pygame.display.set_mode((screen_width,screen_hight))


# 화면 타이틀 설정
pygame.display.set_caption(("프로젝트 게임")) #게임 이름

#FPS
clock=pygame.time.Clock()
#######################################
#1. 사용자 게임 초기화(배경 화면,게임이미지, 좌표,속도,폰트 등)

# 배경 이미지 불러오기
background=pygame.image.load(r"C:\Users\tj-bu\PycharmProjects\pythonProject\game\동피하기\image1.png")

# 캐릭터(스프라이트) 불러오기
character=pygame.image.load(r"C:\Users\tj-bu\PycharmProjects\pythonProject\game\동피하기\image2.png")
character_size=character.get_rect().size #이미지의 크기를 구해옴
character_width=character_size[0] #캐릭터 가로크기
character_hight=character_size[1] # 캐릭터 세로 크기
character_x_pos= screen_width/2-(character_width/2)# 화면 가로의 절반크기의 해야하는 곳의 위치
character_y_pos=screen_hight-character_hight#화면 세로 크기 가장 아래에 해당하는 곳의 위치(세로)
# 이동할 좌표
to_x=0
to_y=0
# 이동 속도
character_speed=0.5
# 적 enemy 캐릭터
# 적캐릭터1  불러오기
enemy=pygame.image.load(r"C:\Users\tj-bu\PycharmProjects\pythonProject\game\동피하기\doun1.jpg")
enemy_size=enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width=enemy_size[0] #적 가로크기
enemy_hight=enemy_size[1] # 적 세로 크기
enemy_x_pos= random.randint(0,screen_width-enemy_width)# 화면 가로의 절반크기의 해야하는 곳의 위치
enemy_y_pos=0#화면 세로 크기 가장 아래에 해당하는 곳의 위치(세로)
enemy_speed=random.randint(10,25)
# 적캐릭터2 불러오기
enemy1=pygame.image.load(r"C:\Users\tj-bu\PycharmProjects\pythonProject\game\동피하기\doun1.jpg")
enemy_size1=enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width1=enemy_size[0] #적 가로크기
enemy_hight1=enemy_size[1] # 적 세로 크기
enemy_x_pos1= random.randint(0,screen_width-enemy_width)# 화면 가로의 절반크기의 해야하는 곳의 위치
enemy_y_pos1=0#화면 세로 크기 가장 아래에 해당하는 곳의 위치(세로)
enemy_speed1=random.randint(10,25)

# 폰트 정의
game_font=pygame.font.Font(None,40) # 폰트 객체 생성 (폰트,크기)

# 총 시간
total_time =10
# 시작 시간
start_ticks=pygame.time.get_ticks() # 시작 tick 을 받아옴

# 이벤트 루프
running =True #게임이 진행중인가?
while running:
    dt=clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    # 2.이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():# 어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running=False #게임이 진행중이 아님

        if event.type==pygame.KEYDOWN: #키가 눌렷는지 확인
            if event.key== pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x+=character_speed
            elif event.key==pygame.K_UP: # 캐릭터를 위로
                pass
            elif event.key ==pygame.K_DOWN: #캐릭터를 아래로
                pass

        if event.type==pygame.KEYUP: #방향키를 멈출떄 선언
            if event.key==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key ==pygame.K_DOWN:
                to_y=0
    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt
#가로 경계값 처리
    #3. 캐릭터 위치
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
#세로 경계값 처리
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_hight-character_hight:
        character_y_pos=screen_hight-character_hight
#충돌처리를 위한 rect 정보 업데이트
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    enemy_rect1 = enemy.get_rect()
    enemy_rect1.left = enemy_x_pos1
    enemy_rect1.top = enemy_y_pos1
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요 당신의 점수는:",int(total_time*elapsed_time))
        running=False
    elif character_rect.colliderect(enemy_rect1):
        print("충돌했어요 당신의 점수는:",int(total_time*elapsed_time))
        running=False
    enemy_y_pos+=enemy_speed
    enemy_y_pos1 += enemy_speed1
    if enemy_y_pos>screen_hight:
        enemy_y_pos=0
        enemy_x_pos=random.randint(0,screen_width-enemy_width)

    if enemy_y_pos1 > screen_hight:
        enemy_y_pos1 = 0
        enemy_x_pos1 = random.randint(0, screen_width - enemy_width)
    #screen.fill((0,0,255)) #화면 rbg로 채우기
    screen.blit(background,(0,0))# 배경 그림

    screen.blit(character,(character_x_pos,character_y_pos))#캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기
    screen.blit(enemy1,(enemy_x_pos1,enemy_y_pos1))

#타이머 집어 넣기
# 경과시간 계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
#경과 시간을 1000으로 나누어서 초(s) 단위로 표시
    timer=game_font.render(str(int(total_time*elapsed_time)),True,(255,255,255))
# 출력할 시간,True,글자,색상
    screen.blit(timer,(10,10))

# 만약 시간이 0이하면 게임종료
#     if total_time-elapsed_time<=0:
#         print("타임 아웃")
#         running=False
    pygame.display.update() # 게임화면 그리기


pygame.time.delay((2000)) #2초 대기
# pygame 종료
pygame.quit()
