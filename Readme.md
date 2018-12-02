Data sources :
    most of our data sources were pdf files, images and websites. You can find them in the following links :
        Unemployment indicator : [link](http://www.ins.nat.tn/sites/default/files/publication/pdf/Note_ENPE_2T2018_F.pdf)
        Regional development indicator : [link](http://www.cgdr.nat.tn/upload/files/13.pdf)
        Foreign direct investment : [link](www.investintunisia.tn/Fr/image.php?id=2535) 
        Institutional determinants : [link](http://www.tunisieindustrie.nat.tn/fr/DR.asp?Gvt=0)
        Global unemployment rate :  [link](https://fr.tradingeconomics.com/tunisia/indicators)
        Inflation rate: [link](https://fr.tradingeconomics.com/tunisia/indicators)
        GDP : [link](https://fr.tradingeconomics.com/tunisia/gdp)

Data extraction methods :
    Since our data sources are scanned and not in an iterable state, our extraction methods were basically built on OCR and web scraping.
    Parsing with OCR methods which are ToCsvOCRMethod() and toPdfOcrMethod() extracts respectivly PDF to CSV and Image to PDF.
    Parsing with web scraping is done to extract Institutional determinant by the webScraping() method. This method sends a request to the correspanding url and extract some specific li tags and h2 tags that describes the Institutional determinants.

