input = str(input("Enter your string"))
input = input.strip()
news = []
splitted = input.split(" ")

for i in splitted:
    if(i != ""):
        news.append(i)

news.reverse()
news = " ".join(news)
print(news)
