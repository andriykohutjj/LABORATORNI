class EmptyClass:
    def __init__(self):
        pass

    def iterate_and_print(self):
        for i in range(11):
            dynamic_number = i  
            print("Параметр динамічний номер:", dynamic_number)

my_instance = EmptyClass()
my_instance.iterate_and_print()
