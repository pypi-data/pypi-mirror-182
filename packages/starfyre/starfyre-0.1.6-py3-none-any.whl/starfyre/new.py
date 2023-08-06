from html.parser import HTMLParser
from dataclasses import dataclass
import js


@dataclass
class Node:
    tag: str
    props: dict
    children: list


class Parser(HTMLParser):
    stack = []

    def handle_starttag(self, tag, attrs):
        props = {}
        for attr in attrs:
            props[attr[0]] = attr[1]

        self.stack.append(Node(tag, props, []))

    def handle_endtag(self, tag):

        children = []
        while self.stack:
            node = self.stack[-1]
            if type(node) == Node and node.tag == tag:
                break

            self.stack.pop()
            children.append(node)

        children = children[::-1]
        if self.stack:
            self.stack[-1].children = children

        print("Encountered an end tag :", self.stack)

    def handle_data(self, data):
        self.stack.append(data)

    def parse(self):
        return self.stack


def create_element_tree(node):
    if type(node) == str:
        return node

    element = js.document.createElement(node.tag)

    if node.props:
        for key, value in node.props.items():
            element.setAttribute(key, value)

    if node.children:
        for child in node.children:
            next_element = create_element_tree(child)
            if type(next_element) == str:
                element.innerHTML += next_element
            else:
                element.appendChild(next_element)

    return element


def render(element: str, container):
    # not sure what this is supposed to do right now
    container.appendChild(element)
    return container


def render_root(element: str):
    div = js.document.createElement("div")
    div.setAttribute("id", "root")
    parser = Parser()
    parser.feed(element)
    parser.close()

    pytml_tree = parser.parse()
    pytml_root = pytml_tree[0]

    element = create_element_tree(pytml_root)
    if type(element) == str:
        div.innerHTML = element
    else:
        div.appendChild(element)

    js.document.body.prepend(div)
