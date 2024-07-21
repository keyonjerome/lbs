# pylint: disable=unused-import, no-self-use, import-outside-toplevel
import unittest


class TestPackaging(unittest.TestCase):
    """
    Setup.py correctly packages the project
    """

    def test_can_import_src(self) -> None:
        """
        Allows content of 'src'-folder to be imported
        """

        import src


if __name__ == "__main__":
    unittest.main()
