import webbrowser

class Movie():
    def __init__(self,title,story_line,poster,trailer):
        self.title=title
        self.story_line=story_line
        self.poster=poster
        self.trailer=trailer

    def show_triler(self):
        webbrowser.openurl(trailer)
