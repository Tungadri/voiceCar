#!/usr/bin/env python3
#This program finds the reflection of a circle about a line
import numpy as np
#import numpy library as np
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

#This function calculates the normal vector given a line
def norm_vec(AB):
	return np.matmul(omat,np.matmul(AB,dvec))

#These are the assignments required for computing the previous function
dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

#This function calculates the mid point of two given points
def mid_pt(B,C):
	D = (B+C)/2
	return D

#This function creates a line from normal form
def line_intersect_normal_form(N,P):
	return np.matmul(np.linalg.inv(N),P)

#This function finds the reflection of a point about a line from  normal form of the line
def reflection_normal_form(n1,p1,A):
	B=A+(0.1*n1)
	AB=np.vstack((A,B)).T
	n2=norm_vec(AB)
	p2=np.matmul(n2,A.T)
	N=np.vstack((n1,n2))
	P=np.vstack((p1,p2))
	F=line_intersect_normal_form(N,P)
	F.shape=(2)
	return((2*F)-A)


#### About Circle representation ##########
# {X.T} represents transpose of X .
# Equation of the circle is of the form  {X.T} * X - 2 * {C.T} * X = r^2 - {C.T} * C 
# Here C is the center and r is the radius.
###########################################
#### About Line representation ############
# Equation of the line is of the form  B * X = C
# Here B is the normal and C is a constant
###########################################

#### Input Section #######
# Circle Parameters A (:= Coeff. of x and y) & D (:= Constant term in eqn.)
A=(-np.array([2,0]))
D=0

# Line Parameters B (:= Normal to the line ) & C (:= Constant term in eqn.)
B = np.array([1, 1])
C = 3
########################

#This matrix when multiplied with the coefficients give the centre of the circle
cenM=np.array([[-0.5,0],[0,-0.5]])

#This is the centre of the circle
cen=np.matmul(cenM,A.T)

#This is the reflected centre
refCen=reflection_normal_form(B,C,cen)


#This is the radius of the circle
radius=(cen[0]**2+cen[1]**2-D)**0.5

#Foot of perpendicular of the center to the line
E=(cen+refCen)/2

#The following calculates points to make the line
F=E+(0.1*B)
EF=np.vstack((E,F)).T
EFnorm=norm_vec(EF)
lam_1 = np.linspace(-20,20,10)
x_line=np.zeros((2,10))
for i in range(10):
	temp=E+lam_1[i]*EFnorm
	x_line[:,i]= temp.T

#The following lines are for drawing the figure
fig,ax=plt.subplots()
circle1=plt.Circle(cen,radius,color='r')
circle2=plt.Circle(refCen,radius,color='g')
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.set_aspect('equal',adjustable='datalim')
ax.plot()
plt.plot(cen[0], cen[1],'o')
plt.text(cen[0]*0.8, cen[1]*0.8,'O')
plt.plot(refCen[0], refCen[1],'o')
plt.text(refCen[0]*1.05, refCen[1]*1.05,'O-Ref')
plt.plot(x_line[0,:],x_line[1,:],label='$EF$')
circlePoint=(cen+(radius/2**0.5))
plt.plot([cen[0],circlePoint[0]],[cen[1],circlePoint[1]],label='$Radius$',color='b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig('../figs/circles.png')
plt.show()

