import time
import random
from faker import Faker

fake = Faker()
url_Test = "https://www.aliceblueflorist.com/"
input_em = "(//input[@autocomplete='off'])[2]"
input_pas = "//input[@type='password']"
error_png = "aliceblueflorist_page_loading_error.png"
Title = "AliceBlue Florist"


# driver sleep from 2 to 4 seconds
def delay():
    time.sleep(random.randint(2, 4))
