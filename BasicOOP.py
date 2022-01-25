#การสร้าง Class
class Employee: 
    #สร้าง method
    def detail(self,empname,empsalary):
        self.name = empname
        self.salary = empsalary
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))

#การสร้างวัตถุ
obj1 = Employee()
obj1.detail("วิบูลย์",50000)

obj2 = Employee()
obj2.detail("แบ็ค",60000)

obj3 = Employee()
obj3.detail("หมูเป็นหมู",80000)