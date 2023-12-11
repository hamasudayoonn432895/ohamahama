import streamlit as st

# 関数定義
def repeating_point(credits, promotion_value, diligent_value):
    total = credits + promotion_value + diligent_value
    return total

#タイトル画面
st.title('大学留年チェッカー')
st.subheader('留年するかどうかを知りたくはないか？')
st.write('お早う御座います。こんちわ。アンケートに答えて頂きますれば、小生の独断と偏見をもって貴方が留年をする確率を決めつけさせて頂きます。正確な精度を求められましても困っちゃうので気にしないでください。')

# 名前入力欄
name = st.text_input('お名前を教えてください')
if name:
    # 大学一年生前期習得単位数の取得
    credits = st.slider("大学一年生前期習得単位数をザックリとどうぞ", 0, 40)
    credits_value = int(credits)

    # スライダーの回答によって異なる整数に変換
    if credits_value < 1:
        credits_value = 10
    elif 1 < credits_value <= 10:
        credits_value = 8
    elif 10 < credits_value <= 15:
        credits_value = 6
    elif 15 < credits_value <= 20:
        credits_value = 4
    elif 20 < credits_value <= 24:
        credits_value = 0
    else:
        credits_value = -4

    # 進級要件の取得
    promotion_option = ('はい', '違う', '無いと思いたいです')
    promotion = st.selectbox("貴殿の大学に進級要件はあったと思います", promotion_option, index=promotion_option.index('はい') if 'はい' in promotion_option else 0)
    promotion_mapping = {'はい': 5, '違う': 0, '無いと思いたいです': 10}
    promotion_value = promotion_mapping.get(promotion, 0)

    # 真面目の取得
    diligent_option = ('うん', '真面目だよ', '真面目ってそもそも何なんだろう')
    diligent = st.selectbox("真面目ではないですよね???", diligent_option, index=diligent_option.index('うん') if 'うん' in diligent_option else 0)
    diligent_mapping = {'うん': 5, '真面目だよ': 10, '真面目ってそもそも何なんだろう': 0}
    diligent_value = diligent_mapping.get(diligent, 0)

    #留年する意思
    intention_option = ('はい',  '確実にします','しません')
    intention = st.selectbox("留年する意志はありますか？", intention_option, index=intention_option.index('はい') if 'はい' in intention_option else 0)
    intention_mapping = {'はい':100 , '確実にします': 100, 'しません':0}
    intention_value = intention_mapping.get(intention, 0)

    # 点数化
    total_value = credits_value + promotion_value + diligent_value + intention_value

    # 結果の表示
    if st.button("結果を表示"):
        # 条件分岐によって異なる結果を表示
        if total_value > 100:
            st.write(f"{name}さんの留年率ですが、私も信じることができません。 {total_value} 点です。貴方は留年します。")
        elif 20 <= total_value <= 30:
            st.write(f"{name}さんの留年率は {total_value} 点ですね。キツそうです。御覚悟を。")
        else:
            st.write(f"{name}さんの留年率は {total_value} 点。安心してください。留年の心配はありません。趣味や自分のやりたいことを全力でどうぞ。") 