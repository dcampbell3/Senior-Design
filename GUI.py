import tkinter
import tkinter.messagebox
import customtkinter
import mysql.connector
from GUI_callbacks import *
from connections import mydb

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("/Users/dannycampbell/Desktop/Senior Design/SHED_theme.json")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("SHED")
        self.geometry(f"{580}x{300}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # configure frame for sensors
        self.sensor_frame = customtkinter.CTkFrame(self, width= 100, corner_radius= 0)
        self.sensor_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sensor_frame.grid_rowconfigure(4, weight=1)

        self.sensor_header = customtkinter.CTkLabel(self.sensor_frame, text= "Sensor Indicators", font= customtkinter.CTkFont(size = 30, weight='bold'))
        self.sensor_header.grid(row=0, column=0, padx=10, pady=20)
        
        # battery label
        self.bat_label = customtkinter.CTkLabel(self.sensor_frame, text= "Battery Level:", font= customtkinter.CTkFont(size=15, weight='bold'))
        self.bat_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.bat = customtkinter.CTkLabel(self.sensor_frame, text= "0%", font= customtkinter.CTkFont(size=15, weight='bold'))
        self.bat.grid(row=1, column=1, padx=10, pady=10)

        # gray water label
        self.gw_label = customtkinter.CTkLabel(self.sensor_frame, text= "Gray Water Level:", font= customtkinter.CTkFont(size=15, weight='bold'))
        self.gw_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.gw = customtkinter.CTkLabel(self.sensor_frame, text= "0%", font= customtkinter.CTkFont(size=15, weight='bold'))
        self.gw.grid(row=2, column=1, padx=10, pady=10)





if __name__ == "__main__":
    app = App()
    updateBatteryLevel(app.bat)
    updateGWLevel(app.gw)
    app.mainloop()