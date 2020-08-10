from newsplease import NewsPlease
article = NewsPlease.from_url('https://www.nytimes.com/interactive/projects/cp/opinion/election-night-2016/paul-krugman-the-economic-fallout')
print(article.title)
print(article.maintext)