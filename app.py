from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def ola_mundo():
    return "<p> Ola mundoa </p> <style> color: blue </style>"

@app.get("/teste")
def teste():
    return{'teste': 'teste'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000) 