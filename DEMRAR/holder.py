"""class Thing(StructuredNode):
    name = StringProperty(unique_index=True, required=True)


class Action(StructuredNode):
    name = StringProperty(unique_index=True, required=True)


class Place(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    is_a = RelationshipTo(Thing, "related_to")


class Person(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    locations = RelationshipTo(Place, "location")
    things = RelationshipTo(Thing, "related_to")
    doing = RelationshipTo(Action, 'does')"""

from lxml import html
import requests
import bisect
import queue
from neomodel import StructuredNode, StringProperty, Relationship, config


class Basic(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    to = Relationship("Basic", "related_to")
    link = StringProperty(required=False)


def process_wiki(site, depth, parent, searched=False):
    first_search = None
    if not searched:
        first_search = Basic.nodes.get_or_none(name=site)
    if not first_search:
        this_node = Basic(name=site)
        this_node.save()
    if parent:
        this_node.to.connect(parent)

    if depth <= 1:
        return

    page = requests.get(base + site)
    tree = html.fromstring(page.content)

    for el in tree.xpath(xpath):
        try:
            el.attrib['href']
        except KeyError:
            continue

        search = Basic.nodes.get_or_none(name=el.attrib['href'])

        if "/wiki/" == el.attrib['href'][:6] and ("BookSources" and "citation_needed" and "Citation_needed" and ":") \
                not in el.attrib['href'] and el.text_content():
            if search:
                this_node.to.connect(search)
            else:
                process_wiki(el.attrib['href'], depth - 1, this_node, True)


if __name__ == '__main__':
    server = "bolt://neo4j:1234@localhost:7687"
    config.DATABASE_URL = server

    user = "neo4j"
    password = "1234"

    for x in Basic.nodes.all():
        print(x)
        x.delete()

    base = "https://en.wikipedia.org"
    link = "/wiki/Jarvis_Island/People"

    if link.count("/") > 2:
        link = "/".join(link.split("/")[:3])

    # with "see also part"
    xpath = '//div[@id="mw-content-text"]//p//a'

    q = queue.Queue()

    process_wiki(link, 2, None)
