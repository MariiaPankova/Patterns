from employee import *
from visitor import *

if __name__ == '__main__':
    staff_list = StaffList()
    staff_list.add_employee(Manager(60000))
    staff_list.add_employee(SalesPerson(5000))
    staff_list.add_employee(SalesPerson(4000))

    print(staff_list.get_salary())

    visitor_salary_up =  SalaryUpVisitor(0.10)
    staff_list.accept(visitor_salary_up)

    print(staff_list.get_salary())

    visitor_salary_down = SalaryDownVisitor(0.1)
    staff_list.accept(visitor_salary_down)
    print(staff_list.get_salary())
    staff_list.accept(visitor_salary_down)
    print(staff_list.get_salary())



    gosha = ITSupport(1000000000)
    gosha.accept(visitor_salary_down)
    print(gosha.get_salary())

