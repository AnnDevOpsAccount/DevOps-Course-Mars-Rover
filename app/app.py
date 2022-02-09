from flask import Flask, render_template, request, redirect, url_for
import requests
import os


app = Flask(__name__)

@app.route('/')
def index():
    image_x = get_picture()
    return render_template('index.html', landing_image=image_x)


@app.route('/mars' , methods=['POST'])
def mars():
    #itemTitle = request.form.get('item-input')
    #add_item(itemTitle)        
    #return redirect(url_for('index'))
    



    image_x = 'https://upload.wikimedia.org/wikipedia/commons/4/47/American_Eskimo_Dog.jpg'
    
    #return redirect(url_for('index'))
    return (image_x)

def get_picture():

    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

    querystring = {"sol":"1000","camera":"fhaz","api_key": os.getenv("API_KEY")}

    response = requests.request("GET", url, params=querystring)
    resp = response.json()
    photos = resp['photos']
    
    return photos[0]['img_src']