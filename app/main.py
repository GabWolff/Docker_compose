from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql

app = FastAPI(title="API de Usuários", version="1.0.0")

def get_connection():
    return pymysql.connect(
        host="db",  # nome do serviço no docker-compose
        user="root",
        password="root",
        database="usuarios_db",
        cursorclass=pymysql.cursors.DictCursor
    )

class Usuario(BaseModel):
    nome: str
    email: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

@app.get("/")
def root():
    return {"status": "ok", "mensagem": "API rodando com MySQL 🚀"}

@app.get("/usuarios", response_model=list[UsuarioResponse])
def listar_usuarios():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, nome, email FROM usuarios")
        result = cursor.fetchall()
    conn.close()
    return result

@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = %s", (usuario_id,))
        result = cursor.fetchone()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return result