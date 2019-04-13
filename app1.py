from flask import Flask
import scrape_mars
import pymongo

app = Flask(__name__)

@app.route("/scrape")
def scrape():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn) 
    db = client.mars_data_db
    
    m_collection = db.data_mars

    scraped = scrape_mars.scrape()
    m_collection.insert_one(scraped)
    
    return scraped