from random import choice
sentences_one = [
    'In 1987, Ren Zhengfei, a former engineer in the People\'s Liberation Army, started Huawei.',
    'A former engineer in the People\'s Liberation Army named Ren Zhengfei started Huawei in 1987.',
    'Former People\'s Liberation Army engineer Ren Zhengfei created Huawei in 1987.',
    'Huawei was founded by a former engineer in the People\'s Liberation Army Ren Zhengfei in 1987.',
]

sentence_two = [
    'It is the largest telecommunications equipment manufacturer in the world.',
    'It is the biggest producer of telecom equipment on the planet.',
    'It is the biggest producer of communications gear around the globe.',
    'The biggest producer of telecom equipment is this company over the globe.',
]

sentence_three = [
    'Technology company Huawei Ltd. is a global Chinese networking,telecommunications equipment and services company',
    'Huawei Technologies Co. Ltd. is a Chinese multinational networking,telecommunications equipment and services company',
    'China\'s Huawei Technologies Co Chinese transnational networking company Ltd.telecoms gear and service provider',
    'Beijing Huawei Technologies Co. a Chinese multinational networking,equipment and service provider for telecommunications',
]

# Random selection from sentences
# concatination of all sentences
# add html p tag

def paragraph_formation(s1,s2, s3):
    """
    This function will create random paragraph
    :param s1,s2, s3: List of sentences
    :return: A Pargraph
    """
    paragraph = choice(s1)+ choice(s2)+choice(s3)
    return f'<p>{paragraph}</p>'

print(paragraph_formation(sentences_one, sentence_two, sentence_three))
print(paragraph_formation(sentences_one, sentence_two, sentence_three))
print(paragraph_formation(sentences_one, sentence_two, sentence_three))


