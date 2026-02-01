# CDU20 – Pesquisar Hóspede

**Descrição:** Permite localizar rapidamente um hóspede cadastrado no sistema utilizando o nome como critério de busca.

**Ator Primário:** Administrador e Recepcionista.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- O sistema exibe apenas os hóspedes que correspondem ao critério de busca informado.

## Fluxo Principal

1. O usuário acessa a opção "Hóspede" no menu lateral.
2. O sistema exibe a aba "Listar" contendo a relação completa de hóspedes.
3. O usuário digita o nome (ou parte dele) no campo de pesquisa localizado acima da tabela.
4. O sistema filtra os dados em tempo real ou após a confirmação.
5. O sistema exibe os dados dos hóspedes encontrados (ID, Nome, E-mail e Endereço).

## Fluxos de Exceção

- **FE1 – Hóspede não encontrado:** Se nenhum registro corresponder ao termo pesquisado, a tabela ficará vazia ou exibirá a mensagem "Nenhum hóspede cadastrado.".

- **FE2 – Campo de pesquisa limpo:** Se o usuário apagar o conteúdo do campo de pesquisa, o sistema voltará a exibir a lista completa de hóspedes automaticamente.