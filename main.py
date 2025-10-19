from openai import api_key

from utils import generate_script
import streamlit as st

st.title("视频脚本生成器")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入你的deepseek_api密钥：", type="password")
    st.markdown("[获取deepseek api密钥](https://platform.deepseek.com/api_keys)")

subject = st.text_input("请输入视频的主题")
video_duration = st.number_input("请输入视频的时长（单位：分钟）", min_value=0.1, step=0.1, value=1.00)
creativity = st.slider("请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样)",
                       min_value=0.0, max_value=1.0, step=0.1, value=0.2)

submit = st.button("生成脚本")

if submit and not deepseek_api_key:
    st.info("deepseek_api密钥未提供")
    st.stop()
if submit and not subject:
    st.info("视频标题未提供")
    st.stop()
if submit and video_duration <0.1:
    st.info("视频时长需要大于或等于0.1")
    st.stop()
if submit:
    with st.spinner("ai正在思考，请稍等..."):
        title, search_result, script = generate_script(subject, video_duration, creativity, deepseek_api_key)
    st.success("视频脚本已生成")
    st.subheader("标题：")
    st.write(title)
    st.subheader("视频脚本：")
    st.write(script)
    with st.expander("维基百科搜索结果"):
        st.info(search_result)