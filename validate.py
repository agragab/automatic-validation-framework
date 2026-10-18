import parser 
import data
import re

json = parser.read_json()

# value validation:
def validate_types(Readings: list[dict]) -> list[dict]:


    # return output consisting of a list of dictionaries, each dictionary represents the validation errors in each sensor reading
    # the structure is as follows:
    #  [
    #      {
    #          "test": "temperature",
    #          "exception": "ValueError",
    #      },
    #      {
    #          "test": "temperature",
    #          "exception": "TypeError",
    #      }
    #  ] ... 
    structure_results: list[dict] = []
    
    for i, Reading in enumerate(Readings):
    
        # ValueErrors (catches wrong types, not including "NoneType")
        try:
            int_temp = int(Reading["temperature"])
        except ValueError as e:
            structure_results.append(
                {   
                    "sequence": i+1,
                    "test": "temperature",
                    "exception": e
                }
            )

        try:
            int_exposure = int(Reading["exposure"])
        except ValueError as e:
            structure_results.append(
                {
                    "sequence": i+1,
                    "test": "exposure",
                    "exception": e
                }
            )

        try:
            int_focus = int(Reading["focus_error"])
        except ValueError as e:
            structure_results.append(
                {
                    "sequence": i+1,
                    "test": "focus",
                    "exception": e
                }
            )

    return structure_results





def validate_temperature(Readings: list[dict]) -> dict:

    validation_result = {
        "test": "Temperature",
        "result": False,
        "out_of_bounds": [],
        "in_bounds": [],
        "reading": []
    }

    for Dictionary in Readings:

        if (Dictionary["temperature"]=="") or (Dictionary["temperature"] is None):
            continue


        try: 
            int_temp = int(Dictionary["temperature"])
        except ValueError:
            continue
        else:
            if (int_temp < 20):
                validation_result["result"] = True
                validation_result["out_of_bounds"].append(Dictionary["m_id"])
                validation_result["reading"].append(Dictionary["temperature"])
                
            elif (int_temp > 60):
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

        try:
            int_exposure = int(Dictionary["exposure"])
        except ValueError:
            continue
        else:
            if (int_exposure < 2):
                validation_result["result"] = True
                validation_result["out_of_bounds"].append(Dictionary["m_id"])
                validation_result["reading"].append(Dictionary["exposure"])

            elif (int_exposure > 5):
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

        try:
            int_focus = int(Dictionary["focus_error"])
        except ValueError:
            continue
        else:
            if (int_focus > 52):
                validation_result["result"] = True
                validation_result["out_of_bounds"].append(Dictionary["m_id"])
                validation_result["reading"].append(Dictionary["focus_error"])
            else:
                validation_result["in_bounds"].append(Dictionary["m_id"])

    return validation_result


