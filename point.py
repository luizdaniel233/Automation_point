from datetime import datetime
import time
from send_email import send_email
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class automation_point:

    def automation(self):

        nav = webdriver.Chrome(ChromeDriverManager().install())
        nav.get("https://cliente.apdata.com.br/conecthus/")

        WebDriverWait(nav,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[4]/div/div/a'))).click()
        WebDriverWait(nav,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[3]/div[4]/input'))).send_keys("600744")
        WebDriverWait(nav,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[3]/div[5]/input'))).send_keys("Luiz@1234")
        WebDriverWait(nav,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div/input[1]'))).click()
        date = datetime.now()
        msg = f'Automation Sucessfull,point ready at {date}'
        sts = 'OK'
        send_email.enviar_email(self,msg,sts)
        time.sleep(3)
        nav.quit()

exec = automation_point()
send = send_email()

try:
    #function to access page web and input datas and execute.
    exec.automation()

except WebDriverException:
    # send email to me,report error in automation
    date = datetime.now()
    msg = f'Error in automation at {date}'
    sts = "ERROR"
    send.enviar_email(msg,sts)
