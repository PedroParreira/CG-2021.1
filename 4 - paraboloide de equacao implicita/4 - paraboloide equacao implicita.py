import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

janela = "paraboloide equacao implicita"

dX, dY, dZ = 0, 0, 0
bX, bY = 0, 0
a = 90.0
b = 45.0
da = 0.5
m, n = 100, 100
x0, y0 = -2, -2
xf, yf = 2, 2
dx, dy = (xf - x0)/m, (yf - y0)/n

corFundo = (0.154, 0.302, 0.210, 1)

def f(x,y):
    return x**2-y**2

def figure():
    GL.glPushMatrix()
    GL.glTranslatef(dX, dY, dZ)
    GL.glRotatef(a, 0.0, 1.0, 0.0)
    GL.glRotatef(b, 0.0, 0.0, 1.0)
    for i in range(0, n):
        y = y0 + i*dy      
        GL.glColor3f(1-(i/n), 0, i/n)
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(0,m):
            x = x0 + j*dx
            GL.glVertex3f(x, y, f(x,y))
            GL.glVertex3f(x, y+dy, f(x, y+dy))
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