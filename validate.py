import parser 
import data
import re

json = parser.read_json()

# value validation:


def validate_temperature(Readings: list[dict]) -> dict:

    validation_result = {
        "test": "Temperature",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": [],
        "reading": []
    }

    for Dictionary in Readings:

        if (Dictionary["temperature"]==""):
            continue
        
        if (int(Dictionary["temperature"]) < 20):
            validation_result["result"] = True
            validation_result["out_of_bounds"].append(Dictionary["m_id"])
            validation_result["reading"].append(Dictionary["temperature"])
            
        elif (int(Dictionary["temperature"]) > 60):
            validation_result["result"] = True
            validation_result["out_of_bounds"].append(Dictionary["m_id"])
            validation_result["reading"].append(Dictionary["temperature"])
        else:
            validation_result["in_bounds"].append(Dictionary["m_id"])

    return validation_result

def validate_exposure(Readings: list[dict]) -> dict:

    validation_result = {
        "test": "Exposure",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": [],
        "reading": []
    }

    for Dictionary in Readings:

        if (Dictionary["exposure"] == ""):
            continue

        if (int(Dictionary["exposure"]) < 2):
            validation_result["result"] = True
            validation_result["out_of_bounds"].append(Dictionary["m_id"])
            validation_result["reading"].append(Dictionary["exposure"])

        elif (int(Dictionary["exposure"]) > 5):
            validation_result["result"] = True
            validation_result["out_of_bounds"].append(Dictionary["m_id"])
            validation_result["reading"].append(Dictionary["exposure"])
        else:
            validation_result["in_bounds"].append(Dictionary["m_id"])

    return validation_result


def validate_focus(Readings: list[dict]) -> dict:

    validation_result = {
        "test": "Focus",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": [],
        "reading": []
    }

    for Dictionary in Readings:

        if (Dictionary["focus_error"] == ""):
            continue

        if (int(Dictionary["focus_error"]) > 52):
            validation_result["result"] = True
            validation_result["out_of_bounds"].append(Dictionary["m_id"])
            validation_result["reading"].append(Dictionary["focus_error"])
        else:
            validation_result["in_bounds"].append(Dictionary["m_id"])

    return validation_result


