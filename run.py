from app import app

#importando rotas
from app.routes import *


#importando models
#As tabelas com relacionamento, devem obedecer a ordem de importancia
from app.models import endereco
from app.models import usuario


if __name__ == '__main__':
	app.run(port=8080, debug=True)