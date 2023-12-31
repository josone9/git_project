LEGAL_DRIVING_AGE = 18

class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        # Initialize Adult object with provided attributes
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        # Check if the person is old enough to drive and print the result
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def can_drive(self):
        # Override can_drive method for children and print the result
        print(f"{self.name} is too young to drive.")

def main():
    # Take user inputs
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    eye_colour = input("Enter the eye colour: ")
    hair_colour = input("Enter the hair colour: ")

    # Determine if the person is 18 or older
    if age >= LEGAL_DRIVING_AGE:
        person = Adult(name, age, eye_colour, hair_colour)
    else:
        person = Child(name, age, eye_colour, hair_colour)

    # Call the can_drive() method
    person.can_drive()

if __name__ == "__main__":
    main()
