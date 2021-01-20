import abc

class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_title(self, title):
        pass
    
    @abc.abstractmethod
    def set_text(self, text):
        pass

    @abc.abstractmethod
    def set_items(self, items):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def set_result(self):
        pass

class Director:

    def __init__(self, builder):
        self.builder = builder

    def constructor(self):
        self.builder.setTitle("Greet")
        self.builder.setText("아침에는")
        self.builder.setItems(["goodMorning", "좋은 아침입니다.", "좋아"])
        self.builder.setText("저녁에는")
        self.builder.setItems(["goodEvening", "멋진 저녁입니다.", "좋아"])
        self.builder.close()




class HtmlDocuments(Builder):

    def __init__(self):
        self.str = ""

    def setTitle(self, title):
        self.str += "<h1>"+title+"</h1>\n"

    def setText(self, text):
        self.str += "<p>" + text + "</p>\n"

    def setItems(self, items):
        self.str+="<ul>"
        for i, item in enumerate(items):
            self.str += "<li>"+str(i)+". "+item+"</li>\n"
        self.str += "</ul>\n"

    def close(self):
        super().close()

    def getResult(self):
        return self.str



class TextDocuments(Builder):

    def __init(self):
        self.str = ""

    def setTitle(self, title):
        self.str+="----------------------------"
        self.str += title+"\n"

    def setText(self, text):
        self.str += text + "\n"

    def setItems(self, items):
        for i, item in enumerate(items):
            self.str += "<li>"+i+". "+item+"</li>\n"

    def close(self):
        super().close()

    def getResult(self):
        return self.str





