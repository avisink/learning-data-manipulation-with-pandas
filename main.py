# Import the course packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the four datasets
avocado = pd.read_csv("datasets/avocado.csv")
homelessness = pd.read_csv("datasets/homelessness.csv")
temperatures = pd.read_csv("datasets/temperatures.csv")
walmart = pd.read_csv("datasets/walmart.csv")


hl = pd.read_csv("datasets/homelessness.csv")
head_0 = hl.head()
print(head_0)
hl_rg = hl.sort_values("region")
print(hl_rg.head())