from bokeh.plotting import figure, show

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 140, 200, 220]

# Create figure
p = figure(
    title="Monthly Sales Report",
    x_range=months,
    width=700,
    height=400,
    x_axis_label="Months",
    y_axis_label="Sales"
)

# Line graph
p.line(months, sales,
       line_width=3,
       color="blue",
       legend_label="Sales")

# Scatter points
p.scatter(months, sales,
          marker="circle",
          size=10,
          color="red",
          legend_label="Data Points")

# Grid
p.xgrid.grid_line_color = "gray"
p.ygrid.grid_line_color = "gray"

# Legend
p.legend.location = "top_left"
p.legend.title = "Legend"

# Show graph
show(p)