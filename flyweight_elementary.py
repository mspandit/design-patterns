import unittest
import pickle


class BaseEmployee(object):
    def __init__(self):
        super(BaseEmployee, self).__init__()
        self.health_plan_details = "details" * 400
        self.retirement_plan_details = "details" * 400
        self.stock_purchase_plan_details = "details" * 400


class Employee(object):
    def __init__(self, id, address, base):
        super(Employee, self).__init__()
        self.id = id
        self.address = address
        self.base = base

    base_instance = None
    
    @staticmethod
    def getInstance(id, address):
        if not Employee.base_instance:
            Employee.base_instance = BaseEmployee()
        return Employee(id, address, Employee.base_instance)


class TestMethods(unittest.TestCase):
    def test0(self):
        company = []
        for id0 in range(40):
            company.append(Employee.getInstance(id0 + 1, "9710 Scranton Rd., San Diego, CA")) 
        self.assertLess(len(pickle.dumps(company)), 1024 * 1024)
    
    def test1(self):
        company = []
        for id0 in range(80):
            company.append(Employee.getInstance(id0 + 1, "9710 Scranton Rd., San Diego, CA"))
        for id1 in range(10000):
            company.append(Employee.getInstance(id1 + 100000, "2111 NE 25th Avenue, Hillsboro, OR"))
        for id2 in range(20000):
            company.append(Employee.getInstance(id2 + 101000, "2200 Mission College Blvd., Santa Clara, CA"))
        self.assertLess(len(pickle.dumps(company)), 100 * 1024 * 1024) # Fails 254716530 not less than 1048576
        

if __name__ == "__main__":
    unittest.main()
    