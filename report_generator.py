
def generate_report_string(total_tests: int, failed: int, failed_types: list[dict], temperature: list[dict], exposure: list[dict], focus: list[dict]):

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
        report.append(f"    Value: {i.get("value")}")
        report.append(f"    Exception Type: {i.get("exception")}")
        report.append("\n")

    report.append("\n\n    Temperature Error:")
    for Dictionary in temperature:
        if Dictionary["result"] is False:
            report.append(f"    Sequence: {Dictionary["sequence"]}  Reading: {Dictionary["reading"]}    {Dictionary["note"]}")

    report.append("\n\n    Exposure Error:")
    for Dictionary in exposure:
        if Dictionary["result"] is False:
            report.append(f"    Sequence: {Dictionary["sequence"]}  Reading: {Dictionary["reading"]}    {Dictionary["note"]}")

    report.append("\n\n    Focus Error:")
    for Dictionary in focus:
        if Dictionary["result"] is False:
            report.append(f"    Sequence: {Dictionary["sequence"]}  Reading: {Dictionary["reading"]}    {Dictionary["note"]}")

    response = "\n".join(report)
    return (response)
