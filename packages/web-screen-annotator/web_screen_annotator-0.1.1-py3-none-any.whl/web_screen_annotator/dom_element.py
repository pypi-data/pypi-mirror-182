import re


class DomElement:
    def __init__(self, raw_dom, parent=None):
        self.parent = parent
        self.tag = raw_dom["tag"].lower()
        self.left = raw_dom["left"]
        self.top = raw_dom["top"]
        self.width = raw_dom["width"]
        self.height = raw_dom["height"]
        if "text" in raw_dom:
            self.text = str(raw_dom["text"])
        else:
            self.text = None
        self.value = raw_dom.get("value")
        self.id = raw_dom.get("id")
        self.children = []
        for raw_child in raw_dom["children"]:
            self.children.append(DomElement(raw_child, parent=self))
        if self.children and all(child.tag == "t" for child in self.children):
            self.text = " ".join(child.text for child in self.children)
            self.children = []

    def __eq__(self, other):
        if not isinstance(other, DomElement):
            return False
        return self.ref == other.ref

    def __ne__(self, other):
        return not self.__eq__(other)

   