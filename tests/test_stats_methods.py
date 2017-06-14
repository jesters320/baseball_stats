import unittest
from baseball_stats.stats_methods import set_new_game_item, set_info_item, set_current_pitcher, set_batting_info, set_at_bat
from baseball_stats.pitcher import Pitcher

class TestStatsMethods(unittest.TestCase):
	def test_set_new_game_item(self):
		self.assertEqual( 1, 1)

	def test_set_info_item(self):
		info = "info,daynight,day"
		info_details = info.split(',')
		dict_info = {}
		set_info_item(dict_info, info_details)
		self.assertEqual(dict_info, {"daynight": "day"})

	def test_set_current_pitcher_starter(self):
		starter = 'start,nolaa001,"Aaron Nola",1,9,1'
		starter_details = starter.split(',')
		current_pitcher = ""
		current_pitcher = set_current_pitcher(starter_details)
		self.assertEqual(current_pitcher.id, Pitcher("nolaa001").id)
	
	def test_set_current_pitcher_sub(self):
		sub = 'sub,handb001,"Brad Hand",0,9,1'
		sub_details = sub.split(',')
		current_pitcher = "nolaa001"
		current_pitcher = set_current_pitcher(sub_details)
		self.assertEqual(current_pitcher.id, Pitcher("handb001").id)

	def test_set_current_pitcher_not_a_pitcher(self):
		not_a_pitcher = 'start,galvf001,"Freddy Galvis",1,1,6'
		not_a_pitcher_details = not_a_pitcher.split(',')
		response = set_current_pitcher(not_a_pitcher_details)
		self.assertEqual(response, None)
		
	def test_set_batting_info(self):
		pass
		
	def test_set_at_bat(self):
		pass

if __name__ == '__main__':
    unittest.main()