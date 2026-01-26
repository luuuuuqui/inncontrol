# CDU22 – Abrir Período de Reservas

**Descrição:** Permite que o administrador defina e abra um novo período para realização de reservas no sistema.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- O período de reservas é aberto e disponibilizado no sistema.

## Fluxo Principal

1. O administrador acessa a opção Abrir Período de Reservas no sistema.
2. O sistema exibe o formulário para definição do período.
3. O administrador informa as datas de início e término do período.
4. O administrador confirma a abertura do período.
5. O sistema valida as datas informadas.
6. O sistema registra e abre o período de reservas.
7. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Datas inválidas:** Se as datas informadas forem inválidas ou inconsistentes, o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Período já existente:** Se já existir um período de reservas aberto para as datas informadas, o sistema exibirá uma mensagem informando o conflito.