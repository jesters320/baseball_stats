from . import stats_constants

class Pitcher:

	def __init__(self, id):
		self.id = id
		self.pitch_count = 0
		self.strike_count = 0
		self.ball_count = 0
		self.faced_batters_count = 0
	
	def get_pitch_count(pitch_call):
		normalize_pitch_sequence = pitch_call.translate(str.maketrans('','',stats_constants.non_pitch_symbols))
		
		count_of_pitches = len(normalize_pitch_sequence)
		
		
		balls = normalize_pitch_sequence.translate(str.maketrans('','', stats_constants.strike_symbols))
		count_of_balls = len(balls)
		
		pitches = {"count_of_pitches": count_of_pitches, "count_of_balls": count_of_balls, "count_of_strikes": count_of_pitches-count_of_balls}
		return pitches