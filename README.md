# MR Gesture Icons｜混合實境手勢圖示

兩組研究手勢的對應圖片，供簡報與紙本文件使用。提供兩組共 18 張解剖線稿 PNG（`realistic-`）。

| 資料夾 | 組別 |
|---|---|
| `domestic/` | 本國組，原九宮格 |
| `international/` | 非本國組，原黃色表格 |

## 指令對照

下表直接引用兩組的同名 PNG；圖片更新後，這裡同步顯示新版。雙姿態動態圖以左側灰線為起始姿態、右側黑線為結束姿態，兩姿態分開呈現；重播以單一右手搭配順時針箭頭表示。

| 編號 | 指令／檔名 | 本國組 | 非本國組 |
|---|---|---|---|
| 01 | 開啟 `open` | <img src="domestic/png/realistic-01-open-0-complete.png" width="180" alt="domestic 01 open"> <br> 拇指伸直朝上，其餘四指收合 | <img src="international/png/realistic-01-open-0-complete.png" width="180" alt="international 01 open"> <br> 食指靜態指向前方，其餘四指收合（手背側） |
| 02 | 確認 `confirm` | <img src="domestic/png/realistic-02-confirm-0-complete.png" width="180" alt="domestic 02 confirm"> <br> 拇指與食指接觸成圈，其餘三指伸出 | <img src="international/png/realistic-02-confirm-0-complete.png" width="180" alt="international 02 confirm"> <br> 拇指伸直朝上，其餘四指收合 |
| 03 | 上一步 `previous` | <img src="domestic/png/realistic-03-previous-0-complete.png" width="180" alt="domestic 03 previous"> <br> 食指向左伸直，其餘四指收合（掌側） | <img src="international/png/realistic-03-previous-0-complete.png" width="180" alt="international 03 previous"> <br> 食指向左伸直，其餘四指收合（掌側） |
| 04 | 下一步 `next` | <img src="domestic/png/realistic-04-next-0-complete.png" width="180" alt="domestic 04 next"> <br> 食指向右伸直，其餘四指收合（手背側） | <img src="international/png/realistic-04-next-0-complete.png" width="180" alt="international 04 next"> <br> 食指向右伸直，其餘四指收合（手背側） |
| 05 | 放大 `zoom-in` | <img src="domestic/png/realistic-05-zoom-in-0-complete.png" width="180" alt="domestic 05 zoom-in"> <br> 五指由收合逐漸張開（手背朝自己，拇指在左側） | <img src="international/png/realistic-05-zoom-in-0-complete.png" width="180" alt="international 05 zoom-in"> <br> 拇指與食指由接觸分開，其餘三指收合 |
| 06 | 縮小 `zoom-out` | <img src="domestic/png/realistic-06-zoom-out-0-complete.png" width="180" alt="domestic 06 zoom-out"> <br> 五指由張開逐漸收合（手背朝自己，拇指在左側） | <img src="international/png/realistic-06-zoom-out-0-complete.png" width="180" alt="international 06 zoom-out"> <br> 拇指與食指由分開到接觸，其餘三指收合 |
| 07 | 重播 `reload` | <img src="domestic/png/realistic-07-reload-0-complete.png" width="180" alt="domestic 07 reload"> <br> 整手伸展，沿順時針軌跡畫圈；單一右手與兩個相連的開放式橢圓弧箭頭 | <img src="international/png/realistic-07-reload-0-complete.png" width="180" alt="international 07 reload"> <br> 其餘手指收合，食指順時針畫圈（手背側）；單一右手與兩個相連的開放式橢圓弧箭頭 |
| 08 | 截圖 `capture` | <img src="domestic/png/realistic-08-capture-0-complete.png" width="180" alt="domestic 08 capture"> <br> 拇指與食指由分開到接觸捏合，其餘三指收合 | <img src="international/png/realistic-08-capture-0-complete.png" width="180" alt="international 08 capture"> <br> 拇指與食指各彎一個指節，指尖仍分開；其餘三指收合 |
| 09 | 關閉 `close` | <img src="domestic/png/realistic-09-close-0-complete.png" width="180" alt="domestic 09 close"> <br> 五指收合成拳 | <img src="international/png/realistic-09-close-0-complete.png" width="180" alt="international 09 close"> <br> 五指收合成拳 |

## 命名原則

格式：`兩位指令編號-指令名稱-圖片編號-用途.svg`。兩組使用一致的指令順序。

| 後綴 | 用途 |
|---|---|
| `-0-complete.svg` | 完整表意；新版 PNG 動態手勢左右分開呈現前後姿態；僅重播保留旋轉箭頭 |
| `-1-start.svg` | 動態手勢的起始姿態 |
| `-2-end.svg` | 動態手勢的結束姿態 |

例如 `08-capture-0-complete.svg`。篩選 `-complete.svg` 可取得兩組共 18 張完整圖；連同動態拆分版本，共 34 張 SVG。

新版 PNG 使用 `realistic-兩位編號-指令名稱-0-complete.png`，放在 `domestic/png/` 與 `international/png/`。兩組各 9 張，透明外背景、白色手部內底。原 SVG 與舊 PNG 保留供追溯。

## 製作方式

依研究者提供的原九宮格（本國組）、黃色表格（非本國組）與 [HackMD 實拍](https://hackmd.io/vlS1KejZR96oRrO-DFbUiA) 核對。統一使用本人看自己右手的第一人稱視角，逐張核對掌背面與拇指位置。

`realistic-` 為解剖線稿 PNG，以研究者重附的五張產圖為風格基準，補圖使用 OpenAI imagegen。左側灰線表示起始姿態、右側黑線表示結束姿態，動態圖在同一畫布左右分開，左灰表示先比的姿態、右黑表示後比的姿態；不使用表示前後順序的向右箭頭；重播依研究者實拍右手呈現單一姿態，使用兩個順時針橢圓弧箭頭；開放式尖端與弧線相連，不使用實心三角形。PNG 具有透明外背景與白色手部內底。原 SVG 與舊 PNG 保留供追溯，README 預覽引用新版本。
