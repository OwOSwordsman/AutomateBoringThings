import requests, bs4

def main():
    page = requests.get("https://www.weather.gov/")
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    print(soup.select("#topnews > div.body"))


if __name__ == "__main__":
    main()
