from drafter import *
from dataclasses import dataclass

Ftemperature = open("temperature.txt")
temperature = []
for t in Ftemperature:
        t = str(t)
        t = t.strip()
        temperature.append(t)

Fforce = open("force.txt")
force = []
for f in Fforce:
        f = str(f)
        f = f.strip()
        force.append(f)

Fspeed = open("speed.txt")
speed = []
for s in Fspeed:
        s = str(s)
        s = s.strip()
        speed.append(s)

Fdistance = open("distance.txt")
distance = []
for d in Fdistance:
        d = str(d)
        d = d.strip()
        distance.append(d)

Fmass = open("mass.txt")
mass = []
for m in Fmass:
        m = str(m)
        m = m.strip()
        mass.append(m)

Ftime = open("time.txt")
time = []
for t in Ftime:
        t = str(t)
        t = t.strip()
        time.append(t)

Fpressure = open("pressure.txt")
pressure = []
for p in Fpressure:
        p = str(p)
        p = p.strip()
        pressure.append(p)
        
        
Ftemperature.close()
Fpressure.close()
Fmass.close()
Ftime.close()
Fdistance.close()
Fspeed.close()
Fforce.close()


@dataclass
class Type:
    MEStype:str
    MESfound:bool

@dataclass
class In:
    INvalue:int
    INunit:str
    UNITfound:bool
    
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
        if unit in str(temp):
            return True
    return False
    
def search_pressure(unit:str):
    for p in pressure:
        if unit in str(p):
            return True
    return False

def search_mass(unit:str):
    for m in mass:
        if unit in str(m):
            return True
    return False

def search_distance(unit:str):
    for d in distance:
        if unit in str(d):
            return True
    return False

def search_speed(unit:str):
    for s in speed:
        if unit in str(s):
            return True
    return False

def search_force(unit:str):
    for f in force:
        if unit in str(f):
            return True
    return False

def search_time(unit:str):
    for t in time:
        if unit in str(t):
            return True
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
        temp = temp.split("/")
        if temp[0] == valUNIT.lower() and temp[-1] == conUNIT.lower():
            con = eval(temp[1], {}, {"value": value}) + con
            return con
    return "Conversion could not be calculated, Retry Unit converter"
        
def convert_pressure(value:int,con:int,valUNIT:str,conUNIT:str):
    for p in pressure:
        p = p.split("/")
        if p[0].strip() == valUNIT.lower() and p[-1].strip() == conUNIT.lower():
            con = float(p[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_mass(value:int,con:int,valUNIT:str,conUNIT:str):
    for m in mass:
        m = m.split("/")
        if m[0].strip() == valUNIT.lower() and m[-1].strip() == conUNIT.lower():
            con = float(m[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_speed(value:int,con:int,valUNIT:str,conUNIT:str):
    for s in speed:
        s = s.split("/")
        if s[0].strip() == valUNIT.lower() and s[-1].strip() == conUNIT.lower():
            con = float(s[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_time(value:int,con:int,valUNIT:str,conUNIT:str):
    for t in time:
        t = t.split("/")
        if t[0].strip() == valUNIT.lower() and t[-1].strip() == conUNIT.lower():
            con = float(t[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_distance(value:int,con:int,valUNIT:str,conUNIT:str):
    for d in distance:
        d = d.split("/")
        if d[0].strip() == valUNIT.lower() and d[-1].strip() == conUNIT.lower():
            con = float(d[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_force(value:int,con:int,valUNIT:str,conUNIT:str):
    for f in force:
        f = f.split("/")
        if f[0].strip() == valUNIT.lower() and f[-1].strip() == conUNIT.lower():
            con = float(f[1]) + float(con)
            return float(value) * con
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
def index(state:State)-> Page:
    return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)), [
                Header("Unit Converter"),
                "Type of Measurement(Temperature, Force, Distance, Speed, Force, Pressure, Mass):",
                TextBox("MEStype", state.types.MEStype),
                Button("Next","Found_type"),
                ])

@route
def Found_type(state:State, MEStype:str)-> Page:
    state.types.MEStype = MEStype
    value = state.types.MEStype
    value = value.lower()
    if value == "temperature" or value == "time" or value == "force" or value == "speed" or value == "distance" or value == "mass" or value == "pressure":
        state.types.MESfound = True
        return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                    Header("Unit Converter"),
                    "Measurment Found!",
                    Button("Next","Input_Values")
                    ])
    else:
        state.types.MESfound = False
        return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                    Header("Unit Converter"),
                    "We do not have that form of measurement!",
                    Button("back","index"),
                    Button("End", "end_program")
                    ])
    
@route
def Input_Values(state:State)-> Page:
    return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                Header("Unit Converter"),
                state.types.MEStype.upper() + " -",
                "Measurement:",
                TextBox("INvalue",state.inputs.INvalue),
                "Unit:",
                TextBox("INunit", state.inputs.INunit),
                Button("Next","Found_Input")
                ])

@route
def Found_Input(state:State, INvalue:int, INunit:str)-> Page:
    state.inputs.INunit = INunit
    state.inputs.INvalue = INvalue
    found = search_for_unit(state.types.MEStype, state.inputs.INunit)
    state.inputs.UNITfound = found
    if found:
        return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                    Header("Unit Converter"),
                    "Input Unit Found! Proceed to Next Step!",
                    Button("Next","Desired_Unit")
                    ])
    else:
        return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                    Header("Unit Converter"),
                    "Input Unit not Found!",
                    Button("Back","Input_Values"),
                    Button("Reset", "index"),
                    Button("End", "end_program")
                    ])
                
@route
def Desired_Unit(state:State)-> Page:
    return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                Header("Unit Converter"),
                state.types.MEStype.upper() + " -",
                "Desired Unit:",
                TextBox("desired", state.process.DESunit),
                Button("Next", "Found_desire")
                ])

@route
def Found_desire(state:State, desired:str)-> Page:
    state.process.DESunit = desired
    found = search_for_unit(state.types.MEStype, state.process.DESunit)
    if found:
        return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                    Header("Unit Converter"),
                    "Desired Unit Found! Proceed to Next Step!",
                    Button("Next","Output_Page"),
                    ])
    else:
        return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                    Header("Unit Converter"),
                    "Desired Unit not Found!",
                    Button("Back","Desired_Unit"),
                    Button("Reset", "index"),
                    Button("End", "end_program")
                    ])
@route
def Output_Page(state:State)-> Page:
    answer = Convert_value(state.inputs.INvalue,state.process.CONfactor,state.types.MEStype,state.inputs.INunit,state.process.DESunit)
    state.Output.OUTvalue = answer
    state.Output.OUTunit = state.process.DESunit 
    return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                Header("Unit Converter"),
                "Result: ",
                str(state.Output.OUTvalue) + " " + state.Output.OUTunit.upper() + "S",
                Button("Reset", "index"),
                Button("End", "end_program")
                ])

@route
def end_program(state:State):
    return Page(State(Type(state.types.MEStype, state.types.MESfound),In(state.inputs.INvalue, state.inputs.INunit, state.inputs.UNITfound),Processing(state.process.CONfactor, state.process.DESunit),Out(state.Output.OUTvalue, state.Output.OUTunit)),[
                Header("Unit Converter"),
                "Have a great day!",
                ])

start_server(State(Type("",False),In(0,"",False),Processing(0,""),Out(0,"")))
