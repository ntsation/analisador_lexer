# Analisador Léxico
O Analisador Léxico (Lexer) é uma ferramenta desenvolvida em Python para realizar a tokenização de um código fonte em uma linguagem de programação. Ele identifica e classifica os tokens como identificadores, palavras-chave, operadores, símbolos, etc.

## Funcionamento
O código utiliza expressões regulares para definir padrões de tokens e categorizá-los. A cada iteração, ele busca por correspondências entre os padrões e o código fonte fornecido, gerando uma lista de tokens com suas respectivas classificações.

## Utilização
Para utilizar o analisador léxico, basta fornecer o código fonte desejado como uma string para a função lexer(code). A função retornará uma lista de tokens com suas classificações.

