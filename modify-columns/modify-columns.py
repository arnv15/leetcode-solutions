import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    double = []
    for i in employees["salary"]:
        double.append(i * 2)
    employees["salary"] = double
    return employees
