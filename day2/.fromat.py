name = input("input your name:")
age = input("input your age:")
job = input("input ypur job:")
salary = input("input your salary:")

Info = '''
------------info of {_name} ----------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
--------------------------------------
'''.format(
    _name=name,
    _age=age,
    _job=job,
    _salary=salary
)

print(Info)