bakery import assert_equal
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
class Output:
    OUTvalue:int
    OUTunit:str
    
@route
def Input_Type(types:Type):
    return Page(Type(types.MEStype, types.MESfound), [
                Header("Unit Converter"),
                "Type of Measurement(Temperature, Pressure, Force, Mass, Time, Distance, Speed):",
                TextBox("input type", state.MEStype)
                Button("Next","Found_type")
                ])

@route
def Found_type(types:Type):
    measurement = types.MEStype
    value = measurement.lowercase() + ".txt"
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
    return Page(Input(inputs.INvalue, inputs.INunit), [
                Header("Unit Converter"),
                "Measurement:",
                TextBox("input value",state.INvalue),
                "Unit:",
                TextBox("input unit", state.INunit)
                Button("Next","Found_Input")
                ])

@route
def Found_Input(inputs:Input):
    Unit = inputs.INunit
    
    if Unit
    return Page([
                Header("Unit Converter"),
                "Measurement:",
                TextBox("input value",state.INvalue),
                "Unit:",
                TextBox("input unit", state.INunit)
                Button("Next","Found_Input")
                ])
                

start_server(Type("",False),Input(0,"",""),Processing(0,""),Output(0,""))
