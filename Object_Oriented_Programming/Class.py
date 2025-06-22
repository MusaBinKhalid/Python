class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, country):
        self.name = name
        self.salary = salary
        self.country = country

p = Programmer("Mike", 100000, "USA")
print(p.name, p.salary, p.company, p.country)

q = Programmer("Rahul", 200000, "India")
print(q.name, q.salary, q.company, q.country)

r = Programmer("Cristiano", 120000, "Portugal")
print(r.name, r.salary, r.company, r.country) 

