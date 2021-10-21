def gen(n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    return(abc[:n])

print(gen(7))


def letra_o(n):

    if(n%2 == 0):
        n += 1

    output = ('*' * n) + '\n'
    
    for i in range(1,n-1):
        output += '*'
        for j in range(1,n-1):
            output += ' '
        output += '*\n'

    output += ('*' * n) + '\n'
    print(output)

letra_o(6)

def letra_i(n):

    if(n%2 == 0):
        n += 1

    output = ('*' * n) + '\n'

    for i in range(1,n-1):
        for i in range(0,n):

            if(n%2 == 0 and (i == int(n/2)-1 or i == int(n/2) )):
                output += '*'
            elif (n%2 == 1 and i == int(n/2) ):
                output += '*'
            else:
                output += ' '
            
        output += '\n'

    output += ('*' * n) + '\n'
    print(output)

letra_i(6)

def letra_x(n):

    if(n%2 == 0):
        n += 1

    output = ''

    for i in range(n): # Con este for recorro las filas
        
        fila = list(' ' * (n+1))

        fila[i] = '*'
        fila[n-i-1] = '*'
        fila[n] = '\n'

        output += ''.join(fila)
    
    print(output)

letra_x(6)