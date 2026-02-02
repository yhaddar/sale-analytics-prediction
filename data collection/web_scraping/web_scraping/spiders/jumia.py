import scrapy


class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["www.jumia.ma"]
    start_urls = ["https://www.jumia.ma"]

    def parse(self, response):
        voir_plus = response.xpath("//main[@class='has-b2top']//div[@class='row -pvm']//div[contains(@class, 'col16')]")
        for v in voir_plus:
            section = v.css("section.card")
            if section:
                header = section.xpath("//header")
                link_container = header.css("div.col")
                if link_container:
                    link = link_container.css("a::attr(href)").get()
                    print(f"https://www.jumia.ma{link}")