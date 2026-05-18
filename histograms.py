import matplotlib.pyplot as mb
import numpy as np
#loc = average score
#scale = Standard deviation. Controls spread of values. Small value → numbers stay close to 70 ... Large value → numbers spread farther away.
# size=100 -- Number of random values to generate.

scores=np.random.normal(loc=70,scale=10,size=100)

# Keep / clip scores between 0 and 100
scores=np.clip(scores,0,100)

# bins=10 -- Number of groups/bars. More Numbers of bins increase the graph details. 
mb.hist(scores,bins=10, 
        color="skyblue",
        edgecolor="black")

mb.show()


