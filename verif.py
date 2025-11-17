# from htmldate import find_date

# print(find_date('https://www.artificialintelligence-news.com/news/ibm-data-silos-are-holding-back-enterprise-ai/'))
def stergere_fisier():
    with open("plain_text.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate(0)
# with open("plain_text.txt", "w") as f:
#     f.write("fasole")
