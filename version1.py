import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

def main():
    logo_path = r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1200px-Xiamen_University_logo.svg.png?raw=true"
    st.logo(logo_path, icon_image=logo_path)
    st.sidebar.markdown("""
    厦门大学 \n
    公共卫生学院 \n
    卫生经济政策暨老年健康研究中心"""
                        )
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

    # 根据选择的页面显示相应内容
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
            中国糖尿病疾病负担预测平台
            """)
    st.write("""
            糖尿病作为一种营养代谢性疾病，已成为慢性非传染性疾病的重要组成部分，每年全球因此丧生的病例高达160万[1]。\n
            近年来，随着生活方式的变迁和饮食结构的改变，糖尿病患病率逐年上升，严重危害居民健康，成为当前社会亟待解决的重大公共卫生挑战。预计到2045年，全球将有高达7.83亿人受到糖尿病的困扰[2]。\n
            近30年来，我国糖尿病患病率显著上升，2002年患病率首次超过全球平均水平，并在2002－2016年间始终高于平均全球水平[3]。
            但该病的知晓率及治愈率仍处于低水平[4, 5]。\n
            本平台将采用多种预测模型，探讨不同场景下我国未来糖尿病疾病负担发展趋势。\n
    """)
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 93%;
            background-color: #f1f1f1;
            padding: 10px;
            border-top: 1px solid #dcdcdc;
            font-size: 5px;
            text-align: left;
            box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);
        }
        </style>
        <div class="footer">
        <p>[1] BUDREVICIUTE A, DAMIATI S, SABIR D K, et al. Management and Prevention Strategies for Non-communicable Diseases (NCDs) and Their Risk Factors [J]. Front Public Health, 2020, 8: 574111.</p>
        <p>[2] SUN H, SAEEDI P, KARURANGA S, et al. IDF Diabetes Atlas: Global, regional and country-level diabetes prevalence estimates for 2021 and projections for 2045 [J]. Diabetes Res Clin Pract, 2022, 183: 109119.</p>
        <p>[3] 曹新西, 徐晨婕, 侯亚冰, et al. 1990—2025年我国高发慢性病的流行趋势及预测 [J]. 中国慢性病预防与控制, 2020, 28(01): 14-9.</p>
        <p>[4] SOCIETY C D. 中国2型糖尿病防治指南（2020年版）（上） [J]. 中国实用内科杂志, 2021, 41(08): 668-95.</p>
        <p>[5] ASSOCIATION D B O C M. 中国2型糖尿病防治指南（2020年版）（下） [J]. 中国实用内科杂志, 2021, 41(09): 757-84.</p>
        </div>
        """, unsafe_allow_html=True)
def display_introduction():
    st.title("数据来源基本介绍")
    st.write("""
    以下是用于构建预测模型的数据来源基本介绍
    """)
    # st.markdown("""
    #     <style>
    #     .streamlit-expanderHeader {
    #         font-size: 50px;
    #         font-weight: bold;
    #     }
    #     </style>
    #     """, unsafe_allow_html=True)
    with st.expander("全球疾病负担数据库（Global of Burden Disease，GBD）"):
        st.write("""
        全球疾病负担数据库由美国华盛顿大学健康指标与评估研究所精心打造的，它基于全球众多数据源，运用统一且具备可比性的方法，依据年份、年龄、性别等维度对1990年以来全球204个国家和地区的369种疾病或伤害、87种危险因素的疾病负担数据进行估计和分析。
        """)
    with st.expander("世界卫生组织数据库（the World Health Organization，WHO）"):
        st.write("""
        世界卫生组织数据库汇集了全球卫生领域关键信息和数据的综合资源，涵盖了从健康趋势到疾病负担的广泛指标。
        """)
    with st.expander("世界银行数据库（World Bank Open Data，WBOD）"):
        st.write("""
        世界银行数据库是一个全面、权威的宏观经济数据库，它收录了来自全球各国的统计数据，涵盖了经济、财政、人口、健康、教育等多个方面。
        """)
    with st.expander("非传染性疾病风险因素协作组（NCD Risk Factor Collaboration，NCD-RisC）"):
        st.write("""
        非传染性疾病风险因素协作组致力于及时向全球200个国家和地区提供非传染性疾病（NCD）风险因素方面的数据。\n
        NCD-RisC运用先进的统计方法汇总高质量的基于人群的数据，这些统计方法专门用于分析NCD风险因素。\n
        自1957年以来，NCD-RisC目前已从197个国家收集到超过3300项基于人群的调查数据，有近2亿参与者的风险因素水平已被测量。""")

def display_current_status():
    st.title("基于GBD数据的2021年中国糖尿病疾病负担状况")
    with st.expander("发病情况"):
        st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EGBD%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%98%E5%88%B62021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%8C%89%E5%B9%B4%E9%BE%84%E7%BB%84%E3%80%81%E6%80%A7%E5%88%AB%E5%88%92%E5%88%86%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%8F%91%E7%97%85%E6%83%85%E5%86%B5%EF%BC%88A-%E5%8F%91%E7%97%85%E6%95%B0%EF%BC%8CB-%E5%8F%91%E7%97%85%E7%8E%87%EF%BC%89.png?raw=true",
                 caption="基于GBD数据库绘制2021年中国按年龄组、性别划分的糖尿病发病情况（A-发病数，B-发病率）")
    with st.expander("死亡情况"):
        st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EGBD%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%98%E5%88%B62021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%8C%89%E5%B9%B4%E9%BE%84%E7%BB%84%E3%80%81%E6%80%A7%E5%88%AB%E5%88%92%E5%88%86%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E6%AD%BB%E4%BA%A1%E6%83%85%E5%86%B5%EF%BC%88A-%E6%AD%BB%E4%BA%A1%E6%95%B0%EF%BC%8CB-%E6%AD%BB%E4%BA%A1%E7%8E%87.png?raw=true",
                 caption="基于GBD数据库绘制2021年中国按年龄组、性别划分的糖尿病死亡情况（A-死亡数，B-死亡率）")
    with st.expander("伤残调整寿命年（DALY）情况"):
        st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EGBD%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%98%E5%88%B62021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%8C%89%E5%B9%B4%E9%BE%84%E7%BB%84%E3%80%81%E6%80%A7%E5%88%AB%E5%88%92%E5%88%86%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E4%BC%A4%E6%AE%8B%E8%B0%83%E6%95%B4%E5%AF%BF%E5%91%BD%E5%B9%B4%EF%BC%88Disability%20Adjusted%20Life%20Years,%20DALY%EF%BC%89%E6%83%85%E5%86%B5%EF%BC%88A-%20DALY%E6%95%B0%EF%BC%8CB-%20DALY%E7%8E%87%EF%BC%89.png?raw=true",
                 caption="基于GBD数据库绘制2021年中国按年龄组、性别划分的糖尿病伤残调整寿命年（Disability Adjusted Life Years, DALY）情况（A- DALY数，B- DALY率）")

def display_trends():
    st.title("基于GBD数据1990-2021年中国糖尿病疾病负担的趋势")
    with st.expander("发病趋势"):
        st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1990-2021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84%E5%8F%91%E7%97%85%E4%BE%8B%E6%95%B0%E4%B8%8E%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A0%87%E5%8C%96%E7%8E%87%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true",
                 caption="1990-2021年中国糖尿病的发病例数与相应的标化率变化趋势（ASIR: age-standardized incident rate; ASMR: age-standardized mortality rate; ASDR: age-standardized DALY rate）")
    with st.expander("死亡趋势"):
        st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1990-2021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84%E6%AD%BB%E4%BA%A1%E4%BE%8B%E6%95%B0%E4%B8%8E%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A0%87%E5%8C%96%E7%8E%87%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true",
                 caption="1990-2021年中国糖尿病的死亡例数与相应的标化率变化趋势\n（ASIR: age-standardized incident rate; ASMR: age-standardized mortality rate; ASDR: age-standardized DALY rate）")
    with st.expander("伤残调整寿命年（DALY）趋势"):
        st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1990-2021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84DALY%E6%95%B0%E4%B8%8E%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A0%87%E5%8C%96%E7%8E%87%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true",
                 caption="1990-2021年中国糖尿病的DALY数与相应的标化率变化趋势（ASIR: age-standardized incident rate; ASMR: age-standardized mortality rate; ASDR: age-standardized DALY rate）")

def display_forecast():
    st.title("未来中国糖尿病疾病负担的预测结果")

    # 选择框：选择指标
    selected_indicator = st.selectbox(
                                    "请选择指标",
                                      ["发病率",
                                     "死亡率",
                                     "伤残调整寿命年（Disability Adjusted Life Years, DALY）",
                                     "年龄标化发病率 (age-standardized incident rate, ASIR)",
                                     "年龄标化死亡率(age-standardized mortality rate, ASMR)",
                                     "年龄标化DALY率(age-standardized DALY rate, ASDR)"
                                    ])
    if selected_indicator == "发病率":
        st.write("发病率是指某一人群在一年内新发生糖尿病的频率")
    elif selected_indicator == "死亡率":
        st.write("死亡率是指某人群在一定期间内（通常以年为单位）死于糖尿病的人数在该人群中所占的比例")
    elif selected_indicator == "伤残调整寿命年（Disability Adjusted Life Years, DALY）":
        st.write("衡量从发病到死亡所损失的全部健康寿命年，综合考虑了因早死所致的寿命损失年 (Years of life lost, YLL)和疾病所致伤残引起的健康寿命损失年 (Years lived with disability, YLD)两部分")
    else: pass

    # 选择框：选择模型
    selected_model = st.selectbox("请选择模型", ["ARIMA模型（AutoRegressive Integrated Moving Average Model）",
                                                 "LSTM模型（Long Short Term Memory）",
                                                 "ARIMA-LSTM混合模型",
                                                 "GAMM模型（Generalized Additive Mixed Models, GAMM）"])

    if selected_model == "GAMM模型（Generalized Additive Mixed Models, GAMM）":
        st.write("GAMM是混合效应和相加模型的结合，其中混合模型引入了随机效应反映了不同对象之间的异质性，以及同一对象不同观测之间的相关性。GAMM综合了参数、非参数及随机效应的影响")
        selected_year = st.slider("请选择预测终止年份", 2020, 2040, 2020)

        # 选择超重率
        selected_obese_trend = st.selectbox("请选择成人超重率（BMI ≥ 25kg/m², %）", ["不变","自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E6%88%90%E4%BA%BA%E8%B6%85%E9%87%8D%E7%8E%87%E5%8F%91%E5%B1%95%E8%B6%8B%E5%8A%BF.png?raw=true",
                     caption="成人超重率（BMI ≥ 25kg/m², %）发展趋势")
        if selected_obese_trend == "自然趋势基础上上升":
            obese_percentage = st.slider("请选择上升百分比", 0, 100, 10, key="up_percentage")
        elif selected_obese_trend == "自然趋势基础上下降":
            obese_percentage = st.slider("请选择下降百分比", 0, 100, 10, key="down_percentage")

        # 选择sdi趋势
        selected_sdi_trend = st.selectbox("请选择SDI【社会人口指数（Socio-demographic Index, SDI）综合反应了一个国家/地区发展状况，由25岁以下女性的总体生育率、15岁及以上女性的平均教育水平、人均收入等数据综合评估得出】",
                                          ["不变", "自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        if selected_sdi_trend == "自然趋势基础上上升":
            sdi_percentage = st.slider("请选择上升百分比", 0, 100, 10)
        elif selected_sdi_trend == "自然趋势基础上下降":
            sdi_percentage = st.slider("请选择下降百分比", 0, 100, 10)

        # 选择人均蔬菜消费量
        selected_vegan_trend = st.selectbox("请选择人均蔬菜消费量", ["不变", "自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        if selected_vegan_trend == "自然趋势基础上上升":
            vegan_percentage = st.slider("请选择上升百分比", 0, 100, 10, key="up_percentage")
        elif selected_obese_trend == "自然趋势基础上下降":
            vegan_percentage = st.slider("请选择下降百分比", 0, 100, 10, key="down_percentage")

        # 选择人均水果消费量
        selected_fruit_trend = st.selectbox("请选择人均水果消费量", ["不变", "自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        if selected_fruit_trend == "自然趋势基础上上升":
            fruit_percentage = st.slider("请选择上升百分比", 0, 100, 10, key="up_percentage")
        elif selected_obese_trend == "自然趋势基础上下降":
            fruit_percentage = st.slider("请选择下降百分比", 0, 100, 10, key="down_percentage")

        # 选择人均红肉消费量
        selected_meat_trend = st.selectbox("请选择人均红肉消费量", ["不变", "自然趋势", "自然趋势基础上上升", "自然趋势基础上下降"])
        if selected_meat_trend == "自然趋势基础上上升":
            meat_percentage = st.slider("请选择上升百分比", 0, 100, 10, key="up_percentage")
        elif selected_obese_trend == "自然趋势基础上下降":
            meat_percentage = st.slider("请选择下降百分比", 0, 100, 10, key="down_percentage")
    elif selected_model == "ARIMA模型（AutoRegressive Integrated Moving Average Model）":
        st.write("ARIMA是一种基于随机理论的时间序列分析方法，通过整合自回归（AR）、差分（I）和移动平均（MA）三个成分，能够有效捕捉时间序列数据中的线性关系和趋势变化")
        selected_year = st.slider("请选择预测终止年份", 2020, 2040, 2020)
    elif selected_model == "LSTM模型（Long Short Term Memory）":
        st.write("LSTM是一种递归神经网络（RNN）的变体，它在处理长序列数据时，能够有效地解决标准 RNN 的梯度消失问题。相比于普通的神经网络，LSTM 模型引入了三个门控单元，即输入门、遗忘门和输出门，来控制信息的输入、输出和遗忘")
        selected_year = st.slider("请选择预测终止年份", 2020, 2040, 2020)
    elif selected_model == "ARIMA-LSTM混合模型":
        st.write("ARIMA-LSTM是一种结合了ARIMA和LSTM两种时间序列预测方法的技术。该模型利用ARIMA模型提取原始序列数据的线性特征，将ARIMA模型预测值与实际值之间的残差输入LSTM模型进行残差预测提取非线性特征。将线性部分和非线性部分结合起来，得到ARIMA-LSTM混合模型的预测结果")
        selected_year = st.slider("请选择预测终止年份", 2020, 2040, 2020)

    # 显示结果
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("显示结果", key="forecast_button"):
            if selected_model == "GAMM模型（Generalized Additive Mixed Models, GAMM）":
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EGAMM%E6%A8%A1%E5%9E%8B%E6%8B%9F%E5%90%88%E7%9A%84SDI%E3%80%81%E6%88%90%E4%BA%BA%E8%B6%85%E9%87%8D%E7%8E%87%E4%B8%8E%E5%8F%91%E7%97%85%E7%8E%87%E9%97%B4%E7%9A%84%E6%9C%89%E6%95%88%E8%87%AA%E7%94%B1%E5%BA%A6.png?raw=true",
                         caption="基于GAMM模型拟合的SDI、成人超重率与发病率间的有效自由度")
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EGAMM%E6%A8%A1%E5%9E%8B%E9%A2%84%E6%B5%8B%E4%B8%8D%E5%90%8C%E6%88%90%E4%BA%BA%E8%B6%85%E9%87%8D%E7%8E%87%E5%8F%91%E5%B1%95%E5%9C%BA%E6%99%AF%E4%B8%8B2022-2040%E5%B9%B4%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E7%9A%84%E8%B6%8B%E5%8A%BF.png?raw=true",
                         caption="基于GAMM模型预测不同成人超重率发展场景下2022-2040年糖尿病年龄标化发病率的趋势（ASIR: age-standardized incident rate）")
            elif selected_model == "ARIMA模型（AutoRegressive Integrated Moving Average Model）":
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1990-2021%E5%B9%B4%E5%9F%BA%E4%BA%8EARIMA%E6%A8%A1%E5%9E%8B%E6%8B%9F%E5%90%88%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87.png?raw=true",
                         caption="1990-2021年基于ARIMA模型拟合中国糖尿病年龄标化发病率")
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EARIMA%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%9C%AA%E6%9D%A52022-2040%E5%B9%B4%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E9%A2%84%E6%B5%8B.png?raw=true",
                         caption="基于ARIMA模型对未来2022-2040年的糖尿病年龄标化发病率预测")
            elif selected_model == "LSTM模型（Long Short Term Memory）":
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1990-2021%E5%B9%B4%E5%9F%BA%E4%BA%8ELSTM%E6%A8%A1%E5%9E%8B%E6%8B%9F%E5%90%88%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87.png?raw=true",
                         caption="1990-2021年基于LSTM模型拟合糖尿病年龄标化发病率")
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8ELSTM%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%9C%AA%E6%9D%A52022-2040%E5%B9%B4%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E9%A2%84%E6%B5%8B.png?raw=true",
                         caption="基于LSTM模型对未来2022-2040年的糖尿病年龄标化发病率预测")
            else:
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/1990-2021%E5%B9%B4%E5%9F%BA%E4%BA%8EARIMA-LSTM%E6%B7%B7%E5%90%88%E6%A8%A1%E5%9E%8B%E5%90%88%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87.png?raw=true",
                         caption="1990-2021年基于ARIMA-LSTM混合模型合糖尿病年龄标化发病率")
                st.image(r"https://github.com/ChimonGu/Disease_Burden_streamlit/blob/main/images/%E5%9F%BA%E4%BA%8EARIMA-LSTM%E6%B7%B7%E5%90%88%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%9C%AA%E6%9D%A52022-2040%E5%B9%B4%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E9%A2%84%E6%B5%8B.png?raw=true",
                         caption="基于ARIMA-LSTM混合模型对未来2022-2040年的糖尿病年龄标化发病率预测")


if __name__ == "__main__":
    main()
