from robot.api.deco import keyword

json = [
    {
        "m_id": "0",
        "timestamp": "0",
        "temperature": "0",
        "exposure": "0",
        "focus_error": "0"
    }
]

type_state = {}
temperature_state = {}
exposure_state = {}
focus_error_state = {}

type_state_list = []
temperature_state_list = []
exposure_state_list = []
focus_error_state_list = []

state_lists = {
    "type": [],
    "temperature": [],
    "exposure": [],
    "focus_error": []
}

# def set_json(json_input: list[dict]):
#     json = json_input

@keyword("Fields are empty")
def clear_states():

    type_state.clear()
    temperature_state.clear()
    exposure_state.clear()
    focus_error_state.clear()

    type_state_list.clear()
    temperature_state_list.clear()
    exposure_state_list.clear()
    focus_error_state_list.clear()

    state_lists.clear()

@keyword("m_id of reading ${sequence} is ${m_id}")
def set_m_id(sequence: int = 0, m_id: str = "100"):
    json.append({})
    json[sequence]["m_id"] = m_id

@keyword("timestamp of reading ${sequence} is ${timestamp}")
def set_timestamp(sequence: int = 0, timestamp: str = "18:34:22 | Thursday, 15th of October 2019"):
    json[sequence]["timestamp"] = timestamp

@keyword("temperature of reading ${sequence} is ${temperature}")
def set_temperature(sequence: int = 0, temperature: str = "25"): 
    json[sequence]["temperature"] = temperature

@keyword("exposure of reading ${sequence} is ${exposure}")
def set_exposure(sequence: int = 0, exposure: str = "15"):
    json[sequence]["exposure"] = exposure

@keyword("focus error of reading ${sequence} is ${focus_error}")
def set_focus_error(sequence: int = 0, focus_error: str = "5"):
    json[sequence]["focus_error"] = focus_error

@keyword("type validation is ran")
def run_type_validation(payload: list[dict] = json):
    results = []
    for i, Reading in enumerate(payload):
        for key, value in Reading.items():
            if (((value is None) or (value == "")) or (key == "timestamp")):
                continue
            else:
                try:
                    int_value = int(value)
                except ValueError as e:
                    type_state = {
                        "sequence": i,
                        "test": key,
                        "value": value,
                        "exception": type(e).__name__
                    }
                    results.append(type_state)
    type_state_list[:] = results
    return(results)


@keyword("temperature validation is ran")
def run_temperature_validation(payload: list[dict] = json): # 20 < permitted range < 50
    # looping over 
    results = []
    for i, Reading in enumerate(payload):
        # handling empty temperature field
        if(Reading.get("temperature") == "" or (Reading.get("temperature") is None)):
            temperature_state = {
                "sequence": i,
                "test": "Temperature",
                "result": False,
                "reading": "Null",
                "note": "Empty Value"
            }
            results.append(temperature_state)
            continue
        try: 
            int_temperature = int(Reading["temperature"])
        except ValueError:
            continue
        else:
            if (int_temperature) > 50:
                temperature_state = {
                "sequence": i,
                "test": "Temperature",    
                "result": False,
                "reading": int_temperature,
                "note": "WARNING: Temperature is too high"
            }

            elif (int_temperature) < 20:
                temperature_state = {
                "sequence": i,
                "test": "Temperature", 
                "result": False,
                "reading": int_temperature,
                "note": "WARNING: Temperature is too low"
            }
            else:
                temperature_state = {
                "sequence": i,
                "test": "Temperature", 
                "result": True,
                "reading": int_temperature,
                "note": "Temperature is within range"
            } 
            results.append(temperature_state)
    temperature_state_list[:] = results
    return(results)

@keyword("exposure validation is ran")
def run_exposure_validation(payload: list[dict] = json): # 10 < permitted range < 20
    results = []
    # looping over 
    for i, Reading in enumerate(payload):

        # handling empty temperature field
        if(Reading.get("exposure") == "" or (Reading.get("exposure") is None)):
            exposure_state = {
                "sequence": i,
                "test": "Exposure",
                "result": False,
                "reading": "Null",
                "note": "Empty Value"
            }
            results.append(exposure_state)
            continue

        # handling non numerical temperature
        try: 
            int_exposure = int(Reading["exposure"])
        except ValueError:
            continue
        else:
            if (int_exposure) > 20:
                exposure_state = {
                "sequence": i,
                "test": "Exposure",    
                "result": False,
                "reading": int_exposure,
                "note": "WARNING: Subject is overexposed"
            }

            elif (int_exposure) < 10:
                exposure_state = {
                "sequence": i,
                "test": "Exposure", 
                "result": False,
                "reading": int_exposure,
                "note": "WARNING: Subject is underexposed"
            }
            else:
                exposure_state = {
                "sequence": i,
                "test": "Exposure", 
                "result": True,
                "reading": int_exposure,
                "note": "Subject is correctly exposed"
            } 
            results.append(exposure_state)
    exposure_state_list[:] = results
    return(results)

@keyword("focus error validation is ran")
def run_focus_error_validation(payload: list[dict] = json): # permitted range < 10
    results = []
    # looping over 
    for i, Reading in enumerate(payload):

        # handling empty temperature field
        if(Reading.get("focus_error") == "" or (Reading.get("focus_error") is None)):
            focus_error_state = {
                "sequence": i,
                "test": "Focus Error",
                "result": False,
                "reading": "Null",
                "note": "Empty Value"
            }
            results.append(focus_error_state)
            continue

        # handling non numerical temperature
        try: 
            int_focus_error = int(Reading["focus_error"])
        except ValueError:
            continue
        else:
            if (int_focus_error) > 10:
                focus_error_state = {
                "sequence": i,
                "test": "Focus Error",    
                "result": False,
                "reading": int_focus_error,
                "note": "WARNING: Focus Error is outside permitted range"
            }
            else:
                focus_error_state = {
                "sequence": i,
                "test": "Focus Error", 
                "result": True,
                "reading": int_focus_error,
                "note": "Focus error is acceptable"
            } 
            results.append(focus_error_state)
    focus_error_state_list[:] = results
    return(results)



@keyword("defaults are set") # initialize all values within permitted ranges and structure
def set_defaults():
    clear_states()
    set_m_id()
    set_timestamp()
    set_temperature()
    set_exposure()
    set_focus_error()

@keyword("sequence of ${test} result ${sequence} is ${expected}")
def check_sequence_number(test: str, sequence: int, expected: int):
    state_list = globals()[f"{test}_state_list"]
    assert(state_list[sequence]["sequence"] == expected)
   
@keyword("test of ${test} result ${sequence} is ${expected}")
def check_test(test: str, sequence: int, expected: str):
    state_list = globals()[f"{test}_state_list"]
    assert(state_list[sequence]["test"] == expected)

@keyword("result of ${test} result ${sequence} is ${expected}")
def check_result(test: str, sequence: int, expected: bool):
    state_list = globals()[f"{test}_state_list"]
    assert(state_list[sequence]["result"] is expected)

@keyword("reading of ${test} result ${sequence} is ${expected}")
def check_reading(test: str, sequence: int, expected):
    state_list = globals()[f"{test}_state_list"]
    assert(str(state_list[sequence]["reading"]) == str(expected)) # typecast both into a string, as number input can always be string, and string (Null) is no problem

@keyword("note of ${test} result ${sequence} is ${expected}")
def check_note(test:str, sequence: int, expected: str):
    state_list = globals()[f"{test}_state_list"]
    assert(state_list[sequence]["note"] == expected)

@keyword("exception of ${test} result ${sequence} is ${expected}")
def check_exception(test:str, sequence: int, expected: str):
    state_list = globals()[f"{test}_state_list"]
    assert(state_list[sequence]["exception"] == expected)

# @keyword("complete validation is ran")
# def run_complete_validation(payload: list[dict] = json) -> dict[list]:
#     clear_states()
#     state_lists["type"] = run_type_validation(payload)
#     state_lists["temperature"] = run_temperature_validation(payload)
#     state_lists["exposure"] = run_exposure_validation(payload)
#     state_lists["focus_error"] = run_focus_error_validation(payload)
#     return state_lists