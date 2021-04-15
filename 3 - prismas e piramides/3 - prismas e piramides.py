import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

janela = "prismas e piramides"

dX, dY, dZ = 0, 0, 0
bX, bY = 0, 0
a = 0
b = 0
da = 0.5
raio = 2
vertices = 3
modificador = 1
altura = 3

corFundo = (0.154, 0.302, 0.210, 1)
corExtremos = (0.742, 0.726, 0.712)
corLados = (
    (0.831, 0.879, 0.091),
    (0.237, 0.619, 0.245),
    (0, 0.748, 1)
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
    global a
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    a = a + da
    GLUT.glutSwapBuffers()

def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)

def clique(button, state, x, y):
    global modificador
    if button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN:
        if modificador == 1:
            modificador = 0.5
        else:
            modificador = 1
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
    GLUT.glutMouseFunc(clique)
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*corFundo)
    GLU.gluPerspective(-45, larguraJanela / alturaTela, 0.1, 100.0)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()