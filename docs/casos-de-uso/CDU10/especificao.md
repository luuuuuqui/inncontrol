# CDU10 – Consultar Disponibilidade

**Descrição:** Permite que o usuário consulte a disponibilidade de quartos para um período específico.

**Ator Primário:** Administrador ou Hóspede.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- Os quartos disponíveis para o período informado são exibidos.

## Fluxo Principal

1. O usuário acessa a opção de gestão de reservas ou perfil no sistema.
2. O sistema exibe o calendário ou campos para informar o período.
3. O usuário informa o período desejado (data de entrada e saída).
4. O usuário confirma a consulta.
5. O sistema verifica a disponibilidade dos quartos cadastrados no banco de dados.
6. O sistema exibe a lista de quartos que não possuem reservas para o período informado.

## Fluxos de Exceção

- **FE1 – Período inválido:** Se as datas informadas forem inconsistentes (ex: check-out anterior ao check-in), o sistema exibirá uma mensagem de erro e solicitará a correção.

- **FE2 – Nenhum quarto disponível:** Se todos os quartos estiverem ocupados no período informado, o sistema exibirá uma mensagem informando a indisponibilidade.