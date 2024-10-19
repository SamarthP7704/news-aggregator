from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def scrape_hackernews():
    # Start the Safari WebDriver
    driver = webdriver.Safari()
    
    # Open the Hacker News website
    driver.get('https://news.ycombinator.com/')
    
    # Wait for the articles to load, with a maximum wait of 30 seconds
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'titleline'))
        )
    except TimeoutException as e:
        print(f"Timeout Exception: {e}")
        print("Page source for debugging:")
        print(driver.page_source)  # Print the full page source
        driver.quit()
        return []
    except WebDriverException as e:
        print(f"WebDriver Exception: {e}")
        driver.quit()
        return []
    except Exception as e:
        print(f"Other Exception: {e}")
        driver.quit()
        return []

    articles = []
    
    # Find all article links by class name 'titleline'
    article_elements = driver.find_elements(By.CLASS_NAME, 'titleline')
    
    for item in article_elements:
        headline = item.text
        link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        # Append the headline and link to the articles list
        articles.append({
            'headline': headline,
            'summary': 'No summary available',
            'link': link
        })
    
    # Close the WebDriver
    driver.quit()

    # Print number of articles found
    print(f"Number of articles found: {len(articles)}")

    return articles


# Test the function
if __name__ == '__main__':
    news = scrape_hackernews()
    for article in news:
        print(f"Headline: {article['headline']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article['summary']}")
        print()
