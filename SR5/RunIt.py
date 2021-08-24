#Universidad del Valle de Guatemala
#Graficas por Computadora
#Laboratorio SR4
#Diego Crespo 19541
from Engine import Renderer, V3, _color
from shaders import *
from obj import Texture

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.active_texture = Texture('model_normal.bmp')
rend.normal_map = Texture('model_normal.bmp')



#DUTCH Angle
rend.active_shader = normalMap
rend.glLoadModel("model.obj",
               translate = V3(3, 0, -10),
               rotate=V3(55,-55,55),
               scale = V3(3,3,3)) 
   
                 
#HIGH ANGLE
#rend.active_shader = normalMap
#rend.glLoadModel("model.obj",
 #                translate = V3(3, 0, -10),
  #               rotate=V3(55,0,0),
   #              scale = V3(3,3,3))


#LOW ANGLE
#rend.active_shader = normalMap
#rend.glLoadModel("model.obj",
#                translate = V3(3, 0, -10),
 #               rotate=V3(-55,-0,0),
  #              scale = V3(3,3,3))



#MEDIUM ANGLE
#rend.active_shader = normalMap
#rend.glLoadModel("model.obj",
#               translate = V3(3, 0, -10),
#              scale = V3(3,3,3))

#rend.glFinish("salida.bmp")



