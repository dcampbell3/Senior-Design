import mysql.connector
import tkinter as tk
import time

mydb = mysql.connector.connect(
  host="192.168.50.170",
  user="python_ui",
  password ="SHED2023!",
  auth_plugin="mysql_native_password",
  database="Demo"
)

def getTempVal(): 
    mydb.cmd_refresh(1)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Temperature FROM Sensor WHERE ID=1")
    myresult = mycursor.fetchall()
    return myresult[0][0]

def getHumidVal(): 
    mydb.cmd_refresh(1)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Humidity FROM Sensor WHERE ID=1")
    myresult = mycursor.fetchall()
    return myresult[0][0]

window = tk.Tk()
window.title("SHED UI")
window.resizable(width=True, height=True)

sensor_field = tk.Frame(master=window)
name_label = tk.Label(master=sensor_field, text="Sensor Value:")
temp_label = tk.Label(master=sensor_field, text="VAL")
humid_label = tk.Label(master=sensor_field, text="VAL")
temp_label.grid(row=0, column=1, sticky='e')
humid_label.grid(row=0, column=2, sticky='e')
name_label.grid(row=0, column=0, sticky='w')

sensor_field.grid(row=0, column=0, pady=3)

def updateVal(): 
    temp_label.config(text=getHumidVal())
    temp_label.after(1000, updateVal)

updateVal()
window.mainloop()



