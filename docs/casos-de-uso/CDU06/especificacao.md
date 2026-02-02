# CDU06 – Manter Reserva

**Descrição:** Permite que o administrador gerencie as reservas no sistema, incluindo listar, inserir, atualizar e excluir reservas.

**Ator Primário:** Administrador.

**Pré-condições:** - O usuário deve estar logado como administrador no sistema.
- Devem existir hóspedes e quartos cadastrados para criar reservas.

**Pós-condições:** - As reservas estarão atualizadas no banco de dados conforme as operações realizadas.

## Fluxo Principal

1. O administrador acessa a interface de gestão de reservas.
2. O sistema exibe a aba "Listar" com todas as reservas cadastradas (ID, Hóspede, Quarto, Check-in, Check-out, Total e Status).
3. O administrador seleciona a aba correspondente para Inserir, Atualizar ou Excluir.
4. O administrador preenche os dados necessários ou seleciona a reserva na lista.
5. O administrador clica no botão correspondente à ação.
6. O sistema valida os dados fornecidos e a disponibilidade do quarto.
7. O sistema executa a operação no banco de dados.
8. O sistema exibe uma mensagem de sucesso e recarrega a interface.

## Fluxos de Exceção

- **FE1 – Hóspedes ou quartos insuficientes:** Se não houver hóspedes ou quartos cadastrados, o sistema exibirá uma mensagem de erro informando a necessidade desses cadastros prévios.

- **FE2 – Campos obrigatórios não preenchidos:** Se hóspede, quarto ou datas não forem informados, o sistema impedirá a inserção da reserva.

- **FE3 – Quarto indisponível:** Se o quarto selecionado já possuir uma reserva no período informado, o sistema exibirá uma mensagem de indisponibilidade.

- **FE4 – Datas inválidas:** Se as datas forem anteriores ao ano atual, se a data de saída for anterior à entrada ou se o formato estiver incorreto, o sistema exibirá uma mensagem de erro específica.

- **FE5 – Status vazio:** Se o status da reserva não for selecionado ou estiver vazio, o sistema impedirá a gravação e informará o erro.

- **FE6 – Erro inesperado:** Em caso de falha sistêmica ou de banco de dados, o sistema exibirá uma mensagem detalhando o erro ocorrido.