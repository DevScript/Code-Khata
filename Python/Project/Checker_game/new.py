# import gaming
import pygame
import time
from pygame import mixer

pygame.mixer.init()

mixer.music.load("song1.mp3")
mixer.music.play(-1)
num = 0 
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT//COLS 
PADDING = 10
radius = SQUARE_SIZE//2 - PADDING 
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (160, 82, 45)
GREY = (128, 128, 128)
CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (40,25))
Graph = {}
last = (0, 0)
moves= []
single_move = []
jump_moves = []

blue_king_pos = []
grey_king_pos = []
blue_counter = 12
grey_counter = 12
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
num = "blue"
pygame.display.set_caption('CHECKERS')

def push(stack, item):
    stack.append(item)
    return stack

def draw_squares(win):
    for row in range(ROWS):
        pygame.draw.rect(win, WHITE, (600, row*SQUARE_SIZE , SQUARE_SIZE//4, SQUARE_SIZE))
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    

def calc_position(row, col):
        x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + SQUARE_SIZE // 2
        return (x, y)


def graphing(g):
    for row in range(ROWS): 
        for col in range(COLS): 
            if col % 2 == ((row + 1) % 2):
                g[(row*SQUARE_SIZE, col*SQUARE_SIZE)] = {}
    for i in g:
        if (i[0]//SQUARE_SIZE) == 0 and (i[1]//SQUARE_SIZE) == (ROWS)-1: # upper right corner
            grey_king_pos.append(i)
            g[i] = {"holder": None, "down": {"left": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE)} }
        elif (i[0]//SQUARE_SIZE) == (ROWS)-1 and (i[1]//SQUARE_SIZE) == 0:  # lower left corner
            blue_king_pos.append(i)
            g[i] = {"holder": None, "up": {"right": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE)} }
        elif (i[0]//SQUARE_SIZE) == 0: # upper row
            grey_king_pos.append(i)
            g[i] = {"holder": None, "down": {"left": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE),
            "right": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE) } }
        elif (i[0]//SQUARE_SIZE) == ROWS -1: #last row
            blue_king_pos.append(i)
            g[i] = {"holder": None, "up": {"left": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE),
            "right": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE) } }
        elif (i[1]//SQUARE_SIZE) == 0:  #left col
            g[i] = {"holder": None, "up": {"right": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE)},
            "down": {"right": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE)} }
        elif (i[1]//SQUARE_SIZE) == COLS-1: # right col
            g[i] = {"holder": None, "up": {"left": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE)},
            "down": {"left": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE)} }    
        else:
            g[i] = {"holder": None,
            "up": {"left": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE),
            "right": (((i[0]//SQUARE_SIZE) - 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE) },
            "down": {"left": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) - 1 )*SQUARE_SIZE),
            "right": (((i[0]//SQUARE_SIZE) + 1)*SQUARE_SIZE, ((i[1]//SQUARE_SIZE) + 1 )*SQUARE_SIZE) } }
    return g

def adding_pieces(Graph, win):
    Graph = graphing(Graph)
    for i in Graph:
        if i[0] < 3*SQUARE_SIZE:
            Graph[i]["holder"] = "BLUE"
            Blue_piece = pygame.draw.circle(win, BLUE, calc_position(i[0]//SQUARE_SIZE, i[1]//SQUARE_SIZE ), radius)
            # win.blit(CROWN, ((SQUARE_SIZE * i[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * i[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))
        
        elif i[0] > 4*SQUARE_SIZE:
            Graph[i]["holder"] = "GREY"
            Grey_piece = pygame.draw.circle(win, GREY, calc_position(i[0]//SQUARE_SIZE, i[1]//SQUARE_SIZE ), radius)

    return Graph

# def second_valid_moves(graph, pos, holder, moves):
#     if holder == "BLUE":
#         for i in graph[pos]["down"]:
#             temp = graph[pos]["down"][i] 
#             if graph[temp]["holder"] == None:
#                 moves.append(temp)

#     elif holder == "GREY":
#         for i in graph[pos]["up"]:
#             temp = graph[pos]["up"][i] 
#             if graph[temp]["holder"] == None:
#                 moves.append(temp)
#     return moves

def draw_valid_moves(graph, pos, win):
    if graph[pos]['holder'] == "BLUE":
        push(single_move, (pos, graph[pos]['holder'] )) #saving the holder of selected position of jumping and removing 
        push(jump_moves, (pos, graph[pos]['holder'] ))

        if "down" in graph[pos]:
            for i in graph[pos]["down"]:
                temp = graph[pos]["down"][i] 
                movement = i
                # print(movement)
                if graph[temp]["holder"] == None:
                    push(moves, temp), push(single_move, temp)

                elif graph[temp]["holder"] != graph[pos]['holder'] and not graph[temp]["holder"] == "Blue_king":
                    if "down" in graph[temp]:
                        for j in graph[temp]["down"]:
                            if j  == movement:
                                if movement in graph[temp]["down"] and graph[(graph[temp]["down"][movement])]["holder"] == None :
                                    push(moves, (graph[temp]["down"][movement]))    
                                    push(jump_moves, ((graph[temp]["down"][movement]), temp))
                                    

    elif graph[pos]['holder'] == "Blue_king":
        push(single_move, (pos, graph[pos]['holder'] )) #saving the holder of selected position of jumping and removing 
        push(jump_moves, (pos, graph[pos]['holder'] ))

        for i in graph[pos]:
            if i!= "holder":
                movement1= i
                for j in graph[pos][i]:
                    temp = graph[pos][i][j]
                    movement = j
                    if graph[temp]["holder"] == None:
                        push(moves, temp), push(single_move, temp) 

                    elif graph[temp]["holder"] != graph[pos]['holder'] and not graph[temp]["holder"] == "BLUE":
                        for k in graph[temp]:
                            if k == movement1:
                                for p in graph[temp][k]:
                                    if p == movement:
                                        if p in graph[temp][k] and graph[(graph[temp][k][p])]["holder"] == None :
                                            push(moves, (graph[temp][k][p]))    
                                            push(jump_moves, ((graph[temp][k][p]), temp))

    elif graph[pos]['holder'] == "GREY":
        push(single_move, (pos, graph[pos]['holder'])) #saving the holder of selected position of jumping and removing
        push(jump_moves, (pos, graph[pos]['holder'] ))
        if "up" in graph[pos]:
            for i in graph[pos]["up"]:
                temp = graph[pos]["up"][i] 
                movement = i
                if graph[temp]["holder"] == None:
                    push(moves, temp), push(single_move, temp)
                
                elif graph[temp]["holder"] != graph[pos]['holder'] and not graph[temp]["holder"] == "Grey_king":
                    if "up" in graph[temp]:
                        for j in graph[temp]["up"]:
                            if j  == movement:
                                if movement in graph[temp]["up"] and graph[(graph[temp]["up"][movement])]["holder"] == None :
                                    push(moves, (graph[temp]["up"][movement]))    
                                    push(jump_moves, ((graph[temp]["up"][movement]), temp))

    elif graph[pos]['holder'] == "Grey_king":
        push(single_move, (pos, graph[pos]['holder'] )) #saving the holder of selected position of jumping and removing 
        push(jump_moves, (pos, graph[pos]['holder'] ))

        for i in graph[pos]:
            if i!= "holder":
                movement1= i
                for j in graph[pos][i]:
                    temp = graph[pos][i][j]
                    movement = j
                    if graph[temp]["holder"] == None:
                        push(moves, temp), push(single_move, temp) 

                    elif graph[temp]["holder"] != graph[pos]['holder'] and not graph[temp]["holder"] == "GREY":
                        for k in graph[temp]:
                            if k == movement1:
                                for p in graph[temp][k]:
                                    if p == movement:
                                        if p in graph[temp][k] and graph[(graph[temp][k][p])]["holder"] == None :
                                            push(moves, (graph[temp][k][p]))    
                                            push(jump_moves, ((graph[temp][k][p]), temp))

    for i in moves:
        pygame.draw.circle(win, RED, calc_position(i[0]//SQUARE_SIZE, i[1]//SQUARE_SIZE ) , radius - 10)       

#{(0, 75): {'holder': 'BLUE', 'down': {'left': (75, 0), 'right': (75, 150)}}

def pop(stack):
    return stack.pop()

def enqueue(queue, a):
    queue.append(a)

def dequeue(queue):
    return queue.pop(0)

def is_empty(lst):
    return len(lst) == 0

def normal_move(graph, pos, single_move, win):

    single_holder = single_move[0][1]

    if single_holder == "BLUE" and pos in blue_king_pos:
        graph[pos]["holder"], graph[single_move[0][0]]["holder"] = "Blue_king", None
        pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        single_move[0] = (single_move[0][0],"Blue_king")
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))

    elif single_holder == "GREY" and pos in grey_king_pos:
        graph[pos]["holder"], graph[single_move[0][0]]["holder"] = "Grey_king", None
        pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))
        single_move[0] = (single_move[0][0],"Grey_king")

    elif single_holder == "BLUE":
        graph[pos]["holder"], graph[single_move[0][0]]["holder"] = single_move[0][1], None 
        pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)

    elif single_holder == "GREY":
        graph[pos]["holder"], graph[single_move[0][0]]["holder"] = single_move[0][1], None 
        pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)

    if  single_holder == "Blue_king":
        graph[pos]["holder"], graph[single_move[0][0]]["holder"] = single_move[0][1], None
        pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))
    
    if single_holder == "Grey_king":
        graph[pos]["holder"], graph[single_move[0][0]]["holder"] = single_move[0][1], None
        pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))
    
    # if  single_holder == "BLUE":
    #     pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
    # pygame.draw.circle(win, BLACK, calc_position(single_move[0][0][0]//SQUARE_SIZE, single_move[0][0][1]//SQUARE_SIZE ) , radius)

    # if  single_holder == "GREY":
    #     pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
    pygame.draw.circle(win, BLACK, calc_position(single_move[0][0][0]//SQUARE_SIZE, single_move[0][0][1]//SQUARE_SIZE ) , radius)


    queue = []
    i = len(moves) - 1
    while not is_empty(moves):
        if pos == moves[i]:
            pop(moves)
        else:
            push(queue , pop(moves))
        i -=1
    while not is_empty(queue):
        push(moves, dequeue(queue))
    num = "grey"

def beat(graph, pos, jump_moves, win):
    global blue_counter
    global grey_counter
    print(jump_moves)
    jump_holder = jump_moves[0][1]

    if jump_holder == "BLUE" and pos in blue_king_pos:
        graph[pos]["holder"], graph[jump_moves[0][0]]["holder"] = "Blue_king", None
        pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))
        jump_moves[0] = (jump_moves[0][0],"Blue_king")

    if jump_holder == "GREY" and pos in grey_king_pos:
        graph[pos]["holder"], graph[jump_moves[0][0]]["holder"] = "Grey_king", None
        pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        jump_moves[0] = (jump_moves[0][0],"Grey_king")
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))

    # graph[pos]["holder"], graph[jump_moves[0][0]]["holder"]  = jump_moves[0][1], None
    # print(jump_moves)
    pygame.draw.circle(win, BLACK, calc_position(jump_moves[0][0][0]//SQUARE_SIZE, jump_moves[0][0][1]//SQUARE_SIZE ) , radius)
    
    for i in range(1, len(jump_moves)):
        if  jump_moves[i][0] == pos:
            
            if graph[jump_moves[i][1]]["holder"] == "GREY" or graph[jump_moves[i][1]]["holder"] =="Grey_king":
                grey_counter -= 1
            elif graph[jump_moves[i][1]]["holder"] == "BLUE" or graph[jump_moves[i][1]]["holder"] =="Blue_king":
                blue_counter -= 1
            print(grey_counter)
            print(blue_counter)

            graph[jump_moves[i][1]]["holder"] = None
            pygame.draw.circle(win, BLACK, calc_position(jump_moves[i][1][0]//SQUARE_SIZE, jump_moves[i][1][1]//SQUARE_SIZE ) , radius)
            # time.sleep(10)
        
    if  jump_holder == "BLUE":
        graph[pos]["holder"], graph[jump_moves[0][0]]["holder"]  = jump_moves[0][1], None
        pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
    # pygame.draw.circle(win, BLACK, calc_position(single_move[0][0][0]//SQUARE_SIZE, single_move[0][0][1]//SQUARE_SIZE ) , radius)

    if  jump_holder == "GREY":
        graph[pos]["holder"], graph[jump_moves[0][0]]["holder"]  = jump_moves[0][1], None
        pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)

    if  jump_holder == "Blue_king":
        graph[pos]["holder"], graph[jump_moves[0][0]]["holder"]  = jump_moves[0][1], None
        pygame.draw.circle(win, BLUE, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))
    
    if jump_holder == "Grey_king":
        graph[pos]["holder"], graph[jump_moves[0][0]]["holder"]  = jump_moves[0][1], None
        pygame.draw.circle(win, GREY, calc_position(pos[0]//SQUARE_SIZE, pos[1]//SQUARE_SIZE ) , radius)
        win.blit(CROWN, ((SQUARE_SIZE * pos[1]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_width()//2 , (SQUARE_SIZE * pos[0]//SQUARE_SIZE + SQUARE_SIZE // 2)-CROWN.get_height()//2))


    queue = []
    i = len(moves) - 1
    while not is_empty(moves):
        if pos == moves[i]:
            pop(moves)
        else:
            push(queue , pop(moves))
        i -=1
    while not is_empty(queue):
        push(moves, dequeue(queue))
    num = "grey"

def working(graph, pos, win ,moves):
    if pos in single_move:
        normal_move(graph, pos, single_move, win)
    for i in range(1, len(jump_moves)):
        if pos == jump_moves[i][0]:
            beat(graph, pos, jump_moves, win)
    if moves :
        for i in moves:
            pygame.draw.circle(win, BLACK, calc_position(i[0]//SQUARE_SIZE, i[1]//SQUARE_SIZE ) , radius)
        
    # if pos not in jump_moves and pos not in single_move:
    while jump_moves:
        jump_moves.pop()
    while single_move:
        single_move.pop()
    # print(moves)
    if len(moves) == 0:
        # print(moves, single_move)
        draw_valid_moves(graph, pos, win)
    else: 
        while moves:
            moves.pop()    

def get_position(pos):
    x, y = pos
    row, col = (y // SQUARE_SIZE) * SQUARE_SIZE ,(x // SQUARE_SIZE) * SQUARE_SIZE
    # print(row, col)
    return (row, col)

check = False
def main():
    run = True
    num = 0
    draw_squares(WINDOW)
    graph = adding_pieces(Graph, WINDOW)
    turn = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if grey_counter <= 0 or blue_counter <= 0:
                run = False
            # pos = pygame.mouse.get_pos()
            # print(pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                x, y = (x // SQUARE_SIZE) * SQUARE_SIZE ,(y // SQUARE_SIZE) * SQUARE_SIZE
                # if ((x % 2) and not(y % 2)) or (not(x % 2) and (y % 2)):
                if (x%2 != y % 2):
                    working(graph, get_position(pos), WINDOW, moves)
                    
        pygame.display.update()

    pygame.quit()

main()