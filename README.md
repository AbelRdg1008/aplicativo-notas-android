# Arena Arcana

Jogo de duelo de cartas em português, num único `index.html`, sem dependências ou pedidos externos. Abra o HTML num navegador moderno. Para desenvolvimento local opcional: `python3 -m http.server 8000 --directory /workspace/aplicativo-notas-android`.

No iPhone, disponibilize o arquivo numa hospedagem HTTPS, abra o endereço no Safari e use Compartilhar → Adicionar à Tela de Início. O projeto está preparado para GitHub Pages: em Settings → Pages, selecione Deploy from a branch, branch `main`, pasta `/ (root)` e Save. O endereço previsto é https://abelrdg1008.github.io/aplicativo-notas-android/; só use após o GitHub confirmar a implantação. A execução local não precisa de servidor; a instalação pela Tela de Início precisa de um endereço acessível ao Safari.

Toque nas cartas para ver ações. Segure por 220 ms para espiar, deslize para outra carta e solte para fechar. Durante animações, toque para avançar. Selecione alvos ou tributos destacados no campo, ou use Cancelar. A ajuda inclui regras, equilíbrio e coleção. Vitórias e derrotas são guardadas no armazenamento local quando permitido pelo navegador.

Inclui 72 monstros, 36 magias e 17 armadilhas, decks sorteados de 40 cartas, oponentes com 10.000 PV e Oráculo automático. A edição **Obsidiana · Anime** usa 125 cenas originais de anime com contornos marcados e sombras em duas tonalidades: uma célula de arte para cada carta, sem compartilhamento por família. Todas têm cenários e ações próprios. As sete pranchas são incorporadas em JPEG no HTML e usadas como sprites CSS, evitando gerar e guardar 125 cópias de imagem em canvas. Molduras variam por atributo e patamar de nível. Nos detalhes, **Ver ilustração** abre a arte ampliada e retorna à carta sem interromper o duelo. O campo representa o Observatório de Obsidiana com desenho geométrico e cores de anime.

Fontes locais mantêm o arquivo independente de Google Fonts.

Validação: Chromium com viewport móvel 390×664, testes isolados dos 53 efeitos de magias/armadilhas, cálculos de batalha, esgotamento de deck, 12 duelos completos e interação por toque (invocação, seleção de alvo, baixar armadilha, turno do Oráculo e abas da coleção). Scripts e captura da validação estão em `/workspace/scratch/arena-tests` nesta máquina. A instalação do WebKit foi bloqueada pela política de rede; teste num iPhone físico ainda é necessário. A revisão visual também foi validada em 320×568, 375×667, 390×664, 430×932 e 820×1180, com controles visíveis e sem transbordamento. O HTML contém todas as imagens e não as baixa de serviços externos durante o jogo.

A identificação `anime-1` está na meta `arena-version` e a tela inicial mostra **Obsidiana · Edição Anime**. Para verificar uma atualização sem reaproveitar a página antiga, abra o endereço com `?v=anime-1`.
