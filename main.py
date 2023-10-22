# Servidor Web muito bom e Free heroku
# https://www.heroku.com/
'''
- Render - https://render.com
- Railway -https://railway.app
- Cyclic - https://cyclic.sh

🔗 Site oficial Netlify: https://www.netlify.com/
🔗 Site oficial Caprover: https://caprover.com/
🔗 Site oficial Catalyst: https://catalyst.zoho.com/
'''

# Comando para verificar o que está instalado no seu projeto
# pip freeze
# pip freeze > requirements.txt

# criar um ambiente virtual no python
# python -m venv virtualmxs

# para ativar o amb. virtual
# .\virtualmxs\Scripts\Activate.ps1
# . 'C:\Users\Mxs-Desktop\Desktop\projWeb\venv\Scripts\Activate.ps1'
# .\env\Scripts\Activate.ps1 ---- aqui pelo powershell
# .\env\Scripts\Activate.bat ---- aqui pelo DOS
# se der erro, tem que liberar o powershell como adm e digitar o comando abaixo
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# e confirmar com S
# para desativar digite: deactivate




import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")
