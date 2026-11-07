# Arcana

Arcana Versão 2. Jogo de duelo de cartas em português, com HTML, CSS, JavaScript e todas as artes incorporados em `index.html`. Não há bibliotecas de aplicação, dependências externas nem servidor obrigatório. Abra o HTML num navegador; para desenvolvimento HTTP opcional, use `python3 -m http.server 8000 --directory /workspace/aplicativo-notas-android`.

No iPhone, abra o endereço do GitHub Pages após a sincronização e a publicação. O campo permanece ao fundo durante as apresentações; os painéis de decisão usam alvos grandes de toque. Toque para selecionar uma carta e segure para espiar. As cartas pequenas não mostram descrição. Vitórias, derrotas e ritmo das animações são salvos em localStorage quando disponível.

## Catálogo completo

A base oficial é `cards.json`, importada do catálogo completo enviado pelo usuário. São **138 cartas**, identificadas pelos códigos originais: **85 monstros (22 de efeito e 63 normais), 36 magias e 17 armadilhas**. Valores, descrições e raridades seguem as tabelas do documento. Os monstros que perderam habilidade são normais, com os atributos dados na seção de normais; não mantêm gatilhos antigos. As 13 criaturas novas têm ilustrações originais próprias, incorporadas ao HTML. Monstros de efeito têm moldura laranja.

Cada deck tem 40 cartas: **23–27 monstros**, o restante em magias e armadilhas, **1–3 monstros de nível 7+** e no máximo **um de nível 8–9**. Há no máximo uma Lendária de suporte em cerca de metade dos decks e **1–3 Raras**. Monstros médios e fortes têm participação limitada, predominando os de nível baixo.

Regras adicionadas/atualizadas: limite de **duas ativações de magia por turno**, Lendárias a partir do turno 5, alvos e condições específicos, custos de PV, bônus e penalidades temporários com expiração ao fim do turno, Ressurreição limitada ao nível 4 e sem ataque imediato, e Ritual Duplo limitado a uma invocação extra de nível 4 ou menor. As armadilhas com custo pedem confirmação e escolha de uma carta da própria mão ou campo; recusar preserva a armadilha e os recursos. Grimório permite escolher o descarte, e Corvo de Hermes pede dois descartes para o ataque direto por efeito.

Os 22 efeitos de monstro têm gatilhos de entrada/virada, batalha ou envio do campo ao cemitério conforme cada texto, além de imunidade a seleção por magia, proteção da mão até o fim do turno, resistência à primeira destruição em batalha, tributo duplo, ataque direto, dois ataques e perfuração. A Guardiã bloqueia dano de ataque, magia e efeito durante o turno do oponente, com decisão do jogador. A imunidade do Monge se aplica a magias que pedem alvo; efeitos globais continuam atingindo-o. A resistência à primeira destruição é por carta física no duelo, inclusive se ela voltar do cemitério.

**Exceção preservada do catálogo:** m74, Sombra Errante das Dunas, tem ATK 300/DEF 600. Isso soma 900, em vez do orçamento geral 1100 para efeito N2. Os números explícitos da linha foram mantidos; a validação informa a exceção no console. Nenhuma correção automática alterou essa carta.

Para editar a base, preserve `code` e os IDs numéricos de arte, altere `cards.json` e execute `python3 tools/sync-cards.py`. Efeitos executáveis são definidos pelo código da carta no motor; editar o texto sozinho não muda a regra. O HTML continua autônomo: o JSON separado é fonte de desenvolvimento e não é buscado pela página.

Validação com Node e Playwright/Chromium disponíveis:

```sh
node tests/catalog.cjs
node tests/catalog-ui.cjs
node tests/catalog-animation.cjs
```

A suíte cobriu os 53 efeitos de suporte e os 22 monstros de efeito, limites de 1.200 decks, 16 duelos completos em simulação e dois com a fila real de animações. Foram exercitados por toque os custos aceitos/recusados, a proteção opcional da Guardiã, os descartes escolhidos, a Oferenda como tributo duplo, a coleção com 85 monstros e o encaixe da versão no iPhone. As apresentações de efeitos antecedem suas consequências; o campo permanece ao fundo. Sem erros inesperados de JavaScript nos testes. Safari em aparelho físico ainda não foi validado.

Link da versão após sincronizar o fork e concluir a publicação do Pages: https://abelrdg1008.github.io/aplicativo-notas-android/index.html?v=arcana-2
