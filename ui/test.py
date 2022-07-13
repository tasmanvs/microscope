# Test out to see when __del__ is called

from time import sleep

class Foo:
    def __del__(self):
        print("Destructor called")

foo = Foo()


try:
    while(True):
        print ("Looping")
        sleep(1)
except KeyboardInterrupt:
    print("Keyboard interrupt")

sys.exit()