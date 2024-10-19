import pgzrun

WIDTH=700
HEIGHT=700

TITLE='my world'
box1=Rect((450,250) ,(40,41))
def draw():
    screen.clear()
    screen.fill('orange')
    screen.draw.line((150,150), (550,150), ('blue'))
    screen.draw.line((550,150), (550,550), ('blue'))
    screen.draw.line((550,550), (150,550), ('blue'))
    screen.draw.line((150,550), (150,150), ('blue'))
    screen.draw.filled_circle((350,350) ,80,'green')
    screen.draw.filled_rect(box1, 'green')
    screen.draw.text('Hello ',(200,450),)


def update():
    box1.x+=2
    if box1.x>WIDTH:
        box1.x=0
        













pgzrun.go()
