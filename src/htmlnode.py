class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if type(self.props) == type(None):
            return "None"
        string = ""
        for key in self.props:
            string = f'{string} {key}="{self.props[key]}"'
        return string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode needs a tag")
        if self.children == None:
            raise ValueError("Child needs a value")
            
        string = f"<{self.tag}>"
        for child in self.children:
            string = string + child.to_html()
        string = f"{string}</{self.tag}>"
        return string