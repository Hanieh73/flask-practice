from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#name module above is the name of the file, which is the main file in this case

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ykihlfcp:ETF5-d1GaZ-G-kREoCa7vfnLhakUrleI@surus.db.elephantsql.com/ykihlfcp"
db = SQLAlchemy(app)


from application import routes #-> has to be imported here because otherwise if we do it in the top, it will not be defined and wil fail 

