
def generate_report_string(total_tests: int, failed: int, failed_types: list[dict], temperature: list[dict], exposure: dict, focus: dict):

    report = []

    report.append(f"Report on JSON: \n{50*'-'}")
    report.append(f"Total tests: {total_tests}")
    report.append(f"Passed tests: {total_tests-failed}")
    report.append(f"Failed tests: {failed}")
    report.append(f"{50*'-'}")
    report.append(f"    Incorrect Type:")

    for i in failed_types: # 
        report.append(f"    Sequence: {i.get("sequence")}")
        report.append(f"    Test: {i.get("test")}")
        report.append(f"    Exception Type: {i.get("exception")}")
        report.append("\n")

    report.append("\n\n    Focus Error:")
    zipped_focus = zip(focus["out_of_bounds"], focus["reading"])
    for i in zipped_focus:
        report.append(f"    Test: {i[0]}    Reading: {i[1]}")

    report.append("\n\n    Exposure Error:")
    zipped_exposure = zip(exposure["out_of_bounds"], exposure["reading"])
    for i in zipped_exposure:
        report.append(f"    Test: {i[0]}    Reading: {i[1]}")


    # zipped_temp_t = zip(temperature["out_of_bounds"], temperature["reading"])
    # zipped_temp = zip(zipped_temp_t, temperature["note"])
    report.append("\n\n    Temperature Error:")
    for Dictionary in temperature:
        if Dictionary["result"] is False:
            report.append(f"    Sequence: {Dictionary["sequence"]}  Reading: {Dictionary["reading"]}    {Dictionary["note"]}")



    # print(temperature["out_of_bounds"])
    # print("\n"*60)
    # print(temperature["reading"])
    # print("\n"*60)
    # print(temperature["note"])


    response = "\n".join(report)
    return (response)


def generate_report_txt(total_tests: int, failed: int, present_fields: dict, single_ids: dict, temperature: dict, exposure: dict, focus: dict):
    file_string = []        
    file_string.append(f"Report on JSON: \n{50*'-'}\n")
    file_string.append(f"Total tests: {total_tests}\n")
    file_string.append(f"Passed tests: {total_tests-failed}\n")
    file_string.append(f"Failed tests: {failed}\n")
    file_string.append(f"{50*'-'}\n")
    file_string.append(f"    Missing Fields:\n")

    zipped_missing_fields = zip(present_fields["sensor_reading"], present_fields["empty_fields"])
    for i in zipped_missing_fields:
            file_string.append(f"    Test:{i[0]}    Missing Field: {i[1]}\n")

    zipped_duplicate_ids = zip(single_ids["duplicated_ids"], single_ids["reading_numbers"])
    file_string.append("\n\n    Duplicated ID's:\n")
    for i in zipped_duplicate_ids:
        file_string.append(f"    Duplicated ID: {i[0]}    Second Occurence: {i[1]}\n")


    file_string.append("\n\n    Focus Error:\n")
    zipped_focus = zip(focus["out_of_bounds"], focus["reading"])
    for i in zipped_focus:
        file_string.append(f"    Test: {i[0]}    Reading: {i[1]}\n")

    file_string.append("\n\n    Exposure Error:\n")
    zipped_exposure = zip(exposure["out_of_bounds"], exposure["reading"])
    for i in zipped_exposure:
        file_string.append(f"    Test: {i[0]}    Reading: {i[1]}\n")

    file_string.append("\n\n    Temperature Error:\n")
    zipped_temp = zip(temperature["out_of_bounds"], temperature["reading"])
    for i in zipped_temp:
        file_string.append(f"    Test: {i[0]}    Reading: {i[1]}\n")

    with open("response_file.txt", "w", newline="\n") as f:

        f.writelines(file_string)