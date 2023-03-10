import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# inherit TestCase Class and create a new test class
class PythonOrgSearch(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Edge()
 
    # Test case method. It should always start with test_
    def test_search_in_python_org(self):
         
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("https://www.google.com")
 
        # assertion to confirm if title has python keyword in it
        self.assertIn("Google", driver.title)
 
        # locate element using name
        elem = driver.find_element("name","q")
 
        # send data
        elem.send_keys("Birds")
 
        # receive data
        elem.send_keys(Keys.RETURN)
        self.assertIn("Birds",driver.page_source)
 
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()