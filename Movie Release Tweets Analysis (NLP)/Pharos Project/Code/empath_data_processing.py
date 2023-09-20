# Modules import
from locale import normalize
import pandas as pd
import string
from empath import Empath

# Categories for the empath module
categories=[
    'help', 'dance', 'money', 'wedding', 'domestic_work', 'sleep',
    'medical_emergency', 'cold', 'hate', 'cheerfulness', 'aggression', 'occupation',
    'envy', 'anticipation', 'family', 'vacation', 'crime', 'attractive', 'masculine',
    'feminine', 'battles', 'prison', 'health', 'dispute', 'horror', 'leisure',
    'royalty', 'wealthy', 'tourism', 'school', 'magic', 'beach', 'morning',
    'social_media', 'exercise', 'night', 'kill', 'art', 'play', 'computer',
    'college', 'optimism', 'stealing', 'home', 'fear', 'superhero', 'driving',
    'pet', 'childish', 'cooking', 'hipster', 'internet', 'surprise', 'reading',
    'movement', 'body', 'noise', 'eating', 'medieval', 'water', 'sports', 'death',
    'healing', 'legend', 'heroic', 'celebration', 'restaurant', 'violence',
    'military', 'swimming', 'new', 'love', 'old', 'air_travel', 'fight',
    'dominant_personality', 'music', 'vehicle', 'polite', 'toy', 'farming',
    'war', 'speaking', 'listen', 'urban', 'shopping', 'disgust', 'fire', 'tool',
    'phone', 'sound', 'injury', 'sailing', 'rage', 'science', 'work', 'appearance',
    'valuable', 'warmth', 'youth', 'sadness', 'fun', 'emotional', 'joy',
    'affection', 'traveling', 'fashion', 'ugliness', 'anger', 'ship', 'clothing',
    'car', 'strength', 'technology', 'animal', 'party', 'smell', 'plant', 'beauty',
    'negative_emotion', 'cleaning', 'messaging', 'competing', 'friends',
    'achievement', 'liquid', 'weapon', 'children', 'ocean', 'giving', 'contentment',
    'writing', 'rural', 'positive_emotion', 'musical', 'excite', 'song', 'sharing',
    'battles', 'magic', 'alien', 'creature', 'duty','responsibility', 'boys', 
    'girls', 'young', 'monsters', 'games'
    ]

# A function to categorise descriptions to empath topics
def topics_to_empath(tps):
    lexicon = Empath()
    return lexicon.analyze(tps, normalize = True)

# A function to filter the needed empath themes
def empath_to_tags(emp):
    lst = [k for k, v in emp.items() if v != 0]
    return lst

# A function to strip punctuations
def strip(st):
    st = str(st)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    new_s = st.translate(table)
    return new_s