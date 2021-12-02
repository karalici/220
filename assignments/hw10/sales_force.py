"""
Name: Iva Karalic
sales_force.py

Problem:Creates sales force class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from sales_person import SalesPerson


class SalesForce:
    """ 'SalesForce' class is a list that holds information on all of the "SalesPerson" objects """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, "r") as in_file:
            lines = in_file.readlines()
            for line in lines:
                separated_line = line.split(", ")
                emp_id, name = separated_line[0], separated_line[1]
                person = SalesPerson(eval(emp_id), name)

                sales = separated_line[2]
                samples = sales.split()

                for sale in samples:
                    person.enter_sale(eval(sale))

                self.sales_people.append(person)
            in_file.close()

    def quota_report(self, quota):
        quota_list = []
        for employee in self.sales_people:
            quota_list.append([employee.get_id(), employee.get_name(),
                            employee.total_sales(), employee.met_quota(quota)])
        return quota_list

    def top_seller(self):
        top_seller_list = []
        self.sales_people.sort(key=SalesPerson.total_sales, reverse=True)
        i = 0
        top_seller_list.append(self.sales_people[0])
        while self.sales_people[i] == self.sales_people[i + 1]:
            top_seller_list.append(self.sales_people[i+1])
            i += 1
        return top_seller_list

    def individual_sales(self, employee_id):
        id_dict = {}
        for i in range(len(self.sales_people)):
            id_dict[self.sales_people[i].get_id()] = self.sales_people[i]
        if employee_id in id_dict:
            return id_dict.get(employee_id)
        return None
