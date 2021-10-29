import pygame, sys
from screens.blank_screen import Blank

from buttons.image_button import ImageButton
from components.login_form import LoginForm
from buttons.text import Text

BG_COLOR = (255, 255, 255)

class MainScreen: 

    def __init__(self):
        self.width = 1380
        self.height = 800
        self.setup_screen()

        # objects init
        start_button = ImageButton(self.screen, 0, 0, "assets/imgs/cats.png", 1.5)
        exit_button = ImageButton(self.screen, 1200, 700, "assets/imgs/running_man.png", 0.2)
        user_text = Text(self.screen, 15, 15, "Not Logged in")
        balance_text = Text(self.screen, 15, 40, "")
        self.login_form = LoginForm(self.screen, 0, 600, 200, 45)
        
        self.components = { "start": start_button, "exit": exit_button, "user_text": user_text, "balance_text": balance_text }
        

        self.click = False
        self.running = True

        # once user is logged in, user object will contain user information
        self.user_object = {}
        
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill(BG_COLOR)

        for component in self.components.values():
            component.draw()

        #self.login_form.draw()
        pygame.display.update()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")

    def run(self):
        while self.running: 
            pos = pygame.mouse.get_pos()
            print(pos)

            self.draw()

            # if user successfully logged in
            if "success" in self.user_object:
                self.components["user_text"].setText(self.user_object["username"])
                self.components["balance_text"].setText("Balance: " + str(self.user_object["balance"]))

            if self.components["start"].collides(pos):
                if self.click:
                    Blank().run()
                    # self.setup_screen is to reset screen dimensions and window settings 
                    # after the other window closes
                    self.setup_screen()

            if self.components["exit"].collides(pos):
                if self.click:
                    pygame.quit()
                    sys.exit()

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)

    def handle_event(self, event):
        # if not logged in yet
        if "success" not in self.user_object: 
            self.user_object = self.login_form.handle_event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                self.click = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()