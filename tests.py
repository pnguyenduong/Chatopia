from tkinter import *
import customtkinter
import unittest

class TestTkinter(unittest.TestCase):
    def setUp(self):
        self.app = customtkinter.CTk()
        self.title = Label(self.app, text="Hello World")
        self.geometry = '800x600'
        self.title.pack()
 
    def test_title_text(self):
        self.assertEqual(self.title['text'], 'Hello World')
    
    def test_geometry_text(self):
        self.assertEqual(self.geometry, '800x600')
    
    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()