import matplotlib.pyplot as mb
import numpy as np
games=np.array(["Cricket", "Football", "Chess", "Badminton"])
players=np.array([65, 28, 21, 10])

#autopct = Auto Percentage 
#explode function will move the protion from the pie according to the value for better understanding.
#shadow will add shadow to each slice 
#startangle will move the angle of the pie according to the inputed degree value. 


mb.pie(players, labels=games,
       autopct="%1.1f%%",
       explode=[0.1, 0, 0, 0 ],
       shadow=True,
       startangle=90)

mb.show()
