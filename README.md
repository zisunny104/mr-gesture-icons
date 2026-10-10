# MR Gesture Icons｜混合實境手勢圖示

兩組研究手勢的對應圖片，供簡報與紙本文件使用。SVG 手型仍在確認中。

| 資料夾 | 組別 |
|---|---|
| `domestic/` | 本國組，原九宮格 |
| `international/` | 非本國組，原黃色表格 |

## 指令對照

下表直接引用兩組的同名 PNG；圖片更新後，這裡同步顯示新版。灰色表示起始姿態，黑色表示結束姿態。

| 編號 | 指令／檔名 | 本國組 | 非本國組 |
|---|---|---|---|
| 01 | 開啟 `open` | <img src="domestic/png/01-open-0-complete.png" width="180" alt="domestic 01 open"> <br> 比讚 | <img src="international/png/01-open-0-complete.png" width="180" alt="international 01 open"> <br> 食指靜態向前指 |
| 02 | 確認 `confirm` | <img src="domestic/png/02-confirm-0-complete.png" width="180" alt="domestic 02 confirm"> <br> OK | <img src="international/png/02-confirm-0-complete.png" width="180" alt="international 02 confirm"> <br> 比讚 |
| 03 | 上一步 `previous` | <img src="domestic/png/03-previous-0-complete.png" width="180" alt="domestic 03 previous"> <br> 食指指向左（掌側，拇指收起） | <img src="international/png/03-previous-0-complete.png" width="180" alt="international 03 previous"> <br> 食指指向左（掌側，拇指收起） |
| 04 | 下一步 `next` | <img src="domestic/png/04-next-0-complete.png" width="180" alt="domestic 04 next"> <br> 食指指向右（掌側，拇指收起） | <img src="international/png/04-next-0-complete.png" width="180" alt="international 04 next"> <br> 食指指向右（掌側，拇指收起） |
| 05 | 放大 `zoom-in` | <img src="domestic/png/05-zoom-in-0-complete.png" width="180" alt="domestic 05 zoom-in"> <br> 手掌展開 | <img src="international/png/05-zoom-in-0-complete.png" width="180" alt="international 05 zoom-in"> <br> 拇指與食指展開 |
| 06 | 縮小 `zoom-out` | <img src="domestic/png/06-zoom-out-0-complete.png" width="180" alt="domestic 06 zoom-out"> <br> 手掌收合 | <img src="international/png/06-zoom-out-0-complete.png" width="180" alt="international 06 zoom-out"> <br> 拇指與食指捏合 |
| 07 | 重播 `reload` | <img src="domestic/png/07-reload-0-complete.png" width="180" alt="domestic 07 reload"> <br> 手掌順時針畫圈 | <img src="international/png/07-reload-0-complete.png" width="180" alt="international 07 reload"> <br> 食指順時針畫圈 |
| 08 | 截圖 `capture` | <img src="domestic/png/08-capture-0-complete.png" width="180" alt="domestic 08 capture"> <br> 沿用研究者指定的截圖手型 | <img src="international/png/08-capture-0-complete.png" width="180" alt="international 08 capture"> <br> 拇指與食指各彎一個指節 |
| 09 | 關閉 `close` | <img src="domestic/png/09-close-0-complete.png" width="180" alt="domestic 09 close"> <br> 握拳 | <img src="international/png/09-close-0-complete.png" width="180" alt="international 09 close"> <br> 握拳 |

## 命名原則

格式：`兩位指令編號-指令名稱-圖片編號-用途.svg`。兩組使用一致的指令順序。

| 後綴 | 用途 |
|---|---|
| `-0-complete.svg` | 完整表意；動態手勢合併前後姿態與箭頭 |
| `-1-start.svg` | 動態手勢的起始姿態 |
| `-2-end.svg` | 動態手勢的結束姿態 |

例如 `08-capture-0-complete.svg`。篩選 `-complete.svg` 可取得兩組共 18 張完整圖；連同動態拆分版本，共 34 張 SVG。

完整圖另存同名 PNG，分別放在 `domestic/png/` 與 `international/png/`，透明背景，1920 × 1920。修改直接更新原圖，預覽與討論留在對話中。

## 製作方式

謝祥紫提供手勢定義、簡報及照片，並確認圖示。OpenAI Codex（GPT-6.1 Sol）協助編寫 SVG 向量路徑；以原圖的手型為基準，照片輔助辨識骨架與指節，統一黑色線條及 320 × 320 畫布。動態圖使用灰色起始姿態、黑色結束姿態與方向箭頭。人體結構與動作以研究者確認為準。
