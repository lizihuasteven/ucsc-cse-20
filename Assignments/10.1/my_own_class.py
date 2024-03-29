# Student Name: Zihua Li
# Assignment 10.1: Your Own Class
# This script implement your own class based on a real-world object. You will write a class to
# meet certain requirements (detailed below) and write a short demo program in the main function that highlights
# all your class variables and methods.

class Dog:
    # Dog properties
    num_of_legs = 4
    has_legs = True

    # default dog is a German Shepard, color yellow and black, runs 5m/s
    def __init__(self, hair_color="Yellow and Black", breed="German Shepard", run_speed="5"):
        # Set hair color and breed and run_speed based on constructor arguments
        self.__hair_color = hair_color  # private
        self.__breed = breed  # private
        self.__run_speed = run_speed # private
        # Set position to start at 0
        self.__position = 0  # private

    def forward(self):
        # Change the position based on the speed
        self.__position += self.__speed

    def reverse(self):
        # Change the position based on the speed
        self.__position -= self.__speed

    def set_speed(self, speed):
        # Change the speed, but it can't be negative.
        if speed < 0:
            print("Speed cannot be less than zero.")
            raise ValueError
        else:
            self.__speed = speed

    def set_position(self, pos):
        # Set a new position, cannot be less than zero.
        if pos < 0:
            print("Position cannot be less than zero.")
            raise ValueError
        else:
            self.__position = pos

    def get_speed(self):
        return self.__speed

    def get_position(self):
        return self.__position

    # Magic methods
    def __str__(self):
        return (f"Dog: Hair Color - {self.__hair_color}, Breed = {self.__breed}, Run Speed - {self.__run_speed}, "
                f"Position - {self.__position}")

    def __int__(self):
        # int should return the position
        return (self.__position)


def main():
    # I want to create a dog that is a Golden Retriever, gold color and goes 4m/s.
    GoldenRetriever = Dog("Gold", "Golden Retriever", 4)
    default_dog = Dog()
    # set golden retriever's position to 5
    GoldenRetriever.set_position(5)
    print(GoldenRetriever.__str__())


if __name__ == "__main__":
    main()