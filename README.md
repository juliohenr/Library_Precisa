# Library_Precisa

## Resumo

Este projeto se trata de uma biblioteca virtual, o qual armazena em um banco de dados postgreSQL o nome do livro, o autor, volume e a edição. Também é armazenada a imagem da capa, porém a mesma é armazenada no servidor.

## Tecnologias Utilizadas

<ul>
<li>Python 3.7</li>
<li>Django</li>
<li>PostgreSQL</li>
<li>Jquery</li>
  
</ul>  


## Interfaces

a aplicação web possui 3 interfaces: A primeira interface exibe todos os livros separados por categoria, a segunda interface contém o descritivo de cada livro e é acionada pelo botão "leia mais", a terceira interface exibe o resultado da pesquisa. As interfaces desenvolvidas contém alguns elementos, os quais são: barra de pesquisa, carrosel de livros e botão "leia mais". Abaixo será exibido detalhes da tela.

### Interface 1 

![tela_principal1](https://user-images.githubusercontent.com/40969977/96358016-01424500-10d9-11eb-994f-b8e386af6481.png)


### Interface 2 

![tela_principal2](https://user-images.githubusercontent.com/40969977/96358054-6ac25380-10d9-11eb-977c-6de714d50277.png)


### Interface 3 

![tela_principal3](https://user-images.githubusercontent.com/40969977/96358071-8af21280-10d9-11eb-9eb8-e2fd0b0af8ec.png)

### Sugestões na barra de pesquisa

![sugestoes_pesquisa](https://user-images.githubusercontent.com/40969977/96358082-abba6800-10d9-11eb-85e5-3cdabf92ae03.png)


### Carrosel de livros

### Botão "leia mais"

## Execução 

É necessário a instalação das dependências através do comando "pip install -r requirements.txt". Após a instalação das dependências o usuário pode iniciar a aplicação através do comando "python manage.py runserver 3000". 

## Popular o banco

Na pasta POPULATE_DATA_BASE_EXAMPLE tem um script python "populate_data_base.py" para popular o banco de dados com alguns exemplos de livros 

## API para realização do CRUD

Na pasta COLLECTION_API possui a collection com todas as requisições necessárias para realização do CRUD no sistema

### Mostrar todos os livros (Requisição GET)

![get_all_books](https://user-images.githubusercontent.com/40969977/96358105-d99fac80-10d9-11eb-935a-5d387d508db8.png)


### Deletar todos os livros (Requisição GET)

![delete_all_books](https://user-images.githubusercontent.com/40969977/96358117-fe941f80-10d9-11eb-9499-3685ed5e931f.png)

### Adicionar um livro (Requisição POST)

![add_book_request1](https://user-images.githubusercontent.com/40969977/96358126-19669400-10da-11eb-94d5-30da2a3fab43.png)

![add_book_request4](https://user-images.githubusercontent.com/40969977/96358132-2f745480-10da-11eb-968b-7f649d93cef8.png)

### Atualizar um livro (Requisição POST)

![update_book_request](https://user-images.githubusercontent.com/40969977/96358138-4450e800-10da-11eb-939b-3156d84a919e.png)

### Deletar um livro (Requisição POST)

![delete_request](https://user-images.githubusercontent.com/40969977/96358159-5e8ac600-10da-11eb-8e6e-b2feea397a7f.png)

