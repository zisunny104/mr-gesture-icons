"""Original editable path drawings: shared thumbs-up and domestic OK samples."""
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
# Thumb-up anatomy based on the original domestic grid: four curled fingers,
# a distinct raised thumb, broad palm, and a short oblique wrist.
THUMB='M 263,223 C 249,218 244,211 240,199 L 209,126 C 198,103 193,93 188,82 C 184,72 181,63 175,64 C 168,65 162,76 164,88 L 173,128 C 179,145 173,151 157,151'
THUMB_DETAILS=[
'M 98,145 C 81,143 77,152 76,166 C 77,176 90,179 98,179 C 121,181 141,181 155,177 C 168,173 170,163 161,156 C 145,148 118,144 98,145 Z',
'M 98,179 C 84,176 77,178 77,189 C 74,200 82,210 94,210 C 114,213 135,213 151,207 C 160,204 166,194 155,177 C 141,181 121,181 98,179 Z',
'M 94,210 C 82,209 77,214 78,225 C 80,234 87,239 92,239 C 110,242 127,242 145,236 C 157,231 162,221 151,207 C 135,213 114,213 94,210 Z',
'M 92,239 C 83,238 79,242 82,251 C 85,262 97,269 111,268 C 125,268 141,260 148,253 C 155,246 157,242 145,236 C 127,242 110,242 92,239 Z',
'M 111,268 C 140,284 173,280 195,271 C 215,268 235,277 252,288'
]
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
