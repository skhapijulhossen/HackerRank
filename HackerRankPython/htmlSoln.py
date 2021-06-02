def handle_Tags(string):
    strLen = len(string)
    tags = []
    for index in range(strLen):
        if string[index] == '<' or string[index:(index+2)] == '</':
            tag = ''
            index = index+1 if string[index:(index+2)] == '</' else index

            for tindex in range(index+1, strLen):
                if string[tindex] != '>':
                    tag += string[tindex]
                else:
                    break
            if len(tag.split()) > 1:
                tag_attr = tag.split()
                tags.append({tag_attr[0]: tag_attr[1]})
            else:
                tags.append(tag)

    # print(tags)
    return tags


def tagsToString(tags):
    string = ''
    for tag in tags:
        if type(tag) == dict:
            key = list(tag.keys())[0]
            string = string + "<"+str(key)+" "+str(tag[key])+'>'
        else:
            string = string + '</'+tag+">"

    return string


def append(givenString, id, stringToadd):
    tags = handle_Tags(givenString)
    tagToadd = handle_Tags(stringToadd)
    newtags = []
    index = 0
    tags_len = len(tags)
    for tag in tags:
        if type(tag) == dict and tag[list(tag.keys())[0]][-2] == id:
            newtags.append(tag)
            checktag = [tag]
            for innertag in tags[index+1:]:
                checktag.append(innertag)
                if type(innertag) != dict and len(checktag) % 2 == 0:
                    newtags.append(tagToadd[0])
                    newtags.append(tagToadd[1])
                    newtags.append(tagToadd[1])
                else:
                    newtags.append(innertag)

        else:
            if tags_len+2 == len(newtags):
                break
            newtags.append(tag)
        index += 1
    print(tagsToString(newtags))


def prepend(givenString, id, stringToadd):
    tags = handle_Tags(givenString)
    tagToadd = handle_Tags(stringToadd)
    newtags = []
    tags_len = len(tags)
    for tag in tags:
        if type(tag) == dict and tag[list(tag.keys())[0]][-2] == id:
            newtags.append(tag)
            newtags.append(tagToadd[0])
            newtags.append(tagToadd[1])
        else:
            if tags_len+2 == len(newtags):
                break
            newtags.append(tag)
    print(tagsToString(newtags))


def after(givenString, id, stringToadd):
    tags = handle_Tags(givenString)
    tagToadd = handle_Tags(stringToadd)
    newtags = []
    index = 0
    tags_len = len(tags)
    for tag in tags:
        if type(tag) == dict and tag[list(tag.keys())[0]][-2] == id:
            newtags.append(tag)
            checktag = [tag]
            for innertag in tags[index+1:]:
                checktag.append(innertag)
                if type(innertag) != dict and len(checktag) % 2 == 0:
                    newtags.append(tagToadd[1])
                    newtags.append(tagToadd[0])
                    newtags.append(tagToadd[1])
                else:
                    newtags.append(innertag)

        else:
            if tags_len+2 == len(newtags):
                break
            newtags.append(tag)
        index += 1
    print(tagsToString(newtags))


def before(givenString, id, stringToadd):
    tags = handle_Tags(givenString)
    tagToadd = handle_Tags(stringToadd)
    newtags = []
    tags_len = len(tags)
    for tag in tags:
        if type(tag) == dict and tag[list(tag.keys())[0]][-2] == id:
            newtags.append(tagToadd[0])
            newtags.append(tagToadd[1])
            newtags.append(tag)
        else:
            if tags_len+2 == len(newtags):
                break
            newtags.append(tag)
    print(tagsToString(newtags))


if __name__ == '__main__':
    print('Before Operations : <div id="1"><div id="2"><div id="3"></div></div></div>')
    print('\n\n After append() :')
    append('<div id="1"><div id="2"><div id="3"></div></div></div>',
           '2', '<div id="4"></div>')
    print('\n\n After prepend() :')
    prepend('<div id="1"><div id="2"><div id="3"></div></div></div>',
            '2', '<div id="4"></div>')
    print('\n\n After after() :')
    after('<div id="1"><div id="2"><div id="3"></div></div></div>',
          '2', '<div id="4"></div>')
    print('\n\n After before() :')
    before('<div id="1"><div id="2"><div id="3"></div></div></div>',
           '2', '<div id="4"></div>')
