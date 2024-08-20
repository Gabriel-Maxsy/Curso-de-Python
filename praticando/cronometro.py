import asyncio

# Função assíncrona para incrementar o timer
async def contador():
    timer = 0
    
    while timer <= 100:
        print('Tempo:', timer)
        await asyncio.sleep(0.12) # Espera 2 segundos de forma assíncrona
        timer += 1

# Executa a função assíncrona
asyncio.run(contador())