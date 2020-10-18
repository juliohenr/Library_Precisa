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

### Interface 1 completa

### Interface 2 completa

### Interface 3 completa

### Sugestões na barra de pesquisa

### Carrosel de livros

### Botão "leia mais"

## Execução 

É necessário a instalação das dependências através do comando "pip install -r requirements.txt". Após a instalação das dependências o usuário pode iniciar a aplicação através do comando "python manage.py runserver 3000". 

## Popular o banco

Na pasta POPULATE_DATA_BASE_EXAMPLE tem um script python "populate_data_base.py" para popular o banco de dados com alguns exemplos de livros 

## API para realização do CRUD

Na pasta COLLECTION_API possui a collection com todas as requisições necessárias para realização do CRUD no sistema

### Mostrar todos os livros (Requisição GET)
### Deletar todos os livros (Requisição GET)
### Adicionar um livro (Requisição POST)
### Atualizar um livro (Requisição POST)
### Deletar um livro (Requisição POST)


