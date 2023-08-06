import js

from .parser import Node, Parser


def create_element_tree(node) -> js.Element | str:
    if type(node) == str:
        return node

    element = js.document.createElement(node.tag)

    if node.props:
        for key, value in node.props.items():
            element.setAttribute(key, value)

    if node.children:
        for child in node.children:
            element.appendChild(create_element_tree(child))

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


# create a function that takes a html string and returns a python object
def parse_html(html):



__all__ = ["render", "render_root", "js"]


if __name__ == "__main__":

    div = js.document.createElement("div")
    div.innerHTML = "Hello World"
    js.document.body.prepend(div)
