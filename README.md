# 🐍 Automação de Formulários com Python  

Este projeto foi desenvolvido durante a **Jornada Python da Hashtag Treinamentos** e tem como objetivo explorar duas abordagens diferentes para automação de tarefas repetitivas em páginas web: **PyAutoGUI** e **Selenium**.  

## 📌 Objetivo  
Automatizar o preenchimento de um formulário de produtos a partir de uma base de dados (`produtos.csv`), comparando duas técnicas:  
- **PyAutoGUI** → automação de interface (movendo o mouse, clicando em posições fixas).  
- **Selenium** → automação web (interagindo diretamente com elementos HTML).  

---

## 🚀 Tecnologias utilizadas  
- Python 3
- Pandas  
- PyAutoGUI  
- Selenium  
- Navegador **Firefox** 

---

## 📂 Estrutura do projeto  

```
automation-jornada-python/
│── bot_pyautogui.py   # Automação utilizando PyAutoGUI
│── bot_selenium.py    # Automação utilizando Selenium
│── produtos.csv       # Base de dados dos produtos
│── README.md          # Documentação do projeto
│── requirements.txt   # Dependências
```

---

## ▶️ Como executar  

### 1. Clone o repositório  
```bash
git clone https://github.com/Mariana-RDS/automation-jornada-python.git
cd automation-jornada-python
```

### 2. Crie um ambiente virtual (opcional)  
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências  
```bash
pip install -r requirements.txt
```

### 4. Execute a automação  

#### Usando PyAutoGUI  
```bash
python bot_pyautogui.py
```

#### Usando Selenium  
```bash
python bot_selenium.py
```