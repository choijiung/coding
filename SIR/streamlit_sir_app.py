import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="SIR Model Interactive Demo", layout="wide")

st.title("SIR 모델 인터랙티브 시뮬레이터")

st.markdown("감염률 β와 회복률 γ를 조정하여 SIR 모델에 따른 S, I, R 군집의 사람수 변화를 확인하세요 ")
st.markdown("SIR 모델 미분방정식")
st.markdown("$$\\frac{dS}{dt} = -\\beta \\frac{SI}{N},\\quad \\frac{dI}{dt} = \\beta \\frac{SI}{N} - \\gamma I,\\quad \\frac{dR}{dt} = \\gamma I.$$")

with st.sidebar:
    st.header("초기값")
    N = st.number_input("총 인구 N", min_value=1, value=1_000_000, step=1_000)
    I0 = st.number_input("초기 감염자 I0", min_value=0, max_value=int(N), value=10, step=1)
    R0_init = st.number_input("초기 회복자 R0", min_value=0, max_value=int(N), value=0, step=1)
    S0 = max(N - I0 - R0_init, 0)
    st.write(f"초기 비감염자 S0: **{S0}**")

    st.divider()
    beta = st.slider("감염률 β (1/일)", min_value=0.0, max_value=2.0, value=0.3, step=0.001)
    gamma = st.slider("회복률 γ (1/일)", min_value=0.0001, max_value=2.0, value=0.1, step=0.001)
    days = st.slider("시뮬레이션 기간 (일)", min_value=1, max_value=365, value=180, step=1)
    dt = st.select_slider("시간 간격 Δt (일)", options=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0], value=0.1)

R0_eff = beta / gamma
st.metric("기초감염재생산수 R₀(추정)", f"{R0_eff:0.3f}", help="R₀ ≈ β/γ")

# Euler integration for SIR model
def simulate_sir(N, S0, I0, R0, beta, gamma, days, dt=0.1):
    steps = int(days / dt) + 1
    t = np.linspace(0, steps*dt, steps)
    S = np.zeros(steps)
    I = np.zeros(steps)
    R = np.zeros(steps)
    S[0], I[0], R[0] = S0, I0, R0

    for k in range(1, steps):
        dS = -beta * S[k-1] * I[k-1] / N
        dI =  beta * S[k-1] * I[k-1] / N - gamma * I[k-1]
        dR =  gamma * I[k-1]
        S[k] = S[k-1] + dS * dt
        I[k] = I[k-1] + dI * dt
        R[k] = R[k-1] + dR * dt

        # 수치 안정화: 음수 방지 및 집단 합 보정
        S[k] = max(S[k], 0.0)
        I[k] = max(I[k], 0.0)
        R[k] = max(R[k], 0.0)
        total = S[k] + I[k] + R[k]
        if total != 0:
            scale = N / total
            S[k] *= scale
            I[k] *= scale
            R[k] *= scale

    return t, S, I, R

t, S, I, R = simulate_sir(N, S0, I0, R0_init, beta, gamma, days, dt)

peak_I_idx = int(np.argmax(I))
peak_I = I[peak_I_idx]
peak_t = t[peak_I_idx]

col1, col2, col3 = st.columns(3)
col1.metric("최대 감염자 수", f"{peak_I:,.0f}")
col2.metric("최대 시점 (일)", f"{peak_t:0.1f}")
final_R = R[-1]
col3.metric("최종 누적 회복", f"{final_R:,.0f}")
plt.rcParams['font.family'] = 'AppleGothic'
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(t, S, label="S(t) 비감염자", linewidth=2)
ax.plot(t, I, label="I(t) 감염자", linewidth=2)
ax.plot(t, R, label="R(t) 회복/제거", linewidth=2)
ax.set_xlabel("시간 (일)")
ax.set_ylabel("사람 수")
ax.set_title("SIR 모델 시뮬레이션")
ax.legend()
ax.grid(True)


st.pyplot(fig, clear_figure=True)

with st.expander("가정"):
    st.markdown(
        "- 모든 개인이 동일한 확률로 접촉한다고 가정\n"
        "- 총 인구수 변화를 무시\n"
        "- 감염률, 회복률이 일정하다고 가정\n"
    )

st.markdown("---")
st.markdown("참고 문헌 : Compartmental models (epidemiology), Wikipedia, https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)")
