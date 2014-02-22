import pygame
import os
import ConfigParser

class App:
	def __init__(self):

		self.title = "Gamepad"
		self.window_size = (600, 429)
		self.running = True
		self.fps = 30

		# the axes
		self.axes = []
		self.num_axes = 0

		# buttons
		self.buttons = []
		self.num_buttons = 0

		# initializing pygame
		pygame.init()

		self.screen = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.clock = pygame.time.Clock()

		self.load_images()
		self.load_config()

		pygame.joystick.init()
		self.init_gamepad()
		self.run()

	def load_images(self):
		self.base_sprite = pygame.image.load(os.path.join("res", "base.png"))
		self.stick_sprite = pygame.image.load(os.path.join("res", "stick.png"))
		self.button_sprite = pygame.image.load(os.path.join("res", "button.png"))
		self.shoulder_left_sprite = pygame.image.load(os.path.join("res", "shoulder_left.png"))
		self.shoulder_right_sprite = pygame.image.load(os.path.join("res", "shoulder_right.png"))

	def load_config(self):
		# reading the configuration file
		self.config = ConfigParser.ConfigParser()
		if not self.config.read("config.txt"):
			raise IOError("Could not find 'config.txt'")

		# buttons mapping
		self.button_mapping = {
			"A": int(self.config.get("settings", "A")),
			"B": int(self.config.get("settings", "B")),
			"X": int(self.config.get("settings", "X")),
			"Y": int(self.config.get("settings", "Y")),
			"LB": int(self.config.get("settings", "LB")),
			"RB": int(self.config.get("settings", "RB")),
			"BACK": int(self.config.get("settings", "BACK")),
			"START": int(self.config.get("settings", "START")),
		}

		# axis mapping
		self.axis_mapping = {
			"LX": int(self.config.get("settings", "LX")),
			"LY": int(self.config.get("settings", "LY")),
			"RX": int(self.config.get("settings", "RX")),
			"RY": int(self.config.get("settings", "RY")) 
		}

		self.controller_id = int(self.config.get("settings", "ID"))

	def init_gamepad(self):
		try:
			self.gamepad = pygame.joystick.Joystick(self.controller_id)
			self.gamepad.init()

			# setting the window title
			name = self.gamepad.get_name()
			pygame.display.set_caption(self.title + ": " + name)

			# loading the axes and initializing the exes array
			self.num_axes = self.gamepad.get_numaxes()
			for i in range(self.num_axes):
				self.axes.append(0)

			# initialzing the buttons
			self.num_buttons = self.gamepad.get_numbuttons()
			for i in range(self.num_buttons):
				self.buttons.append(0)

		except pygame.error:
			print "No compatible input device was found!"

	# updating the axes
	def update_axes(self):
		for i in range(self.num_axes):
			axis = self.gamepad.get_axis(i)
			self.axes[i] = axis

	# updating all the buttons
	def update_buttons(self):
		for i in range(self.num_buttons):
			button = self.gamepad.get_button(i)
			self.buttons[i] = button

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

        		# checking for gamepad events
				if event.type == pygame.JOYBUTTONDOWN:
					self.update_buttons()

				if event.type == pygame.JOYBUTTONUP:
					self.update_buttons()

				if event.type == pygame.JOYAXISMOTION:
					self.update_axes()					

			self.render()
			self.clock.tick(self.fps)

	def render(self):
		self.screen.blit(self.base_sprite, (0, 0))

		# render buttons
		if self.buttons[self.button_mapping["A"]]:
			self.screen.blit(self.button_sprite, (445, 116))
		if self.buttons[self.button_mapping["B"]]:
			self.screen.blit(self.button_sprite, (489, 72))
		if self.buttons[self.button_mapping["X"]]:
			self.screen.blit(self.button_sprite, (401, 72))
		if self.buttons[self.button_mapping["Y"]]:
			self.screen.blit(self.button_sprite, (445, 27))
		if self.buttons[self.button_mapping["LB"]]:
			self.screen.blit(self.shoulder_left_sprite, (70, -13))
		if self.buttons[self.button_mapping["RB"]]:
			self.screen.blit(self.shoulder_right_sprite, (430, -13))
		if self.buttons[self.button_mapping["BACK"]]:
			self.screen.blit(self.button_sprite, (337, 74))
		if self.buttons[self.button_mapping["START"]]:
			self.screen.blit(self.button_sprite, (213, 74))

		# render stick
		self.screen.blit(self.stick_sprite, (self.axes[self.axis_mapping["LX"]] * 12 + 94, self.axes[self.axis_mapping["LY"]] * 12 + 54))
		self.screen.blit(self.stick_sprite, (self.axes[self.axis_mapping["RX"]] * 12 + 351, 157))
		# the right y axis doesnt work with my driver
		#self.screen.blit(self.stick_sprite, (self.axes[self.axis_mapping["RX"]] * 12 + 351, self.axes[self.axis_mapping["RY"]] * 12 + 157))

		pygame.display.flip()



# running the app
if __name__ == "__main__":
	App()
