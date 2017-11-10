from app import app

#importando rotas
from app.routes import *


#importando models
from app.models import usuario

if __name__ == '__main__':
	app.run(port=8080, debug=True)