import random

def getauthor(url):
    print(url)
    url = url[url.index("by-")+3:]
    url = url[:url.index("?")]
    authorlist = url.split('-')
    temporaryauthorlist=[]
    for name in authorlist:
        if "%" not in name:
            temporaryauthorlist.append(name)
        author = " ".join(temporaryauthorlist)
    print(author)
    return author


def getcomment(topic, author):
    first_part_comment = ["Awesome ", "Amazing ", "Excellent ", "Stunning ", "Cool ", "Lovely ", "Wonderful ",
                          "Superb ", "Spectacular ", "Great ", "Fantastic ", "Nice ", "Impressive ", "Fabulous ",
                          "Splendid ", "Captivating "]

    special_first_part = ["What a ", "Love this ", "Daaaamn, ", "", "", ""]

    second_part_comment = ["image", "photo", "shot", "work", "picture", "frame", "snapshot"]

    comment = random.choice(special_first_part)
    if comment == "":
        comment += random.choice(first_part_comment)
        comment += random.choice(second_part_comment)
    else:
        comment += random.choice(first_part_comment).lower()
        comment += random.choice(second_part_comment)
    if author == "":
        return comment + "!"
    else:
        comment += (", " + author.split(" ")[0] + "!")
        return comment
