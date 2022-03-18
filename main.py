from engine import Engine

if __name__ == "__main__":
    # The client code.

    engine1 = Engine()
    engine2 = Engine()

    if id(engine1) == id(engine2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")