# CDU10 – Consultar Disponibilidade

**Descrição:** Permite que o usuário consulte se um quarto está livre para reserva em um período específico, evitando sobreposição de estadias.

**Ator Primário:** Administrador, Recepcionista ou Hóspede.

**Pré-condições:** 
- O usuário deve estar logado no sistema.

**Pós-condições:** 
- O sistema confirma a disponibilidade ou informa o conflito de datas.

## Fluxo Principal

1. O usuário acessa a funcionalidade de consulta ou de realização de reserva.
2. O usuário informa o período desejado preenchendo as datas de check-in e check-out.
3. O usuário seleciona o quarto que deseja consultar.
4. O sistema valida se as datas foram inseridas no formato correto.
5. O sistema verifica se existe alguma reserva ativa para o quarto selecionado que coincida com o período informado.
6. O sistema confirma que o quarto está disponível para o período.

## Fluxos de Exceção

- **FE1 – Formato de data inválido:** Caso as datas não sigam o padrão esperado pelo sistema, será exibida uma mensagem solicitando o formato correto.

- **FE2 – Inconsistência no período:** Se a data de check-in for igual ou posterior à data de check-out, o sistema exibirá uma mensagem de erro e impedirá a consulta.

- **FE3 – Quarto indisponível:** Se o quarto já estiver reservado para o período selecionado, o sistema exibirá a mensagem "Quarto indisponível!" acompanhada do intervalo em que o quarto já está ocupado.