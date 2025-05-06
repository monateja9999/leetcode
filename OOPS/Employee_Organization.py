from collections import defaultdict
from typing import List, Dict

class Employee:
    def __init__(self, name: str, age: int, department: str, experience: int):
        self.name = name
        self.age = age
        self.department = department
        self.experience = experience
        self.direct_reports: List['Employee'] = []

    def add_direct_report(self, employee: 'Employee'):
        self.direct_reports.append(employee)


class Organization:
    def __init__(self):
        self.employees: Dict[str, Employee] = {}

    def add_employee(self, employee: Employee):
        self.employees[employee.name] = employee

    def get_employee(self, name: str) -> Employee:
        return self.employees.get(name)

    def get_reports(self, name: str, include_indirect: bool = True) -> List[Employee]:
        result = []

        def dfs(emp: Employee):
            for report in emp.direct_reports:
                result.append(report)
                if include_indirect:
                    dfs(report)

        employee = self.get_employee(name)
        if employee:
            dfs(employee)
        return result

    def group_reports(self, name: str, attribute: str) -> Dict[str, List[str]]:
        grouped = defaultdict(list)
        reports = self.get_reports(name, include_indirect=True)

        for emp in reports:
            key = getattr(emp, attribute, 'unknown')
            grouped[key].append(emp.name)

        return grouped


if __name__ == "__main__":
    # Create the organization (Singleton instance)
    org = Organization()

    # Create employee instances
    ceo = Employee("Alice", 50, "Management", 30)
    head_eng = Employee("Bob", 40, "Engineering", 15)
    eng1 = Employee("Charlie", 30, "Engineering", 5)
    eng2 = Employee("David", 28, "Engineering", 3)
    hr_head = Employee("Eve", 45, "HR", 20)

    # Build employee hierarchy
    ceo.add_direct_report(head_eng)
    ceo.add_direct_report(hr_head)
    head_eng.add_direct_report(eng1)
    head_eng.add_direct_report(eng2)

    # Add employees to the organization
    for emp in [ceo, head_eng, eng1, eng2, hr_head]:
        org.add_employee(emp)

    # Fetch direct + indirect reports under Alice
    all_reports = org.get_reports("Alice", include_indirect=True)
    print("All reports under Alice:")
    for emp in all_reports:
        print(f"- {emp.name} ({emp.department}, {emp.experience} yrs)")

    # Group Alice's reports by department
    grouped_by_dept = org.group_reports("Alice", "department")
    print("\nGrouped by Department:")
    for dept, emps in grouped_by_dept.items():
        print(f"{dept}: {[e.name for e in emps]}")

    # Group Alice's reports by experience
    grouped_by_exp = org.group_reports("Alice", "experience")
    print("\nGrouped by Experience:")
    for exp, emps in grouped_by_exp.items():
        print(f"{exp} yrs: {[e.name for e in emps]}")
