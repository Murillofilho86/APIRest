from app import app

@app.route('/')
def index():
	return "Hello, It's Work!"