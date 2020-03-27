from pydub import AudioSegment
import wave
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
import librosa
from sklearn import svm
import os
"""
编辑音乐
"""
def clip_music(filename,savename,star,end):
    """
    裁剪wav音乐
    :param filename:目标音乐路径
    :param savename:存储
    :param star:开始时间 以秒为单位
    :param end:结束时间
    :return: None
    """
    try:
        music = wavfile.read(filename)
        wavfile.write(savename,44100,music[1][star*44100:end*44100])
    except Exception as msg:
        print(msg)


def clip_lrc(filename,star,end):
    """
    裁剪歌词
    :param filename: 歌词文件
    :param star: 开始时间
    :param end: 结束时间
    :return: 时间片段
    """
    with open(filename, "r",encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
    # 用来储存[时间：歌词]键值对的字典
    Dict = {}
    # strip函数去除str两边空格，splitlines函数将字符串str按行进行分割
    myList = data.strip().splitlines()
    for line in myList:
        # 每一行用 ] 分割
        lineList = line.split(']')
        if lineList[-1] == '':
            continue
        # 遍历歌词前的时间信息
        tt = lineList[0]

        if tt[1] > '9' or tt[1] < '0':# 不是时间轴部分
            continue
        else:
            # 将时间信息去除'['，并以':'进行分割
            TimeList = tt.strip('[').split(':')
            # 将分割后的时间列表整合成浮点数时间
            Time = float(TimeList[0]) * 60 + float(TimeList[1])
            Time = round(Time,3)
            # 将时间对应的歌词存入字典中
            Dict[Time] = lineList[-1]
    cliplrcs =[]
    for key in Dict:
        if key <= end and key >= star:
            cliplrcs.append(Dict[key])
        print(key,Dict[key])
    return cliplrcs

if __name__ == '__main__':
    # clip_music("wavfile/antique_music/0.wav","clip.wav",60,120)
    lrc = clip_lrc("lrcfile/1354477202.txt",30,60)
    print(lrc)