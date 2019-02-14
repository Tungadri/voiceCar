#!/usr/bin/env python3
import numpy as np 
import matplotlib.pyplot as plt 

#This function calculates the normal vector given a line
def norm_vec(AB):
	return np.matmul(omat,np.matmul(AB,dvec))

#These are the assignments required for computing the previous function
dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

# Returns the reflection of P about line AB (:= (N * X = C))
def reflection_normal_form(P, AB):
	N, C = AB
	if(N[1] == 0):		# Checks if slope is infinity
		return(np.array([ 2*C/N[0] - P[0], 
							P[1]  ]))
	m = -1*N[0]/N[1]	# Slope of the line
	intercept = C/N[1]	#Intercept of the line
	return reflection_slope_form(P, m, intercept)

# Returns the reflection of P about line ( := s.t. m = slope & intercept = y-intercept of line )
def reflection_slope_form(P, m, intercept):
	P_temp = [P[0], P[1] - intercept]				# translate (0, 0)-->(0, -intercept)
	Trans = (1/(1+m**2))*np.array([[1-m**2, 2*m], 	# using reflection transform matrix for y = mx
						 		   [2*m, m**2-1]])
	P_ref_temp = np.matmul(Trans, P_temp)
	return [P_ref_temp[0], P_ref_temp[1]+intercept]	# translate back (0, -intercept)-->(0, 0)

#### About Circle representation ##########
# {X.T} represents transpose of X .
# Equation of the circle is of the form  {X.T} * X - 2 * {C.T} * X = r^2 - {C.T} * C 
# Here C is the center and r is the radius.
###########################################
#### About Line representation ############
# Equation of the line is of the form  N * X = C
# Here N is the normal and C is a constant
###########################################


#### Input Section #######
# Circle Parameters A (:= Coeff. of x and y) & D (:= Constant term in eqn.)
A=(-np.array([2,0]))
D=0

# Line Parameters N (:= Normal to the line ) & C (:= Constant term in eqn.)
N = np.array([1, 1])
C = 3
########################

# Finding Center P of the circle and it's radius
cenM=np.array([[-0.5,0],[0,-0.5]])
P=np.matmul(cenM,A.T)
radius=(P[0]**2+P[1]**2-D)**0.5
###############################

line = (N, C)	# Normal Form of the Line

# Finding reflection (:=D) of center about the line
D = reflection_normal_form(P, line)


#Foot of perpendicular of the center to the line
E=(P+D)/2


#The following lines are for drawing the figure

#The following calculates points to draw the line
F=E+(0.1*N)
EF=np.vstack((E,F)).T
EFnorm=norm_vec(EF)
lam_1 = np.linspace(-20,20,10)
x_line=np.zeros((2,10))
for i in range(10):
	temp=E+lam_1[i]*EFnorm
	x_line[:,i]= temp.T

fig,ax=plt.subplots()
circle1=plt.Circle(P,radius,color='r')
circle2=plt.Circle(D,radius,color='g')
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.set_aspect('equal',adjustable='datalim')
ax.plot()
plt.plot(P[0], P[1],'o')
plt.text(P[0]*0.8, P[1]*0.8,'O')
plt.plot(D[0], D[1],'o')
plt.text(D[0]*1.05, D[1]*1.05,'O-Ref')
plt.plot(x_line[0,:],x_line[1,:],label='$EF$')
circlePoint=(P+(radius/2**0.5))
plt.plot([P[0],circlePoint[0]],[P[1],circlePoint[1]],label='$Radius$',color='b')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig('../figs/circles.png')
plt.show()