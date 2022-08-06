class Computer:
    processor = ""
    ram = 1
    hard_drive = 1

    def __init__(self):
        pass
    
    def config(self, processor, ram, hard_drive):
        self.processor = processor
        self.ram = ram
        self.hard_drive = hard_drive

    def sys_config(self):
        print("Processor " + self.processor)
        print("Ram " + str(self.ram))
        print("Hard Drive " + str(self.hard_drive))


computer_1 = Computer()
computer_2 = Computer()
computer_3 = Computer()

computer_1.config("AMD Ryzen 5950X", 32, 2)
computer_1.sys_config()
print(type(computer_1))
print(type(computer_2))
