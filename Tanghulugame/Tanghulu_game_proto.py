import tkinter
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
fruits = ""      ##변수값 지정

def key_down(e): #키 입력값 받기
    global key       
    key = e.keysym  
        
def draw_txt(txt, x, y, siz, col, tg): #글씨체 지정및 그림자 넣기
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)
    
def drow_answer():  # 정답 탕후루 그리기 함수
    global answer
    cvs.delete("ANS")
    
    for i in range(len(answer)): 
        
        if int(answer[i]) > -1:
            cvs.create_image(1165, 560 - i * int(300/(difficulty + combo)) , image=Making_image[int(answer[i])], tag="ANS")
            
def drow_making(): # 만드는 탕후루 그리기 함수
    global making
    cvs.delete("MAKE")
    for i in range(len(making)):
        
        if int(making[i]) > -1:
            cvs.create_image(940, 560 - i * int(300/(difficulty + combo)), image=Making_image[int(making[i])], tag="MAKE")
            
def drow_fruits(): # 왼쪽 과일들 그리기 및 눈 감기 함수
    global fruits
    cvs.delete("FRUIT")

    for i in range(6):

        if i < 3:
            cvs.create_image(175 + 255* i, 375, image=fruit_image[1+2*i-int(fruits[i])], tag="FRUIT")

        else:
            cvs.create_image(-590 +255* i, 604, image=fruit_image[1+2*i-int(fruits[i])], tag="FRUIT")
            
def drow_bar(): # 제한시간 바 함수
    global timer
    cvs.delete("BAR")
    cvs.create_rectangle(150, 32,int(150+timer*2.37), 45, fill="red", width=0, tag="BAR")

def game_main(): #게임메인
    global index, timer, score, difficulty, combo, count, key, answer, making, fruits
    fruits = "000000"
    
    if index == 0: # 타이틀 로고
        count = 0
        cvs.delete("Maingame")
        cvs.delete("Clear")
        cvs.create_image(640, 360 , image= Title_bg, tag = "Title")        
        draw_txt("탕후루 게임", 630, 175, 80, "#9F521E", "Title")
        cvs.create_image(640, 410, image=difficulty_image[0], tag="Title")
        cvs.create_image(640, 530, image=difficulty_image[1], tag="Title")
        cvs.create_image(640, 650, image=difficulty_image[2], tag="Title")
        index = 1 
    
    elif index == 1: # 타이틀 화면, 시작 대기
        difficulty = 0
        
        if key == "q" or key == "Q" or key == "ㅂ": # 대문자 및 한글자판에서 작동 안되는 오류 해결
                difficulty = 4
        
        if key == "w" or key == "W" or key == "ㅈ":
                difficulty = 5
        
        if key == "e" or key == "E" or key == "ㄷ":
                difficulty = 6
            
        if difficulty != 0:
            index = 2

    elif index == 2: # 설명
        cvs.delete("Title")
        cvs.create_image(640, 360 , image= Explain_bg, tag = "Explain")
        
        if key == "q" or key == "Q" or key == "ㅂ":
            timer = 487
            score = 0
            cvs.create_image(640, 360 , image= Main_bg, tag = "Maingame")
            draw_txt("목표금액\n50,000 원", 135, 175 , 30, "white", "Maingame")
            index = 3
    
    elif index == 3: # 카운트 다운
        count += 1
        
        if count % 4 == 1:
            cvs.delete("COUNT")
            cvs.create_image(640, 360, image=count_image[count // 4], tag="COUNT")
        
        elif count == 15:
            index = 4
            cvs.delete("COUNT")
            
    elif index == 4: # 정답과 만들기 초기화
        answer = ""
        making = ""
        index = 5
        
    elif index == 5: # 정답 탕후루 리스트(여기서는 str을 리스트 형태로 이용) 생성
        answer += str(random.randint(0,5)) #for i in range 로 해볼까도 생각해보았지만 그럼 한번에 그려지는게 너무 멋없어서 수정
        drow_answer()
        
        if len(answer) == (difficulty + combo): # 정답 리스트 길이가 난이도 + 콤보인지 판별
            index = 6
    
    elif index == 6: # 만들기 리스트 작성 fruits 변수는 왼쪽 과일들의 눈 감기에 사용하기 위해 추가
        
        if len(making) != (difficulty + combo):
        
            if key == "q" or key == "Q" or key == "ㅂ":
                making += "0"
                fruits = "100000"                              

            elif key == "w" or key == "W" or key == "ㅈ":            
                making += "1"
                fruits = "010000"
                
            elif key == "e" or key == "E" or key == "ㄷ":
                making += "2"
                fruits = "001000"
                
            elif key == "a" or key == "A" or key == "ㅁ":            
                making += "3"
                fruits = "000100"
                
            elif key == "s" or key == "S" or key == "ㄴ":
                making += "4"
                fruits = "000010"

            elif key == "d" or key == "D" or key == "ㅇ":      
                making += "5"
                fruits = "000001"
            drow_making()
            
        else:
            index = 7
    
    elif index == 7: # 정답과 만든 리스트 일치하는지 확인 이후 콤보와 점수 판정
        
        if making == answer:
            score += 2 + combo
            fruits = "111111" # 정답을 맞췄을대 왼쪽 과일들 다 눈 감았다 뜨게 만들기
        
            if combo != 5: # 콤보 최대치 설정을 위한 if문
                combo +=1        
        else:    
            combo = 0
        index = 4
        
    elif index == 8: # 시간이 다되면 아래 if timer == 1 에서 인덱스 8로 설정해서 타임오버 완성
        cvs.delete("FRUIT")

        if score >= 50: #기준금액
            cvs.create_image(640, 360 , image= Game_Clear_bg, tag = "Clear")
            count += 1
            if key !="" and count > 20:
                index = 0
                timer -=1

        else:
            cvs.create_image(640, 360 , image= Game_Over_bg, tag = "Clear")
            count += 1
            if key !="" and count > 20:
                index = 0
                timer -=1
                
    if timer == 1: # 타이머가 0일대로 하면 0.25초의 딜레이와 시작할때 기본 타이머값이 0이라서 버그 발생해서 1로 처리함
        index = 8

    else:
        timer -=1 # 시간 감소

        if index != 0  and index != 1 and index != 2 and index != 3: # 시작 전에 바랑 그림들이 안보이게 하는 이프문
            drow_fruits()
            drow_bar()
            cvs.delete("COMBO")

            if combo == 5: #맥스콤보 글자 출력
                draw_txt("MAX COMBO!!"  , 700, 170, 25, "white", "COMBO")
                
            else:    
                draw_txt(str(combo) + " COMBO!!"  , 700, 170, 25, "white", "COMBO")
            draw_txt("현재금액\n" + str(score) + ",000원", 400, 175 , 30, "white", "COMBO")
            
    key = ""
    root.after(250, game_main) #100밀리초로 하면 과일이 2번 연속으로 놔지는 현상이 키 입력 딜레이로 인해 가끔 발생, 없애기위해 250 밀리초로 설정
                        
                        
root = tkinter.Tk() #페이지 만들기
root.title("Tanghulu_game")
root.resizable(False, False)
root.bind("<KeyPress>",key_down)
cvs = tkinter.Canvas(root, width=1280, height=720)
cvs.pack()

Making_image = [
    tkinter.PhotoImage(file="Apple.png"),
    tkinter.PhotoImage(file="GApple.png"),
    tkinter.PhotoImage(file="Orange.png"),
    tkinter.PhotoImage(file="Grape.png"),
    tkinter.PhotoImage(file="GGrape.png"),
    tkinter.PhotoImage(file="Straw.png")
    ] # 정답탕후루랑 만드는 탕후루 이미지

fruit_image = [
    tkinter.PhotoImage(file="Wry_Apple.png"),
    tkinter.PhotoImage(file="Smile_Apple.png"),
    tkinter.PhotoImage(file="Wry_GApple.png"),
    tkinter.PhotoImage(file="Smile_GApple.png"),
    tkinter.PhotoImage(file="Wry_Orange.png"),
    tkinter.PhotoImage(file="Smile_Orange.png"),
    tkinter.PhotoImage(file="Wry_Grape.png"),
    tkinter.PhotoImage(file="Smile_Grape.png"),
    tkinter.PhotoImage(file="Wry_GGrape.png"),
    tkinter.PhotoImage(file="Smlie_GGrape.png"),
    tkinter.PhotoImage(file="Wry_Straw.png"),
    tkinter.PhotoImage(file="Smile_Straw.png")
    ] # 왼쪽에 나오는 과일들 2개를 기준으로 감기 웃기 반복해서 눈 감는거 만드는데 사용

count_image = [
    tkinter.PhotoImage(file="3.png"),
    tkinter.PhotoImage(file="2.png"),
    tkinter.PhotoImage(file="1.png"),
    tkinter.PhotoImage(file="Start.png")
    ] # 카운트 다운 이미지

difficulty_image =[
    tkinter.PhotoImage(file="Easy.png"),
    tkinter.PhotoImage(file="Normal.png"),
    tkinter.PhotoImage(file="Hard.png")
    ] # 시작화면 난이도 선택 이미지

Title_bg = tkinter.PhotoImage(file="Title_BG.png")
Explain_bg = tkinter.PhotoImage(file="Explain_BG.png")
Main_bg = tkinter.PhotoImage(file="Maingame_BG.png")
Game_Clear_bg = tkinter.PhotoImage(file="Game_Clear.png")
Game_Over_bg = tkinter.PhotoImage(file="Game_Over.png") #배경들

game_main()
root.mainloop()