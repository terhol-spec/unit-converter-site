##from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

temperature = open("temperature.txt")


force = open("force.txt")


speed = open("speed.txt")


distance = open("distance.txt")


mass = open("mass.txt")


time = open("time.txt")


pressure = open("pressure.txt")

@dataclass
class Type:
    MEStype:str
    MESfound:bool

@dataclass
class In:
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
    
@dataclass
class State:
    types:Type
    inputs:In
    process:Processing
    Output:Out

def search_temperature(unit:str):
    for temp in temperature:
        if unit in temp.strip():
            return True
        else:
            return False
    
def search_pressure(unit:str):
    for p in pressure:
        if unit in p.strip():
            return True
        else:
            return False

def search_mass(unit:str):
    for m in mass:
        if unit in m.strip():
            return True
        else:
            return False

def search_distance(unit:str):
    for d in distance:
        if unit in d.strip():
            return True
        else:
            return False

def search_speed(unit:str):
    for s in speed:
        if unit in s.strip():
            return True
        else:
            return False

def search_force(unit:str):
    for f in force:
        if unit in f.strip():
            return True
        else:
            return False

def search_time(unit:str):
    for t in time:
        if unit in t.strip():
            return True
        else:
            return False

def search_for_unit(measurement:str, Unit:str):
    if measurement.lower() == "temperature":
        return search_temperature(Unit)
    elif measurement.lower() == "pressure":
        return search_pressure(Unit)
    elif measurement.lower() == "mass":
        return search_mass(Unit)
    elif measurement.lower() == "speed":
        return search_speed(Unit)
    elif measurement.lower() == "time":
        return search_time(Unit)
    elif measurement.lower() == "distance":
        return search_distance(Unit)
    elif measurement.lower() == "force":
        return search_force(Unit)
    else:
        return False

def convert_temperature(value:int,con:int,valUNIT:str,conUNIT:str):
    for temp in temperature:
        temp = temp.strip()
        temp = temp.split("/")
        if temp[0] == valUNIT and temp[2] == conUNIT:
            con = temp[1]
            value = 0
            return con + value
        else:
            return "Conversion could not be calculated, Retry Unit converter"
        
def convert_pressure(val:int,con:int,valUNIT:str,conUNIT:str):
    for p in pressure:
        p = p.strip()
        p = p.split("/")
        if p[0] == valUNIT and p[2] == conUNIT:
            con = p[1]
            return val*con
        else:
            return "Conversion could not be calculated, Retry Unit converter"

def convert_mass(val:int,con:int,valUNIT:str,conUNIT:str):
    for m in mass:
        m = m.strip()
        m = m.split("/")
        if m[0] == valUNIT and m[2] == conUNIT:
            con = m[1]
            return val*con
        else:
            return "Conversion could not be calculated, Retry Unit converter"

def convert_speed(val:int,con:int,valUNIT:str,conUNIT:str):
    for s in speed:
        s = s.strip()
        s = s.split("/")
        if s[0] == valUNIT and s[2] == conUNIT:
            con = s[1]
            return val*con
        else:
            return "Conversion could not be calculated, Retry Unit converter"

def convert_time(val:int,con:int,valUNIT:str,conUNIT:str):
    for t in time:
        t = t.strip()
        t = t.split("/")
        if t[0] == valUNIT and t[2] == conUNIT:
            con = t[1]
            return val*con
        else:
            return "Conversion could not be calculated, Retry Unit converter"

def convert_distance(val:int,con:int,valUNIT:str,conUNIT:str):
    for d in distance:
        d = d.strip()
        d = d.split("/")
        if d[0] == valUNIT and d[2] == conUNIT:
            con = d[1]
            return val*con
        else:
            return "Conversion could not be calculated, Retry Unit converter"

def convert_force(val:int,con:int,valUNIT:str,conUNIT:str):
    for f in force:
        f = f.strip()
        f = f.split("/")
        if f[0] == valUNIT and f[2] == conUNIT:
            con = f[1]
            return val*con
        else:
            return "Conversion could not be calculated, Retry Unit converter"
    
def Convert_value(num1:int,num2:int,measurement:str,unit1:str,unit2:str):
    if measurement.lower() == "temperature":
        return convert_temperature(num1,num2,unit1,unit2)
    elif measurement.lower() == "pressure":
        return convert_pressure(num1,num2,unit1,unit2)
    elif measurement.lower() == "mass":
        return convert_mass(num1,num2,unit1,unit2)
    elif measurement.lower() == "speed":
        return convert_speed(num1,num2,unit1,unit2)
    elif measurement.lower() == "time":
        return convert_time(num1,num2,unit1,unit2)
    elif measurement.lower() == "distance":
        return convert_distance(num1,num2,unit1,unit2)
    elif measurement.lower() == "force":
        return convert_force(num1,num2,unit1,unit2)
    else:
        return False
    
@route
def Input_Type(state:State):
    return Page((State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)), [
                Header("Unit Converter"),
                "Type of Measurement(Temperature, Pressure, Force, Mass, Time, Distance, Speed):",
                TextBox("input type", state.types.MEStype),
                Button("Next","Found_type")
                ]))

@route
def Found_type(state:State):
    measurement = state.types.MEStype
    measurement = measurement.lower()
    value = measurement + ".txt"
    if value == "temperature.txt" or value == "time.txt" or value == "force.txt" or value == "speed.txt" or value == "distance.txt" or value == "mass.txt" or value == "pressure.txt":
        state.types.MESfound = True
        return Page([
                    Header("Unit Converter"),
                    "Measurment Found!",
                    Button("Next","Input_Values")
                    ])
    else:
        state.types.MESfound = False
        return Page([
                    Header("Unit Converter"),
                    "We do not have that form of measurement!",
                    Button("Go back","Input_Type")
                    ])
    
@route
def Input_Values(state:State):
    return Page([
                Header("Unit Converter"),
                "Measurement:",
                TextBox("input value",state.inputs.INvalue),
                "Unit:",
                TextBox("input unit", state.inputs.INunit),
                Button("Next","Found_Input")
                ])

@route
def Found_Input(state:State):
    found = search_for_unit(state.types.MEStype, state.inputs.INunit)
    if found:
        return Page([
                    Header("Unit Converter"),
                    "Input Unit Found! Proceed to Next Step!",
                    Button("Next","Desired_Unit")
                    ])
    else:
        return Page([
                    Header("Unit Converter"),
                    "Input Unit not Found!",
                    Button("Go Back","Input_Values"),
                    Button("Reset Unit Converter", "Input_Type")
                    ])
                
@route
def Desired_Unit(state:State):
    return Page([
                Header("Unit Converter"),
                "Desired Unit:",
                TextBox("desired unit", state.process.DESunit),
                Button("Next", "Found_Desire")
                ])

@route
def Found_desire(state:State):
    found = search_for_unit(state.types.MEStype, state.process.DESunit)
    if found:
        return Page([
                    Header("Unit Converter"),
                    "Desired Unit Found! Proceed to Next Step!",
                    Button("Next","Output_Page")
                    ])
    else:
        return Page([
                    Header("Unit Converter"),
                    "Desired Unit not Found!",
                    Button("Go Back","Desired_Unit"),
                    Button("Reset Unit Converter", "Input_Type")
                    ])
@route
def Output_Page(state:State):
    Answer = Convert_value(state.inputs.INvalue,state.process.CONfactor,state.types.MEStype, state.inputs.INunit, state.process.DESunit)
    if Answer: 
        return Page([
                    Header("Unit Converter"),
                    "Result",
                    Answer,
                    Button("Reset Unit Converter", "Input_Type")
                    ])
    else:
        return Page([
                    Header("Unit Converter"),
                    "Result Inconclusive, Please try again!",
                    Button("Reset Unit Converter", "Input_Type")
                    ])
    
temperature.close()
pressure.close()
mass.close()
time.close()
distance.close()
speed.close()
force.close()

start_server(State(Type("",False),In(0,"",""),Processing(0,""),Out(0,"")))
