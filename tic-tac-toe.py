#tic tac toe

from graphics import *
from math import *
from string import *
from random import *
from time import *


#检查哪里是必走的
def exam_line(x):
    n1 = 0
    n2 = 0
    for index in range(3):
        if x[index][index] == -1:
            n2 += 1
    if (n1 == 0 and n2 == 2):
        for index in range(3):
            if x[index][index] == 0:
                return [index , index]

    n1 = 0
    n2 = 0
    for index in range(3):
        if x[index][2 - index] == -1:
            n2 += 1
    if (n1 == 0 and n2 == 2):
        for index in range(3):
            if x[index][2 - index] == 0:
                return [index , 2 - index]

    for i in range(3):
        n1 = 0
        n2 = 0
        for j in range(3):
            if x[i][j] == -1:
                n2 += 1
        if (n1 == 0 and n2 == 2):
            for j in range(3):
                if x[i][j] == 0:
                    return [i , j]

    for j in range(3):
        n1 = 0
        n2 = 0
        for i in range(3):
            if x[i][j] == -1:
                n2 += 1
        if(n1 == 0 and n2 == 2):
            for i in range(3):
                if x[i][j] == 0:
                    return [i , j]

    #上下
    n1 = 0
    n2 = 0
    for index in range(3):
        if x[index][index] == 1:
            n1 += 1
    if (n1 == 2 and n2 == 0):
        for index in range(3):
            if x[index][index] == 0:
                return [index , index]

    n1 = 0
    n2 = 0
    for index in range(3):
        if x[index][2 - index] == 1:
            n1 += 1
    if (n1 == 2 and n2 == 0):
        for index in range(3):
            if x[index][2 - index] == 0:
                return [index , 2 - index]

    for i in range(3):
        n1 = 0
        n2 = 0
        for j in range(3):
            if x[i][j] == 1:
                n1 += 1
        if (n1 == 2 and n2 == 0):
            for j in range(3):
                if x[i][j] == 0:
                    return [i , j]

    for j in range(3):
        n1 = 0
        n2 = 0
        for i in range(3):
            if x[i][j] == 1:
                n1 += 1
        if (n1 == 2 and n2 == 0):
            for i in range(3):
                if x[i][j] == 0:
                    return [i , j]

    return [-1 , -1]


# 判断谁赢了
def exam_judge(x):
    for index in range(4):
        if (index <= 1):
            if x[index] == 1:
                return [1,index]
        else:
            count = 0
            for ptr in x[index]:
                if ptr == 1:
                    return [1,index,count]
                count += 1
    return [0]




#判断是否赢了一句
def judge(x):
    flag1 = 1
    for index in range(2):
        if x[index][index] == x[index + 1][index + 1] and x[0][0] != 0:
            continue
        else:
            flag1 = 0
            break
    
    flag2 = 1
    for index in range(2):
        if x[index][2 - index] == x[index + 1][1 - index] and x[0][2] != 0:
            continue
        else:
            flag2 = 0
            break

    row = [1] * 3
    for i in range(3):
        for j in range(2):
            if x[i][j] == x[i][j + 1] and x[i][0] != 0:
                continue
            else:
                row[i] = 0
                break

    col = [1] * 3
    for j in range(3):
        for i in range(2):
            if x[i][j] == x[i + 1][j] and x[0][j] != 0:
                continue
            else:
                col[j] = 0

    return [flag1 , flag2 , row , col]


#纠正列表中正确的存储位置
def list_position(x):
    if x[1] == 2:
        return [0,x[0]]
    elif x[1] == 1:
        return [1,x[0]]
    else:
        return [2,x[0]]


#检测是否点在游戏区
def playboard_click(p):
    x = p.x
    y = p.y
    if(y < 10.0):
        return 1
    else:
        return 0


# 退出键判断
def quit_button(p):
    x = p.x
    y = p.y
    if (1.4 < x < 2.0 and 10.1 < y < 10.7):
        return 1
    else:
        return 0


# 刷新键判断
def restart_button(p):
    x = p.x
    y = p.y
    if (0.8 < x < 1.4 and 10.1 < y < 10.7):
        return 1
    else:
        return 0


# 人机游戏键判断
def player1_button(p):
    x = p.x
    y = p.y
    if (0.2 < x < 1.4 and 11.3 < y < 11.9):
        return 1
    else:
        return 0


# 双人游戏键判断
def player2_button(p):
    x = p.x
    y = p.y
    if (0.2 < x < 1.4 and 10.7 < y < 11.3):
        return 1
    else:
        return 0


def main():
    #basic figure
    gold_ratio = (sqrt(5) - 1 )/ 2
    k = sqrt(2) / 2

    #初始化文本框
    win = GraphWin("GAME" , 900 , 1080)
    win.setCoords( 0.0 , 0.0 , 10.0 , 12.0 )
    win.setBackground("white")

    #画游戏区与分界区的分割线
    tline_red = []
    tline_blue = []
    for index in range(5):
        tline_red.append(Line(Point(2 * index + 1 , 10.0) , Point(2 * index + 2 , 10.0)))
        tline_blue.append(Line(Point(2 * index , 10.0) , Point(2 * index + 1 , 10.0)))
        tline_red[index].setFill("red")
        tline_red[index].setWidth(5)
        tline_blue[index].setFill("blue")
        tline_blue[index].setWidth(5)
        tline_red[index].draw(win)
        tline_blue[index].draw(win)

    #初始比分
    p1_score = 0
    p2_score = 0

    #p1的棋子符号——红圈
    p1_circle = Circle(Point(8.5 , 11.0) , 0.5)
    p1_circle.setWidth(10)
    p1_circle.setOutline("red")
    p1_circle.draw(win)

    pcover = Polygon(Point(8.0 , 10.5) , Point(9.0 , 11.5) , Point(9.5 , 10.1))
    pcover.setFill("white")
    pcover.setOutline("white")
    pcover.draw(win)

    #p1 p2比分显示牌的分割线
    pline = Line(Point(7.5 , 10.0) , Point(9.5 , 12.0))
    pline.setFill("gray")
    pline.draw(win)

    #p2的棋子符号——蓝叉
    p2_cross1 = Line(Point(8.5 - 0.55 * sqrt(2) / 2 , 11.0 - 0.55 * sqrt(2) / 2) , Point(8.5 + 0.55 * sqrt(2) / 2 , 11.0 + 0.55 * sqrt(2) / 2))
    p2_cross1.setWidth(10)
    p2_cross1.setFill("blue")
    p2_cross1.draw(win)
    p2_cross2 = Line(Point(8.5 , 11.0) , Point(8.5 + 0.55 * sqrt(2) / 2 , 11.0 - 0.55 * sqrt(2) / 2))
    p2_cross2.setWidth(10)
    p2_cross2.setFill("blue")
    p2_cross2.draw(win)

    #比分牌中的名称与比分显示
    p1_t = Text(Point(7.5 , 11.5) , "Player 1")
    p1_t.draw(win)

    p1_s = Text(Point(7.5 , 11.0) , "%d" % p2_score)
    p1_s.setSize(28)
    p1_s.setFill("red")
    p1_s.draw(win)

    p1_t = Text(Point(9.5 , 10.5) , "Player 2")
    p1_t.draw(win)
    
    p2_s = Text(Point(9.5 , 11.0) , "%d" % p2_score)
    p2_s.setSize(28)
    p2_s.setFill("blue")
    p2_s.draw(win)

    #指引语
    g1 = Text(Point(4.61, 11.65) , "TIC           TOE")
    g1.setStyle("bold")
    g1.setFill("red")
    g1.setSize(24)
    g1.draw(win)

    g2 = Text(Point(5.25 , 11.65) , "TAC           !")
    g2.setStyle("bold")
    g2.setFill("blue")
    g2.setSize(24)
    g2.draw(win)

    g3 = Text(Point(3.97 , 11.2) , "Click         1 Player       to play with computer")
    g3.setSize(8)
    g3.draw(win)
    

    g4 = Text(Point(4.0 , 10.9) , "Click         2 Player       to play with your friend")
    g4.setSize(8)
    g4.draw(win)

    g5 = Text(Point(3.58 , 10.6) , "Click       R       to clear the score")
    g5.setSize(8)
    g5.draw(win)

    g6 = Text(Point(3.83 , 10.3) , "Click       Q       to end the game anytime")
    g6.setSize(8)
    g6.draw(win)

    # 左侧按键区
    x_left = 0.2
    x_right = 2.0
    y_top = 11.9
    y_down = 10.1
    
    line1 = Line(Point(0.2 , 11.3) , Point(2.0 , 11.3))
    line1.setWidth(5)
    line1.setFill("blue")
    line1.draw(win)

    line2 = Line(Point(0.2 , 10.7) , Point(2.0 , 10.7))
    line2.setWidth(5)
    line2.setFill("blue")
    line2.draw(win)

    line3 = Line(Point(1.4 , 10.1) , Point(1.4 , 11.9))
    line3.setWidth(5)
    line3.setFill("red")
    line3.draw(win)

    line4 = Line(Point(0.8 , 10.1) , Point(0.8 , 10.7))
    line4.setWidth(5)
    line4.setFill("red")
    line4.draw(win)

    line5 = Line(Point(1.4 , 11.3) , Point(2.0 , 11.3))
    line5.setWidth(5)
    line5.setFill("red")
    line5.draw(win) 

    # restart button
    # x = 0.8 , x = 1.4 , y = 10.1 , y = 10.7
    rb = Polygon(Point(0.8 , 10.1) , Point(0.8 , 10.7) , Point(1.4 , 10.7) , Point(1.4 , 10.1))
    rb.setWidth(5)
    rb.setOutline("blue")
    rb.setFill("blue")
    rb.draw(win)

    rw = Text(Point(1.1 , 10.4) , "R")
    rw.setStyle("bold")
    rw.setSize(14)
    rw.draw(win) 

    # quit button
    # x = 1.4 , x = 2.0 , y = 10.1 , y = 10.7
    qb = Polygon(Point(1.4 , 10.1) , Point(1.4 , 10.7) , Point(2.0 , 10.7) , Point(2.0 , 10.1))
    qb.setWidth(5)
    qb.setOutline("red")
    qb.setFill("red")
    qb.draw(win)

    qw = Text(Point(1.7 , 10.4) , "Q")
    qw.setStyle("bold")
    qw.setSize(14)
    qw.draw(win)

    # 1 Player button
    # x = 0.2 , x = 1.4 , y = 11.3 , y = 11.9
    p1mode = Text(Point(0.8 , 11.6) , "1 Player")
    p1mode.setStyle("bold")
    p1mode.setFill("blue")
    p1mode.setSize(14)
    p1mode.draw(win)

    # 2 Player button
    # x = 0.2 , x = 1.4 , y = 10.7 , y = 11.3
    p2mode = Text(Point(0.8 , 11.0) , "2 Player")
    p2mode.setStyle("bold")
    p2mode.setFill("blue")
    p2mode.setSize(14)
    p2mode.draw(win)
    
    #decoration
    #circle
    d_circle = Circle(Point(0.5 , 10.4) , 0.3 * gold_ratio)
    d_circle.setWidth(10)
    d_circle.setOutline("red")
    d_circle.draw(win)

    #cross
    d_cross1 = Line(Point(1.7 - 0.3 * gold_ratio * k , 11.6 - 0.3 * gold_ratio * k) , Point(1.7 + 0.3 * gold_ratio * k , 11.6 + 0.3 * gold_ratio * k))
    d_cross1.setWidth(10)
    d_cross1.setFill("blue")
    d_cross2 = Line(Point(1.7 + 0.3 * gold_ratio * k , 11.6 - 0.3 * gold_ratio * k) , Point(1.7 - 0.3 * gold_ratio * k , 11.6 + 0.3 * gold_ratio * k))
    d_cross2.setWidth(10)
    d_cross2.setFill("blue")
    d_cross1.draw(win)
    d_cross2.draw(win)

    # grid line
    grid_line1 = Line(Point(10.0 / 3 , 0.0) , Point(10.0 / 3 , 10.0))
    grid_line1.setFill("gray")
    grid_line1.draw(win)

    grid_line2 = Line(Point(20.0 / 3 , 0.0) , Point(20.0 / 3 , 10.0))
    grid_line2.setFill("gray")
    grid_line2.draw(win)

    grid_line3 = Line(Point(0.0 , 10.0 / 3) , Point(10.0 , 10.0 / 3))
    grid_line3.setFill("gray")
    grid_line3.draw(win)

    grid_line4 = Line(Point(0.0 , 20.0 / 3) , Point(10.0 , 20.0 / 3))
    grid_line4.setFill("gray")
    grid_line4.draw(win)


    #mode = 0 是初始状态
    #mode = 1 是1player
    #mode = -1是2player
    mode = 0
    while(1):
        p = win.getMouse()
        if player1_button(p):
                
            decide_circle1 = Circle(Point(0.1 , 11.6) , 0.05)
            decide_circle1.setOutline("blue")
            decide_circle1.setFill("blue")
            decide_circle1.draw(win)

            decide_circle2 = Circle(Point(0.1 , 11.6) , 0.02)
            decide_circle2.setOutline("red")
            decide_circle2.setFill("red")
            decide_circle2.draw(win)
            if mode <= 0:
                p1_s.undraw()
                p2_s.undraw()

                p1_score = 0
                p2_score = 0
            
                p1_s = Text(Point(7.5 , 11.0) , "%d" % p2_score)
                p1_s.setSize(28)
                p1_s.setFill("red")
                p1_s.draw(win)

                p2_s = Text(Point(9.5 , 11.0) , "%d" % p2_score)
                p2_s.setSize(28)
                p2_s.setFill("blue")
                p2_s.draw(win)
            
            board = [[0,0,0],[0,0,0],[0,0,0]]
            quit_flag = 0
            red_circle = []
            blue_cross1 = []
            blue_cross2 = []
            mode = 1
            if p1_score == 0 and p2_score == 0:
                turn = 0
            elif p1_flag:
                turn = 1
            else:
                turn = 0
            count_p1 = -1
            count_p2 = -1
            while(1):
                trans = pow(-1,turn)
                time = -1
                
                #人的轮
                if trans == 1:
                    p = win.getMouse()

                    if playboard_click(p):
                        x = p.x
                        y = p.y
                        xn = (int(x / (10.0 / 3)) + 0.5)* (10.0 / 3)
                        yn = (int(y / (10.0 / 3)) + 0.5)* (10.0 / 3)

                        index_group = list_position([int(x / (10.0 / 3)) , int(y / (10.0 / 3))])

                        if board[int(x / (10.0 / 3))][int(y / (10.0 / 3))] == 0:
                            count_p1 += 1
                            red_circle.append(Circle(Point(xn , yn) , gold_ratio))
                            red_circle[count_p1].setOutline("red")
                            red_circle[count_p1].setWidth(10)
                            red_circle[count_p1].draw(win)
                            turn += 1
                            board[int(x / (10.0 / 3))][int(y / (10.0 / 3))] = trans
                        else:
                            continue
                        
                    elif quit_button(p):
                        quit_flag = 1
                        break
                
                    else:
                        continue

                #计算机的轮
                if trans == -1:
                    count_p2 += 1
                    thinking = exam_line(board)

                    if thinking[0] == -1:
                        while(1):
                            x = randint(0 , 2)
                            y = randint(0 , 2)
                            if board[x][y] == 0:
                                board[x][y] = trans
                                xn = (10.0 / 3) * x + (10.0 / 3 / 2.0)
                                yn = (10.0 / 3) * y + (10.0 / 3 / 2.0)
                                break
                    else:
                        x = thinking[0]
                        y = thinking[1]
                        board[x][y] = trans
                        xn = (10.0 / 3) * x + (10.0 / 3 / 2.0)
                        yn = (10.0 / 3) * y + (10.0 / 3 / 2.0)

                    blue_cross1.append(Line(Point(xn - k * gold_ratio , yn - k * gold_ratio) , Point(xn + k * gold_ratio , yn + k * gold_ratio)))
                    blue_cross2.append(Line(Point(xn - k * gold_ratio , yn + k * gold_ratio) , Point(xn + k * gold_ratio , yn - k * gold_ratio)))
                    blue_cross1[count_p2].setFill("blue")
                    blue_cross2[count_p2].setFill("blue")
                    blue_cross1[count_p2].setWidth(10)
                    blue_cross2[count_p2].setWidth(10)
                    blue_cross1[count_p2].draw(win)
                    blue_cross2[count_p2].draw(win)
                    turn += 1

                judging = judge(board)
                list_flag = exam_judge(judging)

                #一局棋是否分出胜负以及总比分的加分
                if list_flag[0] or count_p1 + count_p2 == 7:
                    if list_flag[0]:
                        if list_flag[1] == 0:
                            if board[0][0] == 1:
                                p1_score += 1
                                p1_flag = 1
                            else:
                                p2_score += 1
                                p1_flag = 0
                        elif list_flag[1] == 1:
                            if board[0][2] == 1:
                                p1_score += 1
                                p1_flag = 1
                            else:
                                p2_score +=1
                                p1_flag = 0
                        elif list_flag[1] == 2:
                            if board[list_flag[2]][0] == 1:
                                p1_score += 1
                                p1_flag = 1
                            else:
                                p2_score += 1
                                p1_flag = 0
                        else:
                            if board[0][list_flag[2]] == 1:
                                p1_score += 1
                                p1_flag = 1
                            else:
                                p2_score += 1
                                p1_flag = 0
                    else:
                        pass
                            
                    #总比分的刷新显示
                    p1_s.undraw()
                    p1_s = Text(Point(7.5 , 11.0) , "%d" % p1_score)
                    p1_s.setSize(28)
                    p1_s.setFill("red")
                    p1_s.draw(win)

                    p2_s.undraw()
                    p2_s = Text(Point(9.5 , 11.0) , "%d" % p2_score)
                    p2_s.setSize(28)
                    p2_s.setFill("blue")
                    p2_s.draw(win)
                                
                    sleep(1.0)

                    #擦除红圈
                    for ptr in red_circle:
                        ptr.undraw()

                    #擦除蓝叉
                    count = 0
                    for ptr in blue_cross1:
                        ptr.undraw()
                        blue_cross2[count].undraw()
                        count += 1

                    
                    break
                    
                    
            if quit_flag:
                break
            else:
                decide_circle1.undraw()
                decide_circle2.undraw()
                continue
            
        elif player2_button(p):
            try:
                decide_circle1.undraw()
                decide_circle2.undraw()
            except:
                pass
                
            decide_circle1 = Circle(Point(0.1 , 11.0) , 0.05)
            decide_circle1.setOutline("blue")
            decide_circle1.setFill("blue")
            decide_circle1.draw(win)

            decide_circle2 = Circle(Point(0.1 , 11.0) , 0.02)
            decide_circle2.setOutline("red")
            decide_circle2.setFill("red")
            decide_circle2.draw(win)

            if mode >= 0:
                p1_s.undraw()
                p2_s.undraw()

                p1_score = 0
                p2_score = 0
            
                p1_s = Text(Point(7.5 , 11.0) , "%d" % p2_score)
                p1_s.setSize(28)
                p1_s.setFill("red")
                p1_s.draw(win)

                p2_s = Text(Point(9.5 , 11.0) , "%d" % p2_score)
                p2_s.setSize(28)
                p2_s.setFill("blue")
                p2_s.draw(win)
            
            board = [[0,0,0],[0,0,0],[0,0,0]]
            quit_flag = 0
            turn = 0
            red_circle = []
            blue_cross1 = []
            blue_cross2 = []
            mode = -1
            while(1):
                p = win.getMouse()
                if playboard_click(p):
                    trans = pow(-1 , turn)

                    x = p.x
                    y = p.y
                    xn = (int(x / (10.0 / 3)) + 0.5)* (10.0 / 3)
                    yn = (int(y / (10.0 / 3)) + 0.5)* (10.0 / 3)

                    if(board[int(x / (10.0 / 3))][int(y / (10.0 / 3))] == 0):

                        #player1的绘画红圈以及标记位置
                        if (trans == 1):
                            red_circle.append(Circle(Point(xn , yn) , gold_ratio))
                            red_circle[turn / 2].setOutline("red")
                            red_circle[turn / 2].setWidth(10)
                            red_circle[turn / 2].draw(win)
                            turn += 1
                            board[int(x / (10.0 / 3))][int(y / (10.0 / 3))] = trans

                        #player2的绘画蓝叉以及标记位置
                        if (trans == -1):
                            blue_cross1.append(Line(Point(xn - k * gold_ratio , yn - k * gold_ratio) , Point(xn + k * gold_ratio , yn + k * gold_ratio)))
                            blue_cross2.append(Line(Point(xn - k * gold_ratio , yn + k * gold_ratio) , Point(xn + k * gold_ratio , yn - k * gold_ratio)))
                            blue_cross1[turn / 2].setFill("blue")
                            blue_cross2[turn / 2].setFill("blue")
                            blue_cross1[turn / 2].setWidth(10)
                            blue_cross2[turn / 2].setWidth(10)
                            blue_cross1[turn / 2].draw(win)
                            blue_cross2[turn / 2].draw(win)
                            turn += 1
                            board[int(x / (10.0 / 3))][int(y / (10.0 / 3))] = trans

                        judging = judge(board)
                        list_flag = exam_judge(judging)

                        #一局棋是否分出胜负以及总比分的加分
                        if list_flag[0] or turn == 9:
                            if list_flag[0]:
                                if list_flag[1] == 0:
                                    if board[0][0] == 1:
                                        p1_score += 1
                                    else:
                                        p2_score += 1
                                elif list_flag[1] == 1:
                                    if board[0][2] == 1:
                                        p1_score += 1
                                    else:
                                        p2_score +=1
                                elif list_flag[1] == 2:
                                    if board[list_flag[2]][0] == 1:
                                        p1_score += 1
                                    else:
                                        p2_score += 1
                                else:
                                    if board[0][list_flag[2]] == 1:
                                        p1_score += 1
                                    else:
                                        p2_score += 1
                            else:
                                pass
                            
                            #总比分的刷新显示
                            p1_s.undraw()
                            p1_s = Text(Point(7.5 , 11.0) , "%d" % p1_score)
                            p1_s.setSize(28)
                            p1_s.setFill("red")
                            p1_s.draw(win)

                            p2_s.undraw()
                            p2_s = Text(Point(9.5 , 11.0) , "%d" % p2_score)
                            p2_s.setSize(28)
                            p2_s.setFill("blue")
                            p2_s.draw(win)
                                
                            sleep(1.0)

                            #擦除红圈
                            for ptr in red_circle:
                                ptr.undraw()

                            #擦除蓝叉
                            count = 0
                            for ptr in blue_cross1:
                                ptr.undraw()
                                blue_cross2[count].undraw()
                                count += 1


                            break
                        
                elif quit_button(p):
                    quit_flag = 1
                    break
                
                else:
                    continue
            if quit_flag:
                break
            else:
                decide_circle1.undraw()
                decide_circle2.undraw()
                continue
        
        elif quit_button(p):
            break
        
        elif restart_button(p):
            p1_s.undraw()
            p2_s.undraw()

            p1_score = 0
            p2_score = 0
            
            p1_s = Text(Point(7.5 , 11.0) , "%d" % p2_score)
            p1_s.setSize(28)
            p1_s.setFill("red")
            p1_s.draw(win)

            p2_s = Text(Point(9.5 , 11.0) , "%d" % p2_score)
            p2_s.setSize(28)
            p2_s.setFill("blue")
            p2_s.draw(win)
            continue
        else:
            continue



    win.close()

    

main()
