""" 
Partner Excersize: 
    
GUI for the Municipality simulation 

"""

__author__ = "6963879, Tverdohleb, "


import tkinter as tk
from tkinter import ttk
from citizens import Citizens
from building import Building, BasicBuilding, ElectiveBuilding

class MunicipalitySimulatorGUI(tk.Tk):
    def __init__(self, municipality):
        super().__init__()

        self.municipality = municipality

        self.title("Municipality Simulator")
        self.geometry("800x400")
        
        self.label = tk.Label(text="Welcome to XXXXX!", font=('Arial', 18))
        self.abel.pack(padx=20, pady=20)

        # Left side: Display stats
        self.stats_frame = tk.Frame(self)
        self.stats_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.round_label = tk.Label(self.stats_frame, text="Round:")
        self.round_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.population_count_label = tk.Label(self.stats_frame, text="Population Count:")
        self.population_count_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.immigration_entry = tk.Entry(self.stats_frame)
        self.immigration_entry.grid(row=1, column=1, padx=5, pady=5)

        self.emigration_entry = tk.Entry(self.stats_frame)
        self.emigration_entry.grid(row=1, column=2, padx=5, pady=5)

        self.balance_label = tk.Label(self.stats_frame, text="Balance:")
        self.balance_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.tax_rate_label = tk.Label(self.stats_frame, text="Tax Rate:")
        self.tax_rate_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        self.tax_rate_entry = tk.Entry(self.stats_frame)
        self.tax_rate_entry.grid(row=3, column=1, padx=5, pady=5)

        self.resources_label = tk.Label(self.stats_frame, text="Resources Available:")
        self.resources_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.event_label = tk.Label(self.stats_frame, text="Event:")
        self.event_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)

        # Right side: Progress bar for Population Satisfaction
        self.progress_bar_frame = tk.Frame(self)
        self.progress_bar_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.population_satisfaction_label = tk.Label(self.progress_bar_frame, text="Population Satisfaction:")
        self.population_satisfaction_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.population_satisfaction_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", length=200, mode="determinate")
        self.population_satisfaction_bar.grid(row=1, column=0, padx=5, pady=5)
        
        # Building selection dropdown
        self.building_label = tk.Label(self.progress_bar_frame, text="Select Building:")
        self.building_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.building_options = [building.name for building in self.municipality.buildings]
        self.selected_building = tk.StringVar()
        self.building_dropdown = ttk.Combobox(self.progress_bar_frame, textvariable=self.selected_building, values=self.building_options)
        self.building_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Checkbox for each building
        self.building_checkboxes = []
        for index, building_name in enumerate(self.building_options):
            checkbox = ttk.Checkbutton(self.progress_bar_frame, text=building_name, variable=tk.BooleanVar(), onvalue=True, offvalue=False)
            checkbox.grid(row=index + 3, column=0, columnspan=2, sticky="w", padx=5, pady=2)
            self.building_checkboxes.append(checkbox)
        
        # Buttons
        self.simulate_button = tk.Button(self, text="Simulate One Round", command=self.simulate_one_round)
        self.simulate_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Initialize the GUI with current stats
        self.update_stats()

    def simulate_one_round(self):
        try:
            # Update municipality parameters from entry fields
            self.municipality.immigration = int(self.immigration_entry.get())
            self.municipality.emigration = int(self.emigration_entry.get())
            self.municipality.tax_rate = float(self.tax_rate_entry.get())

            # Add selected buildings
            for index, checkbox in enumerate(self.building_checkboxes):
                if checkbox.instate(['selected']):
                    selected_building = self.municipality.buildings[index]
                    self.municipality.buildings.append(selected_building)

            # Run one simulation round
            self.municipality.simulate_one_round()

            # Update displayed stats
            self.update_stats()
        except ValueError:
            # Handle incorrect entry (non-integer or non-float input)
            print("Invalid input. Please enter valid numbers for immigration, emigration, and tax rate.")


    def update_stats(self):
        # Update labels and entry fields with current stats
        self.round_label.config(text=f"Round: {self.municipality.month}")
        self.population_count_label.config(text=f"Population Count: {self.municipality.citizens.count}")
        self.immigration_entry.delete(0, tk.END)
        self.immigration_entry.insert(0, str(self.municipality.immigration))
        self.emigration_entry.delete(0, tk.END)
        self.emigration_entry.insert(0, str(self.municipality.emigration))
        self.balance_label.config(text=f"Balance: {self.municipality.balance}")
        self.tax_rate_label.config(text=f"Tax Rate: {self.municipality.tax_rate}")
        self.tax_rate_entry.delete(0, tk.END)
        self.tax_rate_entry.insert(0, str(self.municipality.tax_rate))
        self.resources_label.config(text=f"Resources Available: {self.municipality.resources}")
        self.event_label.config(text=f"Event: {self.municipality.current_event}")

        # Update building options and checkboxes
        self.building_options = [building.name for building in self.municipality.buildings]
        self.building_dropdown['values'] = self.building_options

        for index, checkbox in enumerate(self.building_checkboxes):
            checkbox.destroy()

        self.building_checkboxes = []
        for index, building_name in enumerate(self.building_options):
            checkbox = ttk.Checkbutton(self.progress_bar_frame, text=building_name, variable=tk.BooleanVar(), onvalue=True, offvalue=False)
            checkbox.grid(row=index + 3, column=0, columnspan=2, sticky="w", padx=5, pady=2)
            self.building_checkboxes.append(checkbox)

        # Update Population Satisfaction progress bar
        self.population_satisfaction_bar["value"] = self.municipality.citizens.satisfaction
        self.population_satisfaction_bar.update()



if __name__ == "__main__":
    # Create a sample municipality for testing
    municipality = Municipality()

    # Create and run the GUI
    simulator_gui = MunicipalitySimulatorGUI(municipality)
    simulator_gui.mainloop()
