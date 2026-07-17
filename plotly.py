import plotly.express as px

data = {
    "Day": [1, 2, 3, 4, 5],
    "Sales": [10, 20, 15, 30, 25]
}

fig = px.line(data, x="Day", y="Sales",
              title="Sales Line Chart",
              markers=True)

fig.show()