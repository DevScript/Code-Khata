from Summatory import suma
def matrix(lines):                                             #Function to solve matrix form of polynomial regression using Guass Elimination Method
    for x in range(len(lines) - 1):
        for y in range(x+1,len(lines)):
            if lines[y][x] != 0:
                co = lines[x][x] / (-lines[y][x])
                for i in range(len(lines[0])):
                    lines[y][i] *= co
                    lines[y][i] += lines[x][i]
    awn = [0]
    length = len(lines)
    for x in range(len(lines)-1,-1,-1):
        awn.append(round((lines[x][length] - suma([awn[length-i] * lines[x][i] for i in range(length-1,x,-1)])) / lines[x][x],14))
    return awn[1:]

def polyreg(ord,xl,yl): #Polynomial Regression of any order. Order 1 for Linear Regression

    #ord argument is the order of the polynomial regression (2 outputs a quadratic function, 3 a cubic one etc.)
    #xl is first set of values
    #yl is second set of values

    if len(xl)!=len(yl):
        raise ValueError('Data lists must be the same size')
    if len(xl) <= ord:
        raise ValueError('Data list length must be greater than the order')
    ord += 1
    Sum_list_x = []
    Sum_list_xy = []
    for x in range(2 * ord - 1):
        Sum_list_x.append(suma([i**x for i in xl]))
    for x in range(ord):
        Sum_list_xy.append(suma([yl[i] * (xl[i] ** (x)) for i in range(len(yl))]))
    F_x = matrix([Sum_list_x[x:x+ord] + [Sum_list_xy[x]] for x in range(ord)])
    if ord-1 == 1:
        return f"The Linear Regression is F(x) = {' + '.join([f'({F_x[x]} x**{ord-1-x})' for x in range(len(F_x))])}"
    else:
        return f"The Polynomial Regression of {ord-1}º order, is F(x) = {' + '.join([f'({F_x[x]} x**{ord-1-x})' for x in range(len(F_x))])}"

#example: polyreg(2,[1,2,3],[5,6,7])