import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

janela = "prismas e piramides"

botaoDireito = False
botaoEsquerdo = False
dX, dY, dZ = 0, 0, 0
bX, bY = 0, 0
a = 0
b = 0
da = 0.5
raio = 2
vertices = 3
modificador = 1
altura = 3

corExtremos = (0.862, 0.866, 0.882)
corFundo = (0.154, 0.302, 0.210, 1)
corLados = (
    (0.909, 0.254, 0.094),
    (0.298, 0.819, 0.215),
    (0, 0.658, 1)
)

def figure():
    pontos = []
    angulo = (2*pi)/vertices
    GL.glPushMatrix()
    GL.glTranslatef(0.0, 1.5, -10)
    GL.glRotatef(90,1.0,0.0,0.0)
    GL.glTranslatef(dX, dY, dZ)
    GL.glRotatef(a, 0.0, 0.0, 1.0)
    GL.glRotatef(b, 0.0, 1.0, 0.0)
    GL.glColor3fv(corExtremos)
    GL.glBegin(GL.GL_POLYGON)
    for i in range(vertices):
        x = raio * cos(i*angulo)
        y = raio * sin(i*angulo)
        pontos += [ (x,y) ]
        GL.glVertex3f(x,y,0.0)
    GL.glEnd()
    GL.glBegin(GL.GL_POLYGON)
    for x,y in pontos:
        GL.glVertex3f(modificador*x,modificador*y, altura)
    GL.glEnd()
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        GL.glColor3fv(corLados[i%3])
        GL.glVertex3f(pontos[i][0],pontos[i][1],0)
        GL.glVertex3f(modificador*pontos[i][0],modificador*pontos[i][1],altura)
        GL.glVertex3f(modificador*pontos[(i+1)%vertices][0],modificador*pontos[(i+1)%vertices][1],altura)
        GL.glVertex3f(pontos[(i+1)%vertices][0],pontos[(i+1)%vertices][1],0)
    GL.glEnd()
    GL.glPopMatrix()

def draw():
    global a, botaoEsquerdo, botaoDireito
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    a = a + da
    GLUT.glutSwapBuffers()

def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)

def teclaE(key, x, y):
    global vertices, modificador
    if (key == GLUT.GLUT_KEY_UP and vertices < 12):
        vertices += 1
    elif (key == GLUT.GLUT_KEY_DOWN and vertices > 3):
        vertices -= 1
    GLUT.glutPostRedisplay()

def teclaP(key, x, y):
    global da, modificador
    if key == b"\033":
        GLUT.glutLeaveMainLoop()
    elif key == b"p":
        if modificador == 1:
            modificador = 0.5
        else:
            modificador = 1
    elif key == b" ":
        if da == 0:
            da = 0.5
        else:
            da = 0
    GLUT.glutPostRedisplay()

def clique(button, state, x, y):
    global bX, bY, botaoEsquerdo, botaoDireito, dY, modificador
    bX, bY = x, y
    botaoDireito = button == GLUT.GLUT_RIGHT_BUTTON and state == GLUT.GLUT_DOWN
    botaoEsquerdo = button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN
    if button == 3 and state == GLUT.GLUT_DOWN:
        dY += 1
    elif button == 4 and state == GLUT.GLUT_DOWN:
        dY -= 1
    elif button == GLUT.GLUT_MIDDLE_BUTTON and state == GLUT.GLUT_DOWN:
        if modificador == 1:
            modificador = 0.5
        else:
            modificador = 1
    GLUT.glutPostRedisplay()

def movimentacao(x, y):
    global a, b, dX, dY, bX, bY, da
    if botaoEsquerdo:
        da = 0
        a -= ((x - bX) / 4.0) * -1
        if a >= 360:
            a -= 360
        if a <= 0:
            a += 360
        if a >= 180:
            b += (y - bY) / 4.0 * -1
        else:
            b -= (y - bY) / 4.0 * -1
        if b >= 360:
            b -= 360
        if b <= 0:
            b += 360
    if botaoDireito:
        dX += -1 * (x - bX) / 100.0
        dY += (y - bY) / 100.0
    bX, bY = x, y
    GLUT.glutPostRedisplay()

def main():    
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE)
    larguraTela = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    alturaTela = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)
    larguraJanela = round(2 * larguraTela / 3)
    alturaJanela = round(2 * alturaTela / 3)
    GLUT.glutInitWindowSize(larguraJanela, alturaJanela)
    GLUT.glutInitWindowPosition(round((larguraTela - larguraJanela) / 2), round((alturaTela - alturaJanela) / 2))
    GLUT.glutCreateWindow(janela)
    GLUT.glutDisplayFunc(draw)
    GLUT.glutSpecialFunc(teclaE)
    GLUT.glutKeyboardFunc(teclaP)
    GLUT.glutMouseFunc(clique)
    GLUT.glutMotionFunc(movimentacao)
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*corFundo)
    GLU.gluPerspective(-45, larguraJanela / alturaTela, 0.1, 100.0)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()