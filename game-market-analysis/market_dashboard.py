import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="游戏竞品分析看板", layout="wide")

st.title("📊 游戏竞品分析看板")
st.markdown("> Block Blast vs Tetris Block Party | 2025年市场调研数据")

# 侧边栏
st.sidebar.header("🔍 导航")
section = st.sidebar.radio(
    "选择模块",
    ["整体概览", "产品对比", "下载与营收", "投放策略", "素材风格", "策略建议"]
)

# 1. 整体概览
if section == "整体概览":
    st.subheader("市场关键发现")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("女性玩家占比", "46%", "+5%")
    with col2:
        st.metric("40-50岁付费意愿", "33%", "+8%")
    with col3:
        st.metric("女性游戏时长", "+25%", "超男性")
    with col4:
        st.metric("情绪价值驱动", "50.8%", "首要因素")
    
    st.markdown("---")
    st.subheader("竞品格局")
    st.write("- Block Blast：下沉市场王者，MAU 1.5亿+")
    st.write("- Candy Crush：消除类常青树，月营收1.08亿美元")
    st.write("- Gossip Harbor：女性合成黑马，月营收增长254%")
    st.write("- Tetris Block Party：IP情怀+PVP，小众精品定位")

# 2. 产品对比
elif section == "产品对比":
    st.subheader("核心产品对比")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Block Blast")
        st.write("- 开发商：北京迦游")
        st.write("- 玩法：8x8网格方块匹配")
        st.write("- 变现：纯IAA广告")
        st.write("- 月活：1.5-1.6亿")
        st.write("- 日活：4000万+")
        st.write("- 累计下载：5亿+")
    with col2:
        st.markdown("### Tetris Block Party")
        st.write("- 开发商：Playstudios")
        st.write("- 玩法：俄罗斯方块+派对")
        st.write("- 变现：内购为主")
        st.write("- 月活：约50万")
        st.write("- 日活：约15万")
        st.write("- 累计下载：约400万")

# 3. 下载与营收
elif section == "下载与营收":
    st.subheader("月度下载量对比")
    
    months = ["3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月"]
    block_blast = [2500, 2600, 2700, 2800, 2900, 2850, 2950, 3009]
    tetris = [3.2, 3.5, 3.8, 4.0, 3.9, 4.2, 4.1, 4.0]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(months, block_blast, marker="o", linewidth=2, label="Block Blast", color="#FF6B6B")
    ax.plot(months, tetris, marker="s", linewidth=2, label="Tetris", color="#4ECDC4")
    ax.set_xlabel("月份")
    ax.set_ylabel("下载量 (万次)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    st.info("Block Blast 2025年10月达3009万次，Tetris月下载约3-4万次")

# 4. 投放策略
elif section == "投放策略":
    st.subheader("投放策略对比")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Block Blast")
        st.write("- 单日展现：最高2000万次")
        st.write("- 月素材量：1.4万组")
        st.write("- 核心地域：印度、印尼、巴西")
        st.write("- 渠道：TikTok、Facebook、Instagram")
    with col2:
        st.markdown("### Tetris Block Party")
        st.write("- 单日展现：约50万次")
        st.write("- 月素材量：约500组")
        st.write("- 核心地域：英国、加拿大、荷兰")
        st.write("- 渠道：Facebook、Bluestacks")

# 5. 素材风格
elif section == "素材风格":
    st.subheader("素材风格对比")
    
    data = {
        "维度": ["色彩", "画面", "特效", "文案"],
        "Block Blast": ["高饱和度", "简洁UI", "连击爽感", "低门槛轻松"],
        "Tetris": ["复古+现代", "派对场景", "PVP竞技感", "情怀+竞技"]
    }
    st.dataframe(pd.DataFrame(data), use_container_width=True)
    
    st.markdown("---")
    st.subheader("A/B测试建议")
    st.write("- 版本A（下沉市场）：模仿Block Blast，高饱和+简单玩法")
    st.write("- 版本B（欧美市场）：模仿Tetris，派对风+PVP对战")

# 6. 策略建议
elif section == "策略建议":
    st.subheader("核心结论")
    
    st.success("""
    **Block Blast 成功要素**
    1. AI驱动低门槛：失败率控制在5%以下
    2. 纯IAA适配下沉：契合印度、巴西用户习惯
    3. 社交竞技强化留存：全球排行榜、组队对战
    """)
    
    st.info("""
    **Tetris Block Party 差异化策略**
    1. IP情怀+创新：经典玩法+派对场景
    2. PVP对战：1V1全球对战满足竞技需求
    3. 精准投放：聚焦英、加、荷等T1市场
    """)
    
    st.markdown("---")
    st.subheader("对CrazyFox的建议")
    st.write("1. 优化核心道具的高饱和色彩与连击特效")
    st.write("2. 小范围测试两类素材，根据数据调整配比")
    st.write("3. 复用Block Blast的AI低门槛思路，降低新手流失")

st.markdown("---")
st.caption("数据来源：2025年游戏市场调研报告 | 竞品分析看板")