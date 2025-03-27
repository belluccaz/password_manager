# 🔐 Password Manager

Um gerenciador de senhas simples e eficiente, desenvolvido com **Python** e **Tkinter**, utilizando conceitos de **Programação Orientada a Objetos (OOP)**.

## 📌 Funcionalidades

- **Gerador de Senhas Seguras** 🔑  
  - Gera senhas aleatórias e seguras, com letras, números e símbolos.
  - Copia automaticamente a senha para a área de transferência.
  
- **Armazenamento de Senhas** 💾  
  - Salva as senhas em um arquivo `data.txt`, junto com o site e e-mail associado.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍  
- **Tkinter** (Interface gráfica) 🎨  
- **pyperclip** (Copia a senha gerada automaticamente para a área de transferência) 📋  

## 🚀 Como Executar

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/seu-usuario/password-manager.git
   cd password-manager
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o programa**  
   ```bash
   python main.py
   ```

## 📁 Estrutura do Projeto

```
password-manager/
│── password_generator.py  # Classe para gerar senhas seguras
│── data_manager.py        # Classe responsável por salvar as senhas
│── ui.py                  # Interface gráfica do aplicativo
│── main.py                # Arquivo principal para rodar o app
│── data.txt               # Arquivo onde as senhas são salvas
│── logo.png               # Logo do aplicativo
│── requirements.txt       # Lista de dependências do projeto
│── README.md              # Documentação do projeto
```

## 📜 Licença

Este projeto é de código aberto e está licenciado sob a **MIT License**.
