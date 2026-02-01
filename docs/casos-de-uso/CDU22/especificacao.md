# CDU22 – Abrir Período de Reservas

**Descrição:** Permite que o administrador defina e disponibilize um novo intervalo de datas para a realização de reservas no sistema (ex: Alta Temporada 2026).

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.

**Pós-condições:** 
- O intervalo de datas torna-se elegível para novas reservas por parte dos usuários.

## Fluxo Principal

1. O administrador acessa a opção "Abrir Período" (ou configuração de datas) no sistema.
2. O sistema exibe o formulário para definição do período.
3. O administrador informa a **Data de Início** e a **Data de Término** do período.
4. O administrador confirma a abertura clicando no botão de ação.
5. O sistema valida se as datas são consistentes (início anterior ao fim).
6. O sistema registra o período, habilitando a disponibilidade para essas datas.
7. O sistema exibe uma mensagem de sucesso.

## Fluxos de Exceção

- **FE1 – Datas inválidas:** Se a data de término for anterior à data de início ou se as datas forem passadas, o sistema exibirá uma mensagem de erro.

- **FE2 – Conflito de período:** Se o período informado sobrepor um intervalo já aberto ou existente, o sistema alertará sobre o conflito.