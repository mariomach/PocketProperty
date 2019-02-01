import pandas as pd
from flask import Flask, render_template, request

df = pd.read_csv('house.csv')
print(len(df)) # to get number of listings 

df = df.iloc[0:349,:] 

home = df.to_dict('list') #store dataframe into a dictionary form that can be read by JS

#Data attribute of a home
address = home['ADDRESS'][:]
price = home['PRICE'][:]
propertytype = home['PROPERTY TYPE'][:]
beds = home['BEDS'][:]
baths = home['BATHS'][:]
squareft = home['SQUARE FEET'][:]
lotsize = home['LOT SIZE'][:]
yearbuilt = home['YEAR BUILT'][:]
location = home['LOCATION'][:]
url = home['URL'][:]


#Using Flask to pass data into the webpage 
app = Flask(__name__)

@app.route('/')
def hello_world():

	#Passing the attributes to index.html
	return render_template('index.html', home=home, address=address, price=price,
		propertytype=propertytype, beds=beds, baths=baths, squareft=squareft, 
		lotsize=lotsize, yearbuilt=yearbuilt, location=location, url=url)

if __name__ == '__main__':
 	app.run(threaded=True)
