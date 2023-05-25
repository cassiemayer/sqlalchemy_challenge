import datetime as dt
import numpy as np 
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup 

engine = create_engine("sql:///hawaii.sqlite")

# Reflect an exisiting database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
#Save reference to table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session
session = Session(engine)

#Flask setup
app = Flask(__name__)

#Flask route
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f""
        
    )
