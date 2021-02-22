import math
import matplotlib.pyplot as plt

v_0 = 80.5 # in m/s
theta = (90-37.4109) # in degrees
g = -9.8 # in m/s^2
m = 0.04593 # in Kg
C = 4E-4 # in Kg/m
w = 7.27E-5 # in rad/s
l = 37.4109 # in degrees

x = 0.0 # in m
y = 0.0 # in m
z = 0.0 # in m
y_max = 0.0 # in m
t = 0.0 # in s
dt = 2E-6

def acceleration(v_x, v_y, v_z, C, m):
    a_x = -C*v_x*math.sqrt(v_x*v_x + v_y*v_y)/m
    a_y = g - C*v_y*math.sqrt(v_x*v_x + v_y*v_y)/m
    a_z = -C*v_z*math.sqrt(v_z*v_z + v_y*v_y)/m
    return a_x, a_y, a_z

def update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    z = z + v_z*dt + 0.5*a_z*dt*dt
    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    v_z = v_z + a_z*dt
    return x, y, z, v_x, v_y, v_z

v_x = v_0*math.cos(theta*math.pi/180.0)
v_y = v_0*math.sin(theta*math.pi/180.0)
v_z = 0.0

outFile = open("MorrillProjectileData.txt", "w")

inFlight = True

while(inFlight):
    a_x, a_y, a_z = acceleration(v_x, v_y, v_z, C, m)
    x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt)
    t += dt
    if(y>= 0):
        outFile.write(str(t) + " " + str(x) + " " + str(y) + " " + str(z) + " " + str(v_x) +" " + str(v_y) + " " + str(v_z) + " " + str(a_x) + " " + str(a_y) + " " + str(a_z) + "\n")
        if(y > y_max):
            y_max = y
    else:
            inFlight = False

outFile.close()

print("Max Height: ", y_max)
print("Horizontal Range: ", x)

X = []
Y = []
Z = []

inFile = open("MorrillProjectileData.txt", "r")
for line in inFile:
    t, x, y, z, v_x, v_y, v_z, a_x, a_y, a_z = line.split(" ")
    X.append(float(x))
    Y.append(float(y))
    Z.append(float(z))
inFile.close()

plt.xlabel("$x$ (m)")
plt.ylabel("$y$ (m)")
plt.plot(X, Y)
plt.show()

plt.xlabel("$x$ (m)")
plt.ylabel("$z$ (m)")
plt.plot(X, Z)
plt.show()