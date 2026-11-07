# Preferências de entrega do Arcana

- A cada atualização funcional ou visual entregue do jogo, incremente `GAME_VERSION` em `index.html`. Não incremente só por executar testes ou ajustar documentação.
- A numeração simples começou em **1** e segue 2, 3 e assim por diante. O valor atual está em `GAME_VERSION`; incremente uma unidade por atualização entregue. Use números sem zero à esquerda.
- A tela inicial e o título devem mostrar apenas **Arcana Versão N**, sem nomes de edições, subtítulos ou codinomes de atualização. `GAME_BUILD`, o título, a meta `arena-version` e os identificadores visíveis devem refletir esse número; use a constante como origem do valor.
- Verifique se o selo e todos os botões da tela inicial cabem no iPhone em 320×568 e 390×664.
- Sempre termine cada resposta de atualização com DOIS links: **Atualizar o fork** (`https://github.com/AbelRdg1008/aplicativo-notas-android`, para Sync fork → Update branch) e **Testar Arcana Versão N** (`https://abelrdg1008.github.io/aplicativo-notas-android/index.html?v=arcana-N`). Use o número real da entrega e informe se a sincronização/publicação ainda está pendente.
- Diferencie atualização enviada à origem, sincronização da cópia e deploy do Pages. Não diga que a versão está no site sem confirmação. Caso a cópia precise de Sync fork, informe isso claramente; para evitar abertura no app GitHub, forneça o endereço do repositório como texto para copiar ao navegador.

- Formato obrigatório: **Atualizar o fork** deve ser um bloco de código com a URL para copiar, sem link Markdown clicável; **Testar Arcana Versão N** deve ser um link Markdown clicável. O iPhone abre links do GitHub no aplicativo; instrua colar apenas o endereço de atualização na barra do Chrome e usar Sync fork → Update branch. O link do jogo funciona diretamente e deve continuar clicável.

- A base oficial é `cards.json`, importada do catálogo completo do usuário (138 cartas nesta revisão). Use `code` (m/s/t) como identidade em alterações futuras; nomes podem mudar. Preserve os IDs numéricos de arte já existentes. Após editar a base, execute `python3 tools/sync-cards.py` e verifique o motor de efeitos correspondente. Monstros normais devem ter `effect:false`; não reative efeitos removidos pelo usuário.
- Para alterações de cartas/regras, execute `node tests/catalog.cjs` e `node tests/catalog-ui.cjs` com Playwright/Chromium disponíveis. A carta m74 tem uma exceção de orçamento explicitamente preservada: ATK 300/DEF 600, como no documento.
- Quando um documento do usuário deixar um monstro sem efeito, trate-o como normal (`effect:false`), usando os valores da tabela de normais quando fornecidos. Não preserve uma habilidade antiga por causa do código da carta.
