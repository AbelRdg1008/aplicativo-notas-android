# Preferências de entrega do Arcana

- A cada atualização funcional ou visual entregue do jogo, incremente `GAME_VERSION` em `index.html`. Não incremente só por executar testes ou ajustar documentação.
- A numeração foi reiniciada em **1** por pedido do usuário. A próxima atualização será 2, depois 3 e assim por diante. Use números sem zero à esquerda.
- A tela inicial e o título devem mostrar apenas **Arcana Versão N**, sem nomes de edições, subtítulos ou codinomes de atualização. `GAME_BUILD`, o título, a meta `arena-version` e os identificadores visíveis devem refletir esse número; use a constante como origem do valor.
- Verifique se o selo e todos os botões da tela inicial cabem no iPhone em 320×568 e 390×664.
- Sempre termine cada resposta de atualização com DOIS links: **Atualizar o fork** (`https://github.com/AbelRdg1008/aplicativo-notas-android`, para Sync fork → Update branch) e **Testar Arcana Versão N** (`https://abelrdg1008.github.io/aplicativo-notas-android/index.html?v=arcana-N`). Use o número real da entrega e informe se a sincronização/publicação ainda está pendente.
- Diferencie atualização enviada à origem, sincronização da cópia e deploy do Pages. Não diga que a versão está no site sem confirmação. Caso a cópia precise de Sync fork, informe isso claramente; para evitar abertura no app GitHub, forneça o endereço do repositório como texto para copiar ao navegador.
