import matplotlib.pyplot as mb
import numpy as np

height1 =np.array([150, 155, 160, 165, 170])
weight1 =np.array([45, 50, 55, 60, 68])

height2 =np.array([152, 158, 162, 168, 172]) 
weight2 =np.array([48, 53, 57, 63, 70]) 

mb.title("Height and Weight Analysis")
mb.xlabel("Height")
mb.ylabel("Weight")
# alpha = transparency
# s is the size of the scatter points
# label will identify the points if there is more than one;
# to display them, call the legend() function

mb.scatter(height1,weight1, color="#f029d5",
                          alpha=0.7,
                          s=40, 
                          label="class7")

mb.scatter(height2,weight2, color="#11043E",
                          alpha=0.7,
                          s=40,
                          label="class8")

mb.legend()
mb.show()