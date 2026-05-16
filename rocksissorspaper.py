def mukssippa(turn) :
    while True :
        while True:
            player = input("묵찌빠 ")

            if player == "찌" :
                player_num = 1
                break
            elif player == "묵" :
                player_num = 2
                break
            elif player == "빠":
                player_num = 3 
                break
            else :
                print("묵, 찌, 빠 중 하나를 입력하시오")
        
        random.randint(1, 3)
        if computer_num == 2:
            computer = "찌"
        elif computer_num == 3:
            computer = "묵"
        else :
            computer = "빠"
            
        print(f"플레이어:{player}")
        print(f'컴퓨터  :{computer}')
        if computer_num == player_num :
            print('플레이어 턴')
            turn = 1
        elif computer_num - 1 == player_num or computer_num + 2 == player_num:
            if turn == 1:
                print('플레이어 승')
                break
            else :
                print('컴퓨터 승')
                break
        else :
            print('컴퓨터 턴')
            turn = 2
    
turn = 0

while True :
    player_num = 0
    while True:
        player = input("가위, 바위, 보 ")

        if player == "가위" :
            player_num = 1
            break
        elif player == "바위" :
            player_num = 2
            break
        elif player == "보":
            player_num = 3
            break
        else :
            print("가위, 바위, 보 중 하나를 입력하시오")
    import random

    computer_num = random.randint(1, 3)

    if computer_num == 2:
        computer = "가위"
    elif computer_num == 3:
        computer = "바위"
    else :
        computer = "보"
            
            
    print(f"플레이어:{player}")
    print(f'컴퓨터  :{computer}')
    if computer_num == player_num :
        print('플레이어 턴')
        turn = 1
    elif computer_num - 1 == player_num or computer_num + 2 == player_num:
        print('무승부')
        turn = 0
    else :
        print('컴퓨터 턴')
        turn = 2
    
    if turn != 0 :
        mukssippa(turn)
        break