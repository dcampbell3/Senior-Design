import mysql.connector
import tkinter
import customtkinter

mydb = mysql.connector.connect(
  host="192.168.50.170",
  user="python_ui",
  password ="SHED2023!",
  auth_plugin="mysql_native_password",
  database="SHED"
)

# def getTemp(): 
#     try: 
#         mydb.cmd_refresh(1)
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT Temperature FROM Sensor WHERE ID=1")
#         myresult = mycursor.fetchall()
#         return myresult[0][0]
#     except: 
#         return "ERROR GETTING TEMPERARTURE"
    
# def updateTemp(temp_label): 
#     val = getTemp()
#     color = ""
#     if val != "ERROR GETTING TEMPERATURE" and float(val) > 75: 
#         color = "#ED1400"
#     else: 
#         color = "#6BE11D"

#     temp_label.configure(text=getTemp() + u'\N{DEGREE SIGN}', text_color = color)
#     temp_label.after(1000, lambda: updateTemp(temp_label))
    
# def getHumid(): 
#     try: 
#         mydb.cmd_refresh(1)
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT Humidity FROM Sensor WHERE ID=1")
#         myresult = mycursor.fetchall()
#         return myresult[0][0]
#     except: 
#         return "ERROR GETTING TEMPERATURE"

# def updateHumid(humid_label):
#     val = getHumid() 
#     color = ""
#     if val != "ERROR GETTING TEMPERATURE":
#         if float(val) > 70: 
#             color = "#ED1400"
#         else: 
#             color = "#6BE11D"

#     humid_label.configure(text=getHumid() + "%", text_color = color)
#     humid_label.after(1000, lambda: updateHumid(humid_label))
    
def getBatteryLevel(): 
    try: 
        mydb.cmd_refresh(1)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Value FROM Sensors WHERE Sensor = 'Shunt'")
        myresult = mycursor.fetchall()
        return myresult[0][0]
    except: 
        return "ERROR GETTING BATTERY LEVEL"

def updateBatteryLevel(bat_label):
    val = getBatteryLevel() 
    color = ""
    if val != "ERROR GETTING BATTERY LEVEL":
        if float(val) > 10: 
            color = "#6BE11D" 
        else: 
            color = "#ED1400"

    bat_label.configure(text=getBatteryLevel() + "%", text_color = color)
    bat_label.after(1000, lambda: updateBatteryLevel(bat_label))
    