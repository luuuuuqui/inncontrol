# CDU20 – Pesquisar Hóspede

**Descrição:** Permite pesquisar um hóspede cadastrado no sistema utilizando critérios como nome ou CPF.

**Ator Primário:** Administrador ou Recepcionista.

**Pré-condições:**  
- O usuário deve estar logado no sistema.

**Pós-condições:**  
- Os dados do hóspede pesquisado são exibidos.

## Fluxo Principal

1. O usuário acessa a opção Pesquisar Hóspede no sistema.
2. O sistema exibe o campo de pesquisa.
3. O usuário informa o nome ou CPF do hóspede.
4. O usuário confirma a pesquisa.
5. O sistema busca o hóspede no sistema.
6. O sistema exibe os dados do hóspede encontrado.

## Fluxos de Exceção

- **FE1 – Hóspede não encontrado:**  
  Se não existir hóspede com os dados informados, o sistema exibirá uma mensagem informando que não foram encontrados resultados.

- **FE2 – Dados inválidos:**  
  Se os dados informados estiverem inválidos, o sistema exibirá uma mensagem de erro e solicitará a correção.
