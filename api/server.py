from flask import Flask, request, send_file
import os
from flask_cors import CORS, cross_origin
from data.database import db
from models.fitter import Fitter
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'data/plot_data'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
db.init_app(app)

with app.app_context():
    db.create_all()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/fit', methods=['POST'])
@cross_origin()
def fit_data():
    fitter = Fitter()
    file = request.files['file']
    if file and allowed_file(file.filename):
        file_name = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, file_name))
        fitter.plot(f'./data/plot_data/{file_name}')
        image_path = f'plots/{file_name}.png'
        return send_file(image_path, mimetype='image/png')