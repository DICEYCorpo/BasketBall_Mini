from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np


score = 0
def plotpoints(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# -----------------------------------------------FOR DRAWING LINES------------------------------------------------------
def FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return "zone-0"
        if dx < 0 and dy >= 0:
            return "zone-3"
        if dx < 0 and dy < 0:
            return "zone-4"
        if dx >= 0 and dy < 0:
            return "zone-7"
    else:
        if dx >= 0 and dy >= 0:
            return "zone-1"
        if dx < 0 and dy >= 0:
            return "zone-2"
        if dx < 0 and dy < 0:
            return "zone-5"
        if dx >= 0 and dy < 0:
            return "zone-6"

def scale(x1, y1, r):
    sc = 0.75
    s = np.array([[sc, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])

    line_matrix = np.array([[1, r, 1]])

    # Rotate the line matrix using matmul
    scaled_line = np.matmul(line_matrix, s)
    r =  scaled_line[0,1]

    draw_circle(x1, y1, r)

def ConvertToZone0(x1, y1, x2, y2, zone):
    if zone == "zone-0":
        x1, y1 = x1, y1
        x2, y2 = x2, y2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-1":
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-2":
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-3":
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-4":
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-5":
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-6":
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
        converted = [x1, y1, x2, y2]
        return converted
    if zone == "zone-7":
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
        converted = [x1, y1, x2, y2]
        return converted


def ConvertToOriginalZone(x, y, zone):
    if zone == "zone-0":
        x, y = x, y
        return [x, y]
    if zone == "zone-1":
        x, y = y, x
        return [x, y]
    if zone == "zone-2":
        x, y = -y, x
        return [x, y]
    if zone == "zone-3":
        x, y = -x, y
        return [x, y]
    if zone == "zone-4":
        x, y = -x, -y
        return [x, y]
    if zone == "zone-5":
        x, y = -y, -x
        return [x, y]
    if zone == "zone-6":
        x, y = y, -x
        return [x, y]
    if zone == "zone-7":
        x, y = x, -y
        return [x, y]


def DrawLine(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x = x1
    y = y1
    while x < x2:
        x = x + 1
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE
        values = ConvertToOriginalZone(x, y, zone)
        plotpoints(values[0], values[1])
def up1():
  value=[430,560,480,560]
  callforplot(value[0],value[1],value[2],value[3])
def upright1():
  value=[480,560,480,520]
  callforplot(value[0],value[1],value[2],value[3])
def upleft1():
  value=[430,560,430,520]
  callforplot(value[0],value[1],value[2],value[3])
def middle1():
  value=[430,520,480,520]
  callforplot(value[0],value[1],value[2],value[3])
def down1():
  value=[430,480,480,480]
  callforplot(value[0],value[1],value[2],value[3])
def downright1():
  value=[480,520,480,480]
  callforplot(value[0],value[1],value[2],value[3])
def downleft1():
  value=[430,520,430,480]
  callforplot(value[0],value[1],value[2],value[3])
def digits(value):
  if value==0:
    up1()
    upright1()
    upleft1()
    down1()
    downright1()
    downleft1()
  if value==1:
    upright1()
    downright1()
  if value==2:
    up1()
    upright1()
    middle1()
    downleft1()
    down1()
  if value==3:
    up1()
    upright1()
    middle1()
    downright1()
    down1()
  if value==4:
    upleft1()
    middle1()
    upright1()
    downright1()
  if value==5:
    up1()
    upleft1()
    middle1()
    downright1()
    down1()
  if value==6:
    up1()
    upleft1()
    downleft1()
    down1()
    downright1()
    middle1()
  if value==7:
    up1()
    upright1()
    downright1()
  if value==8:
    up1()
    upleft1()
    middle1()
    upright1()
    downright1()
    down1()
    downleft1()
  if value==9:
    up1()
    upleft1()
    middle1()
    upright1()
    down1()
    downright1()

def callforplot(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    values = ConvertToZone0(x1, y1, x2, y2, zone)
    DrawLine(values[0], values[1], values[2], values[3], zone)
# ---------------------------------------------START OF CIRCLE DRAWING ALGO---------------------------------------------
def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
def draw_circle(x1, y1, rad):
    d = 1 - rad
    x = 0
    y = rad
    circlepoints(x, y, x1, y1)
    while x < y:
        if d > 0:
            d = d + 2 * x - 2 * y + 5
            y -= 1
        else:
            d = d + 2 * x + 3
        x += 1
        circlepoints(x, y, x1, y1)
def circlepoints(x, y, x1, y1):
    draw_points(x + x1, y + y1)
    draw_points(y + x1, x + y1)
    draw_points(y + x1, -x + y1)
    draw_points(x + x1, -y + y1)
    draw_points(-x + x1, -y + y1)
    draw_points(-y + x1, -x + y1)
    draw_points(-y + x1, x + y1)
    draw_points(-x + x1, y + y1)

def trans(x,y,amnt_x,amnt_y,r):


    # move the circle to the right by a certain amount

    matrix1 = np.array([[x], [y]])
    matrix2 = np.array([[amnt_x], [amnt_y]])
    result = np.add(matrix1, matrix2)
    scale(result[0],result[1],r)

# ---------------------------------------------END OF LINE DRAWING ALGO-------------------------------------------------






def promptBox():
    # First Prompt Box
    callforplot(-570, 570, -350, 570)  # top
    callforplot(-570, 570, -570, 470)  # left
    callforplot(-570, 470, -350, 470)  # down
    callforplot(-350, 470, -350, 570)  # right
    # Second Prompt Box
    callforplot(-50, 570, -270, 570)
    callforplot(-270, 570, -270, 470)
    callforplot(-270, 470, -50, 470)
    callforplot(-50, 470, -50, 570)
    # Third Prompt Box
    callforplot(570, 570, 350, 570)
    callforplot(570, 570, 570, 470)
    callforplot(570, 470, 350, 470)
    callforplot(350, 470, 350, 570)

def projectile_Line():
    # Starting Projectile Line
    callforplot(-350, 350, -350, -350)
def ball():
    draw_circle(-385, 20, 30)  # Ball

def projectiles():
    # Projectils
    callforplot(-350, 0, -120, 30)
    callforplot(-350, 0, -120, 70)
    callforplot(-350, 0, -120, -10)
    callforplot(-350, 0, -120, -50)

def basketBallStand():
    # Basketball board
    callforplot(350, 300, 570, 300)
    callforplot(350, 300, 350, 50)
    callforplot(350, 50, 570, 50)
    callforplot(570, 50, 570, 300)
    # Basketball loop stand
    callforplot(425, 120, 250, 50)
    callforplot(495, 120, 270, 15)
    draw_circle(240, 22.5, 30)

    # Basketball stand line
    callforplot(455, 50, 455, -400)
    callforplot(465, 50, 465, -400)

    # Basketball stand base
    callforplot(405, -400, 515, -400)
    callforplot(405, -400, 405, -450)
    callforplot(405, -450, 515, -450)
    callforplot(515, -450, 515, -400)

def stickman():
    # Stickman
    callforplot(-415, 20, -450, 70)  # right arm
    callforplot(-450, 70, -485, 20)  # left arm
    # rotate(-415, 20, -450, 70)

    callforplot(-450, -160, -485, -250)  # left leg
    callforplot(-450, -160, -415, -250)  # right leg

    callforplot(-450, 130, -450, -160)  # body

    draw_circle(-450, 150, 20)

def exit():
    # EXIT (X) Labelling
    callforplot(-172.5, 565, -147.5, 475)
    callforplot(-147.5, 565, -172.5, 475)

def scoreWord():
    # Score labelling
    callforplot(100, 570, 125, 570)  # S
    callforplot(100, 570, 100, 520)
    callforplot(100, 520, 125, 520)
    callforplot(125, 520, 125, 470)
    callforplot(125, 470, 100, 470)

    callforplot(150, 570, 175, 570)  # C
    callforplot(150, 570, 150, 470)
    callforplot(150, 470, 175, 470)

    callforplot(200, 570, 225, 570)  # O
    callforplot(225, 570, 225, 470)
    callforplot(225, 470, 200, 470)
    callforplot(200, 470, 200, 570)

    callforplot(250, 570, 250, 470)  # R (long line)
    callforplot(250, 570, 275, 570)  # top line
    callforplot(275, 570, 275, 520)  # short vertical line
    callforplot(250, 520, 275, 520)  # middle line
    callforplot(250, 520, 275, 470)  # diagonal line

    callforplot(300, 570, 300, 470)  # E (vertical long line)
    callforplot(300, 570, 325, 570)  # (top line)
    callforplot(300, 520, 325, 520)  # middle line
    callforplot(300, 470, 325, 470)  # bottom line

def reset():
    # RST Label
    callforplot(-550, 565, -525, 565)  # R
    callforplot(-525, 565, -525, 520)
    callforplot(-525, 520, -550, 520)
    callforplot(-550, 565, -550, 475)
    callforplot(-550, 520, -525, 470)

    callforplot(-500, 565, -475, 565)  # S
    callforplot(-500, 565, -500, 520)
    callforplot(-500, 520, -475, 520)
    callforplot(-475, 520, -475, 475)
    callforplot(-475, 475, -500, 475)

    callforplot(-450, 565, -425, 565)  # T
    callforplot(-437.5, 565, -437.5, 475)
def labellingProjectiles():
    # Labeling projectile
    callforplot(-105, 80, -105, 60)  # 1

    callforplot(-111, 40, -100, 40)  # 2
    callforplot(-100, 40, -100, 30)
    callforplot(-100, 30, -110, 30)
    callforplot(-110, 30, -110, 20)
    callforplot(-110, 20, -100, 20)

    callforplot(-100, 0, -100, -20)  # full straight line of 3
    callforplot(-110, 0, -100, 0)  # top line
    callforplot(-110, -10, -100, -10)  # middle line
    callforplot(-110, -20, -100, -20)  # bottom line

    callforplot(-110, -40, -110, -50)  # left short line of 4
    callforplot(-110, -50, -100, -50)  # right long line
    callforplot(-100, -40, -100, -60)  # horizontal line

def creatingTheGameWindow():
    promptBox()
    projectile_Line()
    ball()
    projectiles()
    basketBallStand()
    stickman()
    exit()
    scoreWord()
    reset()
    labellingProjectiles()
    digits(0)
    glFlush()
    glutSwapBuffers()

def increaseScore():
    global score
    score += 1
    digits(score)
    glFlush()
    glutSwapBuffers()
def createScore():

    promptBox()
    projectile_Line()
    projectiles()
    basketBallStand()
    stickman()
    exit()
    scoreWord()
    reset()
    labellingProjectiles()
    glFlush()
    glutSwapBuffers()
    trans(-385, 20,600, 20, 30)
def createScore2():

    promptBox()
    projectile_Line()
    projectiles()
    basketBallStand()
    stickman()
    exit()
    scoreWord()
    reset()
    labellingProjectiles()
    digits(score)
    glFlush()
    glutSwapBuffers()
    trans(-385, 20,700, -50, 30)

def createScore3():

    promptBox()
    projectile_Line()
    projectiles()
    basketBallStand()
    stickman()
    exit()
    scoreWord()
    reset()
    labellingProjectiles()
    digits(score)
    glFlush()
    glutSwapBuffers()
    trans(-385, 20,700, -150, 30)
def createScore4():

    promptBox()
    projectile_Line()
    projectiles()
    basketBallStand()
    stickman()
    exit()
    scoreWord()
    reset()
    digits(score)
    labellingProjectiles()
    glFlush()
    glutSwapBuffers()
    trans(-385, 20,700, -300, 30)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.5, 0.0)
    creatingTheGameWindow()


def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-600, 600, -600, 600, 0, 1.0)


def keyboard(key, x, y):


    if key == b'1':
        glClear(GL_COLOR_BUFFER_BIT)
        createScore()
        increaseScore()

    if key == b'2':
        glClear(GL_COLOR_BUFFER_BIT)
        createScore2()
        glFlush()
        glutSwapBuffers()

    if key == b'3':
        glClear(GL_COLOR_BUFFER_BIT)
        createScore3()
        glFlush()
        glutSwapBuffers()
    if key == b'4':
        glClear(GL_COLOR_BUFFER_BIT)
        createScore4()
        glFlush()
        glutSwapBuffers()
    if key == b'r':
        glClear(GL_COLOR_BUFFER_BIT)
        global score
        score = 0
        creatingTheGameWindow()
    if key == b'x':
        glutDestroyWindow(glutGetWindow())

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Line and Circle")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    init()
    glutMainLoop()

main()
