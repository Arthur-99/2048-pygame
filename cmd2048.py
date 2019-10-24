import os
import sys
import copy
from ds import deque
import numpy as np


sz = 5
board = np.zeros((sz, sz), dtype=np.int16)


def generate_squares(arr, n):
    opening = len(arr[arr == 0])
    if opening == 0:
        return

    i = np.random.randint(sz)
    j = np.random.randint(sz)
    for _ in range(min(n, opening)):
        while arr[i][j] != 0:
            i = np.random.randint(sz)
            j = np.random.randint(sz)
        arr[i][j] = 2 * np.random.randint(1, 3)

def init():
    generate_squares(board, 2)


def adhere_same(arr):
    for k in range(4):
        tmp = np.rot90(arr, k=k)
        for i in range(sz):
            for j in range(sz - 1):
                if tmp[i][j] == tmp[i][j+1]:
                    return True
    return False


def lose(a):
    if (a == 0).any():
        return False
    elif adhere_same(a):
        return False
    else:
        return True

def win(a):
    if (a == 2048).any():
        return True
    else:
        return False


def arr_update(arr, op):
    if op == 'a':
        arr = np.rot90(arr, k=4)
    elif op == 's':
        arr = np.rot90(arr, k=3)
    elif op == 'd':
        arr = np.rot90(arr, k=2)
    elif op == 'w':
        arr = np.rot90(arr, k=1)
    else:
        return 

    q = [deque() for i in range(sz)]
    for i in range(sz):
        for j in range(sz):
            if arr[i][j] != 0:
                q[i].push_back(arr[i][j])

    qq = [deque() for i in range(sz)]
    for i in range(sz):
        merge = False
        while not q[i].empty():
            if qq[i].back() == q[i].front() and not merge:
                qq[i].pop_back()
                qq[i].push_back(2 * q[i].pop_front())
                merge = True
            else:
                qq[i].push_back(q[i].pop_front())
                merge = False

        while qq[i].size < sz:
            qq[i].push_back(0)

    #################################################
    for i in range(sz):
        for j in range(sz):
            arr[i][j] = qq[i][j]

    if op == 'a':
        arr = np.rot90(arr, k=0)
    elif op == 's':
        arr = np.rot90(arr, k=1)
    elif op == 'd':
        arr = np.rot90(arr, k=2)
    elif op == 'w':
        arr = np.rot90(arr, k=3)


def update(op):
    if op != 'q' and not lose(board):
        a_dpcp = copy.deepcopy(board)
        arr_update(board, op)
        if (a_dpcp == board).all():
            return
        else:
            generate_squares(board, 1)
    else:
        sys.exit()


def run():
    init()

    while True:
        os.system("cls")
        print("wasd+Enter to ctrl")
        print(board)

        op = input()
        update(op)



if __name__ == "__main__":
    run()
