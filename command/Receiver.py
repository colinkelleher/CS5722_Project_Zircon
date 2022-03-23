'''
Receiver Class

- Business Logic - where actions can be carried out
'''
class Receiver:
    def completeTask2(self, b:str) -> tuple[str, str]:
        return ("Receiver working on", b)


    def completeTask1(self, a:str) -> None:
        print("Receiver working on",a)