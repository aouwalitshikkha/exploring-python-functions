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

# Random selection of sentences from every list
# Concatination of selected sentences
# add p tag
#  return output with p tag

def generate_paragraph(*args):
    paragraph = ''
    for sentence in args:
        from random import choice
        paragraph += choice(sentence)
    return f'<p>{paragraph}</p>'

print(generate_paragraph(sentences_one, sentence_two, sentence_three))