import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

janela = "paraboloide revolucao"

botaoDireito = False
botaoEsquerdo = False
dX, dY, dZ = 0, 0, 0
bX, bY = 0, 0
a = 0
b = 180.0
da = 0.5
m, n = 20, 20
raio = 2

corFundo = (0.154, 0.302, 0.210, 1)

def f(i,j):
    theta = ( (pi * i) / (m -1) ) - (pi / 2)
    phi = 2*pi*j/(n-1)
    x = raio * cos(theta) * cos(phi)
    y = raio * sin(theta)
    z = raio * cos(theta) * sin(phi)
    return x, y**2, z

def figure():
    GL.glPushMatrix()
    GL.glTranslatef(dX, dY + 1.5, dZ)
    GL.glRotatef(a, 0.0, 1.0, 0.0)
    GL.glRotatef(b, 0.0, 0.0, 1.0)
    for i in range(round(m/2)):
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(n):
            GL.glColor3fv(
                ((1.0*i/(m-1)),
                0,
                1 - (1.0*i/(m-1))))
            x, y, z = f(i,j)
            GL.glVertex3f(x,y,z)
            GL.glColor3fv(
                ((1.0*(i+1)/(m-1)),
                0,
                1 - (1.0*(i+1)/(m-1))))
            x, y, z = f(i+1, j)
            GL.glVertex3f(x,y,z)
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
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*corFundo)
    GLU.gluPerspective(-45, larguraJanela / alturaJanela, 0.1, 100.0)
    GL.glTranslatef(0.0, 0.0, -10)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()