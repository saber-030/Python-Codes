# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:08:38 2020

@author: neel
"""
"""
Program to view 3 normal distribution in the same plot,
using matplotlib, numpy, scipy and math libraries,
view label, style and legend
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

#First graph in blue
mu = 0
variance = 5
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma),label="μ = 0, σ^2 = 5")

#Second graph in red
mu = 4
variance = 0.2
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma),label="μ = 4, σ^2= 0.2")

#Third graph in orange
mu = -3.5
variance = 0.05
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma),label="μ = -3.5, σ^2 = 0.05")
#Legend placement
plt.legend(loc="upper right")
#Style
plt.style.use('fivethirtyeight')

plt.show()

