import matplotlib.pyplot as pb
import numpy as np

x=np.array([1, 2, 3, 4, 5])
y=np.array([12,40,64,28,10])

line_style=dict(marker=".",
                markersize=15,
                markerfacecolor="#48dffa",
                markeredgecolor="#000000",
                linestyle="solid",
                color="#2b27b8",
                linewidth=4)
pb.title("Sample Plot", fontsize=25, 
                        family="Arial",
                        color="#d732ed",
                        fontweight="bold",
                        fontstyle="oblique")

pb.xlabel("X axis")
pb.ylabel("Y axis")

pb.xticks(x)
pb.tick_params(axis="x",colors="#47cc1e", labelsize=15)


pb.plot(x,y, **line_style)
pb.show()