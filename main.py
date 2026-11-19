from drafter import *
from dataclasses import dataclass
from bakery import assert_equal

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
    """Stores the selected measurement category and whether it is valid.

    Attributes:
        MEStype: The name of the measurement type (e.g., 'temperature', 'mass').
        MESfound: True if the measurement type is supported, False otherwise.
    """
    MEStype:str
    MESfound:bool

@dataclass
class In:
    """Stores the user's input numerical value, unit, and unit validation status.

    Attributes:
        INvalue: The numerical measurement value entered by the user.
        INunit: The unit of measurement associated with the input value.
        UNITfound: True if the input unit exists in the dataset, False otherwise.
    """
    INvalue:int
    INunit:str
    UNITfound:bool
    
@dataclass
class Processing:
    """Stores intermediate conversion data and the target unit.

    Attributes:
        CONfactor: The conversion factor offset or base value used during calculation.
        DESunit: The desired target unit to convert the input value into.
    """
    CONfactor:int
    DESunit:str
    
@dataclass
class Out:
    """Stores the final converted measurement value and its unit.

    Attributes:
        OUTvalue: The resulting numerical value after unit conversion.
        OUTunit: The unit of the converted output value.
    """
    OUTvalue:int
    OUTunit:str
    
@dataclass
class State:
    """Represents the overall application state passed between Drafter routes.

    Attributes:
        types: A Type object holding measurement category details.
        inputs: An In object holding input value and unit details.
        process: A Processing object holding conversion factors and target unit.
        Output: An Out object holding the final converted result.
    """
    types:Type
    inputs:In
    process:Processing
    Output:Out

def search_temperature(unit:str):
    """Checks if a given unit exists in the temperature conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the temperature list, False otherwise.
    """
    for temp in temperature:
        if unit in str(temp):
            return True
    return False
    
def search_pressure(unit:str):
    """Checks if a given unit exists in the pressure conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the pressure list, False otherwise.
    """
    for p in pressure:
        if unit in str(p):
            return True
    return False

def search_mass(unit:str):
    """Checks if a given unit exists in the mass conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the mass list, False otherwise.
    """
    for m in mass:
        if unit in str(m):
            return True
    return False

def search_distance(unit:str):
    """Checks if a given unit exists in the distance conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the distance list, False otherwise.
    """
    for d in distance:
        if unit in str(d):
            return True
    return False

def search_speed(unit:str):
    """Checks if a given unit exists in the speed conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the speed list, False otherwise.
    """
    for s in speed:
        if unit in str(s):
            return True
    return False

def search_force(unit:str):
    """Checks if a given unit exists in the force conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the force list, False otherwise.
    """
    for f in force:
        if unit in str(f):
            return True
    return False

def search_time(unit:str):
    """Checks if a given unit exists in the time conversions list.

    Args:
        unit: The unit string to search for.

    Returns:
        True if the unit is found in the time list, False otherwise.
    """
    for t in time:
        if unit in str(t):
            return True
    return False

def search_for_unit(measurement:str, Unit:str):
    """Dispatches a unit search to the appropriate measurement search helper.

    Args:
        measurement: The category of measurement (e.g., 'temperature', 'mass').
        Unit: The unit name to look up.

    Returns:
        True if the unit is valid for the given measurement type, False otherwise.
    """
    if measurement.lower() == "temperature":
        return search_temperature(Unit.lower())
    elif measurement.lower() == "pressure":
        return search_pressure(Unit.lower())
    elif measurement.lower() == "mass":
        return search_mass(Unit.lower())
    elif measurement.lower() == "speed":
        return search_speed(Unit.lower())
    elif measurement.lower() == "time":
        return search_time(Unit.lower())
    elif measurement.lower() == "distance":
        return search_distance(Unit.lower())
    elif measurement.lower() == "force":
        return search_force(Unit.lower())
    else:
        return False

def convert_temperature(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a temperature value from one unit to another using formula evaluation.

    Args:
        value: The input temperature value to convert.
        con: An additive adjustment to the conversion result.
        valUNIT: The unit of the input temperature.
        conUNIT: The target unit for the output temperature.

    Returns:
        The converted temperature value, or an error string if conversion fails.
    """
    for temp in temperature:
        temp = temp.split(",")
        if temp[0] == valUNIT.lower() and temp[-1] == conUNIT.lower():
            con = eval(temp[1], {}, {"value": value}) + con
            return con
    return "Conversion could not be calculated, Retry Unit converter"
        
def convert_pressure(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a pressure value from one unit to another using a conversion factor.

    Args:
        value: The input pressure value to convert.
        con: An additive adjustment to the conversion factor.
        valUNIT: The unit of the input pressure.
        conUNIT: The target unit for the output pressure.

    Returns:
        The converted pressure value as a float, or an error string if conversion fails.
    """
    for p in pressure:
        p = p.split("/")
        if p[0].strip() == valUNIT.lower() and p[-1].strip() == conUNIT.lower():
            con = float(p[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_mass(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a mass value from one unit to another using a conversion factor.

    Args:
        value: The input mass value to convert.
        con: An additive adjustment to the conversion factor.
        valUNIT: The unit of the input mass.
        conUNIT: The target unit for the output mass.

    Returns:
        The converted mass value as a float, or an error string if conversion fails.
    """
    for m in mass:
        m = m.split("/")
        if m[0].strip() == valUNIT.lower() and m[-1].strip() == conUNIT.lower():
            con = float(m[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_speed(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a speed value from one unit to another using a conversion factor.

    Args:
        value: The input speed value to convert.
        con: An additive adjustment to the conversion factor.
        valUNIT: The unit of the input speed.
        conUNIT: The target unit for the output speed.

    Returns:
        The converted speed value as a float, or an error string if conversion fails.
    """
    for s in speed:
        s = s.split("/")
        if s[0].strip() == valUNIT.lower() and s[-1].strip() == conUNIT.lower():
            con = float(s[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_time(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a time value from one unit to another using a conversion factor.

    Args:
        value: The input time value to convert.
        con: An additive adjustment to the conversion factor.
        valUNIT: The unit of the input time.
        conUNIT: The target unit for the output time.

    Returns:
        The converted time value as a float, or an error string if conversion fails.
    """
    for t in time:
        t = t.split("/")
        if t[0].strip() == valUNIT.lower() and t[-1].strip() == conUNIT.lower():
            con = float(t[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_distance(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a distance value from one unit to another using a conversion factor.

    Args:
        value: The input distance value to convert.
        con: An additive adjustment to the conversion factor.
        valUNIT: The unit of the input distance.
        conUNIT: The target unit for the output distance.

    Returns:
        The converted distance value as a float, or an error string if conversion fails.
    """
    for d in distance:
        d = d.split("/")
        if d[0].strip() == valUNIT.lower() and d[-1].strip() == conUNIT.lower():
            con = float(d[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"

def convert_force(value:int,con:int,valUNIT:str,conUNIT:str):
    """Converts a force value from one unit to another using a conversion factor.

    Args:
        value: The input force value to convert.
        con: An additive adjustment to the conversion factor.
        valUNIT: The unit of the input force.
        conUNIT: The target unit for the output force.

    Returns:
        The converted force value as a float, or an error string if conversion fails.
    """
    for f in force:
        f = f.split("/")
        if f[0].strip() == valUNIT.lower() and f[-1].strip() == conUNIT.lower():
            con = float(f[1]) + float(con)
            return float(value) * con
    return "Conversion could not be calculated, Retry Unit converter"
    
def Convert_value(num1:int,num2:int,measurement:str,unit1:str,unit2:str):
    """Dispatches a unit conversion request to the appropriate measurement converter.

    Args:
        num1: The input value to convert.
        num2: The conversion factor offset.
        measurement: The category of measurement (e.g., 'temperature', 'mass').
        unit1: The input unit.
        unit2: The target output unit.

    Returns:
        The converted value, an error message string, or False if the measurement type is invalid.
    """
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
                "Type of Measurement (Temperature, Force, Distance, Speed, Force, Pressure, Mass):",
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

# Unit tests for search helper functions
assert_equal(search_temperature("celsius"), True)
assert_equal(search_temperature("invalid_unit"), False)

assert_equal(search_pressure("pascal"), True)
assert_equal(search_pressure("invalid_unit"), False)

assert_equal(search_mass("kilogram"), True)
assert_equal(search_mass("invalid_unit"), False)

assert_equal(search_distance("meter"), True)
assert_equal(search_distance("invalid_unit"), False)

assert_equal(search_speed("mile_per_hour"), True)
assert_equal(search_speed("invalid_unit"), False)

assert_equal(search_force("newton"), True)
assert_equal(search_force("invalid_unit"), False)

assert_equal(search_time("second"), True)
assert_equal(search_time("invalid_unit"), False)

assert_equal(search_for_unit("temperature", "Celsius"), True)
assert_equal(search_for_unit("mass", "Kilogram"), True)
assert_equal(search_for_unit("unknown_type", "meter"), False)

# Unit tests for conversion helper functions
assert_equal(convert_temperature(0, 0, "celsius", "fahrenheit"), 32.0)
assert_equal(convert_temperature(0, 0, "invalid", "fahrenheit"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(convert_pressure(1, 0, "atmosphere", "pascal"), 101325.0)
assert_equal(convert_pressure(1, 0, "invalid", "pascal"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(convert_mass(1, 0, "kilogram", "gram"), 1000.0)
assert_equal(convert_mass(1, 0, "invalid", "gram"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(convert_speed(60, 0, "meter_per_second", "kilometer_per_hour"), 216.0)
assert_equal(convert_speed(60, 0, "invalid", "kph"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(convert_time(1, 0, "minute", "second"), 60.0)
assert_equal(convert_time(1, 0, "invalid", "second"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(convert_distance(1, 0, "kilometer", "meter"), 1000.0)
assert_equal(convert_distance(1, 0, "invalid", "meter"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(convert_force(1, 0, "newton", "dyne"), 100000.0)
assert_equal(convert_force(1, 0, "invalid", "dyne"), "Conversion could not be calculated, Retry Unit converter")

assert_equal(Convert_value(0, 0, "temperature", "celsius", "fahrenheit"), 32.0)
assert_equal(Convert_value(1, 0, "mass", "kilogram", "gram"), 1000.0)
assert_equal(Convert_value(1, 0, "unknown_type", "meter", "kilometer"), False)

start_server(State(Type("",False),In(0,"",False),Processing(0,""),Out(0,"")))
