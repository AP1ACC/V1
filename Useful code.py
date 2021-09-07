#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c
import sympy as sy
from sympy import *


# In[2]:


# Funktionen
def std(am, werte):
    summen_der_quadrate = 0
    for wert in werte:
        summen_der_quadrate+=(wert-am)**2       
    return np.sqrt(summen_der_quadrate/(werte.size-1))

def stu(std, werte):
    return std/np.sqrt(werte.size)


# In[ ]:


# Standard plotting
fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(x_1, y_1, color='r', label='Datenpunkte Gruppe 1')
ax.scatter(x_2, y_2, color='b', label='Datenpunkte Gruppe 2')

ax.errorbar(am_1_x, am_1_y, xerr=std_1_x, yerr=std_1_y, fmt='D', color='#d0740b', label='AM-STD Gruppe 1')
ax.errorbar(am_2_x, am_2_y, xerr=std_2_x, yerr=std_2_y, fmt='D', color='#150891', label='AM-STD Gruppe 2')

ax.set(xlabel='Größe a in mm', ylabel='Größe b in mm',
       title='Blattgrößen mit AMs und SDs')
ax.legend()
ax.grid()

#fig.savefig("test.png")
plt.show()


# In[ ]:


# Erinnerungen
# x = np.array([,])
# x.size
# x, y = symbols('x y')
# expr = x*y
# expr.subs([(x, wert_x), (y, wert_y)])

