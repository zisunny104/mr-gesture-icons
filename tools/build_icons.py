"""Build first-pass SVG gesture sets from shared stylized hand paths.
Photos guide joints/actions. These are new paths, not photo-contour traces.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from build_static_samples import THUMB, THUMB_DETAILS, OK, OK_DETAILS
ROOT=Path(__file__).resolve().parents[1]
INK='#111111';GRAY='#B8B8B8'
STYLE='fill="none" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"'
POINT='M 147,269 L 144,241 C 139,229 128,224 116,211 L 82,174 C 76,167 77,159 84,156 C 89,154 95,156 100,161 L 128,184 C 130,186 133,185 132,180 C 138,170 141,156 141,146 L 134,91 C 133,82 138,77 144,77 C 151,77 155,83 155,91 L 154,147 C 159,135 168,137 172,144 C 179,136 188,140 194,148 C 201,144 210,149 213,157 L 228,191 C 233,205 228,222 224,233 L 221,269'
POINT_DETAILS=['M 154,147 L 157,165','M 172,144 L 178,165','M 194,148 L 199,168','M 132,180 C 144,180 152,186 155,197']
SPREAD='M 143,269 L 140,242 C 137,228 120,221 104,205 L 61,159 C 55,153 54,150 59,144 C 64,138 68,137 74,141 L 104,164 C 111,169 113,165 111,160 L 105,83 C 104,73 109,68 115,70 C 121,71 124,76 126,81 L 141,132 L 141,66 C 141,57 147,53 154,56 C 160,58 162,62 162,67 L 171,129 L 181,77 C 183,68 190,69 197,74 C 201,78 201,83 199,86 L 192,141 L 216,111 C 221,102 229,104 231,112 C 232,118 229,124 226,130 L 209,179 C 203,194 203,219 199,234 L 197,269'
SPREAD_DETAILS=['M 141,132 L 145,150','M 171,129 L 171,151','M 192,141 L 187,162']
FIST='M 145,270 L 142,237 C 130,224 113,213 104,196 C 98,183 98,172 101,164 L 104,147 C 105,138 111,134 119,139 C 120,126 133,124 140,131 C 143,118 156,117 163,125 C 169,116 181,122 184,130 C 192,126 202,134 204,144 L 217,177 C 222,193 215,215 209,232 L 207,270'
FIST_DETAILS=['M 119,139 L 129,164 C 133,173 121,182 111,173','M 140,131 L 149,154 C 153,164 141,173 131,165','M 163,125 L 171,148 C 175,158 161,168 151,161','M 184,130 L 188,148 C 191,158 178,166 170,159','M 214,184 C 203,178 193,172 181,173 C 172,175 171,184 179,190 L 195,201']
PINCH=OK.replace('L 139,91 C 137,82 139,74 146,74 C 153,73 158,78 159,82 L 173,136 L 179,100 C 180,91 184,87 190,89 C 197,91 201,97 201,105 L 205,149 L 217,130 C 221,121 228,124 230,131 C 233,140 231,154 229,166 L 223,200','C 152,148 152,143 157,141 C 162,139 166,144 169,151 C 171,142 181,142 185,152 C 189,147 199,151 203,160 L 218,192 C 225,210 217,230 213,241')
PINCH_DETAILS=[OK_DETAILS[0],'M 169,151 L 174,171','M 185,152 L 190,175','M 203,160 L 205,181']
# Previous capture sample, accepted by the researcher for the domestic set.
TAIL='C 180,155 180,143 182,135 C 184,125 192,123 198,128 C 204,134 203,146 204,158 C 205,146 213,141 220,147 C 227,154 224,169 224,181 C 229,171 237,174 239,183 C 243,204 234,223 226,237 L 224,269'
BASE='M 144,269 L 140,241 C 135,226 115,215 101,201 L 72,172 C 66,165 67,157 74,153 C 80,150 87,153 93,158 L 122,177 C 131,183 139,179 143,174 '
CAP_START=BASE+'C 149,164 150,153 145,139 L 131,107 C 128,98 130,91 137,89 C 144,87 151,92 154,99 L 180,151 '+TAIL
CAP_END=BASE+'C 148,164 143,158 130,156 L 122,155 C 113,155 108,149 109,143 C 111,135 118,132 126,134 L 156,143 C 168,147 175,153 180,161 '+TAIL
CAP_DETAILS=['M 182,145 L 181,174','M 204,158 L 203,180','M 224,181 L 221,197']
# International capture: distal thumb and index flex; proximal index stays upright.
IP_START=POINT
IP_END=POINT.replace('L 82,174 C 76,167 77,159 84,156 C 89,154 95,156 100,161 L 128,184','L 98,174 C 93,167 94,157 99,150 C 103,145 109,146 113,153 L 118,163 L 128,184').replace('L 134,91 C 133,82 138,77 144,77 C 151,77 155,83 155,91 L 154,147','L 134,114 L 121,109 C 114,106 111,100 115,94 C 119,88 125,88 131,91 L 148,100 C 155,104 158,111 157,121 L 154,147')
IP_DETAILS=POINT_DETAILS+['M 134,114 L 145,117','M 98,174 L 108,169']
# Circling: palm stays fixed; two illustrative finger phases share MCP roots.
CIRCLE_END=POINT.replace('L 134,91 C 133,82 138,77 144,77 C 151,77 155,83 155,91 L 154,147','L 150,115 L 156,94 C 158,86 165,84 169,89 C 173,94 173,100 167,108 L 155,130 L 154,147')
COMMANDS=[('01','open','開啟'),('02','confirm','確認'),('03','previous','上一步'),('04','next','下一步'),('05','zoom-in','放大'),('06','zoom-out','縮小'),('07','reload','重播'),('08','capture','截圖'),('09','close','關閉')]
def h(shape,details,color=INK,ident='hand',transform=''):
 t=f' transform="{transform}"' if transform else ''
 return f'<g id="{ident}" stroke="{color}" {STYLE}{t}>'+''.join(f'<path d="{d}"/>' for d in [shape,*details])+'</g>'
def a(paths):
 return f'<g id="motion" stroke="{INK}" {STYLE}>'+''.join(f'<path d="{p}"/>' for p in paths)+'</g>'
def svg(title,body,desc):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 320 320" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}第一版樣圖，待研究者確認。</desc>{body}</svg>\n'
def save(group,num,command,cn,body,desc,stage='0-complete'):
 p=ROOT/group/f'{num}-{command}-{stage}.svg';p.write_text(svg(f'{cn}：{group} {stage}',body,desc),encoding='utf-8')
def static(group,num,command,cn,shape,details,transform=''):
 save(group,num,command,cn,h(shape,details,transform=transform),'右手靜態手勢，黑色簡化線條。')
def dynamic(group,num,command,cn,start,end,arrows,desc,trans_start='',trans_end='',details_start=None,details_end=None):
 sd=details_start or [];ed=details_end or []
 save(group,num,command,cn,h(start,sd,GRAY,'start',trans_start)+h(end,ed,INK,'end',trans_end)+a(arrows),desc+'灰色起始，黑色結束，箭頭為動作方向。')
 save(group,num,command,cn,h(start,sd,ident='start',transform=trans_start),desc+'起始姿態。','1-start')
 save(group,num,command,cn,h(end,ed,ident='end',transform=trans_end),desc+'結束姿態。','2-end')
CIRCLE_ARROW=['M 142,18 A 43,28 0 1 1 124,42','M 117,52 L 124,42 L 132,52']
CAP_ARROW=['M 112,98 Q 96,110 99,130','M 92,123 L 99,132 L 106,123']
OUT_ARROWS=['M 99,118 L 81,99','M 81,110 L 81,99 L 92,99','M 187,104 L 209,84','M 197,85 L 209,84 L 208,96']
IN_ARROWS=['M 77,93 L 100,117','M 89,116 L 100,117 L 99,105','M 211,86 L 188,107','M 189,95 L 188,107 L 200,105']
for group in ['domestic','international']:
 (ROOT/group).mkdir(exist_ok=True)
 static(group,'09','close','關閉',FIST,FIST_DETAILS)
 if group=='domestic':
  static(group,'01','open','開啟',THUMB,THUMB_DETAILS)
  static(group,'02','confirm','確認',OK,OK_DETAILS)
  for num,command,cn,sign in [('03','previous','上一步',-1),('04','next','下一步',1)]:
   arrows=['M 90,38 L 229,38','M 216,26 L 229,38 L 216,50'] if sign==1 else ['M 229,38 L 90,38','M 103,26 L 90,38 L 103,50']
   dynamic(group,num,command,cn,SPREAD,SPREAD,arrows,'整隻右手水平移動。',f'translate({-sign*27} 0)',f'translate({sign*27} 0)',SPREAD_DETAILS,SPREAD_DETAILS)
  dynamic(group,'05','zoom-in','放大',FIST,SPREAD,OUT_ARROWS,'整隻手掌與手指展開。',details_start=FIST_DETAILS,details_end=SPREAD_DETAILS)
  dynamic(group,'06','zoom-out','縮小',SPREAD,FIST,IN_ARROWS,'整隻手掌與手指收合。',details_start=SPREAD_DETAILS,details_end=FIST_DETAILS)
  dynamic(group,'07','reload','重播',SPREAD,SPREAD,['M 82,49 A 123,115 0 1 1 42,168','M 39,183 L 42,168 L 56,176'],'整隻手掌沿順時針圓形軌跡移動。','translate(-18 7)','translate(18 -7)',SPREAD_DETAILS,SPREAD_DETAILS)
  dynamic(group,'08','capture','截圖',CAP_START,CAP_END,CAP_ARROW,'沿用研究者指定可用於本國組的現有截圖手型；接觸程度待精修。',details_start=CAP_DETAILS,details_end=CAP_DETAILS)
 else:
  # Depth is a schematic cue, not an unverified change to the command definition.
  dynamic(group,'01','open','開啟',POINT,POINT,['M 223,106 L 267,64','M 253,64 L 267,64 L 267,78'],'食指向前推動；斜向箭頭與較小的後姿態表示離開身體的深度。手型依新增真實照片，與黃色表格一併待研究者核對。','translate(20 20) scale(.94)','translate(14 5) scale(.83)',POINT_DETAILS,POINT_DETAILS)
  static(group,'02','confirm','確認',THUMB,THUMB_DETAILS)
  static(group,'03','previous','上一步',POINT,POINT_DETAILS,'rotate(-90 160 160)')
  static(group,'04','next','下一步',POINT,POINT_DETAILS,'rotate(90 160 160)')
  dynamic(group,'05','zoom-in','放大',PINCH,POINT,OUT_ARROWS,'拇指與食指展開。',details_start=PINCH_DETAILS,details_end=POINT_DETAILS)
  dynamic(group,'06','zoom-out','縮小',POINT,PINCH,IN_ARROWS,'拇指與食指捏合。',details_start=POINT_DETAILS,details_end=PINCH_DETAILS)
  dynamic(group,'07','reload','重播',POINT,CIRCLE_END,CIRCLE_ARROW,'僅食指示意順時針畫圈，手掌與其餘手指固定。灰黑姿態是共同指根的示意相位，並非照片測得的精確端點。',details_start=POINT_DETAILS,details_end=POINT_DETAILS)
  dynamic(group,'08','capture','截圖',IP_START,IP_END,['M 113,66 Q 95,82 104,100','M 95,95 L 104,101 L 108,90','M 66,184 Q 66,164 82,152','M 70,153 L 82,152 L 79,163'],'拇指與食指各彎一個指節，半捏合快門。實際彎曲幅度與手指相對位置待精修。',details_start=POINT_DETAILS,details_end=IP_DETAILS)
