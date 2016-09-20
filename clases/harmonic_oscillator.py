"""Damped Simple Harmonic Oscillator"""
from scipy.integrate import odeint
from pylab import * # for plotting commands

def deriv(x,t): # return derivatives of the array x
	m = 1 # Mass in kg
	k = 100 #Spring constant in N/m
	b = 1 #ddamping constant in Ns/m
	return aray([ x[1],-(k/m)*x[0]-(b/m)*x[1] ])

time = linspace(0.0,5.0,1000)
xinit = array([1.0,0.0]) # initial values
x = odeint(deriv,xinit,time)

figure()
plot(time,x[:,0], 'r-') #x[:,0] is the first column of x
xlabel('t')
ylabel('x')
show()
