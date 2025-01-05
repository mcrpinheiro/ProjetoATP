# Relatório do Projeto: Sistema de Gestão de Publicações Científicas
## Autor: Maria Pinheiro A97304

## Descrição Geral
Este projeto consiste no desenvolvimento de um sistema em **Python** para a criação, atualização e análise de publicações científicas. O objetivo principal é permitir a gestão eficiente de um dataset de artigos e a geração de métricas e relatórios detalhados sobre as publicações e os seus autores.

Este projeto foi dividido em duas parte essenciais: uma linha de comandos e uma interface utilizando **PySimpleGUI**.

## Constituição do Projeto
O projeto é constituído por 7 ficheiros:
* `ata_medica_papers.json` - ficheiro com a base de dados.
* `check_date.py` - ficheiro com funções auxiliares relacionadas com a data, especificamente funções que verificam se o formato da data é o correto e se a data é possível.
* `command_line.py` - ficheiro onde se encontra a função principal da linha de comando.
* `distrib.py` - ficheiro com as funções utilizadas para confirmar quais as keys obrigatórias nas atas. No caso de o número de keys ser inferior ao número total de atas, estas não seriam obrigatórias, que foi o caso das *keywords*, *publish_date* e *pdf*. No caso dos autores, o número de keys *affiliation* é menor ao número total de nomes, sendo então esta key opcional.
* `functions.py` - ficheiro com as funções auxiliares para o funcionamento da linha de comando.
* `interface_auxiliares.py` - ficheiro com as funções auxiliares para o funcionamento da interface. 
* `interface.py` - ficheiro principal para o funcionamento da interface.


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

### Exemplos da Utilização da Linha de Comando 
Para ativar a linha de comandos, deverá ser escrito no terminal `python command_line.py`.

* Resultado de esquisar uma publicação através do nome de autor 'R Anjos':
```Bem vindo ao sistema de consulta e análise de publicações científicas. Que operação deseja executar?
                            (1) Ajuda
                            (2) Criar Publicação
                            (3) Consulta de Publicação
                            (4) Consultar Publicações
                            (5) Eliminar Publicação
                            (6) Relatório de Estatísticas de Publicações por Ano
                            (7) Listar Autores
                            (8) Importar Publicações
                            (9) Guardar Publicações
                            (0) Sair3
Qual campo vai ser o identificador da ata desejada? Selecione o número correspondente:
               (1) Abstract
               (2) Nome de um Autor
               (3) DOI
               (4) PDF
               (5) Data de Publicação
               (6) Título
               (7) URL
               (0) Voltar ao Menu2
Qual authors deseja pesquisar?R Anjos
Abstract: Resumo We describe a case of extra-lobar pulmonary sequestration with broncho-esophageal fistula in a newborn male who presented respiratory distress, cyanosis and feeding difficulties. The diagnosis was made with a swallowed contrast examination, nuclear magnetic resonance, digital subtraction angiography and confirmed by gross and histologic examination. 
The work of a multidisciplinary team was essential for an early diagnosis and the correct and effective treatment of this Cuncommon condition.
Authors:
Name: H Pedroso
Affiliation: Serviço de Pediatria, Hospital São Francisco Xavier, Lisboa.
Name: R Anjos
Name: J S Lino
Name: A M Nunes
Name: M A Bispo
Name: J M Palminha
Doi: https://doi.org/10.20344/amp.2295
Pdf: https://www.actamedicaportuguesa.com/revista/index.php/amp/article/view/2295/1713
Title: Sequestro pulmonar extra-lobar com fístula bronco-esofágica.
URL: https://www.actamedicaportuguesa.com/revista/index.php/amp/article/view/2295
Que operação deseja executar?
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
- Após escolher a opção 3, o sistema questiona qual dos campos desejados para identificar a publicação para listar. Ao escolher o número 2, correspondente ao nome de autor, foi preenchido 'R Anjos'. Após isto, o sistema listou as informações relativas à primeira publicação deste autor.




## Considerações Finais
Este sistema foi projetado para auxiliar na gestão de grandes volumes de dados de publicações científicas, fornecendo funcionalidades intuitivas e análises visuais para facilitar a tomada de decisões e a compreensão de métricas importantes.

