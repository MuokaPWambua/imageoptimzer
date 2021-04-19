from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from functions import save

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////images.db'
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Images(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    image = db.Column(db.Text)
    small = db.Column(db.Text)
    medium = db.Column(db.Text)
    large = db.Column(db.Text)
    x_large = db.Column(db.Text)
    
    def __init__(self, **kwargs):
        self.image = kwargs.get('image')    
        self.small = kwargs.get('small')
        self.large = kwargs.get('large')
        self.xlarge = kwargs.get('xlarge')
    

@app.route('/upload', methods=["POST"])
def upload():
    try:
        data = request.files
        file = data.get('image')
        image_urlpath = save(file)
        image = Images(image=image_urlpath[0], small=image_urlpath[1],
         medium=image_urlpath[2], large=image_urlpath[3], x_large=image_urlpath[4])
        db.session.add(image) 
        db.session.commit()
         
        return "add images"
    except Exception as e:
        print({'message': e})
        return "failed"


if __name__ == "__main__":
    db.create_all()
    app.run()