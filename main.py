import validate
import report_generator
import models
import subprocess


def main(payload: models.jsonnat = None):

    count = 0
    if(payload):
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

    #subprocess for running pytest
    if(payload is None):
        pytest_result = subprocess.run(["py","-m","pytest","-v"], capture_output = True, text=True)
        print(pytest_result.stdout)
    # res = subprocess.run(["python", "--version"], capture_output=True, text=True)
    if(payload):
        pytest_result = subprocess.run(["pytest","-v"], capture_output = True, text=True)
        return(report_generator.generate_report_string(pytest_result.stdout,total_tests,failed,type_errors,temperature,exposure,focus))


if __name__ == "__main__":
    main()



