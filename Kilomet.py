import tkinter as tk
from tkinter import messagebox
import requests

def get_distance(location1, location2, api_key):
    """Get distance between two locations using Google Maps Distance Matrix API."""
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={location1}&destinations={location2}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['status'] == 'OK':
        distance = data['rows'][0]['elements'][0]['distance']['text']
        duration = data['rows'][0]['elements'][0]['duration']['text']
        return distance, duration
    else:
        print(f"Error fetching data: {data.get('error_message', 'Unknown error')}")
        return None, None

def calculate_distance():
    location1 = entry_location1.get()
    location2 = entry_location2.get()

    if not location1 or not location2:
        messagebox.showerror("Input Error", "Please enter both locations.")
        return

    # API Key (make sure to keep this secure)
    api_key = 'AIzaSyA0WrdLe-pQk18WGZ4C8y6DqhaHHjUH1og'
    
    # Get distance and duration
    distance, duration = get_distance(location1, location2, api_key)

    if distance and duration:
        result_label.config(text=f"Distance: {distance}\nEstimated travel time: {duration}")
    else:
        messagebox.showerror("Error", "Could not get distance information.")

# Create the main window
window = tk.Tk()
window.title("Distance Calculator")
window.geometry("400x300")
window.configure(bg="lightblue")

# Create and place labels and entries
label_location1 = tk.Label(window, text="Enter first location:", bg="lightblue")
label_location1.pack(pady=10)

entry_location1 = tk.Entry(window, width=40)
entry_location1.pack(pady=5)

label_location2 = tk.Label(window, text="Enter second location:", bg="lightblue")
label_location2.pack(pady=10)

entry_location2 = tk.Entry(window, width=40)
entry_location2.pack(pady=5)

# Create a button to calculate the distance
calculate_button = tk.Button(window, text="Calculate Distance", command=calculate_distance)
calculate_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(window, text="", bg="lightblue", font=("Arial", 12))
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
