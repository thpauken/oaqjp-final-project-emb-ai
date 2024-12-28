from emotion_detection import emotion_detector
import unittest
#importing the function and the unittest library

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        #test case for joy
        joy_result = emotion_detector("I am glad this happened")
        self.assertEqual(joy_result['dominant_emotion'], 'joy')
    def test_anger(self):    
        #test case for anger
        anger_result = emotion_detector("I am really mad about this.")
        self.assertEqual(anger_result['dominant_emotion'], 'anger')
    def test_disgust(self):    
        #test case for disgust
        disgust_result = emotion_detector("I feel disgusted just hearing about this.")
        self.assertEqual(disgust_result['dominant_emotion'], 'disgust')
    def test_sadness(self):    
        #test case for sadness
        sadness_result = emotion_detector("I am so sad about this.")
        self.assertEqual(sadness_result['dominant_emotion'], 'sadness')
    def test_fear(self):    
        #test case for fear
        fear_result = emotion_detector("I am really afraid that this will happen.")
        self.assertEqual(fear_result['dominant_emotion'], 'fear')

unittest.main()