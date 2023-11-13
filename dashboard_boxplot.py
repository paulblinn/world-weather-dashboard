# This Python code generates the box plot on the dashboard. 
# Power BI automatically creates a Pandas DataFrame stored in the 'dataset' variable containing the columns I selected.
# Whenever data is filtered on the dashboard, Power BI re-executes this code to update the box plot.

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Set up the figure and adjust plot parameters
plt.figure(figsize=(4.6, 2.3))
plt.subplots_adjust(left=0.03, right=0.97, top=0.88, bottom=0.12)
plt.gca().spines['top'].set_color('#FFFFFF')
plt.gca().spines['bottom'].set_color('#FFFFFF')
plt.gca().spines['left'].set_color('#FFFFFF')
plt.gca().spines['right'].set_color('#FFFFFF')

# Create the box plot
plt.boxplot(dataset, vert=False, widths=0.5,
            boxprops={'linewidth': 1.6, 'color': '#FFFFFF'},
            whiskerprops={'linewidth': 1.6, 'color': '#FFFFFF'},
            capprops={'linewidth': 1.6, 'color': '#FFFFFF'},
            medianprops={'linewidth': 2, 'color': '#F2CE16'})

# Customize grid appearance
plt.gca().grid(True, linestyle=':', linewidth=1.5, alpha=0.7, color='#FFFFFF')

# Set title and customize font properties
plt.title('Visibility Range (mi)', fontdict={'family': 'Consolas', 'size': 18}, color='#FFFFFF')

# Customize x-axis ticks
plt.xticks(fontproperties=FontProperties(family='Consolas', size=15), color='#FFFFFF')
plt.gca().tick_params(axis='x', colors='#FFFFFF')

# Hide y-axis ticks
plt.yticks([])

# Set background colors
plt.gcf().set_facecolor('#386273')
plt.gca().set_facecolor('#386273')

# Display the plot
plt.grid(True)
plt.show()

