from flask import Flask, render_template
import scrape_mars
import pymongo

app = Flask(__name__)

@app.route("/scrape")
def scrape():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn) 
    db = client.mars_data_db
    
    m_collection = db.data_mars

    mars_scrape = scrape_mars.scrape()
    print('app1.py line 16')
    m_collection.insert_one(mars_scrape)
    
    return render_template("index.html", scraped=mars_scrape)

if __name__ == "__main__":
    app.run(debug=True)