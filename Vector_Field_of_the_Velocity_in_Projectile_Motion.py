
# ============================================================================
# AUTHOR: Javier Hidalgo Fernández
# DATE: June 11, 2026
# ASSOCIATED DOCUMENT: [Vector field 'Velocity' in projectile motion:
# Mathematical modeling and empirical validation]
#
# LICENSE: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
# LICENSE URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
# ============================================================================

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Arc, Polygon, FancyArrowPatch
import math

# --- GLOBAL VARIABLES ---
current_angle = "30"
plot_elements = []

# --- GENERAL SIMULATION LOGIC ---
def configure_scroll_limits():
    """Adjusts the scroll bar limits based on the actual initial velocity of 1.2 m/s"""
    initial_velocity = 1.2
    gravity = 9.81
    degrees = 30 if current_angle == "30" else 50
    radians = math.radians(degrees)
    v0_y = initial_velocity * math.sin(radians)
    
    time_to_peak = v0_y / gravity
    
    scroll_bar.config(from_=0, to=time_to_peak)
    scroll_bar.set(time_to_peak)

def calculate_and_update(scroll_value=None):
    global current_angle, plot_elements
    
    initial_velocity = 1.2  # Fixed at 1.2 m/s
    gravity = 9.81
    
    if current_angle == "30":
        degrees = 30
        line_color = "blue"
        title = "Projectile Motion: 30°"
        scientific_peak_result = -2.88e15  # Your value for 30 degrees
    else:
        degrees = 50
        line_color = "red"
        title = "Projectile Motion: 50°"
        scientific_peak_result = 5.54e15   # Your value for 50 degrees
        
    radians = math.radians(degrees)
    v0_x = initial_velocity * math.cos(radians)
    v0_y = initial_velocity * math.sin(radians)

    current_time = float(scroll_bar.get())
    classical_time_to_peak = v0_y / gravity
    
    # Kinematic trajectory in meters
    time_vector = np.linspace(0, current_time, 100)
    x_meters = time_vector * v0_x
    y_meters = time_vector * v0_y - 0.5 * gravity * (time_vector ** 2)
    
    # --- CONVERSION TO CENTIMETERS (cm) ---
    x_cm = x_meters * 100
    y_cm = y_meters * 100
    
    cx = x_cm[-1] if len(x_cm) > 0 else 0
    cy = y_cm[-1] if len(y_cm) > 0 else 0
    
    # Keep velocities in m/s for physics calculations
    current_vx = v0_x
    current_vy = v0_y - gravity * current_time
    
    # Update Left Panel (Showing cm)
    lbl_time.config(text=f"Current Time: {current_time:.4f} s")
    lbl_pos_x.config(text=f"Position X: {cx:.2f} cm")
    lbl_pos_y.config(text=f"Position Y: {cy:.2f} cm")
    lbl_vel_x.config(text=f"Velocity X (Vx): {current_vx:.4f} m/s")
    lbl_vel_y.config(text=f"Velocity Y (Vy): {current_vy:.4f} m/s")
    
    # --- CALCULATION OF MODIFIED EQUATIONS ---
    eq1_result = - (gravity / v0_x)
    
    time_difference = current_time - classical_time_to_peak
    if abs(time_difference) < 1e-6:
        eq2_result = scientific_peak_result
    else:
        eq2_result = 1.0 / time_difference
        
    # --- GRAPHICAL INDICATORS CONTROL ---
    rotates_right = (eq1_result < 0)
    bursts_outward = (eq2_result > 0)
    
    for element in plot_elements:
        try: element.remove()
        except: pass
    plot_elements.clear()
    
    # Draw the parabola line and the point in centimeters
    line.set_data(x_cm, y_cm)
    line.set_color(line_color)
    point.set_data([cx], [cy])
    
    # Arc size and bursts scaled proportionally to centimeters (circular_radius = 2.0 cm)
    draw_physical_indicators(cx, cy, rotates_right, bursts_outward, circular_radius=2.0)
    
    ax.set_title(title)
    
    # --- DYNAMIC LIMITS ADJUSTMENT WITH "ZOOM" (In centimeters) ---
    # Calculate the theoretical maximum range in cm for the current angle to frame the plot correctly
    theoretical_flight_time = 2 * v0_y / gravity
    theoretical_max_x_cm = (theoretical_flight_time * v0_x) * 100
    theoretical_max_y_cm = (v0_y**2 / (2 * gravity)) * 100
    
    # Adjust axis limits with comfortable margins so the indicators fit perfectly
    ax.set_xlim(-5, theoretical_max_x_cm + 8)
    ax.set_ylim(-5, theoretical_max_y_cm + 8)
    canvas.draw()
    
    # Show results on the green screens
    show_on_console(lbl_console_eq1, eq1_result)
    show_on_console(lbl_console_eq2, eq2_result)

# --- INDICATORS ADAPTED TO CENTIMETERS SCALE ---
def draw_physical_indicators(cx, cy, rotates_right, bursts_outward, circular_radius):
    global plot_elements
    if rotates_right:
        theta1, theta2 = 0, 270
        tip_angle_deg = 270
        tangent_direction = 1
    else:
        theta1, theta2 = 270, 540
        tip_angle_deg = 270
        tangent_direction = -1

    # Drawing the purple arc
    arc = Arc((cx, cy), width=circular_radius*2, height=circular_radius*2, angle=0,
               theta1=theta1, theta2=theta2, color="purple", lw=2, zorder=4)
    ax.add_patch(arc)
    plot_elements.append(arc)

    tip_angle_rad = np.deg2rad(tip_angle_deg)
    px = cx + circular_radius * np.cos(tip_angle_rad)
    py = cy + circular_radius * np.sin(tip_angle_rad)
    tangent_x = -np.sin(tip_angle_rad) * tangent_direction
    tangent_y = np.cos(tip_angle_rad) * tangent_direction

    # Arc arrow tip scaled to centimeters
    tip_vertex = (px + 1.0 * tangent_x, py + 1.0 * tangent_y)
    left_vertex = (px - 0.7 * tangent_y, py + 0.7 * tangent_x)
    right_vertex = (px + 0.7 * tangent_y, py - 0.7 * tangent_x)

    arrow_tip_triangle = Polygon([tip_vertex, left_vertex, right_vertex], color="purple", zorder=4)
    ax.add_patch(arrow_tip_triangle)
    plot_elements.append(arrow_tip_triangle)

    # Radial bursts scaled to centimeters
    inner_radius = circular_radius + 0.8
    outer_radius = inner_radius + 2.5
    angles_deg = np.linspace(0, 360, 9)
    
    for angle in angles_deg:
        rad = np.deg2rad(angle)
        cos_a, sin_a = np.cos(rad), np.sin(rad)
        p_inner = (cx + inner_radius * cos_a, cy + inner_radius * sin_a)
        p_outer = (cx + outer_radius * cos_a, cy + outer_radius * sin_a)
        
        if bursts_outward:
            start_point, end_point = p_inner, p_outer
            radial_color = "green"
        else:
            start_point, end_point = p_outer, p_inner
            radial_color = "orange"
            
        # Radial arrows with head size optimized for visual scale
        radial_arrow = FancyArrowPatch(start_point, end_point, arrowstyle="->,head_width=3,head_length=4",
                                        color=radial_color, lw=1.5, zorder=3)
        ax.add_patch(radial_arrow)
        plot_elements.append(radial_arrow)

def change_angle(function_type):
    global current_angle
    current_angle = function_type
    if function_type == "30":
        btn_30.config(state="disabled")
        btn_50.config(state="normal")
    else:
        btn_30.config(state="normal")
        btn_50.config(state="disabled")
    configure_scroll_limits()
    calculate_and_update()

def show_on_console(console_label, value):
    scientific_string = f"{value:.6e}"
    if "e" in scientific_string:
        base, exp = scientific_string.split("e")
        clean_exp = exp.replace("+", "")
        console_label.config(text=f"{base} x 10^{int(clean_exp)}")
    else:
        console_label.config(text=scientific_string)

# --- INTERFACE CONSTRUCTION ---
w_left = tk.Tk()
w_left.title("Control Panel")
w_left.geometry("350x380+50+150")

lbl_title = tk.Label(w_left, text="REAL-TIME DATA", font=("Arial", 12, "bold"))
lbl_title.pack(pady=10)

lbl_time = tk.Label(w_left, text="Current Time: 0.00 s", font=("Arial", 11))
lbl_time.pack(anchor="w", padx=20, pady=3)
lbl_pos_x = tk.Label(w_left, text="Position X: 0.00 cm", font=("Arial", 11))
lbl_pos_x.pack(anchor="w", padx=20, pady=3)
lbl_pos_y = tk.Label(w_left, text="Position Y: 0.00 cm", font=("Arial", 11))
lbl_pos_y.pack(anchor="w", padx=20, pady=3)
lbl_vel_x = tk.Label(w_left, text="Velocity X (Vx): 0.00 m/s", font=("Arial", 11))
lbl_vel_x.pack(anchor="w", padx=20, pady=3)
lbl_vel_y = tk.Label(w_left, text="Velocity Y (Vy): 0.00 m/s", font=("Arial", 11))
lbl_vel_y.pack(anchor="w", padx=20, pady=3)

lbl_scroll = tk.Label(w_left, text="Scroll to change time:", font=("Arial", 10, "italic"))
lbl_scroll.pack(pady=(15, 0))

scroll_bar = ttk.Scale(w_left, from_=0.01, to=1.0, orient="horizontal", command=calculate_and_update)
scroll_bar.pack(fill="x", padx=20, pady=5)

# Plot window
plot_window = tk.Toplevel(w_left)
plot_window.title("Kinetic Animation Canvas")
plot_window.geometry("600x550+420+150")

button_panel = ttk.Frame(plot_window, padding=10)
button_panel.pack(side=tk.TOP, fill=tk.X)

btn_30 = ttk.Button(button_panel, text="Angle 30 °", state="disabled", command=lambda: change_angle("30"))
btn_30.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
btn_50 = ttk.Button(button_panel, text="Angle 50 °", state="normal", command=lambda: change_angle("50"))
btn_50.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)

fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
ax.set_aspect('equal')
ax.grid(True, linestyle='--')
ax.set_xlabel("Distance (cm)")
ax.set_ylabel("Height (cm)")

line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro', ms=8, zorder=5)

canvas = FigureCanvasTkAgg(fig, master=plot_window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Right Window 1
w_right_1 = tk.Toplevel(w_left)
w_right_1.title("The vector field is non-conservative")
w_right_1.geometry("380x250+1040+100")

fig_la1, ax_la1 = plt.subplots(figsize=(3, 0.8), dpi=100)
ax_la1.axis('off')
ax_la1.text(0.5, 0.5, r'$\operatorname{rot} \vec{F} = \nabla \times \vec{F} = -\left(\frac{g}{V_{0x}}\right) \quad [s^{-1}]$', fontsize=14, ha='center', va='center')
canvas_la1 = FigureCanvasTkAgg(fig_la1, master=w_right_1)
canvas_la1.get_tk_widget().pack(pady=5)
tk.Label(w_right_1, text="EQUATION 1 RESULT (Console):", font=("Arial", 9, "bold")).pack(pady=5)
frame_c1 = tk.Frame(w_right_1, bg="#000000")
frame_c1.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
lbl_console_eq1 = tk.Label(frame_c1, text="", bg="#000000", fg="#00FF00", font=("Consolas", 14, "bold"))
lbl_console_eq1.pack(fill=tk.BOTH, expand=True, pady=10)

# Right Window 2
w_right_2 = tk.Toplevel(w_left)
w_right_2.title("The vector field is a source (+) or a sink (-)")
w_right_2.geometry("380x250+1040+400")

fig_la2, ax_la2 = plt.subplots(figsize=(3, 0.8), dpi=100)
ax_la2.axis('off')
ax_la2.text(0.5, 0.5, r'$\operatorname{div} \vec{F} = \nabla \cdot \vec{F} = \frac{1}{t - \left(\frac{V_{0y}}{g}\right)}\quad [s^{-1}]$', fontsize=14, ha='center', va='center')
canvas_la2 = FigureCanvasTkAgg(fig_la2, master=w_right_2)
canvas_la2.get_tk_widget().pack(pady=5)
tk.Label(w_right_2, text="EQUATION 2 RESULT (Console):", font=("Arial", 9, "bold")).pack(pady=5)
frame_c2 = tk.Frame(w_right_2, bg="#000000")
frame_c2.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
lbl_console_eq2 = tk.Label(frame_c2, text="", bg="#000000", fg="#00FF00", font=("Consolas", 14, "bold"))
lbl_console_eq2.pack(fill=tk.BOTH, expand=True, pady=10)

# --- INITIALIZATION ---
configure_scroll_limits()
calculate_and_update()
w_left.mainloop()



