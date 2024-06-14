import streamlit as st

def main():

    # 创建导航菜单
    selected_page = st.sidebar.radio("选择一个板块", ("首页", "介绍", "现状", "趋势", "预测"))

    # 根据所选板块显示不同内容
    if selected_page == "首页":
        homepage()
    elif selected_page == "介绍":
        display_introduction()
    elif selected_page == "现状":
        display_current_status()
    elif selected_page == "趋势":
        display_trends()
    elif selected_page == "预测":
        display_forecast()

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
    st.image("https://i.imgur.com/QzFtzn9.png", caption="现状")

def display_trends():
    st.title("趋势")
    st.write("""
    在这个板块，我们将展示xx的趋势。
    """)
    st.image("https://i.imgur.com/ZYHGqL5.png", caption="趋势")

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

    # 按钮：显示结果
    if st.button("显示结果"):
        if selected_model == "GAMM":
            st.image("https://i.imgur.com/1Y6T4xn.png", caption="预测结果")
        else:
            st.image("https://i.imgur.com/wg4Lz9K.png", caption="预测结果")

if __name__ == "__main__":
    main() 
