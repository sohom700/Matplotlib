import matplotlib.pyplot as mb
import numpy as np
#linespace = (start,endpoint,total needed values)
x=np.linspace(-10,10,100)
custom_plot_color={"color": "#29f05a"}
custom_axcolor={"color": "#fc26d5"}
fig, axes =mb.subplots(2,2,figsize=(10,8))

#y=kx
axes[0,0].plot(x,2*x,**custom_plot_color)
axes[0,0].set_title("y=kx")
axes[0,0].axvline(0,**custom_axcolor)
axes[0,0].axhline(0,**custom_axcolor)


#y=k/x
x_nonzero=x[x!=0]
axes[0,1].plot(x_nonzero,2/x_nonzero,**custom_plot_color)
axes[0,1].set_title("y=k/x")
axes[0,1].axvline(0,**custom_axcolor)
axes[0,1].axhline(0,**custom_axcolor)

 
#y=x²
axes[1,0].plot(x,x**2,**custom_plot_color)
axes[1,0].set_title("y=x²")
axes[1,0].axvline(0,**custom_axcolor)
axes[1,0].axhline(0,**custom_axcolor)


#y=√x
x_positive=np.linspace(0,10,100)
axes[1,1].plot(x_positive,np.sqrt(x_positive),**custom_plot_color)
axes[1,1].set_title("y=√x")
axes[1,1].axvline(0,**custom_axcolor)
axes[1,1].axhline(0,**custom_axcolor)

mb.tight_layout()
mb.show()

