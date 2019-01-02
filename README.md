## 專案題目
AnsText∕文字資料分析處理器

## 簡述（100字內）
社會研究方法中有一種研究方法是「內容分析法」，透過分析文本或是圖片的意涵來探究世界。本專案的目的即是協助內容分析法的資料整理。
本專案的功能有三，資料儲存與編號、關鍵字標註、關鍵字搜尋。

---
## 目的/功能說明（約500字即可）
社會研究方法中有一種研究方法是「內容分析法」，透過分析文本或是圖片的意涵來探究世界。本專案的目的即是協助內容分析法的資料整理。本專案的目標功能有三：  
（1）資料儲存與編號：將需要處理的資料分則儲存並編號（如：A01、RE56等）  
（2）關鍵字標註：針對關鍵字，將所有資料中的關鍵字標註起來。（如：以民主做關鍵詞，捍衛台灣《民主》。）  
（3）關鍵字搜尋：針對有關鍵字的資料編號羅列出來，可以選擇查詢所有或特定則資料，也可以只列出有民主的那句話。

## 你覺得可能會遇到的困難，請盡量清楚地條列敘述。
（1）資料儲存的方法還不會。  
（2）編號的方式還在思考。  
（3）只列出含關鍵字的一句話，要判斷是否是標點符號。  
（4）只列出含關鍵字的一句話，要分別向前與向後搜尋。

## 如何達成此專案的功能

（1）資料儲存（先用範例中的，之後有機會再另尋它法）  
  
  本專案將把使用者所輸入的資料以CSV格式儲存。Python有內建的[csv][link_csv]套件可以儲存和讀取CSV檔，但在程式裡，可能仍須另外實作兩個函式負責把事件資料結構寫入CSV，和從CSV載入事件資料結構。

由於此專案的目的之一是保護使用者隱私，即便此程式僅會將資料儲存於本機，但畢竟只是一個明碼（plain text）儲存的文字檔（CSV）。故未來計畫在寫入檔案時將檔案內容加密。Python有眾多加密套件可供選擇，其中[pyCryptodome][link_crypto]是使用社群較廣且程式介面方便、說明文件完整的加密工具。
 [link_csv]: https://docs.python.org/3/library/csv.html
 [link_crypto]: https://www.pycryptodome.org/en/latest/  
   
   （2）編號  
   
   這個應該不難，使用變數儲存數字就行，再搭配上面的資料儲存功能就可以達成。  
   
   （3）斷句  
   
   斷句需要判斷字元是否為標點符號，目前找到以下文章：https://www.cnblogs.com/arkenstone/p/6092255.html，看來現存套件已經可以完成斷句的功能。  
   
   （4）圖形化介面  
   
   希望可以做出GUI，以使用者使用這個程式。但要等其它功能解決再來考慮。另外，視窗程式設計的套件可以有GUI。目前找到以下文章：http://stackoverflow.max-everyday.com/2018/05/python-gui-framework/
