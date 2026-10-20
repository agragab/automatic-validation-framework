import validate
import report_generator
import models



def main(payload: models.jsonnat):

    count = 0
    jsonnaya = payload.listaya

    for Reading in jsonnaya:
        count += 1 

    total_tests = (5*count) + (3*count) ## need to calculate it 

    # type errors
    type_errors = validate.validate_types(jsonnaya)
    failed_type_errors = len(type_errors)

    temperature = validate.validate_temperature(jsonnaya)
    failed_temp = len([x for x in temperature if x["result"] is False])

    exposure = validate.validate_exposure(jsonnaya)
    failed_exposure = len(exposure["out_of_bounds"])

    focus = validate.validate_focus(jsonnaya)
    failed_focus = len(focus["out_of_bounds"])

    failed = failed_type_errors+failed_temp+failed_exposure+failed_focus

    # report_generator.generate_report_txt(total_tests,failed,present_fields,single_ids,temperature,exposure,focus)
    print(jsonnaya)
    print(type_errors)
    return(report_generator.generate_report_string(total_tests,failed,type_errors,temperature,exposure,focus))
    

if __name__ == "__main__":
    main()



