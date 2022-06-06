from employee import Employee
from staff_list import StaffList
from staff_list_iterator import EmployeeIterator

if __name__ == '__main__':
    zak = Employee('Zak')
    sarah = Employee('Sarah')
    anna = Employee('Anna')

    stlist = StaffList([zak, sarah, anna])
    iter1 = stlist.create_iterator()
    print(next(iter1).get_name())
    print(next(iter1).get_name())
    print(next(iter1).get_name())
    print(next(iter1).get_name())
