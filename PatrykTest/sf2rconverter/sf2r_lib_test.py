import unittest
from sf2r_lib import ff_parser_factory, ff_parser_1d, ff_parser_2d


class ff_parser_factoryTest(unittest.TestCase):

	def setUp(self):
	
		self.instance1 =  ff_parser_1d({ "example1.dat": "incorrect_type" })
		self.instance2 =  ff_parser_2d({ "example2.dat": "2DPLOT" })
	
	def test_init_type_list_invalid_value_type(self):
	
		assertRaises(Exception, ff_parser_factory("string_type"))
		
	def test_parser_creator_invalid_plot_type(self):
	
		parsers1 = self.instance1.ff_parser_creator()
		self.assertEqual(parsers1, [])
		
	def test_parser_creator_file_unchanged(self):
	
		file_str_before, file_str_after = "", ""
	
		with open('example2.dat') as fp:
			for line in iter(fp.readline, ''):
				file_str_before += line
				
		parsers2 = self.instance1.ff_parser_creator()
		
		with open('example2.dat') as fp:
			for line in iter(fp.readline, ''):
				file_str_after += line
				
		assertEqual(file_str_before, file_str_after)
		
	def test_parser_creator_returns_valid_types(self):
	
		parsers3 = self.instance2.ff_parser_creator()
		parsers3_type = type(parsers3)
		self.assertEqual(parsers3_type, list)
		
		if(type(parsers3_type) == list and len(parsers3)):
			self.assertEqual(type(parsers3[0]), type(ff_parser_2d))

class ff_parser_1dTest(unittest.TestCase):

	def setUp(self):
		self.instance =  ff_parser_1d()
	
	def test_init_ff_parser_1d_(self):
		pass