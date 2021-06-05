import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi, sqrt

janela = "tronco e piramide iluminados"

a = 0
b = 1
c = 2
raio = 2
vertices = 3
modificador = 1
alturaP = 3
corFundo = (0.154, 0.302, 0.210, 1)

dados = [
    [(0.329412, 0.223529, 0.027451,  1.0),(0.780392, 0.568627, 0.113725, 1.0),(0.992157, 0.941176, 0.807843, 1.0),(27.8974)],         
    [(0.23125,  0.23125,  0.23125,  1.0),(0.2775,  0.2775,  0.2775,  1.0),(0.773911,  0.773911,  0.773911,  1.0),(89.6)],         
    [(0.0215,  0.1745,  0.0215,  0.55),(0.07568,  0.61424,  0.07568,  0.55),(0.633,  0.727811,  0.633,  0.55),(76.8)],               
    [(0.25,  0.20725,  0.20725,  0.922),(1.0,  0.829,  0.829,  0.922),(0.296648,  0.296648,  0.296648,  0.922),(11.264)],         
    [(0.1745,  0.01175,  0.01175,  0.55),(0.61424,  0.04136,  0.04136,  0.55),(0.727811,  0.626959,  0.626959,  0.55),(76.8)],         
    [(0.1,  0.18725,  0.1745,  0.8),(0.396,  0.74151,  0.69102,  0.8),(0.297254,  0.30829,  0.306678,  0.8),(12.8)],                  
    [(0.0, 0.0, 0.0, 1.0),(0.5, 0.5, 0.0, 1.0),(0.60, 0.60, 0.50, 1.0),(32.0)],         
    [(0.02,  0.02,  0.02,  1.0),(0.01,  0.01,  0.01,  1.0),(0.4,  0.4,  0.4,  1.0),(10.0)],         
    [(0.0, 0.05, 0.05, 1.0),(0.4, 0.5, 0.5, 1.0),(0.04, 0.7, 0.7, 1.0),(10.0)],                 
    [(0.05, 0.05, 0.05, 1.0),(0.5, 0.5, 0.5, 1.0),(0.7, 0.7, 0.7, 1.0),(10.0)],
    [(0.05,  0.05,  0.0,  1.0),(0.5,  0.5,  0.4,  1.0),(0.7,  0.7,  0.04,  1.0),(10.0)]
]

def default(v0, v1, v2):
    j = (v2[a]-v0[a], v2[b]-v0[b], v2[c]-v0[c])
    k = (v1[a]-v0[a], v1[b]-v0[b], v1[c]-v0[c])
    l = ((j[b]*k[c]-j[c]*k[b]),(j[c]*k[a]-j[a]*k[c]),(j[a]*k[b]-j[b]*k[a]))
    comprimento = sqrt(l[a]*l[a]+l[b]*l[b]+l[c]*l[c])
    return (l[a]/comprimento, l[b]/comprimento, l[c]/comprimento)

def invertion(v0, v1, v2):
    j = ( v2[a]-v0[a], v2[b]-v0[b], v2[c]-v0[c] )
    k = ( v1[a]-v0[a], v1[b]-v0[b], v1[c]-v0[c] )
    l = ( (j[b]*k[c]-j[c]*k[b]),(j[c]*k[a]-j[a]*k[c]),(j[a]*k[b]-j[b]*k[a]))
    comprimento = sqrt(l[a]*l[a]+l[b]*l[b]+l[c]*l[c])
    return (-l[a]/comprimento, -l[b]/comprimento, -l[c]/comprimento)

def figure():
    GL.glPushMatrix()
    GL.glTranslatef(0.0, -1.0, 0.0)
    GL.glRotatef(-85,1.0,0.0,0.0)
    GL.glBegin(GL.GL_POLYGON)
    angulos = (2*pi)/vertices
    pontos = []
    for i in range(vertices):
        a = raio * cos(i*angulos)
        b = raio * sin(i*angulos)
        pontos += [ (a,b) ]
        GL.glVertex3f(a,b,0.0)
    j = (pontos[0][0], pontos[0][1], 0)
    k = (pontos[1][0], pontos[1][1], 0)
    p = (pontos[2][0], pontos[2][1], 0)
    GL.glNormal3fv(invertion(j,k,p))
    GL.glEnd()
    GL.glBegin(GL.GL_POLYGON)
    for a,b in pontos:
        GL.glVertex3f(modificador*a,modificador*b, alturaP)
    j = (pontos[0][0], pontos[0][1], alturaP)
    k = (pontos[1][0], pontos[1][1], alturaP)
    p = (pontos[2][0], pontos[2][1], alturaP)
    GL.glNormal3fv(default(j,k,p))
    GL.glEnd()
    GL.glBegin(GL.GL_QUADS)
    for i in range(vertices):
        j = (pontos[i][0],pontos[i][1],0)
        k = (modificador*pontos[i][0],modificador*pontos[i][1],alturaP)
        p = (modificador*pontos[(i+1)%vertices][0],modificador*pontos[(i+1)%vertices][1],alturaP)
        q = (pontos[(i+1)%vertices][0],pontos[(i+1)%vertices][1],0)
        GL.glNormal3fv(default(j,k,q))
        GL.glVertex3fv(j)
        GL.glVertex3fv(k)
        GL.glVertex3fv(p)
        GL.glVertex3fv(q)
    GL.glEnd()
    GL.glPopMatrix()

soma = 0
def draw():
    global soma
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glRotatef(2,1,3,0)
    if soma % 100 == 0:
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, dados[(soma+1)%len(dados)][0])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, dados[(soma+1)%len(dados)][1])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, dados[(soma+1)%len(dados)][2])
        GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, dados[(soma+1)%len(dados)][3])
    soma += 1
    figure()
    GLUT.glutSwapBuffers()

def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(30, timer, 1)

def clique(button, state, a, b):
    global modificador
    if button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN:
        if modificador == 1:
            modificador = 0.5
        else:
            modificador = 1
    GLUT.glutPostRedisplay()

def movimento(a, b):
    """
    Template
    """

def reshape(w,h):
    GL.glViewport(0,0,w,h)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GLU.gluPerspective(45, float(w) / float(h), 0.1, 50.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()
    GLU.gluLookAt(10,0,0,0,0,0,0,1,0)

def main():
    light_position = (7, 2, 1)    
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE)
    larguraTela = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    alturaTela = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)
    larguraJanela = round(2 * larguraTela / 3)
    alturaJanela = round(2 * alturaTela / 3)
    GLUT.glutInitWindowSize(larguraJanela, alturaJanela)
    GLUT.glutInitWindowPosition(round((larguraTela - larguraJanela) / 2), round((alturaTela - alturaJanela) / 2))
    GLUT.glutCreateWindow(janela)
    GLUT.glutReshapeFunc(reshape)
    GLUT.glutDisplayFunc(draw)
    GLUT.glutMouseFunc(clique)
    GLUT.glutMotionFunc(movimento)
    GL.glShadeModel(GL.GL_SMOOTH)
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, dados[0][0])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, dados[0][1])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, dados[0][2])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, dados[0][3])
    GL.glEnable(GL.GL_LIGHTING)
    GL.glEnable(GL.GL_LIGHT0)
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, light_position)
    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(*corFundo)
    GLU.gluPerspective(45, larguraJanela / alturaJanela, 0.1, 50.0)
    GLUT.glutTimerFunc(50, timer, 1)
    GLUT.glutMainLoop()

if(__name__ == '__main__'):
    main()