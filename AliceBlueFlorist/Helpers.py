from faker import Faker
import time
import random


# driver sleep from 2 to 4 seconds
def delay():
    time.sleep(random.randint(3, 8))


fake = Faker()
url_Test = "https://www.aliceblueflorist.com/"
input_em = "(//input[@autocomplete='off'])[2]"
input_pas = "//input[@type='password']"
error_png = "aliceblueflorist_page_loading_error.png"
Title = "AliceBlue Florist"
key = 'https://meirbarshay_j1pXRy:9JNPeY1s7y8kdqqsyMQG@hub-cloud.browserstack.com/wd/hub'
logIn = "//span[@class='YT_9QV'][contains(.,'Log In')]"
sUp_withEmail = "//span[contains(.,'Sign up with email')]"
logEmail = "meir.bar.shay+9@gmail.com"
logPass = "1987365TY"



