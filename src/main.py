from textnode import TextNode, TextType

def main():
    my_node = TextNode("test text", TextType.LINK, "test.com")
    print(my_node)

main()