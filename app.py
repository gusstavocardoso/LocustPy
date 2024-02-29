from flask import Flask
from api.routes import album_api

app = Flask(__name__)
app.register_blueprint(album_api)

if __name__ == "__main__":
    app.run(debug=True)
