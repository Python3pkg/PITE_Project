import unittest
from sf2r_lib import ff_parser_factory, ff_parser_1d, ff_parser_2d, plot_1d, plot_2d


class ff_parser_factoryTest(unittest.TestCase):

	def setUp(self):
	
		self.instance1 =  ff_parser_1d({ "foo1": "incorrect_type" })
		self.instance2 =  ff_parser_2d({ "foo2": "2DPLOT" })
		
	def test_parser_creator_invalid_plot_type(self):
	
		parsers1 = self.instance1.ff_parser_creator()
		self.assertEqual(parsers1, [])
		
	def test_parser_creator_file_unchanged(self):
	
		file_str_before, file_str_after = "", ""
	
		with open('foo2') as fp:
			for line in iter(fp.readline, ''):
				file_str_before += line
				
		parsers2 = self.instance1.ff_parser_creator()
		
		with open('foo2') as fp:
			for line in iter(fp.readline, ''):
				file_str_after += line
				
		self.assertEqual(file_str_before, file_str_after)
		
	def test_parser_creator_returns_valid_types(self):
	
		parsers3 = self.instance2.ff_parser_creator()
		parsers3_type = type(parsers3)
		self.assertEqual(parsers3_type, list)
		
		if(type(parsers3_type) == list and len(parsers3)):
			self.assertEqual(type(parsers3[0]), type(ff_parser_2d))

	def test_init_type_list_invalid_value_type(self):
	
		self.assertRaises(Exception, ff_parser_factory("string_type"))

class ff_parser_1dTest(unittest.TestCase):

	def setUp(self):

		self.instance =  ff_parser_1d(open('foo1d'), 'foo1d')

class ff_parser_2dTest(unittest.TestCase):

	def setUp(self):

		self.instance =  ff_parser_2d(open('foo2d'), 'foo2d')

class plot_1dTest(unittest.TestCase):

	def setUp(self):

		self.instance = plot_1d(ff_parser_1d(open('foo1d'), 'foo1d'))
	
	def test_init_proper_working(self):

		self.assertNotEqual(self.instance.get_histo(), None)
		self.assertIsInstance(self.instance.get_histo(), TH1F)
		self.assertEqual(self.instance.get_type(), '1DPLOT')

	def test_set_methods_work_properly(self):

		some_hdata = self.instance.get_parser().get_histogram_data()
		self.instance.set_histo_data(some_hdata)
		
		self.assertTrue(hasattr(self.instance, '__hdata'))

class plot_2dTest(unittest.TestCase):				

		def setUp(self):

			self.instance = plot_2d(ff_parser_2d(open('foo2d'), 'foo2d'))

		def test_init_proper_working(self):

			assertNotEqual(self.instance.get_histo(), None)
			assertIsInstance(self.instance.get_histo(), TH2F)
			assertEqual(self.instance.get_type(), '2DPLOT')
