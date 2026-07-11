import streamlit as st
import plotly.graph_objects as go
import joblib
# ----------------------------------------
# Page Config
# ----------------------------------------

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)
model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
# ----------------------------------------
# Load CSS
# ----------------------------------------

with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ----------------------------------------
# Header
# ----------------------------------------
st.markdown("""
<div style="text-align:center; margin-bottom:35px;">

<div style="display:flex; justify-content:center; align-items:center; gap:15px;">

<span style="font-size:50px;">📧</span>

<span style="color:white; font-size:40px; font-weight:700;">
Email Spam Detector
</span>

</div>

<p style="color:#B5C0D6; font-size:18px; margin-top:12px;">
Analyze email messages using Machine Learning and Natural Language Processing
</p>

</div>
""", unsafe_allow_html=True)
# ======================================================
# MAIN SECTION
# ======================================================

left, right = st.columns([1.2, 1])

# -------------------------------
# LEFT CARD
# -------------------------------

with left:

    st.markdown("""
    <div class="card">

    <h5>✉️ Enter Email</h5>

    </div>
    """, unsafe_allow_html=True)

    email = st.text_area(
        "",
        height=160,
        placeholder="Paste your email here..."
    )

    analyze = st.button(
    "🔍 Analyze Email",
    use_container_width=True
)

prediction = None
probability = 0
progress = 0
result = "Waiting..."
color = "#ff5a5a"
confidence = "--"

if analyze:

    if email.strip() == "":
        st.warning("Please enter an email.")

    else:

        vector = vectorizer.transform([email])

        prediction = model.predict(vector)[0]

        probability = model.predict_proba(vector)[0].max() * 100
        progress = probability
        confidence = f"{probability:.2f}%"

        if prediction == 1:
            result = "🚨 Spam Email"
            color = "#ff4d4d"
        else:
            result = "✅ Safe Email"
            color = "#35d07f"

# -------------------------------
# RIGHT CARD
# -------------------------------
with right:

    st.markdown("""
<div class="prediction-card">
<h3>📊 Prediction Result</h3>
</div>
""", unsafe_allow_html=True)

    if prediction is None:
        st.warning("Waiting...")

    elif prediction == 1:
        st.error(result)

    else:
        st.success(result)

    st.write(f"### Confidence: {confidence}")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=progress,
        number={"suffix":"%"},
        title={"text":"Spam Score"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":color},
            "steps":[
                {"range":[0,50],"color":"green"},
                {"range":[50,80],"color":"orange"},
                {"range":[80,100],"color":"red"}
            ]
        }
    ))

    fig.update_layout(
        paper_bgcolor="#181515",
        plot_bgcolor="#181515",
        font_color="white",
        height=250,
        margin=dict(l=0,r=0,t=30,b=0)
    )

    st.plotly_chart(fig, use_container_width=True)
words = len(email.split())
characters = len(email)
lines = len(email.splitlines())

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(f"""
    <div class="stats">

    <h4>Words</h4>

    <h3>{words}</h3>

    </div>
    """,
    unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class="stats">

    <h4>Characters</h4>

    <h3>{characters}</h3>

    </div>
    """,
    unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="stats">

    <h4>Lines</h4>

    <h3>{lines}</h3>

    </div>
    """,
    unsafe_allow_html=True)
    st.write("")
st.write("")

st.markdown("""
<div class="security">

<h4>
⚠ Security Tips
</h4>

<ul style="font-size:18px">

<li>Don't click unknown links.</li>

<li>Verify the sender's email address.</li>

<li>Never share OTPs or passwords.</li>

<li>Be cautious of urgent prize or reward messages.</li>

</ul>

</div>
""", unsafe_allow_html=True)
st.write("")

st.markdown("""
<div style="text-align:center;
color:#9CA3AF;
font-size:18px;">

🛡 Hansika Indukuri | Machine Learning Project

</div>
""", unsafe_allow_html=True)