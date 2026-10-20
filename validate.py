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

        # handling None's:
        for key, value in Reading.items():
            if (((value is None) or (value == "")) or (key == "timestamp")):
                continue
            else:
                try:
                    int_value = int(value)
                except ValueError as e:
                    structure_results.append(
                        {
                            "sequence": i+1,
                            "test": key,
                            "exception": type(e).__name__
                        }
                    )
            # i would then have to handle timestamps seperately because they are not intable

                #         # ValueErrors (catches wrong types, not including "NoneType")
                # try:
                #     int_temp = int(Reading["temperature"])
                # except ValueError as e:
                #     structure_results.append(
                #         {   
                #             "sequence": i+1,
                #             "test": "temperature",
                #             "exception": e
                #         }
                #     )

                # try:
                #     int_exposure = int(Reading["exposure"])
                # except ValueError as e:
                #     structure_results.append(
                #         {
                #             "sequence": i+1,
                #             "test": "exposure",
                #             "exception": e
                #         }
                #     )

                # try:
                #     int_focus = int(Reading["focus_error"])
                # except ValueError as e:
                #     structure_results.append(
                #         {
                #             "sequence": i+1,
                #             "test": "focus",
                #             "exception": e
                #         }
                #     )

    return structure_results

def validate_temperature(Readings: list[dict]) -> dict:

    # validation_result = {
    #     "sequence": [],
    #     "test": "Temperature",
    #     "result": False, ## where True is passed and False is failed
    #     "out_of_bounds": [],
    #     "in_bounds": [],
    #     "reading": [],
    #     "note": []
    # }

    validation_result = []

    result_dict = {
        "sequence": 0,
        "test": "Temperature",
        "result": True,
        "reading": 0,
        "note": ""
    }


    for i, Reading in enumerate(Readings):
        
        if (Reading["temperature"]=="") or (Reading["temperature"] is None):
            result_dict = {
                "sequence": i+1,
                "test": "Temperature",
                "result": False,
                "reading": "Null",
                "note": "Empty Value"
            }
            validation_result.append(result_dict)
            continue

        try: 
            int_temp = int(Reading["temperature"])
        except ValueError:
            continue
        else:

            if (int_temp <= 19):
                result_dict = {
                    "sequence": i+1,
                    "test": "Temperature",
                    "result": False,
                    "reading": Reading["temperature"],
                    "note": "WARNING: Temperature is too low."
                }
                validation_result.append(result_dict)
            elif (int_temp >= 61):
                result_dict = {
                    "sequence": i+1,
                    "test": "Temperature",
                    "result": False,
                    "reading": Reading["temperature"],
                    "note": "WARNING: Temperature is too high."
                }
            else:
                result_dict = {
                    "sequence": i,
                    "test": "Temperature",
                    "result": True,
                    "reading": Reading["temperature"],
                    "note": "Temperature is within range."
                }


            # if (int_temp <= 19):
            #     validation_result["result"] = True
            #     validation_result["out_of_bounds"].append(i+1)
            #     validation_result["reading"].append(Dictionary["temperature"])  
            #     validation_result["note"].append("WARNING: Temperature too low")
            # elif (int_temp >= 61):
            #     validation_result["result"] = True
            #     validation_result["out_of_bounds"].append(i+1)
            #     validation_result["reading"].append(Dictionary["temperature"])
            #     validation_result["note"].append("WARNING: Temperature too high")
            # else: # add more functionality to in-bounds tests.
            #     validation_result["in_bounds"].append(i+1)
            #     validation_result["reading"].append(Dictionary["temperature"])
            #     validation_result["note"].append("In Range")

        
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


