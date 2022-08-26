from flask import Flask
from api.utils.functions import downloadFileIfNotAvailable

app = Flask(__name__)
print(__name__ + ' started')

downloadFileIfNotAvailable("TF-IDF.pkl")
downloadFileIfNotAvailable("ANN-N.h5")


from api import routes
