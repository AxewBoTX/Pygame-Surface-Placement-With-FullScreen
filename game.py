import pygame,os,time

class Game():
	def __init__(self):
		#Main Window
		pygame.init()
		pygame.font.init()
		self.main_width = 1200
		self.main_height = 700
		self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		pygame.display.set_caption("Window")

		#Game Assets
		self.FPS = 240
		self.running = True
		self.last_time = time.time()
		self.main_clock = pygame.time.Clock()
		self.font = pygame.font.Font("font.ttf",50)
		self.centre_font = self.font.render("CENTER",False,'white')
		self.bottom_right_font = self.font.render("Bottom Right",False,'white')
		self.top_right_font = self.font.render("Top Right",False,'white')
		self.bottom_left_font = self.font.render("Bottom Left",False,'white')
		self.top_left_font = self.font.render("Top Left",False,'white')
	def game_window(self):
		#Delta Time
		dt = self.last_time - time.time()
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('black')
		#Taking The Current Width And Height of the Window
		self.current_w = self.window.get_width()
		self.current_h = self.window.get_height()
		#Center text
		self.center_rect = pygame.Rect(
			self.current_w/2-self.centre_font.get_width()/2,
			self.current_h/2-self.centre_font.get_height()/2,
			self.centre_font.get_width(),self.centre_font.get_height())
		self.window.blit(self.centre_font,(self.center_rect.x,self.center_rect.y))
		#Top Left
		self.top_l_rect = pygame.Rect(
			0,0,
			self.top_left_font.get_width(),self.top_left_font.get_height())
		self.window.blit(self.top_left_font,(self.top_l_rect.x,self.top_l_rect.y))
		#Bottom Left
		self.bottom_l_rect = pygame.Rect(
			0,self.current_h-self.bottom_left_font.get_height(),
			self.bottom_left_font.get_width(),self.bottom_left_font.get_height())
		self.window.blit(self.bottom_left_font,(self.bottom_l_rect.x,self.bottom_l_rect.y))
		#Top Right
		self.top_r_rect = pygame.Rect(
			self.current_w-self.top_right_font.get_width(),0,
			self.top_right_font.get_width(),self.top_right_font.get_height())
		self.window.blit(self.top_right_font,(
			self.top_r_rect.x,self.top_r_rect.y))
		#Bottom Right
		self.bottom_r_rect = pygame.Rect(
			self.current_w-self.bottom_right_font.get_width(),
			self.current_h-self.bottom_right_font.get_height(),
			self.bottom_right_font.get_width(),self.bottom_left_font.get_height())
		self.window.blit(self.bottom_right_font,(
			self.bottom_r_rect.x,self.bottom_r_rect.y))

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				pygame.display.set_mode((
					self.main_width,self.main_height
				))
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)

		pygame.display.update()
		self.main_clock.tick(self.FPS)