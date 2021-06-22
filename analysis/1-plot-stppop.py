from pathlib import Path
import pandas as pd

data = pd.read_csv("output/cohorts/input_1_stppop.csv")

fig = data.stp.plot.hist().get_figure()

Path("output/plots/plot_stppop_bar.png").mkdir(parents=True, exists="ok")

fig.savefig("output/plots/plot_stppop_bar.png")