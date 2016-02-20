#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

"""
# CommandPattern.py
chap2

Client
  |
Invoker
  |
Recevier

"""

class Switch:
	"""The Invoker class"""

	def __init__(self, flipUpCmd, flipDownCmd):
		self.__flipUpCommand = flipUpCmd
		self.__flipDownCommand = flipDownCmd

	def flipUp(self):
		self.__flipUpCommand.execute()

	def flipDown(self):
		self.__flipDownCommand.execute()

class Light:
	"""The Recevier class"""
	def turnOn(self):
		print 'The light is on'

	def turnOff(self):
		print 'The light is off'

class Command(object):
	"""The Command Abstract class"""
	def __init__(self):
		pass

	def execute(self):
		# Override
		pass

class FlipUpCommand(Command):
	"""The Command class for turning on the light"""
	def __init__(self, light):
		# super(FlipDownCommand, self).__init__()
		self.__light = light

	def execute(self):
		self.__light.turnOn()

class FlipDownCommand(Command):
	"""The Command class for turning off the light"""
	def __init__(self, light):
		super(self.__class__, self).__init__()
		self.__light = light

	def execute(self):
		self.__light.turnOff()

class LightSwitch:
	"""The Client class"""
	def __init__(self):
		self.__lamp = Light()
		self.__switchUp = FlipUpCommand(self.__lamp)
		self.__switchDown = FlipDownCommand(self.__lamp)
		self.__switch = Switch(self.__switchUp, self.__switchDown)

	def switch(self, cmd):
		cmd = cmd.strip().upper()
		try:
			if cmd == 'ON':
				self.__switch.flipUp()
			elif cmd == 'OFF':
				self.__switch.flipDown()
			else:
				print "Argument ON or OFF is required"
		except Exception, e:
			print "'Exception : {}".format(e)


if __name__=='__main__':
	def main():
		lightSwitch = LightSwitch()
		print "Switch ON test."
		lightSwitch.switch("ON")
		print "Switch OFF test"
		lightSwitch.switch("OFF")
		print "Invalid Command test"
		lightSwitch.switch("****")

	main()


