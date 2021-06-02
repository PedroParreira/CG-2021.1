import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from png import Reader
from sys import argv
from math import sin, cos, pi

janela = "dado textura"

a = 60.0
b = 0
da = 0.5
dX, dY, dZ = 0, 0, 0
corFundo = (0.264, 0.478, 0.825, 1)
m = 75
raio = 4

textura = []

def load():
    global textura
    textura = GL.glGenTextures(2)
    imagem = Reader(filename='C:\\Users\\Pedro\\Desktop\\computacao grafica\\trabalhos cg 2021.1\\6 - dado textura\\dadomodelo.png')
    w, h, pixels, metadata = imagem.read_flat()
    if(metadata['alpha']):
        modo = GL.GL_RGBA
    else:
        modo = GL.GL_RGB
    GL.glBindTexture(GL.GL_TEXTURE_2D, textura[0])
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL.GL_UNSIGNED_BYTE, pixels.tolist())
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
    GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
    GL.glTexEnvf(GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_DECAL)

def figure():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)    
    GL.glLoadIdentity()    
    GL.glPushMatrix()
    GL.glTranslatef(dX, dY, dZ)
    GL.glRotatef(a, 0.0, 1.0, 0.0)
    GL.glRotatef(b, 0.0, 0.0, 1.0)
    GL.glBindTexture(GL.GL_TEXTURE_2D, textura[0])
    GL.glBegin(GL.GL_QUADS)
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(-1.0, -1.0,  1.0)
    GL.glTexCoord2f(1/3, 0.0); GL.glVertex3f( 1.0, -1.0,  1.0)
    GL.glTexCoord2f(1/3, 1/2); GL.glVertex3f( 1.0,  1.0,  1.0)
    GL.glTexCoord2f(0.0, 1/2); GL.glVertex3f(-1.0,  1.0,  1.0)
    GL.glTexCoord2f(2/3, 1/2); GL.glVertex3f(-1.0, -1.0, -1.0)
    GL.glTexCoord2f(1.0, 1/2); GL.glVertex3f(-1.0,  1.0, -1.0)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f( 1.0,  1.0, -1.0)
    GL.glTexCoord2f(2/3, 1.0); GL.glVertex3f( 1.0, -1.0, -1.0)
    GL.glTexCoord2f(1/3, 1/2); GL.glVertex3f(-1.0,  1.0, -1.0)
    GL.glTexCoord2f(2/3, 1/2); GL.glVertex3f(-1.0,  1.0,  1.0)
    GL.glTexCoord2f(2/3, 1);   GL.glVertex3f( 1.0,  1.0,  1.0)
    GL.glTexCoord2f(1/3, 1);   GL.glVertex3f( 1.0,  1.0, -1.0)
    GL.glTexCoord2f(1/3, 0.0); GL.glVertex3f(-1.0, -1.0, -1.0)
    GL.glTexCoord2f(2/3, 0.0); GL.glVertex3f( 1.0, -1.0, -1.0)
    GL.glTexCoord2f(2/3, 1/2); GL.glVertex3f( 1.0, -1.0,  1.0)
    GL.glTexCoord2f(1/3, 1/2); GL.glVertex3f(-1.0, -1.0,  1.0)
    GL.glTexCoord2f(0.0, 1/2); GL.glVertex3f( 1.0, -1.0, -1.0)
    GL.glTexCoord2f(1/3, 1/2); GL.glVertex3f( 1.0,  1.0, -1.0)
    GL.glTexCoord2f(1/3, 1.0); GL.glVertex3f( 1.0,  1.0,  1.0)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f( 1.0, -1.0,  1.0) 
    GL.glTexCoord2f(2/3, 0.0); GL.glVertex3f(-1.0, -1.0, -1.0)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f(-1.0, -1.0,  1.0)
    GL.glTexCoord2f(1.0, 1/2); GL.glVertex3f(-1.0,  1.0,  1.0)
    GL.glTexCoord2f(2/3, 1/2); GL.glVertex3f(-1.0,  1.0, -1.0)
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
    alturaTela = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)
    larguraTela = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    alturaJanela = round(2 * larguraTela / 3)
    larguraJanela = round(2 * alturaTela / 3)
    GLUT.glutInitWindowSize(alturaJanela, larguraJanela)
    GLUT.glutInitWindowPosition(round((larguraTela - alturaJanela) / 2), round((alturaTela - larguraJanela) / 2))
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
    GLU.gluPerspective(-45, alturaJanela / larguraJanela, 0.1, 100.0)
    GL.glTranslatef(0.0, 0.0, -10)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()