
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random




class Client:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag 
        self.driver = webdriver.Firefox(executable_path=r"C:/Users/usuario/Desktop/geckodriver-v0.30.0-win64/geckodriver.exe")
      

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
 
        
        

        userForm = driver.find_element_by_xpath("//input[@name='username']")
        userForm.click()
        userForm.clear()
        userForm.send_keys(self.username)

        passwordForm = driver.find_element_by_xpath("//input[@name='password']")
        passwordForm.click()
        passwordForm.clear()
        passwordForm.send_keys(self.password)
        passwordForm.send_keys(Keys.RETURN)
        print('[Etapa 1] - Usuario logado')
        time.sleep(5)
        self.sendComentary()

    @staticmethod
    def slowTyping(sentence, typingArea, commentSent):
  
        for letter in sentence:
            typingArea.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)



    def sendComentary(self):
        exploreLinks = []
        commentSent = 0
        driver = self.driver
        hashtag = self.hashtag
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        print("[Etapa 2] - redirecionando para o explore")
        time.sleep(5)

        for i in range(1, 10): 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print("[Etapa 3] - Foi encontrado" + str(len(pic_hrefs)) + "links em " + hashtag)

        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    exploreLinks.append(link)
            except:
                pass

# comentado nas fotos
        for nowLink in exploreLinks:
            driver.get(nowLink)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
           
            try:
                comments = [
                    "comentario 1",
                    "comentario 2",
                    "comentario 3"
                ] 
                driver.find_element_by_class_name("Ypffh").click()
                commentBox = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.slowTyping(random.choice(comments), commentBox, commentSent)
              
                driver.find_element_by_xpath("//html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button").click()
                time.sleep(random.randint(20, 30))
            except Exception as e:
                print(e)
                time.sleep(5)

# Entre com o usuário e senha aqui
bot = Client("user", "senha", "tag")
bot.login()
