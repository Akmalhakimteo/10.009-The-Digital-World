# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:07:55 2019

@author: akmal
"""
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

#%%
def mgrid2d (xs, xe, xp, ys, ye, yp):
    x_step = ( (xe - xs) / (xp - 1) )
    y_step = ( (ye - ys) / (yp - 1) )
    new = [[],[]]
    for i in range (xp):
        new[0].append ([])
        new[1].append ([])
        for j in range (yp):
            new[0][i].append (xs + (x_step * i))
            new[1][i].append (ys + (y_step * j))
    return new
