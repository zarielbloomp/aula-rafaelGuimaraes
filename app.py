from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def ola_mundo():
    return "<p> Ola mundoa </p>"

@app.get("/teste")
def teste():
    return{'teste': 'teste'}
@app.get('/aluno')
def aluno():
    return{'nome': 'miguel', 'turma': 'imi3'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000) 