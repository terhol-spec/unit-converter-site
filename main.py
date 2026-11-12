##from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

temperature = open("temperature.txt")
STRtemperature = temperature.read()

force = open("force.txt")
STRforce = force.read()

speed = open("speed.txt")
STRspeed = speed.read()

distance = open("distance.txt")
STRdistance = distance.read()

mass = open("mass.txt")
STRmass = mass.read()

time = open("time.txt")
STRtime = time.read()

pressure = open("pressure.txt")
STRpressure = pressure.read()

@dataclass
class Type:
    MEStype:str
    MESfound:bool

@dataclass
class Input:
    INvalue:int
    INunit:str
    UNITfound:str
    
@dataclass
class Processing:
    CONfactor:int
    DESunit:str
    
@dataclass
class Out:
    OUTvalue:int
    OUTunit:str
    
@route
def Input_Type(types:Type):
    return Page(Type(types.MEStype, types.MESfound), [
                Header("Unit Converter"),
                "Type of Measurement(Temperature, Pressure, Force, Mass, Time, Distance, Speed):",
                TextBox("input type", types.MEStype),
                Button("Next","Found_type")
                ])

@route
def Found_type(types:Type):
    measurement = types.MEStype
    measurement = measurement.lower()
    value = measurement + ".txt"
    if value == "temperature.txt" or value == "time.txt" or value == "force.txt" or value == "speed.txt" or value == "distance.txt" or value == "mass.txt" or value == "pressure.txt":
        types.MESfound = True
        return Page([Header("Unit Converter"),
                    "Measurment Found!",
                    Button("Next","Input_Values")
                    ])
    else:
        types.MESfound = False
        return Page([Header("Unit Converter"),
                    "We do not have that form of measurement!",
                    Button("Go back","Input_Type")
                    ])
    
@route
def Input_Values(inputs:Input):
    return Page(Input(inputs.INvalue, inputs.INunit,inputs.UNITfound), [
                Header("Unit Converter"),
                "Measurement:",
                TextBox("input value",inputs.INvalue),
                "Unit:",
                TextBox("input unit", inputs.INunit),
                Button("Next","Found_Input")
                ])

@route
def Found_Input(inputs:Input):
    
    return Page([
                Header("Unit Converter"),
                "Measurement:",
                TextBox("input value",inputs.INvalue),
                "Unit:",
                TextBox("input unit", inputs.INunit),
                Button("Next","Found_Input")
                ])
                


start_server(Type("",False),Input(0,"",""),Processing(0,""),Out(0,""))

