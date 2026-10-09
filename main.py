import parser
import validate
import structural_validation
import report_generator

def main():

    json = parser.read_json()
    count = 0
    tests = 5

    for Reading in json:
        count += 1 

    # print(structural_validation.validate_present_fields(json))
    # print(structural_validation.validate_single_ids(json))
    # print(validate.validate_focus(json))
    # print(validate.validate_exposure(json))
    # print(validate.validate_temperature(json))

    total_tests = (count*5 + count + count*3) ## need to calculate it 

    # present fields
    present_fields = structural_validation.validate_present_fields(json)
    missing = len(present_fields["sensor_reading"])

    # single ids
    single_ids = structural_validation.validate_single_ids(json)
    duplicate_ids = len(single_ids["reading_numbers"])

    temperature = validate.validate_temperature(json)
    failed_temp = len(temperature["out_of_bounds"])

    exposure = validate.validate_exposure(json)
    failed_exposure = len(exposure["out_of_bounds"])

    focus = validate.validate_focus(json)
    failed_focus = len(focus["out_of_bounds"])

    # print(missing)
    # print(duplicate_ids)
    # print(failed_temp)
    # print(failed_exposure)
    # print(failed_focus)

    failed = missing+duplicate_ids+failed_temp+failed_exposure+failed_focus

    # print(f"Total tests: {total_tests}")
    # print(f"Passed tests {total_tests-failed}")
    # print(f"Failed tests: {failed}")

    report_generator.generate_report(total_tests,failed,present_fields,single_ids,temperature,exposure,focus)



if __name__ == "__main__":
    main()



