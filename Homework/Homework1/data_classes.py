import json
class Person(object):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Email": self.email
        }
class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init(name, age, email)
        self.student_id = student_id

    def to_dict(self):
        person_dict = super().to_dict()
        person_dict["Student ID"] = self.student_id
        return person_dict
    
def save_to_json(obj,filename):
    with open('hw3.json', 'w') as json_file:
        json.dump(obj.to_dict(), json_file, indent=4)

def display_json(filename):
    with open('hw3.json', 'r') as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=4))

person = Person("bobby joe", 30, "bobbyjoe@khbsv.com")
student = Student("cindy joe", 20, "cindyjoe@ksjdbv.com", "S12345")

save_to_json(person, 'person.json')
save_to_json(student, 'student.json')
display_json(filename ='hw3.json')
display_json(filename ='hw3.json')