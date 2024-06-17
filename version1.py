import streamlit as st
import streamlit.components.v1 as components

def main():
    st.markdown("""
                <style>
                .stButton>button {
                    background-color: #BEB8DC;
                    border: none;
                    color: white;
                    padding: 20px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 100px !important;
                    margin: 0px;
                    cursor: pointer;
                    border-radius: 5px;
                    width: 110%;
                }
                .stButton>button:hover {
                    background-color: #E7EFFA;
                    color: black;
                }
                .stButton>button:active {
                    background-color: #E7EFFA; 
                    color: black; 
                }
                .stButton>button:focus {
                    color: black; 
                }
                .stButton>button:visited {
                    color: black; 
                }
                
                </style>
                """, unsafe_allow_html=True)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("首页", key="home"):
            navigateTo("home")
    with col2:
        if st.button("介绍", key="introduction"):
            navigateTo("introduction")
    with col3:
        if st.button("现状", key="current"):
            navigateTo("current")
    with col4:
        if st.button("趋势", key="trends"):
            navigateTo("trends")
    with col5:
        if st.button("预测", key="forecast"):
            navigateTo("forecast")

    selected_page = get_page_from_url()

    if selected_page == "home":
        homepage()
    elif selected_page == "introduction":
        display_introduction()
    elif selected_page == "current":
        display_current_status()
    elif selected_page == "trends":
        display_trends()
    elif selected_page == "forecast":
        display_forecast()
    else:
        homepage()

def navigateTo(page):
    url = st.experimental_get_query_params()
    url["page"] = page
    st.experimental_set_query_params(**url)

def get_page_from_url():
    query_params = st.experimental_get_query_params()
    return query_params.get('page', ['home'])[0]


def homepage():
    st.title("""
            国家老年糖尿病基础数据库

            在这里，你可以查看数据介绍、现状、趋势及预测。
            
            请在左侧栏选择一个板块查看详细内容。
            """)
def display_introduction():
    st.title("数据介绍")
    st.write("""
    在这个板块，我们将提供数据的基本介绍。
    """)

def display_current_status():
    st.title("现状")
    st.write("""
    在这个板块，我们将展示xx的现状。
    """)
    st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/91f77cc8a696e13b78355fd76718210.png?raw=true", caption="现状")

def display_trends():
    st.title("趋势")
    st.write("""
    在这个板块，我们将展示xx的趋势。
    """)
    st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/0791c6a3d25f3519850edabccc2a7be.png?raw=true", caption="趋势")

def display_forecast():
    st.title("预测")
    st.write("""
    在这个板块，我们将展示xx的预测结果。
    """)
    # 选择框：选择指标
    selected_indicator = st.selectbox("请选择指标", ["Prevalence", "ASPR", "DALY", "ASDR"])

    # 选择框：选择模型
    selected_model = st.selectbox("请选择模型", ["ARIMA", "LSTM", "ARIMA-LSTM", "GAMM"])

    if selected_model == "GAMM":
        selected_year = st.slider("请选择年份", 2020, 2040, 2020)
        # 选择框：选择趋势
        selected_sdi_trend = st.selectbox("请选择SDI", ["自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        if selected_sdi_trend == "自然趋势基础上上升":
            sdi_percentage = st.slider("请选择上升百分比", 0, 100, 10)
        elif selected_sdi_trend == "自然趋势基础上下降":
            sdi_percentage = st.slider("请选择下降百分比", 0, 100, 10)

        selected_obese_trend = st.selectbox("请选择肥胖水平", ["自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        if selected_obese_trend == "自然趋势基础上上升":
            obese_percentage = st.slider("请选择上升百分比", 0, 100, 10, key="up_percentage")
        elif selected_obese_trend == "自然趋势基础上下降":
            obese_percentage = st.slider("请选择下降百分比", 0, 100, 10, key="down_percentage")
    else:
        selected_year = st.slider("请选择年份", 2020, 2040, 2020)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("显示结果", key="forecast_button"):
            if selected_model == "GAMM":
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/62f0a24779a67cb4bc1bb214dbf75e5.png?raw=true", caption="预测结果")
            else:
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/19b4c524216920ee9a9a1ac620a6b5c.png?raw=true", caption="预测结果")


if __name__ == "__main__":
    main()
