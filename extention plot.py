import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data for plotting
angle = np.array([30, 40, 50, 60, 70, 80, 90, 100])
extension = np.array([20.0, 20.5, 21.0, 21.4, 22.1, 22.4, 23.4, 24.4])
angle_error = np.array([0.1] * len(angle))
extension_error = np.array([0.15, 0.05, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05])

# Define model function for curve fitting, here using a quadratic function for demonstration
def model_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model function to the data
popt, pcov = curve_fit(model_func, angle, extension)

# Calculate the values from the fitted model function
fitted_extension = model_func(angle, *popt)

# Create plot with improved aesthetics
plt.figure(figsize=(10, 5))

# Plot data points with error bars
plt.errorbar(angle, extension, yerr=extension_error, xerr=angle_error, fmt='o', label='Data', ecolor='red', capsize=5, markersize=4)

# Plot fitted curve
plt.plot(angle, fitted_extension, label=f'Fitted Curve\ny = {popt[0]:.4f}x² + {popt[1]:.4f}x + {popt[2]:.2f}', color='blue')

# Aesthetics for the plot
plt.title('Graph: Extension vs Angle with Uncertainties')
plt.xlabel('Angle (Deg)')
plt.ylabel('Extension (cm)')
plt.xticks(np.arange(min(angle), max(angle)+10, 5))
plt.yticks(np.arange(min(extension)-1, max(extension)+1, 0.5))
plt.legend()
plt.grid(True)
plt.tight_layout()  # Adjust the padding between and around subplots

# Show the plot
plt.show()
