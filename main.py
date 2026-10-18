import validate
import structural_validation
import report_generator
import models



def main(payload: models.jsonnat):

    count = 0
    tests = 6

    jsonnaya = payload.listaya

    for Reading in jsonnaya:
        count += 1 

    total_tests = (count*5 + count + count*5 + count*3) ## need to calculate it 

    # type errors
    type_errors = validate.validate_types(jsonnaya)
    failed_type_errors = len(type_errors)

    # present fields
    present_fields = structural_validation.validate_present_fields(jsonnaya)
    missing = len(present_fields["sensor_reading"])

    # single ids
    single_ids = structural_validation.validate_single_ids(jsonnaya)
    duplicate_ids = len(single_ids["reading_numbers"])

    temperature = validate.validate_temperature(jsonnaya)
    failed_temp = len(temperature["out_of_bounds"])

    exposure = validate.validate_exposure(jsonnaya)
    failed_exposure = len(exposure["out_of_bounds"])

    focus = validate.validate_focus(jsonnaya)
    failed_focus = len(focus["out_of_bounds"])

    failed = failed_type_errors+missing+duplicate_ids+failed_temp+failed_exposure+failed_focus

    # report_generator.generate_report_txt(total_tests,failed,present_fields,single_ids,temperature,exposure,focus)
    print(jsonnaya)
    print(type_errors)
    return(report_generator.generate_report_string(total_tests,failed,type_errors, present_fields,single_ids,temperature,exposure,focus))
    

if __name__ == "__main__":
    main()



