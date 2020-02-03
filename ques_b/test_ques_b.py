import unittest
from ques_b import cmp_verson


class TestQuesB(unittest.TestCase):

    def test_major_versions(self):
        v1, v2 = "1.0", "2.0"
        self.assertEqual(cmp_verson(v1, v2), -1)

    def test_minor_versions(self):
        v1, v2 = "1.2", "1.1"
        self.assertEqual(cmp_verson(v1, v2), 1)

    def test_patch_versions1(self):
        v1, v2 = "1.2.0", "1.2.1"
        self.assertEqual(cmp_verson(v1, v2), -1)

    def test_patch_versions2(self):
        v1, v2 = "1.0.1", "1"
        self.assertEqual(cmp_verson(v1, v2), 1)

    def test_patch_versions3(self):
        v1, v2 = "1.2.0", "1.2.1"
        self.assertEqual(cmp_verson(v1, v2), -1)

    def test_pre_rel_versions1(self):
        v1, v2 = "1.0.0-alpha", "1.0.0"
        self.assertEqual(cmp_verson(v1, v2), -1)

    def test_pre_rel_versions2(self):
        v1, v2 = "1.0.0-alpha.1", "1.0.0-alpha"
        self.assertEqual(cmp_verson(v1, v2), 1)

    def test_pre_rel_versions3(self):
        v1, v2 = "1.0.0-alpha", "1.0.0-alpha.beta"
        self.assertEqual(cmp_verson(v1, v2), -1)

    def test_pre_rel_versions4(self):
        v1, v2 = "1.0.0-beta.11", "1.0.0-beta.2"
        self.assertEqual(cmp_verson(v1, v2), 1)

    def test_pre_rel_versions5(self):
        v1, v2 = "1.0.0-rc.1", "1.0.0"
        self.assertEqual(cmp_verson(v1, v2), -1)

    def test_pre_rel_versions6(self):
        # v1, v2 = "1.0.0-rc.1", "1.0.0"
        v1, v2 = "1.0.0-rc", "1.0.0-alpha"
        self.assertEqual(cmp_verson(v1, v2), 1)


if __name__ == '__main__':
    unittest.main()
