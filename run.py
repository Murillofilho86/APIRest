from app import app

#importando rotas
from app.routes import *

if __name__ == '__main__':
	app.run(port=8080, debug=True)