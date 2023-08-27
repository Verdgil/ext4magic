#!/usr/bin/python3

from json import loads, dumps

with open("Analysis_Report.json") as report:
    report_dict = loads(report.read())
    set_warn = set(warning['code'] for warning in report_dict['warnings'])
    print(f"Типы ошибок: {', '.join(sorted(set_warn, key=lambda el: int(el[1:])))}")
    print(f"Число типов ошибок: {len(set_warn)}")
    print(f"Число ошибок: {len(report_dict['warnings'])}")

    result_warn = {
        "version": 2,
        "warnings": []
    }
    for warn in sorted(report_dict['warnings'], key=lambda el: int(el['code'][1:])):
        result_warn["warnings"].append(warn)

    with open("Analysis_Report.json", "w") as new_report:
        print(dumps(result_warn, indent=2), file=new_report)
