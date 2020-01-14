# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:19:13 2019

@author: akmal
"""
import numpy as np
import scipy.constants as c
import math

def spherical_to_cartesian(r,theta,phi):
    x=round(r*math.sin(theta)*math.cos(phi),5)
    y=round(r*math.sin(theta)*math.sin(phi),5)
    z=round(r*math.cos(theta),5)
    return x,y,z
	

def cartesian_to_spherical(x, y, z):
    r=round(math.sqrt(z**2+y**2+x**2),5)
    phi=round(math.atan2(y,x),5)
    theta=math.atan2(math.sqrt(x**2+y**2),z)
    theta=round(theta,5)
    return r,theta,phi

#def angular_wave_func(m,l,theta,phi):        BELOW
#    pass

def radial_wave_func(n,l,r):
    a=c.physical_constants['Bohr radius'][0]
    
    if n == 1 and l == 0:
        R = 2*np.exp(-r/a)
    elif n == 2 and l == 0:
        R = (1/np.sqrt(2))*(1-r/(2*a))*np.exp(-r/(2*a))
    elif n == 2 and l == 1:
        R = (1/np.sqrt(24))*(r/a)*np.exp(-r/(2*a))
    elif n == 3 and l == 0:
        R = (2/(81*np.sqrt(3)))*(27-18*(r/a)+2*(r/a)**2)*np.exp(-r/(3*a))
    elif n == 3 and l == 1:
        R = (8/(27*np.sqrt(6)))*(1 - r/(6*a))*(r/a)*np.exp(-r/(3*a))
    elif n == 3 and l == 2:
        R = (4/(81*np.sqrt(30)))*((r/a)**2)*np.exp(-r/(3*a))
    elif n == 4 and l == 0:
        R = (1/4)*(1-(3/4)*(r/a)+(1/8)*((r/a)**2)-(1/192)*((r/a)**3))*np.exp(-r/(4*a))
    elif n == 4 and l == 1:
        R = (np.sqrt(5)/(16*np.sqrt(3)))*(r/a)*(1-(1/4)*(r/a)+(1/80)*((r/a)**2))*np.exp(-r/(4*a))
    elif n == 4 and l == 2:
        R = (1/(64*np.sqrt(5)))*((r/a)**2)*(1-(1/12)*(r/a))*np.exp(-r/(4*a))
    elif n == 4 and l == 3:
        R = (1/(768*np.sqrt(35)))*((r/a)**3)*np.exp(-r/(4*a))

    R = round(R,5)

    return R 

def mgrid3d (xs, xe, xp, ys, ye, yp, zs, ze, zp):
    x_step = ( (xe - xs) / (xp - 1) )
    y_step = ( (ye - ys)/ (yp - 1))
    z_step = ( (ze - zs)/ (zp - 1))
    new = [[],[],[]]
    for i in range(xp):
        new[0].append([])
        new[1].append([])
        new[2].append([])
        for j in range(yp):
            new[0][i].append([])
            new[1][i].append([])
            new[2][i].append([])
            for k in range(zp):
                new[0][i][j].append(xs + (x_step * i))
                new[1][i][j].append(ys + (y_step * j))
                new[2][i][j].append(zs + (z_step * k))    
    return new



def angular_wave_func(m, l, theta, phi):

    i = np.complex(0,1)
    
    if l == 0 and m == 0:
        Y = np.sqrt(1/(4*np.pi))

    
    elif l == 1 and m == 0:
        Y = np.sqrt(3/(4*np.pi))*np.cos(theta)

    
    elif l == 1 and m == 1:
        Y = -np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(i*phi)

    
    elif l == 1 and m == -1:
        Y = np.sqrt(3 / (8 * np.pi)) * np.sin(theta) * np.exp(-i * phi)

    
    elif l == 2 and m == 0:
        Y = np.sqrt(5 / (16 * np.pi)) * (3*np.cos(theta)**2-1)

    
    elif l == 2 and m == 1:
        Y = -np.sqrt(15 / (8 * np.pi)) * (np.cos(theta)*np.sin(theta)*np.exp(i*phi))

    
    elif l == 2 and m == -1:
        Y = np.sqrt(15 / (8 * np.pi)) * (np.cos(theta)*np.sin(theta)*np.exp(-i*phi))

    
    elif l == 2 and m == 2:
        Y = np.sqrt(15 / (32 * np.pi)) * (np.sin(theta)**2*np.exp(i*2*phi))

    
    elif l == 2 and m == -2:
        Y = np.sqrt(15 / (32 * np.pi)) * (np.sin(theta)**2*np.exp(-i*2*phi))

    
    elif l == 3 and m == 0:
        Y = np.sqrt(7/(16*np.pi))*(5*np.cos(theta)**3-3*np.cos(theta))

    
    elif l == 3 and m == 1:
        Y = -np.sqrt(21 / (64 * np.pi)) * (np.sin(theta)*np.exp(i*phi)*(5*np.cos(theta)**2-1))

    
    elif l == 3 and m == -1:
        Y = np.sqrt(21 / (64 * np.pi)) * (np.sin(theta)*np.exp(-i*phi)*(5*np.cos(theta)**2-1))

    
    elif l == 3 and m == 2:
        Y = np.sqrt(105 / (32 * np.pi)) * (np.sin(theta)**2*np.exp(i*2*phi)*(np.cos(theta)))

    
    elif l == 3 and m == -2:
        Y = np.sqrt(105 / (32 * np.pi)) * (np.sin(theta)**2*np.exp(-i*2*phi)*(np.cos(theta)))

    
    elif l == 3 and m == 3:
        Y = -np.sqrt(35 / (64 * np.pi)) * (np.sin(theta)**3*np.exp(i*3*phi))

    
    elif l == 3 and m == -3:
        Y = np.sqrt(35 / (64 * np.pi)) * (np.sin(theta)**3*np.exp(-i*3*phi))

    
    else:
        print("Error: Out of range")
        return None

    Y = round(Y, 5)
    Y = np.complex(Y)

    return Y

s2c= np.vectorize(spherical_to_cartesian)
c2s = np.vectorize(cartesian_to_spherical)
rwf = np.vectorize(radial_wave_func)
m3d= np.vectorize(mgrid3d)
awf = np.vectorize(angular_wave_func)
vround = np.vectorize(round)


def mag(c):
    vabs = np.vectorize(np.absolute)
    magnitude = vabs(c)
    return magnitude
vecmag = np.vectorize(mag)

def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    a=c.physical_constants['Bohr radius'][0]
    xx,yy,zz=np.array(m3d(-roa,roa,Nx,-roa,roa,Ny,-roa,roa,Nz))
    r,theta,phi=c2s(xx,yy,zz)
    
    
    R = rwf(n,l,r)
    r *= a
    y0 = awf(0, l, theta, phi)
    y1 = awf(m, l, theta, phi)
    y2 = awf(-m, l, theta, phi)
    if m < 0:
        ylm = (1j/math.sqrt(2))*(y1-((-1)**m)*y2)
    elif m == 0:
        ylm = y0
    elif m > 0:
        ylm = (1/math.sqrt(2))*(y2+((-1)**m)*y1)
    psi = R*ylm
    
    return vround(xx,5),vround(yy,5),vround(zz,5),vecmag(psi) 

print('Test 1')
x,y,z,mag = hydrogen_wave_func(2 ,1 ,1 ,8 ,2 ,2 ,2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('\n')
print('Test 2')
x,y,z,mag = hydrogen_wave_func(2 ,1 ,1 ,5 ,3 ,4 ,2)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)

print('\n')
print('Test 3')
x,y,z,mag = hydrogen_wave_func(2 ,0 ,0 ,3 ,5 ,4 ,3)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)