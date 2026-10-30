import report_generator
from utils import *
from validators import *

# def main(payload: models.Readings = None):
def main(payload):

    # payload of json from http request
    failed_types = run_type_validation(payload)
    failed_temperature = run_temperature_validation(payload)
    failed_exposure = run_exposure_validation(payload)
    failed_focus_error = run_focus_error_validation(payload)

    state_lists = {
        "type": failed_types,
        "temperature": failed_temperature,
        "exposure": failed_exposure,
        "focus_error": failed_focus_error
    }

    total_tests = get_test_count(payload)
    failed_tests = get_failure_count(state_lists)

    return(report_generator.generate_report_string(total_tests, failed_tests, failed_types, failed_temperature, failed_exposure, failed_focus_error))


if __name__ == "__main__":
    main()



