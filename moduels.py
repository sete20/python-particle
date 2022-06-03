import m1 as firstModules
from m1 import sayHello
sayHello = sayHello('abdelrhman')
print(sayHello)


sayHello = firstModules.sayHowAreYou('abdelrhman')
print(sayHello)

import termcolor
import pyfiglet

# print(dir(pyfiglet))
print(pyfiglet.figlet_format('abdelrhman abdullah'))
print(termcolor.colored(pyfiglet.figlet_format('abdelrhman abdullah'),color='red'))