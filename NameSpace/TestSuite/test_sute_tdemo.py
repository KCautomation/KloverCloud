import unittest

from NameSpace.CreateNamespaceWithAccessGroupCompany.NamespaceWithCompany import NamespaceCreationOnCompany
from NameSpace.NamespaceWithOrganization.NamespaceOrganization import NamespaceCreationOrganization
from NameSpace.CreateNameSpaceWithTeam.NamespaceWithTeam import NamespaceCreationTeam


class MyTestCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite
        # Get all tests from TestClass1 and TestClass2
        tc1 = unittest.TestLoader().loadTestsFromTestCase(NamespaceCreationOnCompany)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(NamespaceCreationOrganization)
        tc3 = unittest.TestLoader().loadTestsFromTestCase(NamespaceCreationTeam)

        # Create a test suite combining TestClass1 and TestClass
        smokeTest = unittest.TestSuite([tc1, tc2, tc3])
        unittest.TextTestRunner(verbosity=2).run(smokeTest)
        return suite


if __name__ == '__main__':
    unittest.main()
