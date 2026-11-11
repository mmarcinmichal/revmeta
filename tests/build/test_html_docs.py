"""Portable tests for deterministic, source-backed HTML vocabulary documentation."""
from __future__ import annotations

from copy import deepcopy
from html.parser import HTMLParser
import json
import tempfile
import unittest
from pathlib import Path

from revmeta.build.html_docs import write_html
from revmeta.build.vocabulary import build, canonical_turtle, registry_graph

ROOT = Path(__file__).resolve().parents[2]


class _Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.references = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if 'id' in attributes:
            self.ids.append(attributes['id'])
        if tag == 'a' and attributes.get('href', '').startswith('#'):
            self.references.append(attributes['href'][1:])


class HtmlDocumentationTests(unittest.TestCase):
    def test_full_graph_has_stable_valid_internal_anchors(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            ttl, _ = build(ROOT / 'resources/inputs/vocabulary/registry.json', root / 'rdf')
            index = root / 'index.html'
            write_html(ttl, index)
            first = index.read_bytes()
            write_html(ttl, index)
            self.assertEqual(first, index.read_bytes())
            parsed = _Links()
            parsed.feed(first.decode('utf-8'))
            self.assertEqual(len(parsed.ids), len(set(parsed.ids)))
            self.assertEqual(len([i for i in parsed.ids if i.startswith('concept-')]), 102)
            self.assertEqual(len([i for i in parsed.ids if i.startswith('facet-') and not i.endswith('-title')]), 14)
            self.assertTrue(set(parsed.references) <= set(parsed.ids))
            self.assertIn(b'Resource version: <code>1.0.0</code>', first)
            self.assertIn(b'Apache-2.0', first)
            self.assertIn(b'Publication status and persistent identifier resolution', first)
            self.assertNotIn(b'Development preview', first)
            self.assertNotIn(b'not establish a public release, approved license', first)
            self.assertIn(b'vocabulary.jsonld', first)

    def test_source_definitions_are_escaped_not_rendered_as_markup(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            registry = json.loads((ROOT / 'resources/inputs/vocabulary/registry.json').read_text(encoding='utf-8'))
            changed = deepcopy(registry)
            changed['terms'][0]['definition'] = '<script>alert("injected")</script> & value'
            ttl = root / 'vocabulary.ttl'
            ttl.write_text(canonical_turtle(registry_graph(changed)), encoding='utf-8')
            index = write_html(ttl, root / 'index.html')
            contents = index.read_text(encoding='utf-8')
            self.assertNotIn('<script>alert', contents)
            self.assertIn('&lt;script&gt;alert(&quot;injected&quot;)&lt;/script&gt; &amp; value', contents)


if __name__ == '__main__':
    unittest.main()
