import package_1.tst1
from package_1.classes.person import Person

def main():
    people = []
    people.append(Person("Tony", "Montana", 43))
    people.append(Person("John", "Wick", 58))
    people.append(Person("Inigo", "Montoya", 36))

    for person in people:
        print(person.get_id())

    for i in range(1, 10):
        print(package_1.tst1.calc_factorial(i))

if __name__ == "__main__":
    main()





