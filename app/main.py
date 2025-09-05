from app.db import get_collection
from app.crud import AlunoCRUD

def demo():
    col = get_collection()
    crud = AlunoCRUD(col)

    print("\n== CRUD DEMO ==\n")

    
    aluno = {"nome": "João", "idade": 20, "curso": "ADS"}
    inserted_id = crud.create(aluno)
    print(f"[CREATE] ID inserido: {inserted_id}")

    
    todos = crud.read_all()
    print(f"[READ] Todos os alunos: {todos}")

    
    qtd_att = crud.update({"nome": "João"}, {"idade": 21})
    print(f"[UPDATE] Documentos atualizados: {qtd_att}")

    
    joao = crud.read({"nome": "João"})
    print(f"[READ] João atualizado: {joao}")

    
    qtd_del = crud.delete({"nome": "João"})
    print(f"[DELETE] Documentos removidos: {qtd_del}")

if __name__ == "__main__":
    demo()
