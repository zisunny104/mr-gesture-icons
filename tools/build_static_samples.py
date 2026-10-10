"""Original editable path drawings: shared thumbs-up and domestic OK samples."""
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
THUMB='M 132,270 L 130,244 C 116,243 106,238 102,231 C 94,226 94,219 95,216 C 88,211 78,215 81,197 C 78,195 76,190 85,183 C 80,181 76,169 78,162 C 80,152 107,152 129,155 C 141,151 145,142 143,130 L 135,100 C 132,86 132,82 138,77 C 144,72 151,76 153,82 C 158,96 162,109 167,124 L 183,157 C 190,172 194,187 198,199 C 204,211 203,224 199,238 L 197,270'
THUMB_DETAILS=['M 85,183 C 100,185 114,186 128,181','M 81,197 C 96,201 112,202 124,197','M 95,216 C 106,218 117,218 125,213','M 129,155 C 141,161 143,174 128,181']
OK='M 147,270 L 143,241 C 131,226 114,216 102,201 C 82,184 77,176 81,161 C 85,148 88,141 92,136 C 99,127 110,129 122,137 C 133,146 142,156 146,162 C 150,165 153,163 152,158 L 139,91 C 137,82 139,74 146,74 C 153,73 158,78 159,82 L 173,136 L 179,100 C 180,91 184,87 190,89 C 197,91 201,97 201,105 L 205,149 L 217,130 C 221,121 228,124 230,131 C 233,140 231,154 229,166 L 223,200 C 220,216 214,230 213,241 L 214,270'
OK_DETAILS=['M 126,166 C 119,157 110,152 103,158 C 96,164 89,170 91,178 C 92,191 105,199 115,200 C 126,201 136,189 135,179 C 134,173 131,169 126,166','M 173,136 L 177,158','M 205,149 L 203,170']
def write(relative,title,gesture,outline,details):
 p=ROOT/relative;p.parent.mkdir(exist_ok=True,parents=True)
 paths='\n'.join(f'<path d="{v}"/>' for v in [outline,*details])
 p.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">右手{escape(gesture)}，圓潤簡化線條，保留手指與掌部必要輪廓。不含文字與動態箭頭。樣圖待研究者確認。</desc>
<g id="hand" fill="none" stroke="#111111" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
{paths}
</g>
</svg>\n''',encoding='utf-8')
for target in ['domestic/01-open-0-complete.svg','international/02-confirm-0-complete.svg']:
 write(target,'比讚：完整手勢示意','比讚',THUMB,THUMB_DETAILS)
write('domestic/02-confirm-0-complete.svg','OK：完整手勢示意','OK 手勢',OK,OK_DETAILS)
