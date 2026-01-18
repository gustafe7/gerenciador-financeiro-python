from datetime import datetime

def registrar_acao(tipo, mensagem):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("auditoria_financeira.log", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] {tipo} - {mensagem}\n")