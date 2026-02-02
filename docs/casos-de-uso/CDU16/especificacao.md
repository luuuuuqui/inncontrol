# CDU16 – Listar Hóspedes

**Descrição:** Permite visualizar a lista de hóspedes cadastrados no sistema, com opções de busca e filtro.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- A lista de hóspedes é exibida conforme os filtros aplicados.

## Fluxo Principal

1. O administrador acessa a opção Listar Hóspedes no sistema.
2. O sistema busca todos os registros de hóspedes no banco de dados.
3. O sistema exibe a lista contendo nome, e-mail, telefone e endereço.
4. O administrador pode realizar buscas por nome.
5. O sistema exibe os hóspedes correspondentes à busca realizada.

## Fluxos de Exceção

- **FE1 – Nenhum hóspede encontrado:** Se não existir nenhum hóspede cadastrado ou que atenda ao critério de busca, o sistema exibirá uma mensagem informando que não há registros.