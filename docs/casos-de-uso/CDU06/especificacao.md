# CDU06 – Manter Reserva

**Descrição:** Permite que o administrador gerencie as reservas no sistema, podendo listar, cadastrar, atualizar e excluir reservas.

**Ator Primário:** Administrador.

**Pré-condições:** 
- O administrador deve estar logado no sistema.
- Devem existir hóspedes e quartos cadastrados para criar reservas.

**Pós-condições:** 
- As reservas são registradas, alteradas ou removidas conforme a ação executada.

## Fluxo Principal

1. O administrador acessa a opção "Reserva" no menu lateral.
2. O sistema exibe as abas: Listar, Inserir, Atualizar e Excluir.
3. O sistema exibe na aba "Listar" todas as reservas com informações de hóspede, quarto, período, total e status.
4. O administrador seleciona a aba correspondente à operação desejada.
5. O administrador seleciona o hóspede, o quarto, o período de estadia e o status inicial.
6. O administrador clica no botão correspondente à ação (Inserir Reserva, Salvar Alterações ou Excluir Reserva).
7. O sistema valida os dados, verificando se o quarto está disponível no período selecionado.
8. O sistema executa a operação e exibe uma mensagem de sucesso, atualizando a lista de reservas.

## Fluxos de Exceção

- **FE1 – Hóspedes ou quartos insuficientes:** Se não houver hóspedes ou quartos cadastrados, o sistema exibe uma mensagem de erro informando a necessidade desses cadastros.

- **FE2 – Campos obrigatórios não preenchidos:** Se o administrador tentar confirmar a reserva sem selecionar o hóspede, quarto ou o período completo, o sistema impedirá a ação.

- **FE3 – Quarto indisponível:** Se houver sobreposição de datas com outra reserva ativa para o mesmo quarto, o sistema exibirá a mensagem "Quarto indisponível!" informando o período ocupado.

- **FE4 – Datas inválidas:** Se a data de check-in for igual ou posterior à de check-out, ou se as datas forem anteriores a 2026, o sistema exibirá uma mensagem de erro específica.

- **FE5 – Status vazio:** Se o status da reserva não for informado, o sistema impedirá a gravação informando que o campo não pode ser vazio.

- **FE6 – Erro inesperado:** Caso ocorra uma falha durante o processamento, o sistema exibirá uma mensagem detalhando o erro.