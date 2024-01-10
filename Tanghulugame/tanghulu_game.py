import pygame
import sys
import random

index = 0
timer = 0
score = 0
difficulty = 0
combo = 0
count = 0

key = ""
answer = ""
making = ""
fruits = "" 

def main():
    global index, timer, score, difficulty, combo, count, key, answer, making, fruits
    fruits = "000000"
    
    pygame.init()
    pygame.display.set_caption("Tanghulugame")
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 45) #페이지 만들기
    
    Title_bg = pygame.image.load("Title_BG1.png")
    Explain_bg = pygame.image.load("Explain_BG.png")
    Main_bg = pygame.image.load("Maingame_BG.png")
    Game_Clear_bg = pygame.image.load("Game_Clear.png")
    Game_Over_bg = pygame.image.load("Game_Over.png") #배경들
    
    count_image = [
        pygame.image.load("31.png"),
        pygame.image.load("21.png"),
        pygame.image.load("11.png"),
        pygame.image.load("Start1.png")] # 카운트 다운 이미지
    
    fruit_image = [pygame.image.load("Wry_Apple.png"),
                   pygame.image.load("Smile_Apple.png"),
                   pygame.image.load("Wry_GApple.png"),
                   pygame.image.load("Smile_GApple.png"),
                   pygame.image.load("Wry_Orange.png"),
                   pygame.image.load("Smile_Orange.png"),
                   pygame.image.load("Wry_Grape.png"),
                   pygame.image.load("Smile_Grape.png"),
                   pygame.image.load("Wry_GGrape.png"),
                   pygame.image.load("Smlie_GGrape.png"),
                   pygame.image.load("Wry_Straw.png"),
                   pygame.image.load("Smile_Straw.png")
                   ] #과일들 이미지 눈 감기 눈 뜨기
    
    Making_image = [pygame.image.load("Apple.png"),
                    pygame.image.load("GApple.png"),
                    pygame.image.load("Orange.png"),
                    pygame.image.load("Grape.png"),
                    pygame.image.load("GGrape.png"),
                    pygame.image.load("Straw.png")
                    ] # 정답탕후루랑 만드는 탕후루 이미지
    
    try:
        music = pygame.mixer.Sound("country-swing-night-108987.ogg")
        sucess = pygame.mixer.Sound("cash-register.mp3")
        fail = pygame.mixer.Sound("negative_beeps.mp3")
        se = [pygame.mixer.Sound("pop10.ogg"),
              pygame.mixer.Sound("pop9.ogg"),
              pygame.mixer.Sound("pop8.ogg"),
              pygame.mixer.Sound("pop7.ogg"),
              pygame.mixer.Sound("pop6.ogg"),
              pygame.mixer.Sound("pop5.ogg"),
              pygame.mixer.Sound("pop4.ogg"),
              pygame.mixer.Sound("pop3.ogg"),
              pygame.mixer.Sound("pop2.ogg"),
              pygame.mixer.Sound("pop1.ogg"),
              pygame.mixer.Sound("pop0.ogg")
             ]
    except:
        print("오디오 기기를 연결해주세요")
    
    Key_Count = 0 # 키 입력 원활하게 하기위한 변수
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() #종료
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    key = "q"
                elif event.key == pygame.K_w:
                    key = "w"
                elif event.key == pygame.K_e:
                    key = "e"
                elif event.key == pygame.K_a:
                    key = "a"
                elif event.key == pygame.K_s:
                    key = "s"
                elif event.key == pygame.K_d:
                    key = "d"  # 키 입력 받기
            
        if Key_Count == 10: # 키 입력 씹힘 방지용 프레임 단위쪼개기
            Key_Count = 0               
            if index == 0: # 타이틀 화면, 시작 대기
                screen.blit(Title_bg,[0,0])
                difficulty = 0
                timer = 0
                count = 0
                
                if key == "q":
                    difficulty = 4
                if key == "w":
                    difficulty = 5        
                if key == "e":
                    difficulty = 6
        
                if difficulty != 0:
                    se[0].play()
                    index = 1
                    timer = 0
                       
            elif index == 1: # 설명
                screen.blit(Explain_bg,[0,0])
                if key == "q" and timer < -4:
                    
                    timer = 470 
                    score = 0
                    combo = 0
                    target_txt = font.render("target sales 50$",True,(0, 0, 0))
                    target_txt1 = font.render("target sales 50$",True,(255, 255, 255))
                    index = 2
            
            elif index == 2: # 카운트 다운
                if 470 - timer == 15:
                    index = 3
                    music.play()
                
                elif timer % 4 == 1:
                    se[5].play()
                    screen.blit(Main_bg,[0,0])
                    screen.blit(count_image[(470-timer)//4],[0,0]) # 카운트다운
                
            elif index == 3: # 정답과 만들기 초기화
                fruits = "000000"
                screen.blit(Main_bg,[0,0])
                screen.blit(draw_txt, [302, 177])
                screen.blit(draw_txt1, [300, 175])
                screen.blit(combo_txt, [612, 162])
                screen.blit(combo_txt1, [610, 160])
                screen.blit(target_txt, [25, 177])
                screen.blit(target_txt1, [23, 175])
                answer = ""
                making = ""
                index = 4
        
            elif index == 4: # 정답 탕후루 리스트(여기서는 str을 리스트 형태로 이용) 생성
                answer += str(random.randint(0,5)) #for i in range 로 해볼까도 생각해보았지만 그럼 한번에 그려지는게 너무 멋없어서 수정
                for i in range(len(answer)): 
                    if int(answer[i]) > -1:
                        screen.blit(Making_image[int(answer[i])],[1110, 505 - i * int(300/(difficulty + combo))])
                        se[len(answer)-1].play()
        
                if len(answer) == (difficulty + combo): # 정답 리스트 길이가 난이도 + 콤보인지 판별
                    index = 5
                
            elif index == 5: # 만들기 리스트 작성 fruits 변수는 왼쪽 과일들의 눈 감기에 사용하기 위해 추가
                if len(making) != (difficulty + combo):
        
                    if key == "q":
                        making += "0"          
                        fruits = "100000"
                        se[len(making)-1].play()
                    
                    elif key == "w":            
                        making += "1"
                        fruits = "010000"
                        se[len(making)-1].play()
                    
                    elif key == "e":
                        making += "2"
                        fruits = "001000"
                        se[len(making)-1].play()
                
                    elif key == "a":            
                        making += "3"
                        fruits = "000100"
                        se[len(making)-1].play()
                
                    elif key == "s":
                        making += "4"
                        fruits = "000010"
                        se[len(making)-1].play()
                    
                    elif key == "d":      
                        making += "5"
                        fruits = "000001"
                        se[len(making)-1].play()

                    for i in range(len(making)): 
                        if int(making[i]) > -1:
                            screen.blit(Making_image[int(making[i])],[885, 505 - i * int(300/(difficulty + combo))])
            
                else:
                    index = 6
            
            elif index == 6: # 정답과 만든 리스트 일치하는지 확인 이후 콤보와 점수 판정
                if making == answer:
                    score += 2 + combo
                    fruits = "111111" # 정답을 맞췄을대 왼쪽 과일들 다 눈 감았다 뜨게 만들기
                    sucess.play()
                    if combo != 5: # 콤보 최대치 설정을 위한 if문
                        combo +=1        
                else:    
                    combo = 0
                    fail.play()
                index = 3
            
            elif index == 7: # 시간이 다되면 아래 if timer == 1 에서 인덱스 8로 설정해서 타임오버 완성
                if score >= 50: #기준금액
                    screen.blit(Game_Clear_bg,[0,0])
                    count += 1
                    
                    if count > 19:
                        ending_txt = font.render("press any key to restart" ,True,(0, 0, 0))
                        ending_txt1 = font.render("press any key to restart" ,True,(255, 255, 255))
                        screen.blit(ending_txt, [402, 677])
                        screen.blit(ending_txt1, [400, 675])
                        if key !="":
                            index = 0
                            
                else:
                    screen.blit(Game_Over_bg,[0,0])
                    count += 1
                    if count > 19:
                        ending_txt = font.render("press any key to restart" ,True,(0, 0, 0))
                        ending_txt1 = font.render("press any key to restart" ,True,(255, 255, 255))
                        screen.blit(ending_txt, [402, 677])
                        screen.blit(ending_txt1, [400, 675])
                        if key !="":
                            index = 0

            if timer == 1:
                index = 7
                
            else:            
                timer -=1
                if index != 0  and index != 1 and index != 2: # 시작 전에 바랑 그림들이 안보이게 하는 이프문
        
                    for i in range(6):
                        if i < 3:
                            screen.blit(fruit_image[1+2*i-int(fruits[i])],[110 + 255* i, 310])
                        else:
                            screen.blit(fruit_image[1+2*i-int(fruits[i])],[-655 +255* i, 529]) # 눈 깜빡이는 과일들 그리기
                        
                    pygame.draw.rect(screen, (255,255,255), [150, 32, 1117, 13])
                    pygame.draw.rect(screen, (255,0,0), [150, 32, int(timer*2.37), 13])

                    if combo == 5: #맥스콤보 글자 출력
                        combo_txt = font.render("MAX COMBO!!",True,(0, 0, 0))
                        combo_txt1 = font.render("MAX COMBO!!",True,(255, 255, 255))           
                
                    else:
                         combo_txt = font.render(str(combo) + " COMBO!!",True,(0, 0, 0))
                         combo_txt1 = font.render(str(combo) + " COMBO!!",True,(255, 255, 255))
                    draw_txt = font.render("now sales " + str(score) + "$",True,(0, 0, 0))
                    draw_txt1 = font.render("now sales " + str(score) + "$",True,(255, 255, 255))            
                    
            pygame.display.update()
            key = ""
        Key_Count += 1    
        clock.tick(40)
        
if __name__ =='__main__':
    main()
