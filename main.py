GlowScript 3.0 VPython

ground=box(pos=vector(0,0,0),size=vector(1200,2,2),color=color.green)
ball=sphere(pos=vector(-5,1.4,1),radius=.1, color=color.cyan, make_trail=True)
r0=ball.pos
g=vector(0,-9.8,0) 
g_value= -9.8
ball.m=0.2
v0= 100
angle = 80
theta=80*pi/180
ball.p=ball.m*v0*vector(cos(theta),sin(theta),0)
max_height = v0^2/(2*g_value)

#                                   Script Author: Abdul Basit Tonmoy                                       

t=0
dt=0.001

while ball.pos.y>=0.1:
  rate(8000)
  Fnet=ball.m*g
  ball.p=ball.p+Fnet*dt
  ball.pos=ball.pos+ball.p*dt/ball.m
  t=t+dt
  
displacement = (v0^2*2*sin(angle)*cos(angle))/g_value

print("dr final = ",ball.pos-r0," m")
print("t final = ",t," s")
print("Max Height = ", max_height, " m")
print("Displacement = ", displacement, " m")
