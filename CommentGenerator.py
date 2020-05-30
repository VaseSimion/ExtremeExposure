import random

def getauthor(url):
    print(url)
    while "by-" in url:
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
                          "Splendid ", "Captivating ", "Formidable ", "Enchanting "]

    special_first_part = ["What a ", "Love this ", "Daaaamn, ", "", "", "", "", "", "", "", "", "", ""]

    second_part_comment = ["image", "photo", "shot", "work", "picture", "frame", "snapshot", "composition", "capture",
                           "scene"]

    third_part_comment = [" Congrats!", " Congratulations!", " Good job!", " Well taken!", "", "", "", "", "", "", "",
                          "", ""]

    comment = random.choice(special_first_part)
    if comment == "":
        comment += random.choice(first_part_comment)
        comment += random.choice(second_part_comment)
    else:
        comment += random.choice(first_part_comment).lower()
        comment += random.choice(second_part_comment)
    if author == "":
        return comment + "!" + random.choice(third_part_comment)
    else:
        comment += (", " + author.split(" ")[0] + "!" + random.choice(third_part_comment))
        return comment
