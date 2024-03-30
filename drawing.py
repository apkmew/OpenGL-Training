from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myInit():
    '''
        This function is used for Initial Display and others
        Input: -
        Output: -
    '''
    glClearColor( 1.0, 1.0, 0.0, 1.0 ) 
    glColor3f( 0.2, 0.5, 0.4 )
    glPointSize( 10.0 )
    gluOrtho2D( 0, 500, 0, 500 )

def drawSquare():
    '''
        This function is used for draw square on display
        Input: -
        Output: Square 200 x 200
    '''
    glBegin( GL_QUADS ) 
    glVertex2f( 100.0, 100.0 ) 
    glVertex2f( 300.0, 100.0 ) 
    glVertex2f( 300.0, 200.0 ) 
    glVertex2f( 100.0, 200.0 ) 
    glEnd()

def drawTriangle():
    '''
        This function is used for draw triangle
        Input: -
        Output: Triangle
    '''
    glBegin( GL_TRIANGLE_STRIP ) 
    glVertex2f( 300.0, 210.0 ) 
    glVertex2f( 100.0, 210.0 ) 
    glVertex2f( 300.0, 310.0 ) 
    glEnd()

def main():
    # Initial Display   
    glutInit()
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )   
    glutInitWindowSize( 500, 500 )  
    glutInitWindowPosition( 100, 100 )  
    glutCreateWindow( "My OpenGL Code" )
    myInit()

    # Drawing
    glClear( GL_COLOR_BUFFER_BIT )
    drawSquare()
    drawTriangle()
    glFlush()

    glutMainLoop()

if __name__ == '__main__':
    main()