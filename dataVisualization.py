import pandas as pd
import matplotlib.pyplot as mpl

df = pd.read_csv("final_data.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

mpl.plot(radius,mass)
mpl.title("Radius & Mass of the Star")
mpl.xlabel("Radius")
mpl.ylabel("Mass")
mpl.show()

mpl.plot(mass,gravity)
mpl.title("Mass & Gravity of the Star")
mpl.xlabel("Mass")
mpl.ylabel("Gravity")
mpl.show()