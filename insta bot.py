from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import click


class InstaBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot = webdriver.Firefox(executable_path=r'C:\Users\user\Desktop\random\geckodriver.exe')
        

    def login(self):
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher/')
        time.sleep(3)
        username = bot.find_element_by_name('username')
        username.clear()
        username.send_keys(self.username)
        time.sleep(3)
        password = bot.find_element_by_name('password')
        password.clear()
        password.send_keys(self.password)
        time.sleep(3)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def likePosts(self,userName):
        count=0
        bot = self.bot
        time.sleep(2)
        bot.get(f'https://www.instagram.com/{userName}/?hl=en')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            posts = bot.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
            print(posts,links)
            for link in links:
                count=count+1
                bot.get(link)
                try:
                    div=bot.find_elements_by_class_name('dCJp8')
                    lov = [el.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click() for el in div]
                    time.sleep(3)
                except Exception:
                    pass
        #bot.close()    


@click.group()
def insta_cmd_group():
    pass


@insta_cmd_group.command(short_help = 'Give Your Username followed by whose User\'s Posts you wish to Like')
@click.argument('myusername',required = 1, default='kanhapatro37@gmail.com')
@click.argument('yourusername',required = 1, default = 'animalplanetindia')
@click.password_option()
def givelikes(myusername,yourusername,password):
    obj = InstaBot(myusername,password)
    obj.login()
    obj.likePosts(yourusername)

if(__name__ == '__main__'):
    insta_cmd_group()
