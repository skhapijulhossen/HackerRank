from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : ',tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
    def handle_endtag(self,tag):
        print(f'End   : ',tag)
    def handle_comment(self,data):
        pass
    def handle_startendtag(self,tag,attrs):
        print(f'Empty : {tag}')
parser = MyParser()
parser.feed("<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")