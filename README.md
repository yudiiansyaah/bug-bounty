# 🚀 Bug Bounty Scraper

![Bug Bounty Scraper](test.png)

Bug Bounty Scraper is a Python script designed to scrape information from websites that provide bug bounty programs or security news.

---

## ✨ Features

✔️ Scrapes data from specific websites.  
✔️ Saves output in **Text, CSV, or JSON** format.  
✔️ Uses **requests** and **BeautifulSoup4** for scraping.  
✔️ Displays colorful banners using **pyfiglet** and ANSI codes.  
✔️ Includes **retry logic** and **execution time limits**.  
✔️ Configurable **delay settings**.  

---

## 🚀 How to Use

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yudiiansyaah/bug-bounty.git
cd bug-bounty-scraper
```

### 2️⃣ Install Dependencies
```bash
pip install requests beautifulsoup4 pyfiglet lolcat
```

### 3️⃣ Run the Script

🔹 **Basic Usage (text output):**
```bash
python3 main.py --url <website_url>
```

🔹 **CSV Output:**
```bash
python3 main.py --url <website_url> --output csv --output_file output.csv
```

🔹 **JSON Output:**
```bash
python3 main.py --url <website_url> --output json --output_file output.json
```

🔹 **Custom Delay and Execution Time:**
```bash
python3 main.py --url <website_url> --delay 2 --time 15
```

> Replace `<website_url>` with the URL you want to scrape (e.g., `https://www.undira.ac.id`).

---

## 📝 Important Notes

🔹 Adjust the HTML tags in the `extract_news` function to match the structure of the website you're scraping.  
🔹 This script is intended for **educational purposes** only. Always comply with the **Terms of Service** of the websites you access. Do not overload servers with excessive scraping!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

💡 **Support this project by giving a ⭐ on the repository!** 🚀

