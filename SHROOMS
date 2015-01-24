'''
http://www.spoj.com/problems/SHROOMS/
parti dalla cella r,c -> calcola i costi verso sinistra
controlla che sia il costo minimo tra il path che va a est e quello che va a sud
se il guadagno e' maggiore di 0 -> lascia 0, voglio il min num di funghi
'''

m = [0]  # input matrix


def mush(r, c):
    # shrooms cost matrix
    s = [[float('inf') for i in range(c)] for j in range(r)]

    s[r-1][c-1] = m[r-1][c-1]*-1 if m[r-1][c-1] < 0 else 0

    for row in range(r-1, -1, -1):
        for col in range(c-1, -1, -1):
            # --- bordo destro
            if col == c-1 and row < r-1:
                s[row][col] = max(s[row+1][col]-m[row][col], 0)
            # --- ultima riga
            elif row == r-1 and col > 0:
                s[row][col-1] = max(s[row][col]-m[row][col-1], 0)
            
            elif row < r-1:
                s[row][col] = max(min(s[row+1][col], s[row][col+1])-m[row][col], 0)
            
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in s]))
    return s[0][0]


def start():
    global m

    while True:
        num_test = int(raw_input())
        for i in range(num_test):
            r, c = [int(i) for i in raw_input().split()]
            
            # --- build matrix from input
            m = [0]*r
            for row in range(int(r)):
                m[row] = [int(i) for i in raw_input().split()]
            # print m  # " m[",row,"]",m[row]
            
            # --- search for paths
            print mush(r, c)

        return

if __name__ == '__main__': 
    start()


