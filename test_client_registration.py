import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # This test case tests the path of least resistance
    def test_happy_path(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        """
        This dictionary holds parameters for every field in the Client Registration Form. Every key-pair is 1 field.
        'element ID or NAME': ['value to be populated', 'lookup element by NAME OR ID']
        TOS is handled separately.
        """
        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for success page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "SuccessPage"))
        )
        self.assertIn("Thanks for Registering!", driver.page_source)

    # This negative test case tests an invalid company name (in this case empty)
    def test_negative_company_name(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Legal Business Name is required.", driver.page_source)

    # This negative test case tests an invalid first name (in this case empty)
    def test_negative_first_name(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("First name is required.", driver.page_source)
    
    # This negative test case tests an invalid last name (in this case empty)
    def test_negative_last_name(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Last name is required.", driver.page_source)

    # This negative test case tests an invalid email (in this case empty)
    def test_negative_email_empty(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Please enter a valid email address.", driver.page_source)

    # This negative test case tests an invalid email (in this case without a domain)
    def test_negative_email_empty_domain(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['wasd','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Please specify a valid email domain.", driver.page_source)

    # This negative test case tests an invalid email (in this case with an invalid domain)
    def test_negative_email(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['awdawd@qweqw.f1f039yf0','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Please use a valid email address.", driver.page_source)

    # This negative test case tests an invalid country (In this case empty)
    # This should result in a success, as the field is prepopulated
    def test_negative_country_empty(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['Selenium', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "SuccessPage"))
        )
        self.assertIn("Thanks for Registering!", driver.page_source)

    # This negative test case tests an invalid state (in this case empty)
    def test_negative_state(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Company state is required.", driver.page_source)

    # This negative test case tests an invalid company type (in this case empty)
    def test_negative_company_type_empty(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Company type is required.", driver.page_source)

    # This negative test case tests an invalid company type (in this case invalid input)
    def test_negative_company_type(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Invalid Company Type','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = True)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("Company type is required.", driver.page_source)

    # This negative test case tests an unchecked tos agreement
    def test_negative_tos(self):
        driver = self.driver
        driver.get("https://exchange.sandbox.gemini.com/register/institution")

        registration_all_fields = {
            'company.legalName': ['Selenium', 'name'],
            'personal.legalName.firstName': ['', 'name'],
            'personal.legalName.middleName': ['Selenium', 'name'],
            'personal.legalName.lastName': ['Selenium', 'name'],
            'personal.email': ['email@gmail.com','name'],
            'countryDropdown': ['United States', 'id'],
            'stateDropdown': ['AZ', 'id'],
            'companyTypeDropdown': ['Broker-Dealer','id']
        }
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "company.legalName"))
        )
        
        ClientRegistrationTest.complete_form(driver, registration_all_fields, tos = False)

        # Wait for alert error
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Alert.error"))
        )
        self.assertIn("User Agreement is required.", driver.page_source)

    # Cleanup function
    def tearDown(self):
        self.driver.close()

    # Helper Functions
    #===================================================================================
    # This helper function populates the entire form and submits it
    # It reads from a dictionary argument which holds values for each field.
    @staticmethod
    def complete_form(driver, registration_all_fields, tos):
        # Populates text fields
        for element_lookup, value in registration_all_fields.items():
            if value[1] == 'name':
                ClientRegistrationTest.field_input(element_lookup, driver, value[0], name = True)
            elif value[1] == 'id':
                ClientRegistrationTest.field_input(element_lookup, driver, value[0], id = True)

        # Check TOS checkbox
        if tos:
            driver.find_element(By.XPATH, "//*[@id='container']/div/div/div[2]/div/div[2]/form/span/div/label/span").click()
        
        # Submit form
        driver.find_element(By.XPATH, "//*[@id='container']/div/div/div[2]/div/div[2]/form/div/button").submit()

    # This helper function populates a field.
    @staticmethod
    def field_input(element_lookup, driver, input, name = False, id = False):
        if name:    
            elem = driver.find_element(By.NAME, element_lookup)
            elem.clear()
            elem.send_keys(input)
        elif id:
            elem = driver.find_element(By.ID, element_lookup)
            elem.clear()
            elem.send_keys(input)
            elem.send_keys(Keys.RETURN)    
  

if __name__ == "__main__":
    unittest.main()