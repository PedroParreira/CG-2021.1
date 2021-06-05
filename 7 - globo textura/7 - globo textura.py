import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from png import Reader
from sys import argv
from math import sin, cos, pi

janela = "globo textura"

a = 90.0
b = 0
da = 0.5
n = 50
m = 50
raio = 2
corFundo = (0.264, 0.478, 0.825, 1)

def f(i,j):
    theta = ( (pi * i) / (n -1) ) - (pi / 2)
    phi = 2*pi*j/(m-1)    
    x = raio * cos(theta) * cos(phi)
    y = raio * sin(theta)
    z = raio * cos(theta) * sin(phi)    
    s = s_func(phi)
    t = t_func(theta)    
    return x,y,z,s,t
def s_func(phi):
    return (phi/(2*pi))
def t_func(theta):
    return ((theta + (pi/2))/pi)

textura = []

def load():
    global textura
    textura = GL.glGenTextures(2)
    imagem = Reader(filename='C:\\Users\\Pedro\\Desktop\\computacao grafica\\trabalhos cg 2021.1\\7 - globo textura\\globomodelo.png')
    w, h, pixels, metadata = imagem.read_flat()
    if(metadata['alpha']):
        mod = GL.GL_RGBA
    else:
        mod = GL.GL_RGB
    GL.glBindTexture(GL.GL_TEXTURE_2D, textura[0])
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, mod, w, h, 0, mod, GL.GL_UNSIGNED_BYTE, pixels.tolist())
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
    GL.glTexEnvf(GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_DECAL)

def figure():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)    
    GL.glLoadIdentity()    
    GL.glPushMatrix()
    GL.glRotatef(a, 0.0, 1.0, 0.0)
    GL.glRotatef(b, 0.0, 0.0, 1.0)
    GL.glBindTexture(GL.GL_TEXTURE_2D, textura[0])
    for i in range(n):
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(m):
            x, y, z, s, t = f(i,j)
            GL.glTexCoord2f(s, t)
            GL.glVertex3f(x,y,z)
            x, y, z, s, t = f(i+1, j)
            GL.glTexCoord2f(s, t)
            GL.glVertex3f(x,y,z)
        GL.glEnd()
    GL.glPopMatrix()
    GLUT.glutSwapBuffers()

def draw():
    global a
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    figure()
    a = a + da
    GLUT.glutSwapBuffers()

def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)
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
    load()
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_TEXTURE_2D)
    GL.glClearColor(*corFundo)
    GL.glClearDepth(1.0)
    GL.glDepthFunc(GL.GL_LESS)
    GL.glShadeModel(GL.GL_SMOOTH)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(-45, larguraJanela / alturaJanela, 0.1, 100.0)
    GL.glTranslatef(0.0, 0.0, -10)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()