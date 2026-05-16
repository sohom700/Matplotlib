import matplotlib.pyplot as mb
import numpy as np

x=np.array(["Laptop", "Phone", "Tablet", "Watch"])
y=np.array([50, 120, 70, 90])

mb.title("User bar")
mb.xlabel("products")
mb.ylabel("quantity")


mb.bar(x,y,color="#3ef06e")

#Horizontal Bar charts 
# mb.barh(x,y,color="#3ef06e")
mb.show()