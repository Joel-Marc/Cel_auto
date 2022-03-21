import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


from math import ceil, floor
from random import random
from numpy import array
from scipy.sparse import csr_matrix
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

npt = 30


mat = [[round(random()) for _1 in range(npt)] for _ in range(npt)]
# print(mat)

# S = csr_matrix(mat)

# mat = [[0] * 100 for _ in range(100)]
# mat[10][10] = 1
# mat[11][11] = 1
# mat[12][11] = 1
# mat[10][12] = 1
# mat[11][12] = 1
# mat[13][12] = 1

chm = [[0] * npt for _ in range(npt)]

ssw = 50

dsw = 30

fl = 0
noa = 0
yr = 0
# print(S)
def gol():
    global mat, fl, noa

    if mat == chm:
        print("CIVILIZATION DESTROYED ! YEAR : ", yr)
        quit()

    tm = mat.copy()
    for i in range(npt):
        for j in range(npt):
            if mat[i][j] == 1:
                di = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1)]
                cnt = 0
                for k1, k2 in di:
                    try:
                        if mat[i + k1][j + k2] == 1:
                            cnt += 1
                    except:
                        pass
                # print(cnt)
                if cnt not in [2, 3]:
                    tm[i][j] = 0

            elif mat[i][j] == 0:
                di = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1)]
                cnt = 0
                for k1, k2 in di:
                    try:
                        if mat[i + k1][j + k2] == 1:
                            cnt += 1
                    except:
                        pass
                if cnt == 3:
                    tm[i][j] = 1
    # print(array(mat))
    fl += 1
    print(fl % dsw, fl % ssw)
    if fl % dsw == 0:
        noa += 1
        for i in range(npt):
            for j in range(npt):
                # print(round((i + j + random()) / (random() * npt * npt)))
                if round((i + j + random()) / (random() * npt * npt)) > 0:
                    mat[i][j] = 0
        # fl = 0
        return mat

    if fl % ssw == 0:
        for i in range(npt):
            for j in range(npt):
                # print(round((i + j + random()) / (random() * npt * npt)))
                if round((i + j + random()) / (random() * npt * npt)) > 0:
                    mat[i][j] = 1
        # fl = 0
        return mat

    mat = tm.copy()
    return mat


def Cube(Points):
    glPointSize(6)
    glBegin(GL_POINTS)
    for i in range(len(Points)):
        for j in range(len(Points[0])):
            if Points[i][j] == 1:
                glColor3f(
                    (i * 2 + 0.5) / (len(Points)),
                    (j * 2 + 0.5) / (len(Points[0])),
                    (i * j + 0.5) / len(Points),
                )
                glVertex2fv((i * 2 / (len(Points)), j * 2 / (len(Points[0]))))

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube(gol())
        pygame.display.flip()
        pygame.time.wait(1)
        global noa, yr
        yr += 1
        print("Year : ", yr, "No of Apocalypses : ", noa)


main()
