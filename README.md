##Web Scraping with Scrapy then Storing with SQLite database


本計畫主要透過Scrapy於網路擷取博客來網站(books.com.tw)中文熱銷書籍排行榜，並將擷取資料儲存至python內建的SQLite database。

主要的檔案分別為：

1. with_scrapy_books folder  --Scrapy爬蟲所需檔案皆位於此文件夾裡頭。
2. demo_db  --位於folder裡頭，為SQLite產生的database。
3. top_100_from_books.csv  --透過SQLite Browsr產生的.csv檔，為擷取至database的內容資料。
