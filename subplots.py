import matplotlib.pyplot as mb
import numpy as np
#linespace = (start,endpoint,total needed values)
x=np.linspace(-10,10,100)

fig, axes =mb.subplots(2,2)
#y=kx
axes[0,0].plot(x,2*x)
axes[0,0].set_title("y=kx")

#y=k/x
x_nonzero=x[x!=0]
axes[0,1].plot(x_nonzero,2/x_nonzero)
axes[0,1].set_title("y=k/x")
 
#y=x²
axes[1,0].plot(x,x**2)
axes[1,0].set_title("y=x²")

#y=√x
x_positive=np.linspace(0,10,100)
axes[1,1].plot(x,np.sqrt(x))
axes[1,1].set_title("y=√x")

mb.tight_layout()
mb.show()

