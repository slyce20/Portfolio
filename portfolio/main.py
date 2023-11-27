from flask import Flask
from home_page.routes import home_bp


app = Flask(__name__)
app.register_blueprint(home_bp)


app.run(debug=True)
