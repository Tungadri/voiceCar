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

#This fucntion finds the reflection of a point about a line from  normal form of the line
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


#Now we have to find the reflection of the circle
#(x^2)+(y^2)-2x=0 about the line
#x+y=3

#matrix having the coefficients for the line
#We need two points to represent the line
#we have the equation of line as
#(1 1)x=3
#this can be written in the form
#(1 1)(x - C)=0
# where C is a point on the line
#So, B is the normal of the lnb.ine
B=np.array([1,1])

#matrix having the coefficients for the 1-degree terms
A=(-np.array([2,0]))

#This matrix when multiplied with the coefficients give the centre of the circle
cenM=np.array([[-0.5,0],[0,-0.5]])

#This is the centre of the circle
cen=np.matmul(cenM,A.T)

#This is the constant of the line
C=3

#This is the reflected centre
refCen=reflection_normal_form(B,C,cen)

#This is the constant term for the circle
D=0

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
plt.show()
