import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
py.sign_in("lasernite", "tf3nfp5vwu")
# Get lowest_fifth, second_fifth, third_fifth, fourth_fifth, top_fifth, top_twentieth, years
from income_demographics_data import *


# create our stacked data manually
y0 = lowest_fifth
y1 = second_fifth
y2 = third_fifth
y3 = fourth_fifth
y4 = top_fifth
y5 = top_twentieth
# capacity = 3*np.ones(100)

# make the mpl plot (no fill yet)
fig, ax = plt.subplots()
ax.plot(y0, label='Lowest 20%')
ax.plot(y1, label='Second Fifth')
ax.plot(y2, label='Third Fifth')
ax.plot(y3, label='Fourth Fifth')
ax.plot(y4, label='Top 20%')
ax.plot(y5, label='Top 5%')

ax.plot(years, label="Year")

# set all traces' "fill" so that it fills to the next 'y' trace
update = {'data':[{'fill': 'tonexty'}]}

# strip style just lets Plotly make the styling choices (e.g., colors)
plot_url = py.plot_mpl(fig, update=update, strip_style=True, filename='mpl-stacked-line')

