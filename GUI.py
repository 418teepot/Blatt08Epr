""" 
Partner Excersize: 
    
GUI for the Municipality simulation 

"""

__author__ = "6963879, Tverdohleb, "


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

from citizens import Citizens
from building import Building, BasicBuilding, ElectiveBuilding



class InstructionsPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Instructions and Rules")
        
        instructions_text =  """
        Welcome to XXXXXX Municipality!

        Objective:
        Build and manage a thriving city by making strategic decisions in areas such as urban planning, 
        infrastructure development, economy, and citizen satisfaction.

        Getting Started:
        1. You start with a basic city layout and a limited budget.
        2. Use the initial funds to set up essential infrastructure and buildings.

        On the left-hand side of the simulation window, you’ll find all the stats such as:
        - Population count
        - Available balance
        - Tax rate for the citizens
        - Events that can take place
        They will help you make informed choices!

        Game Rounds:
        1. The game is played in rounds, each representing a month.
        2. At the beginning of each round, the stats get updated, and there is the possibility to input:
           - \033[1mTax rate\033[0m
           - \033[1mBuild/demolish buildings\033[0m

        City Elements:
        1. Infrastructure: Build and maintain roads, bridges, and areas for citizens to live. Upgrade as the city expands.
        2. Safety: Provide necessary electricity, water, and waste management, as well as public authorities to oversee peace and order.
        3. Health: Ensure there are facilities for citizens to receive treatment and work on their health by being active.
        4. Entertainment: Don’t forget to provide ample amusement and commercial zones for a vivid social life within the community.
        
        Increase zones as the population grows and maintain a balance for maximum citizen satisfaction.

        Economy:
        1. Monitor the city's budget and manage funds wisely.
        2. Adjust tax rates to generate revenue but be cautious of citizen satisfaction levels.
        3. Income is also generated by certain buildings through ticket/membership sales.

        Citizen Satisfaction:
        1. Keep an eye on citizen happiness indicators, including health, safety, and entertainment.
        2. Address issues such as living space, adequate resources, and free-time activities to improve overall satisfaction.

        Challenges:
        1. Face unexpected events such as natural disasters, economic downturns, or sudden population growth.
        2. Manage crises effectively to minimize negative impacts on the city.

        Have an enjoyable time exploring our city!
        """
    
        
        instructions_label = tk.Label(self, text=instructions_text, padx=20, pady=20)
        instructions_label.pack()



class MunicipalitySimulatorGUI(tk.Tk):
    def __init__(self, municipality):
        super().__init__()

        self.municipality = municipality

        self.title("Municipality Simulator")
        self.geometry("1000x500")
        
        self.label = tk.Label(text="Welcome to XXXXX!", font=('Arial', 18))
        self.abel.pack(padx=20, pady=20)

        # Button for instructions and rules
        self.instructions_button = tk.Button(self, text="Instructions", command=self.show_instructions)
        self.instructions_button.pack(side=tk.TOP, padx=10, pady=10)

        # Left side: Display stats
        self.stats_frame = tk.Frame(self)
        self.stats_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.round_label = tk.Label(self.stats_frame, text="Round:")
        self.round_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.population_count_label = tk.Label(self.stats_frame, text="Population Count:")
        self.population_count_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.immigration_label = tk.Label(self.stats_frame, text="Immigration:")
        self.immigration_lable.grid(row=2, column=0, sticky="w", padx=5, pady=10)

        self.emigration_label = tk.Label(self.stats_frame, text="Emigration:")
        self.emigration_label.grid(row=3, column=0, sticky="w", padx=5, pady=10)

        self.balance_label = tk.Label(self.stats_frame, text="Balance:")
        self.balance_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.tax_rate_label = tk.Label(self.stats_frame, text="Tax Rate:")
        self.tax_rate_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)

        self.tax_rate_entry = tk.Entry(self.stats_frame)
        self.tax_rate_entry.grid(row=5, column=1, padx=5, pady=5)

        self.event_label = tk.Label(self.stats_frame, text="Event:")
        self.event_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)

        # Right side: Progress bar for Population Satisfaction
        self.progress_bar_frame = tk.Frame(self)
        self.progress_bar_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.population_satisfaction_label = tk.Label(self.progress_bar_frame, text="Population Satisfaction:")
        self.population_satisfaction_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.population_satisfaction_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", 
                                                           length=200, mode="determinate")
        self.population_satisfaction_bar.grid(row=1, column=0, padx=5, pady=5)
        
        # Infrastructure Progress Bar
        self.infrastructure_label = tk.Label(self.progress_bar_frame, text="Infrastructure:")
        self.infrastructure_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.infrastructure_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", 
                                                  length=200, mode="determinate")
        self.infrastructure_bar.grid(row=3, column=0, padx=5, pady=5)

        # Safety Progress Bar
        self.safety_label = tk.Label(self.progress_bar_frame, text="Safety:")
        self.safety_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.safety_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", 
                                          length=200, mode="determinate")
        self.safety_bar.grid(row=5, column=0, padx=5, pady=5)

        # Health Progress Bar
        self.health_label = tk.Label(self.progress_bar_frame, text="Health:")
        self.health_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)

        self.health_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", 
                                         length=200, mode="determinate")
        self.health_bar.grid(row=7, column=0, padx=5, pady=5)

        # Entertainment Progress Bar
        self.entertainment_label = tk.Label(self.progress_bar_frame, text="Entertainment:")
        self.entertainment_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)

        self.entertainment_bar = ttk.Progressbar(self.progress_bar_frame, orient="horizontal", 
                                                 length=200, mode="determinate")
        self.entertainment_bar.grid(row=9, column=0, padx=5, pady=5)


        # Listbox for Existing Buildings
        self.existing_buildings_label = tk.Label(self.progress_bar_frame, text="Existing Buildings:")
        self.existing_buildings_label.grid(row=10, column=0, sticky="w", padx=5, pady=5)

        self.existing_buildings_listbox = tk.Listbox(self.progress_bar_frame, selectmode=tk.SINGLE)
        self.existing_buildings_listbox.grid(row=11, column=0, padx=5, pady=5)
        
        # Combobox for Building Selection
        self.building_selection_label = tk.Label(self.progress_bar_frame, text="Select Buildings to Buy/Demolish:")
        self.building_selection_label.grid(row=12, column=0, sticky="w", padx=5, pady=5)

        self.building_options = [building.name for building in self.municipality.buildings]
        self.selected_building = tk.StringVar()
        self.building_combobox = ttk.Combobox(self.progress_bar_frame, textvariable=self.selected_building, 
                                              values=self.building_options)
        self.building_combobox.grid(row=13, column=0, padx=5, pady=5)

        # Checkbox for the selected building
        self.selected_building_checkbox = ttk.Checkbutton(self.progress_bar_frame, text="Buy/Demolish",
                                                          variable=tk.BooleanVar(), onvalue=True, offvalue=False,
                                                          command=self.update_building_checkboxes)
        self.selected_building_checkbox.grid(row=14, column=0, padx=5, pady=5)

        # Buttons for Buy/Demolish
        self.buy_button = tk.Button(self.progress_bar_frame, text="Buy", command=self.buy_selected_building) 
        self.buy_button.grid(row=15, column=0, padx=5, pady=5)

        self.demolish_button = tk.Button(self.progress_bar_frame, text="Demolish", command=self.demolish_selected_building)
        self.demolish_button.grid(row=15, column=1, padx=5, pady=5)
    
            
        # Checkbox for immigration prevention
        self.prevent_immigration_var = tk.BooleanVar()
        self.prevent_immigration_checkbox = ttk.Checkbutton(self.stats_frame, text="Prevent Immigration", 
                                                            variable=self.prevent_immigration_var, 
                                                            command=self.update_stats)
        self.prevent_immigration_checkbox.grid(row=2, column=2, padx=5, pady=5)

        
        # Buttons
        self.simulate_button = tk.Button(self, text="Simulate One Round", command=self.simulate_one_round)
        self.simulate_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Initialize the GUI with current stats
        self.update_stats()
        
        
    def show_instructions(self):
        instructions_popup = InstructionsPopup(self)
        instructions_popup.grab_set()        
        

    def simulate_one_round(self):
        try:
            # Update municipality parameters from entry fields
            self.municipality.tax_rate = float(self.tax_rate_entry.get())

            # Add selected buildings
            for index, checkbox in enumerate(self.building_checkboxes):
                if checkbox.instate(['selected']):
                    selected_building = self.municipality.buildings[index]
                    self.municipality.buildings.append(selected_building)

            # Update immigration prevention status
            self.municipality.prevent_immigration = self.prevent_immigration_var.get()

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
        self.immigration_label.config(text=f"Immigration: {self.municipality.immigration}")
        self.emigration_label.config(text=f"Emigration: {self.municipality.emigration}")
        self.balance_label.config(text=f"Balance: {self.municipality.balance}")
        self.tax_rate_label.config(text=f"Tax Rate: {self.municipality.tax_rate}")
        self.tax_rate_entry.delete(0, tk.END)
        self.tax_rate_entry.insert(0, str(self.municipality.tax_rate))
        self.resources_label.config(text=f"Resources Available: {self.municipality.resources}")
        self.event_label.config(text=f"Event: {self.municipality.current_event}")

    # Update building options and checkboxes
    def update_building_checkboxes(self):
        selected_building = self.selected_building.get()
        if selected_building:
            checkbox_text = f"{selected_building} - Price: {self.citizens.construction_cost(selected_building)}"
            self.selected_building_checkbox.config(text=checkbox_text)
        else:
            self.selected_building_checkbox.config(text="")

    def buy_selected_building(self):
        selected_building = self.selected_building.get()
        if selected_building:
            self.building.build(selected_building)  
            # Update displayed stats after buying
            self.update_stats()

    def demolish_selected_building(self):
        selected_building = self.selected_building.get()
        if selected_building:
            self.municipality.demolish_building(selected_building)  # Call the demolish method in the Building class
            # Update displayed stats after demolishing
            self.update_stats()
            
            
        # Update immigration checkbox
        self.immigration_checkbox.config(state=tk.NORMAL)
        
        if self.municipality.prevent_immigration:
            self.immigration_checkbox.deselect()
            self.immigration_checkbox.config(state=tk.DISABLED)  
            
        else:
            self.immigration_checkbox.config(state=tk.NORMAL)  
                     

        # Update Population Satisfaction progress bar
        self.population_satisfaction_bar["value"] = self.municipality.citizens.satisfaction
        self.population_satisfaction_bar.update()
        
        # Update Infrastructure progress bar
        self.infrastructure_bar["value"] = self.municipality.citizens.infrastructure
        self.infrastructure_bar.update()

        # Update Safety progress bar
        self.safety_bar["value"] = self.municipality.citizens.safety
        self.safety_bar.update()

        # Update Health progress bar
        self.health_bar["value"] = self.municipality.citizens.health
        self.health_bar.update()

        # Update Entertainment progress bar
        self.entertainment_bar["value"] = self.municipality.citizens.entertainment
        self.entertainment_bar.update()



if __name__ == "__main__":
    municipality = Municipality()

    # Create and run the GUI
    simulator_gui = MunicipalitySimulatorGUI(municipality)
    simulator_gui.mainloop()
