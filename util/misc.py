import machine
import os

machine.freq(240000000)

class REPL:
    def __init__(self):
        self.running = True

    def start(self):
        print("MicroPython REPL started. Type 'exit()' to exit.")
        while self.running:
            try:
                command = input(">>> ")
                if command.strip() == "exit()":
                    self.running = False
                else:
                    exec(command)
            except OSError as e:
                print("Error: {}".format(e))

    def stop(self):
        self.running = False
        print("MicroPython REPL stopped.")