import requests

# Se a url do site começar com "http://" siginifica que ele esta rodando na porta -> 80
# Se a url do site começar com "https://" siginifica que ele esta rodando na porta -> 443 (google por exemplo)

url = 'http://localhost:3333/'
response = requests.get(url)

print(response) # Se não especificar ele responde o status do "servidor/site"
print(response.status_code) # Responde o status do "servidor/site" 
print(response.headers) # Responde com o cabeçalho do "servidor"
# print(response.content) # Responde com o conteudo em bytes do servidor
# print(response.json()) Responderia com os dados que o servidor responder em json (o mais comum em sites externos)
print(response.text) # Responde com o conteudo do servidor em si (neste caso de exemplo responderá o html)