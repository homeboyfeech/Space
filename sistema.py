from vpython import sphere, vector, color, rotate
import math

#константы
G = 6.667e-11 #гравитационная постоянная,м^3 кг^-1 с^2
MS = 1.9885e30  # масса Солнца, кг
ME = 5.97e24  # масса Земли, кг
Mm = 3.33e23 # масса Меркурия,кг
MY = 1.89e27 # масса Юпитера, кг
MN = 1.02e26 # масса Нептуна, кг
Ms = 5.68E26 # масса Сатурна
MU = 8917 # масса Урана
MM = 6.42e24 # масса Марса, кг
MV = 4.87e24 # масса Венеры, кг
RSV = 1.08E11 #среднее растояние от Солнца до Венеры, метры 
RSM = 2.28e11 #среднее растояние от Солнца до Марса, метры 
RSE = 1.496e11  # среднее расстояние от Солнца до Земли, метры
RSm = 0.58e11 # среднее расстояние от Солнца до Меркурия, метры
RSY = 7.8e11 #  среднее расстояние от Солнца до Юпитера, метры
RSN = 4.55e12 #  среднее расстояние от Солнца до Нетуна, метры
RSU = 2.8E12 # среднее расстояние от Солнца до Урана, метры
RSs = 1.42E12 # среднее расстояние от Солнца до Сатурана, метры


# Гравитационная сила между Солнцем и Ураном, Н
F_SU = G*MS*MU/(RSU*RSU)
# Гравитационная сила между Солнцем и Сатураном, Н
F_Ss = G*MS*Ms/(RSs*RSs)
# Гравитационная сила между Солнцем и Юпитером, Н
F_SY = G*MS*MY/(RSY*RSY)
# Гравитационная сила между Солнцем и Нептуном, Н
F_SN = G*MS*MN/(RSN*RSN)
# Гравитационная сила между Солнцем и Меркурием, Н
F_Sm = G*MS*Mm/(RSm*RSm)
# Гравитационная сила между Солнцем и Землей, Н
F_SE = G*MS*ME/(RSE*RSE)
# Гравитационная сила между Солнцем и Марсом, Н
F_SM = G*MS*MM/(RSM*RSM)
# Гравитационная сила между Солнцем и Венерой, Н
F_SV = G*MS*MV/(RSV*RSV)


# Угловая скорость Юпитера
wy = 10*math.sqrt(F_SY/(MY*RSY))
# Угловая скорость Нептуна
wn = 10*math.sqrt(F_SN/(MN*RSN))
# Угловая скорость Урана
wu = 10*math.sqrt(F_SU/(MU*RSU))
# Угловая скорость Сатурана
wS = 10*math.sqrt(F_Ss/(Ms*RSs))
# Угловая скорость Меркурия
wM = 10*math.sqrt(F_Sm/(Mm*RSm))
# Угловая скорость Земли
we = 10*math.sqrt(F_SE/(ME*RSE))
# Угловая скорость Марса
wm = 10*math.sqrt(F_SM/(MM*RSM))
# Угловая скорость Венеры
wv = 10*math.sqrt(F_SV/(MV*RSV))



v = vector(0.5, 0, 0)
Ypiter = sphere(pos=vector(6,0,0), color=color.white,radius=.40, make_trail=True)
Uran = sphere(pos=vector(8,0,0), color=color.blue,radius=.20, make_trail=True)
saturn = sphere(pos=vector(7,0,0), color=color.red,radius=.35, make_trail=True)
Neptun = sphere(pos=vector(9,0,0), color=color.blue,radius=.19, make_trail=True)
Merkury = sphere(pos=vector(2,0,0), color=color.orange,radius=.18, make_trail=True)
Venera = sphere(pos=vector(3,0,0), color=color.white,radius=.23, make_trail=True)
Mars = sphere(pos=vector(5,0,0), color=color.red,radius=.25, make_trail=True)
Eearth = sphere(pos=vector(4, 0, 0), color=color.blue, radius=.25, make_trail=True)
Sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=1)
# Будем использовать полярные координаты
# Шаг
dt = 10
# углы поворота за один шаг:
theta_earth = we*dt
theta_ypiter = wy*dt
theta_neptun = wn*dt
theta_uran = wu*dt
theta_saturn = wS*dt
theta_merkury = wM*dt
theta_mars = wm*dt
theta_venera = wv*dt
while dt <= 86400*365:
 # Земля и Луна поворачиваются вокруг оси z (0,0,1)
	Ypiter.pos = rotate(Ypiter.pos, angle=theta_ypiter)
	Neptun.pos = rotate(Neptun.pos, angle=theta_neptun)
	Uran.pos = rotate(Uran.pos, angle=theta_uran)
	saturn.pos = rotate(saturn.pos, angle=theta_saturn)
	Merkury.pos = rotate(Merkury.pos, angle=theta_merkury)
	Mars.pos = rotate(Mars.pos, angle=theta_mars)
	Venera.pos = rotate(Venera.pos, angle=theta_venera) 
	Eearth.pos = rotate(Eearth.pos, angle=theta_earth,)
	
	
