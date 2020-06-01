import unittest
from Rename_By_Type_UI import get_suffix


class TestGetSuffixType(unittest.TestCase):

    def test_typeMesh(self):
        type_obj = "mesh"
        self.assertEqual(get_suffix(type_obj), "geo")

    def test_typeJoint(self):
        type_obj = "joint"
        self.assertEqual(get_suffix(type_obj), "jnt")

    def test_typeNurbsCurve(self):
        type_obj = "nurbsCurve"
        self.assertEqual(get_suffix(type_obj), "crv")

    def test_typeNurbSurface(self):
        type_obj = "nurbsSurface"
        self.assertEqual(get_suffix(type_obj), "surf")

    def test_typeDirLight(self):
        type_obj = "directionalLight"
        self.assertEqual(get_suffix(type_obj), "lgt")

    def test_typeAmbLight(self):
        type_obj = "ambientLight"
        self.assertEqual(get_suffix(type_obj), "lgt")

    def test_typePointLight(self):
        type_obj = "pointLight"
        self.assertEqual(get_suffix(type_obj), "lgt")

    def test_typeSpotLight(self):
        type_obj = "spotLight"
        self.assertEqual(get_suffix(type_obj), "lgt")

    def test_typeAreaLight(self):
        type_obj = "areaLight"
        self.assertEqual(get_suffix(type_obj), "lgt")

    def test_typeCamera(self):
        type_obj = "camera"
        self.assertEqual(get_suffix(type_obj), "camera")

    def test_typeOther(self):
        type_obj = "other"
        self.assertEqual(get_suffix(type_obj), "grp")


if __name__ == '__main__':
    unittest.main()
