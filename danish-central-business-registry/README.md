# SCHWARZTHAL TECH Assignment

## DCBR web scraping
1. As mentioned in the assignment I went to the given webpage and decided to randomly scrap companies with the fields of 'address', 'CVR', 'Status', 'Business_type'. 
2. Made a simple parser to get this data in form of text and stored them in their individual containers
3. Used the url to find pattern between the pages and scrap them together
4. I kept the parser simple as it was not mentioned what data to scrap and how to format it. Fortunately no null or invalid values were encountered
5. If needed more complex parsing can be done by using pagination and web crawling & following links

## Technologies Used
1. Python3, scrapy
2. MongoDB

## How to run
1. Clone the github repository with code and extract it
2. Make sure you have ```python, scrapy and mongodb``` installed
3. Go to the main folder -> $ ```cd danish-central-business-registry/companyscraping```
4. To run the spider -> $ ```scrapy crawl buscom```
5. To store the output in XML/JSON/CSV -> $ ```scrapy crawl buscom -o item.xml/item.json/item.csv```
6. To check the database -> Download the mongoDB compass -> enter credentials -> connect to the database -> Refresh the page

## Difficulties
1. Intiially the webpage did not allow to scrap as it was against the ```robots.txt``` -> I disabled it, i.e set the ```ROBOTSTXT_OBEY = False``` in settings.py
2. 'Insert' method was not working and gave type error when trying to call it on the collection object -> I changed it to ```insert_one```
3. Tried to use google bot user agent and proxies to not breach any data privacy policy
4. Address filled is set in 2 lines with different CSS elements therefore it shows twice as much address as the other fields. 

## Output
1. Sample output during testing can be found in the item.csv and item.json file
2. Output from MongoDB can be found below

