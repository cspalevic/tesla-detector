from icrawler.builtin import BingImageCrawler

models = [
    "Tesla Model 3",
    "Tesla Model S",
    "Tesla Model X",
    "Tesla Model Y"
]

for model in models:
   storage = {
      "backend": "FileSystem",
      "root_dir": "data/" + model
   }
   crawler = BingImageCrawler(storage=storage)
   crawler.crawl(keyword=model, max_num=1000)