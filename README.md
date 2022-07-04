# Desafio MVP - Django Rest Framework

## Requisitos do MVP ✏️
O desafio consta a criação de uma API REST utilizando Django e Django Rest Framework como Backend. Não será necessária a criação de um Client para consumir os endpoints. A validação será feita através de uma coleção de chamadas no Postman.

### Uma Demanda é composta por:
* Descrição da peça que está sendo solicitada
* Endereço de Entrega
* Informações de Contato
* Anunciante (Usuário Dono)
* Status de Finalização (Aberta ou Finalizada)

Devem existir dois tipos de usuário: um Administrador e um Anunciante. O Administrador tem acesso a todos as demandas criadas no sistema, enquanto o Anunciante possui apenas permissão para visualização e manipulação de suas próprias demandas.

### As seguintes ações devem ser disponíveis para um usuário do tipo Anunciante, através de uma API REST:
* Criação de uma Demanda
* Listagem de Demandas
* Edição de Demanda
* Exclusão de Demanda
* Finalização de uma Demanda

O Administrador, através do admin, deve ser capaz de visualizar as Demandas cadastradas na plataforma com todas as suas informações presentes na listagem. Em especial, o Status de Finalização deve ser representado como uma imagem.

---

# Build do projeto 🔨
Utilizando Docker, ao clonar o repositório faça o build da imagem com o comando:
```
docker build -t demanda-project . 
```
Após realizar o build, rode o container com o comando:
```
docker compose up
```

---

# Rodando projeto com Django 🧑‍💻
Acesse o gerenciador de pacotes venv:
```
source venv/bin/activate
```
Rode o projeto:
```
python manage.py runserver
```