# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/GeLive-Cabinet-Stemware-Storage-Organizer/dp/B0BPKYBVLP/ref=pd_day0_d_sccl_1_2/136-6224998-4260658?pd_rd_w=ixHWX&content-id=amzn1.sym.a7884c93-a1a2-4015-9c73-22fb7d3b18fb&pf_rd_p=a7884c93-a1a2-4015-9c73-22fb7d3b18fb&pf_rd_r=8NH7K2CM4REMNY3QCS2S&pd_rd_wg=MYbzw&pd_rd_r=5e19a1a1-1fb1-4b25-98aa-c059de429ae0&pd_rd_i=B0BPKYBVLP&th=1")
# price_dollar = driver.find_element(By.CLASS_NAME , value ="a-price-whole" )
# price_cents = driver.find_element(By.CLASS_NAME , value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME , value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# ID
button = driver.find_element(By.ID , value = "submit")
# print(button.size)

# CSS - SELECTOR
documentation_link =driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# XPATH
link = driver.find_element(By.XPATH , value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(link.text)

driver.find_elements(By.CSS_SELECTOR) # select everything

# driver.close()
driver.quit()
