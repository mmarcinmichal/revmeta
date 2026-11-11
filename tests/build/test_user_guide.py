"""Public-portable tests for consolidated user guide and source SVGs."""
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree

from revmeta.build.decision_states import PRIMARY_DECISION_STATES

ROOT = Path(__file__).resolve().parents[2]
USER = ROOT / "docs/user"
SVGS = ("revmeta-artifacts.svg", "revmeta-teaser.svg", "revmeta-teaser-paper.svg")
SVGNS = "{http://www.w3.org/2000/svg}"


class SingleUserGuideTests(unittest.TestCase):
    def test_one_manual_preserves_terms_states_and_release_warnings(self):
        self.assertEqual(sorted(p.name for p in USER.glob("*.md")), ["README.md"])
        readme = (USER / "README.md").read_text(encoding="utf-8")
        for text in ("Machine-readable Codebook", "Build and verify locally",
                     "Seven coding decision states", "Mapping and interpretation policy",
                     "Provenance, licensing and release status", "691", "102",
                     "14 facets", "141", "107", "34", "public release"):
            with self.subTest(text=text):
                self.assertIn(text, readme)
        for status, _label, definition, _evidence in PRIMARY_DECISION_STATES:
            with self.subTest(status=status):
                self.assertIn(chr(96) + status + chr(96), readme)
                self.assertIn(definition, readme)
        for former in ("build.md", "decision-states.md", "codebook-rdf.md",
                       "mapping-policy.md", "provenance.md"):
            self.assertFalse((USER / former).exists(), former)
            self.assertNotIn("](" + former + ")", readme)

    def test_three_svgs_are_safe_and_linked(self):
        readme = (USER / "README.md").read_text(encoding="utf-8")
        image_links = re.findall(r"!\[[^\]]+\]\((assets/[^)]+\.svg)\)", readme)
        self.assertEqual(sorted(image_links), sorted("assets/" + n for n in SVGS))
        self.assertEqual(sorted(p.name for p in (USER / "assets").glob("*.svg")),
                         sorted(SVGS))
        for name in SVGS:
            with self.subTest(svg=name):
                xml = (USER / "assets" / name).read_text(encoding="utf-8")
                root = ElementTree.fromstring(xml)
                self.assertEqual(root.tag, SVGNS + "svg")
                self.assertEqual(root.get("role"), "img")
                self.assertTrue(root.get("viewBox"))
                self.assertIsNotNone(root.find(SVGNS + "title"))
                self.assertIsNotNone(root.find(SVGNS + "desc"))
                for element in root.iter():
                    self.assertNotIn(element.tag, {SVGNS + "script",
                                                   SVGNS + "foreignObject",
                                                   SVGNS + "image"})
                    for key, value in element.attrib.items():
                        self.assertFalse(key.lower().startswith("on"))
                        if key.endswith("href"):
                            self.assertTrue(value.startswith("#"), value)
                for outdated in ("planned: codebook", "RSP profile ·",
                                 "46 example profiles", "2 profiles"):
                    self.assertNotIn(outdated, xml)

    def test_figure1_profiles_consult_all_three_sources(self):
        svg = (USER / 'assets/revmeta-artifacts.svg').read_text(encoding='utf-8')
        root = ElementTree.fromstring(svg)
        labels = {node.text for node in root.iter(SVGNS + 'text') if node.text}
        self.assertIn(
            'C · Publication coding profiles (created by annotators or tools)',
            labels,
        )
        for label in ('uses controlled terms', 'uses decision states',
                      'uses coding rules'):
            self.assertIn(label, labels)
        for obsolete in ('uses terms', 'uses states', 'rules applied',
                         'by annotators'):
            self.assertNotIn(obsolete, labels)
        paths = {el.get('d'): el for el in root.iter(SVGNS + 'path')}
        for geometry in ('M165 616 V466', 'M760 616 V554', 'M1030 616 V554'):
            self.assertIn(geometry, paths)
            self.assertEqual(paths[geometry].get('class'), 'arb')
        self.assertNotIn('M165 464 V614', paths)
        self.assertIn('blue arrows point from profiles',
                      root.find(SVGNS + 'desc').text)

    def test_no_unverified_real_profile_claim(self):
        architecture = (USER / "assets/revmeta-artifacts.svg").read_text(encoding="utf-8")
        self.assertIn("691 typed Codebook items", architecture)
        self.assertIn("outside this build", architecture)
        for name in SVGS[1:]:
            text = (USER / "assets" / name).read_text(encoding="utf-8")
            self.assertIn("RevMeta", text)
            self.assertNotIn("✓ umbrella review design", text)
            self.assertTrue("not verified" in text.lower() or "hypothetical" in text.lower())


if __name__ == "__main__":
    unittest.main()
