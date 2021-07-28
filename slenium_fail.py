from selenium import webdriver

PATH = '/home/jcamargo09678/MOSTEC CS Project/chromedriver_linux64.zip/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://www.adidas.com/us/nmd_r1-shoes/GX0997.html?forceSelSize=GX0997_610')