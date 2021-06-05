import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from png import Reader
from sys import argv
from math import sin, cos, pi

janela = "piramide textura"

a = 90.0
b = 0
da = 0.5
vertices = 3
raio = 2
alturaP = 3
modificador = 0.5
corFundo = (0.264, 0.478, 0.825, 1)

textura = []

def load():
    global textura
    textura = GL.glGenTextures(2)
    imagem = Reader(filename='C:\\Users\\Pedro\\Desktop\\computacao grafica\\trabalhos cg 2021.1\\9 - piramide textura\\piramidemodelo.png')
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
    GL.glTranslatef(0.0, 1.5, -10)
    GL.glRotatef(90,1.0,0.0,0.0)
    GL.glRotatef(a, 0.0, 0.0, 1.0)
    GL.glRotatef(b, 0.0, 1.0, 0.0)
    GL.glBindTexture(GL.GL_TEXTURE_2D, textura[0])
    GL.glBegin(GL.GL_POLYGON)
    pontos = []
    angulos = (2*pi)/vertices
    for i in range(vertices):
        x = raio * cos(i*angulos)
        y = raio * sin(i*angulos)
        pontos += [ (x,y) ]
        GL.glTexCoord2f(x, y); GL.glVertex3f(x,y,0.0)
    GL.glEnd()
    GL.glBegin(GL.GL_POLYGON)
    for x,y in pontos:
        GL.glTexCoord2f(x, y); GL.glVertex3f(modificador*x,modificador*y, alturaP)
    GL.glEnd()
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(pontos[i][0],pontos[i][1],0)
        GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f(modificador*pontos[i][0],modificador*pontos[i][1],alturaP)
        GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f(modificador*pontos[(i+1)%vertices][0],modificador*pontos[(i+1)%vertices][1],alturaP)
        GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f(pontos[(i+1)%vertices][0],pontos[(i+1)%vertices][1],0)
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
    GLUT.glutTimerFunc(30, timer, 1)

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
    GLUT.glutTimerFunc(50, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()