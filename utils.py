def get_reading_count(payload: list[dict]):
    return len(payload)

def get_test_count(payload: list[dict]):
    return 10*get_reading_count(payload)
    
def get_failure_count(state_lists: dict[list]):

    type_error_count = len(state_lists["type"])
    temperature_error_count = len(list(x for x in state_lists["temperature"] if x["result"] is False))
    exposure_error_count = len(list(x for x in state_lists["exposure"] if x["result"] is False))
    focus_error_error_count = len(list(x for x in state_lists["focus_error"] if x["result"] is False))
    return type_error_count + temperature_error_count + exposure_error_count + focus_error_error_count
