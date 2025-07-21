import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import streamlit as st

# 앱 제목
st.title("Net ODA Received by Region (1960–2022)")

# CSV 파일 링크 (raw URL)
csv_url = "https://raw.githubusercontent.com/Yoonseok-KimtheGreat/ODA-/refs/heads/main/ODA%20Data.csv"

# 데이터 불러오기
try:
    df = pd.read_csv(csv_url, skiprows=4)
except Exception as e:
    st.error(f"CSV 파일 로딩 실패: {e}")
    st.stop()

# 연도 및 지역 코드 정의
years = [str(y) for y in range(1960, 2023)]
region_codes = ["AFE", "AFW", "ARB", "CEB", "EAS", "ECS", "LCN", "MEA", "NAC", "SSF", "SAS"]
code_to_name = {
    "AFE": "Africa Eastern and Southern",
    "AFW": "Africa Western and Central",
    "ARB": "Arab World",
    "CEB": "Central Europe and the Baltics",
    "EAS": "East Asia & Pacific",
    "ECS": "Europe & Central Asia",
    "LCN": "Latin America & Caribbean",
    "MEA": "Middle East & North Africa",
    "NAC": "North America",
    "SSF": "Sub-Saharan Africa",
    "SAS": "South Asia"
}

# 시각화
fig, ax = plt.subplots(figsize=(14, 7))

for code in region_codes:
    row = df[df["Country Code"] == code]
    if row.empty:
        continue
    values = row[years].iloc[0].astype(float) / 1e9  # 십억 달러 단위
    label = f"{code} ({code_to_name.get(code, 'Unknown')})"
    ax.plot(years, values, label=label)

# 그래프 설정
ax.set_title("Net ODA Received by Region (1960–2022)")
ax.set_xlabel("Year")
ax.set_ylabel("ODA Received (Billion US$)")
ax.set_xticks(range(0, len(years), 5))
ax.set_xticklabels(years[::5], rotation=45)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.1f}"))
ax.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(True)

# Streamlit에 출력
st.pyplot(fig)

