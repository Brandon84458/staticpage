from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode):
        if (self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        html_node = LeafNode(None, text_node.text)
        return html_node
    elif text_node.text_type == TextType.BOLD:
        html_node = LeafNode("b", text_node.text)
        return html_node
    elif text_node.text_type == TextType.ITALIC:
        html_node = LeafNode("i", text_node.text)
        return html_node
    elif text_node.text_type == TextType.CODE:
        html_node = LeafNode("code", text_node.text)
        return html_node
    elif text_node.text_type == TextType.LINK:
        html_node = LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        return html_node
    elif text_node.text_type == TextType.IMAGE:
        html_node = LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
        return html_node
    else:
        raise Exception("Error: TextType does not exist.")