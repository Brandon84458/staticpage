import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Method: __eq__()
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "www.test.com")
        self.assertNotEqual(node, node2) 
    def test_eq5(self):
        node = TextNode("This is a text node", TextType.TEXT, "www.test-node.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "www.test-node2.com")
        self.assertNotEqual(node, node2) 
    def test_eq6(self):
        node = TextNode("This is a text node (#1)", TextType.TEXT, "www.test.com")
        node2 = TextNode("This is a text node (#2)", TextType.TEXT, "www.test.com")
        self.assertNotEqual(node, node2)
    # Method: __repr__()
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node_repr = node.__repr__()
        test_repr = "TextNode(This is a text node, bold, www.test.com)"
        self.assertEqual(node_repr, test_repr)
    def test_repr2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_repr = node.__repr__()
        test_repr = "TextNode(This is a text node, bold, None)"
        self.assertEqual(node_repr, test_repr)
    def test_repr3(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node_repr = node.__repr__()
        test_repr = "TextNode(This is a test node, bold, www.test.com)"
        self.assertNotEqual(node_repr, test_repr)

    


if __name__ == "__main__":
    unittest.main()