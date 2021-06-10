from selenium import webdriver
from selenium.webdriver.support.ui import Select
import undetected_chromedriver as uc
from Models.Cookies import Cookies
from Models.Address import Address
import time


class Load:

    def __init__ (self, account, proxy, url):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = uc.Chrome(options=options)
        #self.ck = Cookies()
        self.add = Address()
        self.base_url = "https://www.innvictus.com/"
        self.account = account
        self.proxy = proxy
        self.url = url



    def Proccess(self):

        # INICIALIZAR LOS COOKIES PARA AGILIZAR EL PROCESO
        #self.setCookies()
        
        self.driver.get(self.url)

        # SE DA CLICK EN EL BOTON DE COMPRAR AHORA
        self.handleClicks('//*[@id="notPreorderInfoSection"]/a[1]')

        # SE DA CLICK EN EL BOTON DE CONTINUAR COMPRA
        self.handleClicks('//button[@class="btn btn-checkout btn-block btn-small btn--continue-checkout btn-fix-size js-continue-checkout-button"]')

        #SE HACE EL PROCESO DE LOGIN
        self.handleLogin()

        #SE DA CLICK EN CONINUAR
        self.handleClicks('//*[@id="addressSubmit"]')

        # SE COMPLETAN LOS INPUT
        #time.sleep(3)
        self.handleAddress()

        self.handleClicks('//*[@id="deliveryMethodSubmit"]')

        print("Finished")

    '''    
    def setCookies(self):
        # BASE URL
        self.driver.get(self.base_url)

        # ELIMINAR LAS COOKIES EXISTENTES
        self.driver.delete_all_cookies()

        # Load cookies
        for p in self.ck.getCookies():
            self.driver.add_cookie({'name': p.name, 'value': p.value})
    '''

    def handleLogin(self):
        #self.driver.get(self.urlLogin)
        layout = [
            {
                'field_name': 'j_username',
                'type': 'text'
            },
            {
                'field_name': 'j_password',
                'type': 'password'
            }
        ]
        time.sleep(1)
        for p in layout:
            element = self.driver.find_element_by_name(p['field_name'])
            if p['type'] == 'text':
                element.send_keys(self.account.username)
            elif p['type'] == 'password':
                element.send_keys(self.account.password)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[6]/button').click()


    def handleClicks(self, xpath):
        while True:
            try:
                self.driver.find_element_by_xpath(xpath).click()
                break
            except Exception as e:
                pass

    def handleAddress(self):
        '''
            regionIso   MX-22
            townCity    Querétaro
        '''

        layout = [
            {
                'field_name': 'firstName',
                'type': 'text',
                'value': 'name'
            },
            {
                'field_name': 'lastName',
                'type': 'text',
                'value': 'lastname'
            },
            {
                'field_name': 'displayName',
                'type': 'text',
                'value': 'add2'
            },
            {
                'field_name': 'phone',
                'type': 'number',
                'value': 'telephone'
            },
            {
                'field_name': 'line1',
                'type': 'text',
                'value': 'add1'
            },
            {
                'field_name': 'numExterno',
                'type': 'number',
                'value': 'num_ext'
            },
            {
                'field_name': 'numInterno',
                'type': 'number',
                'value': 'num_int'
            },
            {
                'field_name': 'entrecalles',
                'type': 'text',
                'value': 'entre'
            },
            {
                'field_name': 'colonia',
                'type': 'text',
                'value': 'add2'
            },
            {
                'field_name': 'postcode',
                'type': 'number',
                'value': 'cp'
            },
            {
                'field_name': 'regionIso',
                'type': 'select',
                'value': 'region'
            },
            {
                'field_name': 'townCity',
                'type': 'select',
                'value': 'ciudad'
            }
        ]

        form = self.add.getAddress()[0]

        for p in layout:
            time.sleep(1)
            element = self.driver.find_element_by_name(p['field_name'])
            txt = form.__getattribute__(p['value'])
            if p['type'] == 'text' or p['type'] == 'number':
                element.send_keys(txt)
            elif p['type'] == 'select':
                Select(element).select_by_value(txt)
                print(txt)

        self.handleClicks('//*[@id="addressSubmit"]')
