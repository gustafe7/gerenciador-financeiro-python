# 💰 Gerenciador Financeiro em Python

Projeto desenvolvido em **Python** com foco em boas práticas de programação,
organização de código, persistência de dados e auditoria de ações.

O sistema funciona via **terminal**, permitindo o controle de receitas e despesas
de forma simples, clara e auditável.

---

## 🎯 Objetivo do Projeto

Permitir que o usuário:
- Registre receitas e despesas
- Consulte registros financeiros
- Visualize o saldo atual
- Tenha todas as ações auditadas (logs)

---

## 🚀 Funcionalidades

- Registro de receitas
- Registro de despesas
- Listagem de lançamentos
- Cálculo automático do saldo
- Sistema de auditoria de ações
- Persistência de dados em arquivo
- Logs com data, tipo de ação e descrição

---

## 🛡️ Sistema de Auditoria

O projeto possui um módulo de auditoria responsável por registrar todas as ações
realizadas no sistema.

### Ações auditadas:
- Registro de receitas
- Registro de despesas
- Erros de entrada (valores inválidos)
- Eventos importantes do sistema

### Exemplo de log:
Os registros são armazenados no arquivo `auditoria.log`.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Manipulação de arquivos
- Estruturas de dados (listas)
- Modularização
- Git e GitHub

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/gustafe7/gerenciador-financeiro-python.git
