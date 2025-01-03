'''Unit testing for emotion_detection.py
'''
import unittest
from emotiondetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    '''unit test class'''
    def test_emotion_detector(self):
        '''unit test for all five class labels'''

        #test joy
        res1 = emotion_detector("I am glad this happened")
        self.assertEqual(res1["dominant_emotion"],"joy")
        #test anger
        res2 = emotion_detector("I am really mad about this")
        self.assertEqual(res2["dominant_emotion"],"anger")
        #test disgust
        res3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res3["dominant_emotion"],"disgust")
        #test sadness
        res4 = emotion_detector("I am so sad about this")
        self.assertEqual(res4["dominant_emotion"],"sadness")
        #test fear
        res5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res5["dominant_emotion"],"fear")

unittest.main()
