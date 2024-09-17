import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestMyFunction(unittest.TestCase):
    def test_1(self):
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_2(self):
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_3(self):
        result = emotion_detector('I feel disgusted just hearing about this	')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_4(self):
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_5(self):
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

unittest.main()
