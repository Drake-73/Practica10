from flask import Flask
import redis
import time

app = Flask(__name__)
cache = redis.Redis(host='redis-server', port=6379)

@app.route('/')
def get_data():
    val = cache.get('dato')
    if val:
        return val
    
    time.sleep(3)
    resultado = b"Datos procesados"
    cache.setex('dato', 60, resultado)
    return resultado

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
