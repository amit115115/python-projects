import math
import pyttsx3 as pr
from wasabi2d import Scene, run, event
from random import uniform as fraction
from random import randint as integer
from random import choice

engine = pr.init()

scene = Scene(1300,700)
scene.background = 'black'

screen = scene.layers[0]
screen.set_effect('bloom', radius=50, intensity=0.9)

items = []
words = [ 'Happy Diwali ']

W = scene.width
H = scene.height

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

@event
def on_mouse_move(pos, rel):
    dx, dy = rel
    r = math.sqrt( (dx**2)+(dy**2) )
    pos=(integer(0, W), integer(0, H))
    
    c = screen.add_circle( radius=r, pos=pos, color=random_color() )
    items.append(c)

    l = screen.add_label(choice(words), align='center', fontsize=integer(0, 144), color=random_color(), pos=(integer(0, W), integer(0, H)) )
    items.append(l)

    

@event
def update(dt):
    all_items = items[:]
    items[:] = [ i for i in items if i.scale > 0.1 ]
    for i in all_items:
        if i not in items:
            i.delete()
    for item in items:
        item.scale = item.scale * 0.9 # shrink
        item.y = item.y * 1.09 # fall
        item.x = item.x + integer(-3, 3) # jitter
    
def random_color():
    return ( fraction(0,1), fraction(0,1), fraction(0,1), fraction(0,1) )

speak('happy diwali')
run()
