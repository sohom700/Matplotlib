#Retrive data from a file and Show them as diagrams

import matplotlib.pyplot as mb
import numpy as np
import pandas as pb
mb.figure(figsize=(10,5))
df=pb.read_csv("D:/CODE SPACE/PROGRAMMING/PYTHON/Pandas/Pokemon.csv")
x=df["Type1"].value_counts(ascending=True).to_dict()
mb.title("Type 1 Count Bar chart")
mb.xlabel("Type1 name")
mb.ylabel("Count")
mb.bar(x.keys(),x.values(),
                color="#4ef567",
                edgecolor="#000000")
# mb.grid(color="blue")
mb.tight_layout()

mb.show()


# print(x.values())