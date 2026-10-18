#check this
def validate_present_fields(Readings: list[dict]) -> dict:
    dict_of_empty_vales = {"test":"present fields","test_result": False, "sensor_reading": [], "empty_fields": []}
    counter = 1
    for dictionary in Readings:
        for key, field in dictionary.items():
            if ((field == None) or field == ("")):
                dict_of_empty_vales["sensor_reading"].append(counter)
                dict_of_empty_vales["empty_fields"].append(key)
                dict_of_empty_vales["test_result"] = True
        counter += 1    
    
    return dict_of_empty_vales



# bug here i guess
def validate_single_ids(Readings: list[dict]):

    seen = set()
    duplicates = set()
    list_of_duplicated_ids = []
    result_dict = {"test": "single ids","test_result": False, "duplicated_ids": duplicates, "reading_numbers": list_of_duplicated_ids}

    counter = 1
    for dictionary in Readings:
        if (dictionary["m_id"] in seen):
            duplicates.add(dictionary["m_id"])
            list_of_duplicated_ids.append(counter)
            result_dict["test_result"] = True
        else:
            seen.add(dictionary["m_id"])
        counter += 1 

    return result_dict
