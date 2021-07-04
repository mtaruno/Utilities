# Visualization 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
import plotly.offline as pyo
import plotly.graph_objs as go

def bar(x, y, color ="#FFD700", title = "Bar Plot"):
    trace1 = go.Bar(x=x,y=y, marker=dict(color=color))
    data = [trace1]
    layout = go.Layout(title=title, barmode="stack",
                  xaxis = dict(tickangle = 90,
                              showticklabels = True,
                              type = "category",
                              dtick = 1))
    fig = go.Figure(data = data, layout = layout)
    fig.show()

print("Great! Enabled axis to bar function")

import plotly.figure_factory as ff

def distplot(lengths, title = "Distplot", 
    color = 'rgb(0, 200, 200)'):
    hist_data = [lengths]
    group_labels = ['distplot'] # name of the dataset
    fig = ff.create_distplot(hist_data, 
    group_labels, colors = [color])
    fig.update_layout(title_text=title)
    fig.show()

print("Great! Enabled axis to distplot function")