# Relatório do Projeto: Sistema de Gestão de Publicações Científicas
## Autor: Maria Pinheiro A97304

## Descrição Geral
Este projeto consiste no desenvolvimento de um sistema em **Python** para a criação, atualização e análise de publicações científicas. O objetivo principal é permitir a gestão eficiente de um dataset de artigos e a geração de métricas e relatórios detalhados sobre as publicações e os seus autores.

Este projeto foi dividido em duas parte essenciais: uma linha de comandos e uma interface utilizando **PySimpleGUI**.

## Linha de Comandos

### Funcionalidades Principais
1. **Criação de Publicações**:
   - Inserir novos registos de publicações científicas no sistema.

2. **Consulta de Publicações**:
   - Consultar uma publicação através de um identificador específico, podendo este ser qualquer um dos elementos pertencentes à mesma. Quando for encontrada uma publicação com o identificador escolhido, as informações desta serão exibidas.
   - Listar legivelmente todas as publicações no sistema.

3. **Gestão de Publicações**:
    - Eliminar uma publicação através de um identificador específico, podendo este ser qualquer um dos elementos pertencentes à mesma.

3. **Relatórios de Estatística**:
   - Gerar um relatório de publicações por ano, e o gráfico correspondente.

4. **Gestão do Dataset**:
   - Ler os dados de um ficheiro JSON para a informação em memória.
   - Guardar a informação em memória num ficheiro JSON.

5. **Menu de Ajuda**
    - Lista as funcionalidades do sistema

### Funcionamento da Linha de Comando
A linha de comando funciona através de uma função principal `menu()`, onde cada ação tem um número atribuído. Consuante as intenções do utilizador, este deverá escolher o número correspondente à ação desejada. Abaixo encontram-se as opções disponíveis na linha de comando.
```
(1) Ajuda
(2) Criar Publicação
(3) Consulta de Publicação
(4) Consultar Publicações
(5) Eliminar Publicação
(6) Relatório de Estatísticas de Publicações por Ano
(7) Listar Autores
(8) Importar Publicações
(9) Guardar Publicações
(0) Sair
```                      
* Opção 1 - Corresponde ao menu de ajuda, que explica em detalhe o que cada funcionalidade faz.
* Opção 2 - Cria uma nova publicação através da função `insertNew(dataset)`. Quando esta opção é selecionada, é perguntado ao utilizador que informação colocar em cada campo da publicação, e após isto, esta é adicionada à informação em memória.
* Opção 3 - Permite a consulta de uma publicação através de um dos campos da mesma utilizando a função `findPost(key, info, dataset)`. O utilizador deve selecionar qual dos campos vai identificar a ata, e, após isto, caso uma ata seja encontrada, a mesma vai ser listada no terminal.
* Opção 4 - Permite, através da função `listPosts(dataset)` a consulta de todas as publicações do sistema, sendo que apenas o título, data, e keywords são listadas.
* Opção 5 - Elimina uma publicação através da função `deletePost(key targetInfo, dataset)`. Quando esta opção é selecionada, é perguntado ao utilizador qual o campo pelo qual a ata deve ser identificada, e, qual a informação que corresponde a esse campo. Se uma ata for encontrada dentro dos resquisitos, a mesma será eliminada da informação em memória.
* Opção 6 - Mostra, utilizando a função `postsPerYear(dataset)` o relatório de estátisticas de quantas atas foram publicadas por ano, e mostra também o gráfico correspondente, feito através da biblioteca *matplotlib*.
* Opção 7 - Lista os autores do sistema e os títulos das publicações feitas pelos mesmos utilizando a função `listAuthors(dataset)`.
* Opção 8 - Importa publicações de um ficheiro JSON com recurso à função `loadFile(fname)`. Neste caso, o utilizador tem a opção de adicionar as publicações importadas à informação em memória, ou substituir a informação em memória pela informação do ficheiro.
* Opção 9 - Atualiza o ficheiro `ata_medica_papers.json` com a atual informação em memória, utilizando a função `savefile(data, fname)`.
* Opção 0 - Sair. Caso tenham sido feitas alterações à informação em sistema, o utilizador recebe uma mensagem, confirmado se deseja sair sem guardar as alterações. O mesmo pode escolher entre guardar as alterações e sair do programa, sair sem guardar as alterações, e voltar ao programa.





## Considerações Finais
Este sistema foi projetado para auxiliar na gestão de grandes volumes de dados de publicações científicas, fornecendo funcionalidades intuitivas e análises visuais para facilitar a tomada de decisões e a compreensão de métricas importantes.

