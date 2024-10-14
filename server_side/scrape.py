import requests
from bs4 import BeautifulSoup

def get_job_description(url):
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to find the job description using common tags and classes
        description = None
        
        # Try different common selectors to find the job description
        possible_selectors = [
            'div[class*="job-description"]',
            'div[id*="job-description"]',
            'div[class*="description"]',
            'div[id*="description"]',
            'section[class*="job-description"]',
            'section[id*="job-description"]',
            'section[class*="description"]',
            'section[id*="description"]',
            'article[class*="job-description"]',
            'article[id*="job-description"]',
            'article[class*="description"]',
            'article[id*="description"]',
            'div[data-automation-id="jobPostingDescription"]'
        ]
        
        for selector in possible_selectors:
            description_div = soup.select_one(selector)
            if description_div:
                description = description_div.get_text(strip=True)
                break
        
        if description:
            return description
        else:
            return "Job description not found."
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Main function to test the scraper
if __name__ == '__main__':
    # Example URL of the job posting
    url = "https://scholastic.wd5.myworkdayjobs.com/en-US/External/job/New-York-New-York/Software-Engineering-Intern_R13408"
    
    # Fetch and print the job description
    description = get_job_description(url)
    print(description)
