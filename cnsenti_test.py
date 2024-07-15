import cnsenti
from cnsenti import Sentiment
from cnsenti import Emotion


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m' # 青色
BLACK = '\033[30m'
END_COLOR = '\033[0m'




senti = Sentiment()

test_text= '今天我吃了两个包子'
test_text0 = "我是姚正明的爸爸，我几天有一点难受，因为我的儿子爆炸了，他永远的离开了他亲爱的父亲，我实在是太难过了，呜呜呜。"
test_text1 = "我今天太开心了，哈哈哈。"
test_text2 = "我今天好难过啊，呜呜呜。"
test_text3 = "我真的好喜欢你！"
test_text4 = "我十分惊讶"
test_text5 = "我现在怒火中烧!"
test_text6 = "吓死我了，我好害怕"
test_text7 = "你真讨厌，快滚啊"

#result = senti.sentiment_count(test_text1)
#print(result)


emotion = Emotion()

#result = emotion.emotion_count(test_text1)
#print(result)


# define emotional density

def senti_density (text : str):
    emotion_result = senti.sentiment_count(text)
    emotion_density_positive = emotion_result['pos'] /  emotion_result['words']
    emotion_density_negative = emotion_result['neg'] /  emotion_result['words']
    
    if emotion_density_positive == 0 and emotion_density_negative > 0.1:
        print("This is a sentence full of negative emotions.")
    elif emotion_density_positive > 0.1 and emotion_density_negative == 0:
        print("This is a sentence full of positive emotions.")
        
        
    return emotion_density_positive, emotion_density_negative

#senti_density(test_text2)

def emo_density (text : str):
    emotion_result = emotion.emotion_count(text)
    e1 = emotion_result['好']
    e2 = emotion_result['乐']
    e3 = emotion_result['哀']
    e4 = emotion_result['怒']
    e5 = emotion_result['惧']
    e6 = emotion_result['恶']
    e7 = emotion_result['惊']
    
    #print(e1, e2, e3, e4, e5, e6, e7)
    
    if e1 >= 1 and e2 == e3 == e4 == e5 == e6 == e7 == 0:
        return RED + text + " b(￣▽￣)d" + END_COLOR
    elif e2 >= 1 and e1 == e3 == e4 == e5 == e6 == e7 == 0:
        return PURPLE + text + " φ(゜▽゜*)♪" + END_COLOR
    elif e3 >= 1 and e1 == e2 == e4 == e5 == e6 == e7 == 0:
        return BLUE + text + " (T_T)" + END_COLOR
    elif e4 >= 1 and e1 == e2 == e3 == e5 == e6 == e7 == 0:
        return YELLOW + text + " ┗|`O'|┛" + END_COLOR
    elif e5 >= 1 and e1 == e2 == e3 == e4 == e6 == e7 == 0:
        return CYAN + text + " ( >__<。)" + END_COLOR
    elif e6 >= 1 and e1 == e2 == e3 == e4 == e5 == e7 == 0:
        return BLACK + text + " (;ﾟ;艸;ﾟ;)" + END_COLOR
    elif e7 >= 1 and e1 == e2 == e3 == e4 == e5 == e6 == 0:
        return GREEN + text + " ∑( '口' ||" + END_COLOR
    else:
        return text
    
# print(emo_density(test_text1))
# print(emo_density(test_text2))
# print(emo_density(test_text3))
# print(emo_density(test_text4))
# print(emo_density(test_text5))
# print(emo_density(test_text6))
# print(emo_density(test_text7))

print(emo_density(test_text))
