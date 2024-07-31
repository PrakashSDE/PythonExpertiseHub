import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("D:/Beezlabs/Python/pandas/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.plot()
plt.show()

air_quality["station_paris"].plot()
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

air_quality.plot.box()
plt.show()

air_quality.plot.area()
plt.show()

air_quality.plot.bar()
plt.show()

air_quality.plot.barh()
plt.show()

air_quality.plot.hexbin(x="station_london", y="station_paris", gridsize=30)
plt.show()

air_quality.plot.pie(y="station_paris", autopct='%1.1f%%')
plt.show()