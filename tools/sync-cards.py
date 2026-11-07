"""Embed the canonical card database while preserving the standalone HTML game."""
import json
import re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
cards = json.loads((root / 'cards.json').read_text())
assert [c['id'] for c in cards] == list(range(len(cards))), 'Preserve contiguous, stable art IDs'
assert len({c['code'] for c in cards}) == len(cards), 'Card codes must be unique'
assert all(c['type'] in {'monster', 'spell', 'trap'} for c in cards)
assert all(isinstance(c['effect'], bool) for c in cards if c['type'] == 'monster')
p = root / 'index.html'
content, count = re.subn(r'const CARDS=\[.*?\];\n', lambda _: 'const CARDS=' + json.dumps(cards, ensure_ascii=False, separators=(',', ':')) + ';\n', p.read_text(), count=1)
assert count == 1, 'Embedded database not found'
p.write_text(content)
print(f'Embedded {len(cards)} cards')
