import streamlit as st

# -- タイプごとの簡単な説明 --
explanations = {
    'ISTJ': 'ロジスティシャンは現実的かつファクト重視の気質があり、とても頼りがいがあります。',
    'ESTJ': '幹部は“まとめ役”として非常に優れていて、人やものごとを管理するのが飛び抜けて上手です。',
    'ISFJ': '擁護者は“周りの人を守る”タイプとして非常に献身的かつ友好的で、いつでも喜んで愛する人を擁護します。',
    'ESFJ': '領事は面倒見が良く、社交的です。いつでも喜んで周りの人をサポートする人たちで、コミュニティを大切にします。',
    'ISTP': '巨匠は独創的かつ現実的です。新しいことを試すのが大好きで、どんなツールでも使いこなせます。',
    'ESTP': '起業家はエネルギッシュな上に抜け目がなく、洞察力の鋭い人たちです。危険と隣り合わせの生き方を心から楽しみます。',
    'ISFP': '冒険家はいつも新しいことを体験したり探ってみたりするのが好きな人たちです。柔軟な考えの持ち主で、魅力的でもあります。',
    'ESFP': 'エンターテイナーは熱意にあふれた精力的な人たちで、無計画に行動するのを好みます。エンターテイナーの周りにいて、退屈することは決してないでしょう。',
    'INFJ': '提唱者は静かなビジョナリーです。理想主義者として周りの人をインスパイアしながら精力的に働くことが多いでしょう。',
    'ENFJ': '主人公は楽観主義者として周囲をインスパイアし、自分が正しいと思うことをすぐさま実行します。',
    'INFP': '仲介者は自分の利益を顧みず、大義のためにはいつでも手を差し伸べる優しい人たちです。詩的でもあります。',
    'ENFP': '運動家は熱意にあふれる性分の持ち主で、クリエイティブかつ自由奔放で、社交的です。“笑顔になる理由”をいつでも見つけられます。',
    'INTJ': '建築家は独創的・戦略的にものごとを考える上に、どんなことについても計画がある人たちです。',
    'ENTJ': '指揮官は大胆で意思が強い上に、想像力豊かで、どんな時でも解決手段を見つけたり作り出したりできます。',
    'INTP': '論理学者は創造力に富む発明家で、無限の知識欲があります。',
    'ENTP': '討論者は好奇心旺盛で、柔軟にものごとを考える上に、知的な難題が大好きです。'
}


st.title('MBTI診断アプリ')

st.caption('4つの質問に答えるだけで、MBTIを診断できます')

q1 = st.radio('あなたはどちらですか？', ('外向的 (E)', '内向的 (I)'))

q2 = st.radio('情報をどのように得ることが多いですか？', ('感覚型 (S)', '直感型 (N)'))

q3 = st.radio('意思決定はどのように行いますか？', ('思考型 (T)', '感情型 (F)'))

q4 = st.radio('生活の進め方は？', ('判断型 (J)', '柔軟型 (P)'))


if st.button('診断する'):
    mbti = q1[5] + q2[5] + q3[5] + q4[5]
    st.write(f"あなたのMBTIタイプは {mbti} です！")
    

    
    
    if mbti in explanations:
        st.write(explanations[mbti])
    else:
        st.write('このタイプの説明はまだありません。')

