"""Generate editable SVG samples. Python writes XML paths; Inkscape renders review previews."""
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
# Original path drawings, not traced or copied from source-deck vectors.
POINT='M 147,269 L 144,241 C 139,229 128,224 116,211 L 82,174 C 76,167 77,159 84,156 C 89,154 95,156 100,161 L 128,184 C 130,186 133,185 132,180 L 123,91 C 122,82 127,77 133,77 C 140,77 144,82 145,90 L 152,141 C 157,134 165,135 172,142 C 179,135 188,139 194,147 C 201,143 210,148 213,156 L 228,191 C 233,205 228,222 224,233 L 221,269'
POINT_DETAILS=['M 152,141 L 157,162','M 172,142 L 178,162','M 194,147 L 199,166','M 132,180 C 144,180 152,186 155,197']
# Thumb is stable. Index moves downward while retaining a visible gap at the end.
TAIL='C 180,155 180,143 182,135 C 184,125 192,123 198,128 C 204,134 203,146 204,158 C 205,146 213,141 220,147 C 227,154 224,169 224,181 C 229,171 237,174 239,183 C 243,204 234,223 226,237 L 224,269'
BASE='M 144,269 L 140,241 C 135,226 115,215 101,201 L 72,172 C 66,165 67,157 74,153 C 80,150 87,153 93,158 L 122,177 C 131,183 139,179 143,174 '
START=BASE+'C 149,164 150,153 145,139 L 131,107 C 128,98 130,91 137,89 C 144,87 151,92 154,99 L 180,151 '+TAIL
END=BASE+'C 148,164 143,158 130,156 L 122,155 C 113,155 108,149 109,143 C 111,135 118,132 126,134 L 156,143 C 168,147 175,153 180,161 '+TAIL
DETAILS=['M 182,145 L 181,174','M 204,158 L 203,180','M 224,181 L 221,197']
STYLE='fill="none" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"'
def hand(path,details,color,transform=None,ident='hand'):
 t=f' transform="{transform}"' if transform else ''
 return f'<g id="{ident}" stroke="{color}" {STYLE}{t}>\n'+''.join(f'<path d="{p}"/>\n' for p in [path,*details])+'</g>'
def svg(title,body):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">右手簡化線條樣圖。灰色為起始姿態，黑色為結束姿態；箭頭表示運動方向。待研究者確認。</desc>
{body}
</svg>\n'''
def write(command,stage,title,body):
 p=ROOT/'international'/f'{command}-{stage}.svg';p.write_text(svg(title,body),encoding='utf-8')
for stage,path in [('1-start',START),('2-end',END)]:
 write('08-capture',stage,'截圖：半捏合快門 '+stage,hand(path,DETAILS,'#111111',ident='start' if stage.startswith('1') else 'end'))
# Moving index is legible above stable geometry: the shared palm/wrist naturally overlap.
body=hand(START,DETAILS,'#B8B8B8',ident='start')+'\n'+hand(END,DETAILS,'#111111',ident='end')+'''\n<g id="motion" stroke="#111111" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
<path d="M 112,98 Q 96,110 99,130"/><path d="M 92,123 L 99,132 L 106,123"/>
</g>'''
write('08-capture','0-complete','截圖：半捏合快門完整示意',body)
# Finger traverses a clockwise circle, not twisting about the finger's longitudinal axis.
for stage,tx in [('1-start',-47),('2-end',47)]:
 write('07-reload',stage,'重播：食指順時針畫圈 '+stage,hand(POINT,POINT_DETAILS,'#111111',f'translate({tx} 0)',ident='start' if stage.startswith('1') else 'end'))
body=hand(POINT,POINT_DETAILS,'#B8B8B8','translate(-47 0)',ident='start')+'\n'+hand(POINT,POINT_DETAILS,'#111111','translate(47 0)',ident='end')+'''\n<g id="motion" stroke="#111111" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
<path d="M 108,54 A 58,45 0 1 1 102,112"/>
<path d="M 100,125 L 101,111 L 114,115"/>
</g>'''
write('07-reload','0-complete','重播：食指順時針畫圈完整示意',body)
