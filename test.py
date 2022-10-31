import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Test(unittest.TestCase):
	def testName(self):
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		options.add_argument('--disable-dev-shm-usage')
		driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
		driver.get("http://localhost:31001/")
		h1 = driver.find_element("id","hello").text

		# verify text
		self.assertEqual("Hello Test World!", h1, "text is not matching")
if __name__ == "__main__":
	unittest.main()