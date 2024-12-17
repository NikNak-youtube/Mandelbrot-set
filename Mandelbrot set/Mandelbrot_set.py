import numpy as np
import matplotlib.pyplot as plt

# Remember to install the required packages if you haven't already using the following command:
# pip install -r requirements.txt
# Use python 3.12 in a virtual environment
# Download python 3.12 from https://www.python.org/downloads/release/python-3120/

# Fancy title
print(" ________ ________  ________  ________ _________  ________  ___               ___      ___ ___  _______   ___       __   _______   ________     \n|\\  _____\\\\   __  \\|\\   __  \\|\\   ____\\\\___   ___\\\\   __  \\|\\  \\             |\\  \\    /  /|\\  \\|\\  ___ \\ |\\  \\     |\\  \\|\\  ___ \\ |\\   __  \\    \n\\ \\  \\__/\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\___\\|___ \\  \\_\\ \\  \\|\\  \\ \\  \\            \\ \\  \\  /  / | \\  \\ \\   __/|\\ \\  \\    \\ \\  \\ \\   __/|\\ \\  \\|\\  \\   \n \\ \\   __\\\\ \\   _  _\\ \\   __  \\ \\  \\       \\ \\  \\ \\ \\   __  \\ \\  \\            \\ \\  \\/  / / \\ \\  \\ \\  \\_|/_\\ \\  \\  __\\ \\  \\ \\  \\_|/_\\ \\   _  _\\  \n  \\ \\  \\_| \\ \\  \\\\  \\\\ \\  \\ \\  \\ \\  \\____   \\ \\  \\ \\ \\  \\ \\  \\ \\  \\____        \\ \\    / /   \\ \\  \\ \\  \\_|\\ \\ \\  \\|\\__\\_\\  \\ \\  \\_|\\ \\ \\  \\\\  \\| \n   \\ \\__\\   \\ \\__\\\\ _\\\\ \\__\\ \\__\\ \\_______\\  \\ \\__\\ \\ \\__\\ \\__\\ \\_______\\       \\ \\__/ /     \\ \\__\\ \\_______\\ \\____________\\ \\_______\\ \\__\\\\ _\\ \n    \\|__|    \\|__|\\|__|\\|__|\\|__|\\|_______|   \\|__|  \\|__|\\|__|\\|_______|        \\|__|/       \\|__|\\|_______|\\|____________|\\|_______|\\|__|\\|__|\n")

# Set initial parameters
center_x, center_y = -0.75, 0.0
zoom_limit = 1e12  # Limit zoom level to prevent floating-point precision issues

# Ask the user which fractal formula to use
print("Choose a fractal formula:")
print("1. Mandelbrot Set")
print("2. Julia Set")
print("3. Burning Ship")
print("4. Custom Formula")
choice = input("Enter the number of your choice: ")

if choice == "1":
    formula_name = "Mandelbrot Set"
    def fractal_formula(Z, C):
        return Z * Z + C

elif choice == "2":
    formula_name = "Julia Set"
    print("\nRecommended Julia constants:")
    julia_constants = {
        "1": "-0.4+0.6j",
        "2": "0.355+0.355j",
        "3": "-0.70176-0.3842j",
        "4": "-0.8+0.156j",
        "5": "0.37+0.1j",
    }
    for num, constant in julia_constants.items():
        print(f"{num}. {constant}")

    julia_choice = input("Choose a constant by number, or enter a custom constant (e.g., -0.4+0.6j): ")
    julia_constant_str = julia_constants.get(julia_choice, julia_choice).replace(" ", "")
    
    try:
        julia_constant = complex(julia_constant_str)
    except ValueError:
        print("Invalid constant format. Please enter a valid complex number (e.g., -0.4+0.6j).")
        exit()

    def fractal_formula(Z, C):
        return Z * Z + julia_constant


elif choice == "3":
    formula_name = "Burning Ship"
    def fractal_formula(Z, C):
        Z = np.abs(Z.real) + 1j * np.abs(Z.imag)  # Take absolute value of both real and imaginary parts
        return Z * Z + C

elif choice == "4":
    formula_name = "Custom Formula"
    custom_formula = input("Enter your custom formula using 'Z' and 'C' (e.g., 'Z**2 + C'): ")
    
    # Define the fractal formula based on user input
    def fractal_formula(Z, C):
        return eval(custom_formula)

else:
    print("Invalid choice. Defaulting to Mandelbrot Set.")
    formula_name = "Mandelbrot Set"
    def fractal_formula(Z, C):
        return Z * Z + C

# Ask the user for the zoom factor
zoom_factor_input_str = input("Enter the zoom factor per click (e.g., 2 for doubling, 1.5 for 50% increase): ")

# Handle empty input and invalid input
if zoom_factor_input_str.strip() == "":  # Empty input
    zoom_factor_input = 2.0  # Default to 2.0
else:
    try:
        zoom_factor_input = float(zoom_factor_input_str)
    except ValueError:
        print("Invalid input. Defaulting to 2.")
        zoom_factor_input = 2.0  # Default to 2.0 in case of an error



# Ask the user for the maximum number of iterations, with a recommendation
max_iterations_str = input("Enter the maximum number of iterations (recommended: 256): ") or "256"

# Handle invalid input for max_iterations
try:
    max_iterations = int(max_iterations_str)
except ValueError:
    print("Invalid input. Defaulting to 256.")
    max_iterations = 256  # Default to 256 if input is invalid


zoom_factor = 1.0  # Starting zoom factor

def generate_fractal(width, height, xmin, xmax, ymin, ymax, max_iter):
    # Generate x and y values
    x = np.linspace(xmin, xmax, width).reshape((1, width))
    y = np.linspace(ymin, ymax, height).reshape((height, 1))
    C = x + 1j * y

    # Initialize Z and an array to count iterations
    Z = np.zeros(C.shape, dtype=complex)
    mask = np.full(C.shape, True, dtype=bool)
    fractal_set = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        Z[mask] = fractal_formula(Z[mask], C[mask])
        mask = (abs(Z) <= 2)
        fractal_set += mask

    return fractal_set

def plot_fractal():
    global center_x, center_y, zoom_factor

    # Define the current bounds with an aspect ratio of 16:9
    aspect_ratio = 16 / 9
    zoom_width = 3.5 / zoom_factor
    zoom_height = zoom_width / aspect_ratio

    xmin, xmax = center_x - zoom_width / 2, center_x + zoom_width / 2
    ymin, ymax = center_y - zoom_height / 2, center_y + zoom_height / 2

    # Generate and display fractal set
    fractal_set = generate_fractal(800, 450, xmin, xmax, ymin, ymax, max_iterations)
    plt.imshow(fractal_set, extent=(xmin, xmax, ymin, ymax), cmap="inferno", origin="lower")
    plt.title(f"{formula_name} - Zoom Factor: {zoom_factor:.2f}")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.draw()

def on_click(event):
    global center_x, center_y, zoom_factor
    if event.button == 1 and zoom_factor < zoom_limit:  # Left-click to zoom in, limit zoom factor
        zoom_factor *= zoom_factor_input
        center_x, center_y = event.xdata, event.ydata
        plot_fractal()
    elif event.button == 3 and zoom_factor > 1:  # Right-click to zoom out, prevent negative zoom
        zoom_factor /= zoom_factor_input
        plot_fractal()

def on_key(event):
    global center_x, center_y, zoom_factor
    pan_distance = 0.1 / zoom_factor
    if event.key == "left":
        center_x -= pan_distance
    elif event.key == "right":
        center_x += pan_distance
    elif event.key == "up":
        center_y += pan_distance
    elif event.key == "down":
        center_y -= pan_distance
    plot_fractal()

# Set up the plot
fig, ax = plt.subplots()
plot_fractal()
fig.canvas.mpl_connect("button_press_event", on_click)
fig.canvas.mpl_connect("key_press_event", on_key)
plt.show()
