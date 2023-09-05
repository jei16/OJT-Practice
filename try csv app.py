import tkinter as tk
import csv

# Function to create a CSV file when the button is clicked
def create_csv_file():
    # Get data from the user input fields (replace these with your own data source)
    name = entry_name.get()
    age = entry_age.get()
    
    # Define the CSV file name
    file_name = "output.csv"
    
    # Open the CSV file in write mode
    with open(file_name, mode='w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        
        # Write header row (if needed)
        csv_writer.writerow(["Name", "Age"])
        
        # Write data to the CSV file
        csv_writer.writerow([name, age])

# Create the main application window
app = tk.Tk()
app.title("CSV File Creator")

# Create input fields for data
label_name = tk.Label(app, text="Name:")
label_age = tk.Label(app, text="Age:")
entry_name = tk.Entry(app)
entry_age = tk.Entry(app)

# Create a button to trigger CSV creation
create_button = tk.Button(app, text="Create CSV", command=create_csv_file)

# Arrange widgets using grid layout
label_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
label_age.grid(row=1, column=0)
entry_age.grid(row=1, column=1)
create_button.grid(row=2, columnspan=2)

# Start the Tkinter main loop
app.mainloop()
