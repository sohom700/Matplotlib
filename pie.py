import matplotlib.pyplot as mb
import numpy as np
games=np.array(["Cricket", "Football", "Chess", "Badminton"])
players=np.array([65, 28, 21, 10])

# autopct will automatically display the percentage value on each slice of the pie chart.
# explode moves a slice slightly outward from the pie chart for better visualization.
# shadow adds a shadow effect behind the pie chart slices.
# startangle rotates the starting position of the pie chart by the specified degree value. 


mb.pie(players, labels=games,
       autopct="%1.1f%%",
       explode=[0.1, 0, 0, 0 ],
       shadow=True,
       startangle=90)

mb.show()
