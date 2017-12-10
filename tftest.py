#! /bin/python

import tensorflow as tf
import sys


import input_data
import models

FLAGS = None

def main(_):
	
	tf.logging.set_verbosity(tf.logging.INFO)
	sess = tf.InteractiveSession()
	model_settings = models.prepare_model_settings(
		len(input_data.prepare_words_list(FLAGS.wanted_words.split(','))),
		FLAGS.sample_rate,FLAGS.clip_duration_ms,FLAGS.window_size_ms,
		FLAGS.window_stride_ms,FLAGS.dct_coefficient_count)

	audio_processor = input_data.AudioProcessor(
		FLAGS.data_url,FLAGS.data_dir,FLAGS.silence_percentage,
		FLAGS.unknown_percentage,
		FLAGS.wanted_words.split(','),FLAGS.validation_percentage,
		FLAGS.testing_percentage,model_settings)	
	print FLAGS.data_url
	print FLAGS.data_dir
	print model_settings
import argparse

if __name__ == '__main__':
	parser =  argparse.ArgumentParser()
	parser.add_argument(
		'--data_url',
		type=str,
		default='http://www.baidu.com',
		help= """ \
		where  to download the speeech traing data to.
		""")

	parser.add_argument(
		'--data_dir',
		type=str,
		default='/tmp/speech_dataset/',
		help=""""
		path to your data train or test.
		""")
	parser.add_argument(
		'--wanted_words',
		type=str,
		default='yes,no,up,down,left,right,on,off,stop,go',
		help="words to use ,like yes no up down left right on off,stop).")
	parser.add_argument(
		'--sample_rate',
		type=int,
		default=16000,
		help='expected sample rate')
	parser.add_argument(
		'--clip_duration_ms',
		type =  int,
		default=1000,
		help = "expected duration")
	parser.add_argument(
		'--window_size_ms',
		type = float,
		default=30.0,
		help = "how long each spectrogram timeslice is,")
	parser.add_argument(
		'--window_stride_ms',
		type=float,
		default = 10.0,
		help = "how long each spectrogram timeslice is,")
	parser.add_argument(
		'--dct_coefficient_count',
		type = int,
		default=40,
		help="how many bins to be use for the MFCC fingerprint")
	parser.add_argument(
		'--silence_percentage',
		type=float,
		default=10.0,
		help=""" 
		how much of the training data should be unknown words.
		""")	
	parser.add_argument(
		'--testing_percentage',
		type=float,
		default=10.0,
		help="""
		what percentage of wavs to use as a test set.
		""")
	parser.add_argument(
		'--unknown_percentage',
		type=float,
		default=10.0,
		help = """\
		How much of the training data should be unknown words.
		""")
	parser.add_argument(
		'--validation_percentage',
		type=int,
		default=10,help='what percentage of wvs to use as a validation set.')
	FLAGS,unparsed =  parser.parse_known_args()
	tf.app.run(main=main,argv=[sys.argv[0]]+unparsed)
