from imports import *

def scrape_sports(url, driver_path='chromedriver.exe'):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)

    # Wait until the page is fully loaded
    WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Initialize lists to store scraped data
    titles = []
    links = []

    try:
        # Wait for the div elements to be present and visible
        if(url=="https://www.indiatoday.in/search/sports"):
            wait = WebDriverWait(driver, 20)
            
            # Attempt using CLASS_NAME
            divs = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'B1S3_content__wrap__9mSB6')))
            
            # Iterate through the found div elements and extract the desired data
            for div in divs:
                # Find the h3 tag within the div
                h3_tag = div.find_element(By.TAG_NAME, 'h3')
                titles.append(h3_tag.text)
                # Find the link within the h3 tag
                link = h3_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                links.append(link)
        elif(url=="https://indianexpress.com/section/technology/"):
            wait = WebDriverWait(driver, 20)
            ul_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'article-list')))
            li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
            for li in li_elements:
                h3_tag = div.find_element(By.TAG_NAME, 'h3')
                titles.append(h3_tag.text)
                # Find the link within the h3 tag
                link = h3_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                links.append(link)
        else:
            wait = WebDriverWait(driver, 20)
            divs = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'articles')))
            div=divs.find_elements(By.CLASS_NAME,'img-context')
            for div in divs:
            # Find the h3 tag within the div
                h2_tag = div.find_element(By.TAG_NAME, 'h2')
                titles.append(h3_tag.text)
            # Find the link within the h3 tag
                link = h2_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                links.append(link)



    except TimeoutException:
        print("Elements not found using CLASS_NAME. Trying XPath.")

        try:
            # Attempt using XPath
            divs = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="B1S3_B1__s3_widget__1S13T"]')))
            
            # Iterate through the found div elements and extract the desired data
            for div in divs:
                # Find the h3 tag within the div
                h3_tag = div.find_element(By.TAG_NAME, 'h3')
                titles.append(h3_tag.text)
                # Find the link within the h3 tag
                link = h3_tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
                links.append(link)
                
        except TimeoutException:
            print("Elements not found using XPath.")
    
    # Close the WebDriver
    driver.quit()
    
    return titles, links
