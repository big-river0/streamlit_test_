import streamlit as st

st.title('st.form')

# 'with' 표기법을 사용한 전체 예시
st.header('1. 음식 주문')

with st.form('my_form'):
    st.subheader('**음식 주문하기**')

    # 입력 위젯
    coffee_bean_val = st.selectbox('메인 메뉴', ['돈까스', '제육','파스타','카레돈까스','쫄면','치즈돈까스'])
    coffee_roast_val = st.selectbox('서브 메뉴', ['샐러드', '치킨 샐러드'])
    brewing_val = st.selectbox('음료', ['콜라', '사이다', '레몬에이드', '복숭아 아이스티'])
    serving_type_val = st.selectbox('추가 주문', ['밥 추가', '미니 쫄면', '미니 샐러드'])

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        ☕ 주문하신 내용:
        - 메인 메뉴: `{coffee_bean_val}`
        - 서브 메뉴: `{coffee_roast_val}`
        - 음료: `{brewing_val}`
        - 추가 주문: `{serving_type_val}`
        ''')
else:
    st.write('☝️ 주문하세요!')


# 객체 표기법을 사용한 짧은 예시
st.header('2. 객체 표기법 예시')

form = st.form('my_form_2')
selected_val = form.slider('값 선택')
form.form_submit_button('제출') #모든 양식은 st.form_submit_button을 포함해야 함.
#st.button과 st.download_button은 양식에 추가할 수 없습니다.
st.write('선택된 값: ', selected_val)
