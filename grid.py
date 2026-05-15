import matplotlib.pyplot as pb
import numpy as np

x=np.array([2021, 2022,2023,2024,2025])
y=np.array([34, 45, 57, 27, 63])

pb.grid(axis="both", linewidth=2,linestyle="dashed",color="purple")
pb.plot(x,y)

pb.show()
