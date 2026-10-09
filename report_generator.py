import sys

def generate_report(total_tests: int, failed: int, present_fields: dict, single_ids: dict, temperature: dict, exposure: dict, focus: dict):

    print(f"Report on {sys.argv[1]}: \n {50*"-"}")   
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {total_tests-failed}")
    print(f"Failed tests: {failed}")
    print(f"{50*"-"}")
    print(f"    Missing Fields:")
    # print(present_fields)
    zipped_missing_fields = zip(present_fields["sensor_reading"], present_fields["empty_fields"])
    # print(list(zipped_missing_fields))
    for i in list(zipped_missing_fields):
        print(f"    Test:{i[0]}", end="")
        print(f"    Missing Field: {i[1]}")

    zipped_duplicate_ids = zip(single_ids["duplicated_ids"], single_ids["reading_numbers"])
    # print (list(zipped_duplicate_ids))

    print(2*"\n")
    print("    Duplicated ID's:")

    for i in list(zipped_duplicate_ids):
        print(f"    Duplicated ID: {i[0]}", end="")
        print(f"    Second Occurence: {i[1]}")

    print(2*"\n")
    print("    Focus Error:")
    zipped_focus = zip(focus["out_of_bounds"], focus["reading"])
    
    for i in list(zipped_focus):
        print(f"    Test: {i[0]}", end="")
        print(f"    Reading: {i[1]}")

    print(2*"\n")
    print("    Exposure Error:")
    zipped_exposure = zip(exposure["out_of_bounds"], exposure["reading"])
    
    for i in list(zipped_exposure):
        print(f"    Test: {i[0]}", end="")
        print(f"    Reading: {i[1]}")

    print(2*"\n")
    print("    Temperature Error:")
    zipped_temp = zip(temperature["out_of_bounds"], temperature["reading"])
    
    for i in list(zipped_temp):
        print(f"    Test: {i[0]}", end="")
        print(f"    Reading: {i[1]}")