import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/Visitormanagement/dashboard.php")

    def tearDown(self):
        self.driver.quit()

    def test_TC001_page_load(self):
        """TC001: Verify that the login page loads successfully."""
        self.assertIn("Login", self.driver.title)

    def test_TC002_valid_login(self):
        """TC002: Verify user can login with valid credentials."""
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login"))
        ).click()

        # Add validation for a successful login
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))  # change as per your dashboard page
        )
        self.assertIn("Dashboard", self.driver.page_source)

    def test_TC003_invalid_login(self):
        """TC003: Verify login fails with invalid credentials."""
        self.driver.find_element(By.NAME, "username").send_keys("wronguser")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login"))
        ).click()

        # Expect an error message (adjust text or locator as per your design)
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        self.assertIn("Invalid", error_message.text)

    def test_TC004_empty_fields_validation(self):
        """TC004: Verify validation when username and password fields are empty."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login"))
        ).click()

        # Add assertion for error message or page behavior
        validation_message = self.driver.find_element(By.CLASS_NAME, "alert-danger")
        self.assertIn("required", validation_message.text.lower())

