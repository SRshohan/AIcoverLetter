import requests
from bs4 import BeautifulSoup

def get_job_description(url):
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the div with data-automation-id="jobPostingDescription"
        description_div = soup.find('div', {'data-automation-id': 'jobPostingDescription'})
        
        if description_div:
            # Extract and return the text content of the div
            return description_div.get_text(strip=True)
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
