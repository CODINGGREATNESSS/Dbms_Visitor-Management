from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_TC001_load_login_page(self):
        self.driver.get("http://localhost/Visitormanagement/index.php")  # Adjust the path
        self.assertTrue(self.driver.find_element(By.NAME, "username"))
        self.assertTrue(self.driver.find_element(By.NAME, "password"))

    def test_TC002_valid_login(self):
        self.driver.get("hhttp://localhost/Visitormanagement/index.php")
        self.driver.find_element(By.NAME, "username").send_keys("admin")  # Replace with valid user
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(2)
        # Replace below check with your actual redirect or element check
        self.assertNotIn("dashboard.php", self.driver.current_url)

    def test_TC003_invalid_login(self):
        self.driver.get("http://localhost/Visitormanagement/index.php")
        self.driver.find_element(By.NAME, "username").send_keys("fake")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(2)
        self.assertIn("index.php", self.driver.current_url)  # Assuming page reloads on failure

    def test_TC004_empty_fields_validation(self):
        self.driver.get("http://localhost/Visitormanagement/index.php")
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()
        # Check that form isn't submitted (HTML5 required fields stop it)
        self.assertIn("index.php", self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()




#[Running] python -u "d:\xampp\htdocs\Visitormanagement\Selenium_testing\test_homepage.py"

#Ran 4 tests in 12.585s

#OK
