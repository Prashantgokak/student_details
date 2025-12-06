from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Prashant\n"
        "Employee ID: E1001\n"
        "Department: BCA\n"
        "Salary: 50000"
    )

    assert employee_details("Prashant", "E1001", "BCA", 50000) == expected_output
