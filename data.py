import pandas as pd

# load in file
data = pd.read_csv("Resources/cities.csv")

df = pd.DataFrame(data)

df.to_html("df.html")

