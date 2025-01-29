import requests
from bs4 import BeautifulSoup
import argparse
import time
import random
import csv
import json
from banners import bug_bounty_banner, created_by_banner
import datetime

def fetch_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None


def extract_news(html_content, url):

    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    news_items = []

    news_container = soup.find('div', id="news-container")
    if not news_container:
        print ("Could not find news container")
        return []

    for item in news_container.find_all('div', class_='news-item'):
        a_tag = item.find('a')

        if a_tag:
            link = a_tag['href']
            title_element = item.find('h2', class_='news-title')
            if title_element:
                title = title_element.text.strip()
                news_items.append({"title": title, "link": link})

    return news_items


def output_data(news_items, output_format="text", output_file=None):
    if output_format == "csv":
        if not output_file:
            print("Output file is required for csv format")
            return
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = news_items[0].keys() if news_items else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(news_items)
        print(f"Data written to {output_file}")
    elif output_format == "json":
        if not output_file:
            print("Output file is required for json format")
            return
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(news_items, jsonfile, indent=4)
        print(f"Data written to {output_file}")
    else: 
        if not news_items:
            print("No news items found")
            return

        for item in news_items:
            print("--------------------")
            for key,value in item.items():
                print(f"{key}: {value}")

def main():
    parser = argparse.ArgumentParser(description="Find news on a website.")
    parser.add_argument("--url", type=str, help="URL to target website", required=True)
    parser.add_argument("--output", type=str, help="Output format (text, csv, json). Default text", default='text')
    parser.add_argument("--output_file", type=str, help="Output file name for csv or json output.")
    parser.add_argument("--delay", type=int, help="Delay between requests in seconds (optional).", default=1)
    parser.add_argument("--time", type=int, help="Maximum time to wait before exiting.", default=10)

    args = parser.parse_args()

    url = args.url
    news = [] 

    print(bug_bounty_banner()) 
    print(created_by_banner()) 
    start_time = datetime.datetime.now()
    while True:
        html_content = fetch_html(url)
        if html_content:
            news = extract_news(html_content, url)
            if news:
                print("News Headlines:")
                for item in news:
                    print(f"- {item['title']} (Link: {url}{item['link']})")
            else:
                print("No news items found.")
            output_data(news, args.output, args.output_file)
            break 
        else:
            current_time = datetime.datetime.now()
            time_elapsed = (current_time - start_time).total_seconds()
            if time_elapsed >= args.time:
                print(f"Time limit of {args.time} seconds reached. Exiting...")
                break;
            print(f"Waiting for {args.delay} seconds before retrying...")
            time.sleep(args.delay)
            
            args.delay += random.randint(0, 2)


if __name__ == "__main__":
    main()
