from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Prashant\n"
        "Employee ID: E1001\n"
        "Department: BCA\n"
        "Salary: 50000"
    )

    assert employee_details("Alice", "E1001", "IT", 55000) == expected_output
