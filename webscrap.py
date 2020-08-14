import requests, bs4, csv
 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
page = requests.get("https://www.investing.com/currencies/eur-usd-historical-data", headers = headers)
 
soup = bs4.BeautifulSoup(page.content,'html.parser')
 
results_table = soup.find(id = 'results_box')
 
dates = results_table.find_all(class_="first left bold noWrap")
 
length = len(dates)
info = results_table.find_all('td')
 
cost = info[1:length*6+1:6]
final = []
 
with open('final.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
 
    for i in range(length):
        filewriter.writerow([dates[i].get_text(), cost[i].get_text()])