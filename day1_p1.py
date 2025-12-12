

# Read in the file


# Create a counter for every 0 rotation
zeroCount = 0

class Notch:
    def __init__(self, value):
        self.value  = value
        self.left   = None #next
        self.right  = None #prev



class Dial:
    def __init__(self):
        self.home = None
        self.__current = None

    def reset(self):
        self.__current = self.home

    def getCurrent(self):
        return self.__current

    def addLeft(self, value):
        new_notch = Notch(value)
        if not self.home:
            new_notch.left = new_notch.right = new_notch
            self.home = new_notch
        else:
            # Grab home
            tmp = self.home
            
            # Iterate to the LEFT until at last value (when it loops)
            while tmp.left != self.home:
                tmp = tmp.left

            # Set the last notch's new left
            tmp.left = new_notch

            # Set the new notch's left (looped value) and right (tmp)
            new_notch.left = self.home
            new_notch.right = tmp
        
            # Set home's new right to nn
            self.home.right = new_notch

        # Reset current
        self.reset()

    def addRight(self, value):
        new_notch = Notch(value)
        if not self.home:
            new_notch.right = new_notch.left = new_notch
            self.home = new_notch
        else:
            # Grab home
            tmp = self.home

            # Iterate to the RIGHT until at last value (when it loops)
            while tmp.right != self.home:
                tmp = tmp.right

            # Set the last notch's new right
            tmp.right = new_notch

            # Set the new notch's right (looped value) and left (tmp)
            new_notch.right = self.home
            new_notch.left = tmp

            # Set home's new left to nn
            self.home.left = new_notch

        # Reset current
        self.reset()

    def doCmd(self, cmd):
        # Do a command that always follows this style:
        #           (R/L)(Numeric value of n length)
        direction = cmd[0]
        clicks = int(cmd[1:])

        if direction == "L":
            self.goLeft(clicks)
        elif direction == "R":
            self.goRight(clicks)

    def goLeft(self, clicks):
        # Go Left # of clicks
        if not self.home:
            print("Dial is empty")
            return
        else:
            tmp = self.__current
            for i in range(clicks):
                tmp = tmp.left
        
        # Set current to tmp
        self.__current = tmp
            
    def goRight(self, clicks):
        # Go Right # of clicks
        if not self.home:
            print("Dial is empty")
            return
        else:
            tmp = self.__current
            for i in range(clicks):
                tmp = tmp.right
        
        # Set current to tmp
        self.__current = tmp

    def setHome(self, new_value):
        # If no notches, return
        if not self.home:
            print("Dial is empty")
            return
        else:
            tmp = self.home
            while (tmp.value != new_value):
                tmp = tmp.right
                if tmp == self.home:
                    print("Value of : ", new_value, " does not exist within the Dial")
                    return
            
            self.home = tmp

    def spinLeft(self):
        # If no notches, return
        if not self.home:
            print("Dial is empty")
            return
        # Iterate over notches and print the values going left
        tmp = self.home
        while True:
            print(tmp.value, end=" -> ")
            tmp = tmp.left
            if tmp == self.home:
                print(self.home.value)
                break

    def spinRight(self):
        # If no notches, return
        if not self.home:
            print("Dial is empty")
            return
        # Iterate over notches and print the values going right
        tmp = self.home
        while True:
            print(tmp.value, end=" -> ")
            tmp = tmp.right
            if tmp == self.home:
                print(self.home.value)
                break


if __name__ == "__main__":
    # Create a dial with "home" being on value 50
    dial = Dial()
    for i in range(0, 100):
        dial.addLeft(i)
    dial.setHome(50)
    dial.reset()

    # Read in Cipher (day_1_input.txt) as a list of commands
    with open("P:\\gitrepos\\advent2025\\input\\day_1_input.txt", "r") as file:
        commands = file.read().splitlines()

    # Iterate over all commands
    counter = 0
    for cmd in commands:
        # Do the command
        dial.doCmd(cmd)

        # Check if the current notch is 0, increment if true
        if dial.getCurrent().value == 0:
            counter += 1

    # Print the solution for me to enter
    print(counter)


