import spiceypy as spice
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# print out the toolkit version installed

def test():
	print("which kernels would you like to load?")
	
	meta=input()
	KERNELS_TO_LOAD=('meta.tm')
	print(spice.tkvrsn('TOOLKIT'))
	#help(spice.furnsh)
	spice.furnsh(KERNELS_TO_LOAD)
	print("Load successful")
	print("Enter time:")
	time=input()
	et=spice.str2et( time )
	#et=spice.str2et( '2012-12-03T12:23:52' )
	#help(spice.spkcpo)
	target0 = 'DAWN'
	frame0  = 'DAWN_SPACECRAFT'
	corrtn0 = 'NONE'
	observ0 = 'DAWN'
	state0=[6]
	state0, ltime0 = spice.spkezr(target0, et, frame0,corrtn0, observ0)
	print("target:"+target0)
	print("positions:"+"\nx: "+str(state0[0]))
	print("y: "+str(state0[1]))
	print("z: "+str(state0[2]))
	target1 = 'VESTA'
	frame1  = 'DAWN_SPACECRAFT'
	corrtn1 = 'NONE'
	observ1 = 'DAWN'
	state1, ltime1 = spice.spkezr(target1, et, frame1,corrtn1, observ1)
	print("target:"+target1)
	print("positions:"+"\nx: "+str(state1[0]))
	print("y: "+str(state1[1]))
	print("z: "+str(state1[2]))

	mat=spice.pxform('DAWN_SPACECRAFT','IAU_VESTA',et)
	print("orientation")
	print(mat)
	fig = plt.figure(figsize=(9, 9))
	ax  = fig.add_subplot(111, projection='3d')
	ax.text(state0[0], state0[1], state0[2], target0 )
	ax.text(state1[0], state1[1], state1[2], target1)
	ax.set_xlabel('X axis')
	ax.set_ylabel('Y axis')
	ax.set_zlabel('Z axis')
	plt.show()
def interval():
	print("which kernels would you like to load?")
	
	meta=input()
	KERNELS_TO_LOAD=('meta.tm')
	print(spice.tkvrsn('TOOLKIT'))
	#help(spice.furnsh)
	spice.furnsh(KERNELS_TO_LOAD)
	print("Load successful")

	pass
# Demo 3: text2D
# Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
	#ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)
	#ax.plot(state0[0], state0[1], state0[2])
	#ax.set_xlim(0, -200000000)
	#ax.set_ylim(0,-200000000)
	#ax.set_zlim(0,-200000000)
	
	
	
	#[pos, ltime] = spice.spkpos( 'DAWN_SPACECRAFT', et,'J2000','NONE','EARTH' )
	#spice.getfov()

	#print(pos)
#spiceypy.str2et("2012-12-03 12:23:52")

def driver():
	print("What action would you like to perform?")
	action1=input()
	#print(action1)
	if action1=="POINT":
		test()
	elif action1=="EXIT":
		exit()
	pass
driver()
