import streamlit as st
import time
from PIL import Image #PILをpip install pillowを実施する
import pandas as pd
import random as np
import numpy as np

st.title('大学単位チェッカー')
st.title('其ノ方の単位数は何単位だ！！！')
st.write('お早う御座います。こんちわ。アンケートに答えて頂きますれば、小生の独断と偏見をもって単位数を決めつけさせて頂きます。')
text=st.text_input('其ノ方のお名前を教えてください')
