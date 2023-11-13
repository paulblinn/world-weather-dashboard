# This Python code generates a box plot on the dashboard. 
# Power BI automatically creates a Pandas DataFrame stored in the 'dataset' variable containing the columns I selected.
# Whenever data is filtered on the dashboard, Power BI re-executes this code to update the box plot.

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.figure(figsize=(4.6, 2.3))
plt.subplots_adjust(left=0.03, right=0.97, top=0.88, bottom=0.12)
plt.gca().spines['top'].set_color('#FFFFFF')
plt.gca().spines['bottom'].set_color('#FFFFFF')
plt.gca().spines['left'].set_color('#FFFFFF')
plt.gca().spines['right'].set_color('#FFFFFF')

plt.boxplot(dataset, vert=False, widths = 0.5, boxprops={'linewidth': 1.6,'color': '#FFFFFF'}, whiskerprops={'linewidth': 1.6,'color': '#FFFFFF'}, capprops={'linewidth': 1.6,'color': '#FFFFFF'}, medianprops={'linewidth': 2,'color': '#F2CE16'})
plt.gca().grid(True, linestyle=':', linewidth=1.5, alpha=0.7, color='#FFFFFF')
plt.title('Visibility Range (mi)', fontdict={'family': 'Consolas', 'size': 18}, color='#FFFFFF')
plt.xticks(fontproperties=FontProperties(family='Consolas', size=15), color='#FFFFFF')
plt.gca().tick_params(axis='x', colors='#FFFFFF')
plt.yticks([])

plt.gcf().set_facecolor('#386273')
plt.gca().set_facecolor('#386273')

plt.grid(True)
plt.show()
