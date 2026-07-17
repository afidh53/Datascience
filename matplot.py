import numpy as np
import matplotlib.pyplot as plt

# 1. Create some data points using NumPy
# Generates 100 evenly spaced numbers between 0 and 10
x = np.linspace(0, 10, 100)
y = np.sin(x)  # Compute the sine of each x value

# 2. Plot the data
plt.plot(x, y, label="Sine Wave", color="purple", linewidth=2)

# 3. Add labels and decorations
plt.title("My First Matplotlib Plot")
plt.xlabel("X Axis (Time)")
plt.ylabel("Y Axis (Amplitude)")
plt.grid(True)
plt.legend()

# 4. Display the window
plt.show()