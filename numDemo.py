#!/usr/bin/env python

import random

name = raw_input('Hello! What is your name?\n')

number = random.randint(1, 20)

print 'Hello, {0}'.format(name)


print 'The number is {0}'.format(number)
