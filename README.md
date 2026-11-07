# Arena Arcana

Jogo de duelo de cartas em português, num único `index.html`, sem dependências ou pedidos externos. Abra o HTML num navegador moderno. Para desenvolvimento local opcional: `python3 -m http.server 8000 --directory /workspace/aplicativo-notas-android`.

No iPhone, disponibilize o arquivo numa hospedagem HTTPS, abra o endereço no Safari e use Compartilhar → Adicionar à Tela de Início. O projeto está preparado para GitHub Pages: em Settings → Pages, selecione Deploy from a branch, branch `main`, pasta `/ (root)` e Save. O endereço previsto é https://abelrdg1008.github.io/aplicativo-notas-android/; só use após o GitHub confirmar a implantação. A execução local não precisa de servidor; a instalação pela Tela de Início precisa de um endereço acessível ao Safari.

Toque nas cartas para ver ações. Segure por 220 ms para espiar, deslize para outra carta e solte para fechar. Durante animações, toque para avançar. Selecione alvos ou tributos destacados no campo, ou use Cancelar. A ajuda inclui regras, equilíbrio e coleção. Vitórias e derrotas são guardadas no armazenamento local quando permitido pelo navegador.

Inclui 72 monstros, 36 magias e 17 armadilhas, decks sorteados de 40 cartas, oponentes com 10.000 PV e Oráculo automático. A edição **Obsidiana · Anime** usa 125 cenas originais de anime com contornos marcados e sombras em duas tonalidades: uma célula de arte para cada carta, sem compartilhamento por família. Todas têm cenários e ações próprios. As sete pranchas são incorporadas em JPEG no HTML e usadas como sprites CSS, evitando gerar e guardar 125 cópias de imagem em canvas. Molduras variam por atributo e patamar de nível. Nos detalhes, **Ver ilustração** abre a arte ampliada e retorna à carta sem interromper o duelo. O campo representa o Observatório de Obsidiana com desenho geométrico e cores de anime.

Fontes locais mantêm o arquivo independente de Google Fonts.

Validação: Chromium com viewport móvel 390×664, testes isolados dos 53 efeitos de magias/armadilhas, cálculos de batalha, esgotamento de deck, 12 duelos completos e interação por toque (invocação, seleção de alvo, baixar armadilha, turno do Oráculo e abas da coleção). Scripts e captura da validação estão em `/workspace/scratch/arena-tests` nesta máquina. A instalação do WebKit foi bloqueada pela política de rede; teste num iPhone físico ainda é necessário. A revisão visual também foi validada em 320×568, 375×667, 390×664, 430×932 e 820×1180, com controles visíveis e sem transbordamento. O HTML contém todas as imagens e não as baixa de serviços externos durante o jogo.

A identificação `anime-1` está na meta `arena-version` e a tela inicial mostra **Obsidiana · Edição Anime**. Para verificar uma atualização sem reaproveitar a página antiga, abra o endereço com `?v=anime-1`.


## Relíquias do Duelo (`reliquias-1`)

Apresentação de console antigo: abertura de templo sob raios violetas, menus verticais com seleção dourada, tabuleiro de pedra em perspectiva CSS, cartas amarelas com estrelas vermelhas, retrato original do Oráculo, palco de invocação e telas de vitória/derrota ilustradas. As 125 cenas originais de anime continuam na coleção, com apresentação e tratamento de cor retro. Regras e composição dos decks permanecem as mesmas; esta edição não acrescenta fusão, campanha, loja ou edição manual de deck.

Validação: controles por toque, menus de rival e regras, proporção de tela, alvos no tabuleiro transformado em 320×568, 390×664 e 430×932, animação de invocação e pulo por toque, telas de vitória/derrota, 163 verificações de regras/efeitos e 12 duelos completos. Sem erros de JavaScript no Chromium. Safari físico permanece a validar.

A tela inicial mostra **RELÍQUIAS DO DUELO** e o rodapé **EDIÇÃO RELÍQUIAS · 01**. Para testar esta edição, use https://abelrdg1008.github.io/aplicativo-notas-android/index.html?v=reliquias-1 após sincronizar o fork e concluir o deploy do Pages.


## Animações guiadas (`reliquias-2`)

Ataques têm declaração com as duas cartas e valores, etapa de resposta, revelação do defensor quando necessário, deslocamento até o alvo, destruição, PV com contagem gradual e resultado com cálculo ATK × ATK/DEF. Uma armadilha que anula o ataque interrompe a sequência antes do impacto. Efeitos de magias e armadilhas são resolvidos em ordem, com compra, entrada de cartas, tributos e mudanças de atributos/posição mostrados no campo. O Oráculo espera essas consequências terminarem antes da ação seguinte e não baixa cartas após encerrar o duelo.

O botão **Avançar esta etapa**, ou um toque numa apresentação de carta, avança só a etapa atual. O menu **Ritmo das animações** oferece Guiado (padrão) e Ágil; a preferência fica salva quando o navegador permite. Movimento reduzido evita deslocamentos sem reduzir o tempo para ler o resultado. Os controles permanecem bloqueados até a sequência terminar.

Validação no Chromium: 24 verificações da ordem visual e dos resultados; ritmo real com bloqueio de toques, avanço de etapa e movimento reduzido; duas partidas completas usando a fila real de animações, além das 163 verificações de regras/efeitos e 12 partidas simuladas. Sem erros de JavaScript. Scripts de verificação desta sessão: `/workspace/scratch/animation-check.cjs` e `/workspace/scratch/animation-duels.cjs`. Safari físico segue a validar.

A tela inicial mostra **RELÍQUIAS · ANIMAÇÕES GUIADAS · 02**. Link após sincronizar o fork e concluir o Pages: https://abelrdg1008.github.io/aplicativo-notas-android/index.html?v=reliquias-2


## Cartas compactas (`reliquias-3`)

As cartas pequenas na mão, no campo e na coleção mostram a ilustração e os valores ATK/DEF dos monstros, sem bloco de descrição. A descrição permanece na carta ampliada e no painel de detalhes. A área liberada aumenta a janela da arte. Nenhuma regra ou valor foi alterado.


## Interface móvel (`reliquias-4`)

Painéis com acabamento de vidro escuro, bordas douradas e cantos arredondados, inspirados em seletores do iPhone. Ações de carta têm alvos de pelo menos 52 px; fechar, ajuda e navegação usam alvos de pelo menos 44 px. O controle de turno tem uma linha própria de 56 px, calculada antes do campo e da mão. O dimensionamento acompanha o viewport visual e funciona também em rotação. O avanço de animação foi separado da faixa de controles.

Cartas pequenas usam uma grade idêntica para título, faixa de tipo/nível, janela de arte, rodapé e número de coleção. Monstros têm ATK/DEF no rodapé; magias e armadilhas têm símbolos originais próprios na mesma faixa. Descrições ficam só nas cartas ampliadas. A visualização isolada de ilustrações foi removida; invocações e ataques sempre apresentam a carta inteira. O HUD não exibe o rótulo Pontos de Vida; Mão, Deck e Cemitério usam a mesma tipografia.

Os círculos giratórios foram removidos. A destruição usa chamas em canvas de baixa resolução com pixels visíveis e preserva a ordem dos acontecimentos. As 125 cenas foram reamostradas para sprites pequenos, com acabamento inspirado em consoles de 32 bits; o HTML caiu de cerca de 6,6 MB para cerca de 2,3 MB sem dependências externas. Movimento reduzido continua respeitado.

Cada deck tem 40 cartas: 24–28 monstros e 12–16 magias/armadilhas; dentro dessas últimas, 4–6 são armadilhas. A quantidade de monstros de nível baixo predomina. Como o total continua sendo 40, o mínimo compatível com no máximo 16 cartas de suporte é 24 monstros.

Toda saída de ação limpa efeitos e libera o bloqueio de interação. Uma falha inesperada oferece reinício do duelo em um painel funcional; não retorna a um turno do computador travado. Duelo interrompido não acrescenta derrota ao placar.

Validação no Chromium: 200 decks em todos os cinco totais possíveis, alinhamento das artes e ícones, descrição apenas ampliada, recuperação de falhas no turno do jogador e do Oráculo, invocação de carta inteira, ausência dos círculos, fogo pixelado real e limpeza do efeito; controles acessíveis em 320×568, 375×667, 390×664, 430×932 e 932×430. Testada a transição batalha → armadilha que encerra batalha → turno do Oráculo → próxima batalha. Também passaram as 163 verificações de regras, 24 verificações de ordem visual, 12 partidas simuladas e duas partidas completas com a fila real de animações. Safari físico permanece a validar.

A abertura mostra **RELÍQUIAS · INTERFACE MÓVEL · 04**. Após sincronizar e publicar o Pages: https://abelrdg1008.github.io/aplicativo-notas-android/index.html?v=reliquias-4
