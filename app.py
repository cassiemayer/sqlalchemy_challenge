import datetime as dt
import numpy as np 
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

