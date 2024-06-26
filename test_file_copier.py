import unittest
import os
import tempfile
from file_copier import is_text_file, process_directory

class TestFileCopier(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.output_file = os.path.join(self.temp_dir, "output.txt")

        # Create some test files and directories
        os.makedirs(os.path.join(self.temp_dir, "test_folder"))
        os.makedirs(os.path.join(self.temp_dir, "ignore_folder"))

        with open(os.path.join(self.temp_dir, "file1.txt"), "w") as f:
            f.write("This is file 1")
        with open(os.path.join(self.temp_dir, "file2.txt"), "w") as f:
            f.write("This is file 2")
        with open(os.path.join(self.temp_dir, "test_folder", "file3.txt"), "w") as f:
            f.write("This is file 3")
        with open(os.path.join(self.temp_dir, "ignore_folder", "file4.txt"), "w") as f:
            f.write("This is file 4")
        with open(os.path.join(self.temp_dir, "binary_file.bin"), "wb") as f:
            f.write(b"\x00\x01\x02\x03")

    def tearDown(self):
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)

    def test_is_text_file(self):
        self.assertTrue(is_text_file(os.path.join(self.temp_dir, "file1.txt")))
        self.assertFalse(is_text_file(os.path.join(self.temp_dir, "binary_file.bin")))

    def test_process_directory(self):
        process_directory(self.temp_dir, self.output_file, ignore_folders=["ignore_folder"])

        with open(self.output_file, "r") as f:
            content = f.read()

        self.assertIn("This is file 1", content)
        self.assertIn("This is file 2", content)
        self.assertIn("This is file 3", content)
        self.assertNotIn("This is file 4", content)
        self.assertNotIn("binary_file.bin", content)

if __name__ == "__main__":
    unittest.main()