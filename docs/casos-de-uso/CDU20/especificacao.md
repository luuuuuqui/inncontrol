# CDU20 – Pesquisar Hóspede

**Descrição:** Permite pesquisar um hóspede cadastrado no sistema utilizando o nome como critério.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- Os dados do hóspede pesquisado são exibidos.

## Fluxo Principal

1. O administrador acessa a opção Pesquisar Hóspede no sistema.
2. O sistema exibe o campo de pesquisa.
3. O administrador informa o nome do hóspede.
4. O administrador confirma a pesquisa.
5. O sistema busca o hóspede no banco de dados.
6. O sistema exibe os dados do hóspede encontrado (Nome, E-mail, Telefone e Endereço).

## Fluxos de Exceção

- **FE1 – Hóspede não encontrado:** Se não existir hóspede com o nome informado, o sistema exibirá uma mensagem informando que não foram encontrados resultados.

- **FE2 – Dados inválidos:** Se o campo de pesquisa for enviado vazio ou com caracteres inválidos, o sistema exibirá uma mensagem de erro e solicitará a correção.