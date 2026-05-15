import matplotlib.pyplot as pb
import numpy as np

x=np.array([2021, 2022,2023,2024,2025])
y1=np.array([1, 69, 30, 74, 54])
y2=np.array([10, 20, 37, 44, 14])
y3=np.array([34, 45, 57, 27, 63])

line_style=dict(marker=".",
                markersize=15,
                markerfacecolor="#48dffa",
                markeredgecolor="#000000",
                linestyle="solid",
              # color="#2b27b8",
                linewidth=4)
pb.plot(x,y1, color="red", **line_style)
pb.plot(x,y2, color="black", **line_style)
pb.plot(x,y3,  color="#2b27b8",**line_style)
pb.show()
