import streamlit as st

# Load custom CSS & JS
def load_assets():
    with open("venv\styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    with open("venv\animations.js", "r") as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)

# Apply styles
load_assets()

# Streamlit UI
st.markdown("<h1 class='title'> CODE CARNAGE - HACKATHON</h1>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🚀 Event Overview</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
CODE CARNAGE is an **intense 24-hour hackathon** where developers, designers, and AI enthusiasts come together to **build innovative AI-driven solutions** and battle for top prizes!
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>📌 Problem Statements</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
🛠 **General**: Solve a real-world challenge using AI.<br>
💼 **Sponsors' Problem Statement**: Work on a challenge provided by our event sponsors.<br>
🩺 **Healthcare**: Build an AI-powered assistant for traveling doctors.
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>📜 Participation Guidelines</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
✅ **Each team must select one problem statement.**<br>
👥 **Team Size**: 2–4 members.<br>
📍 **Venue**: CSE(DS) Block.<br>
⌛ **Mode**: 24-hour offline hackathon.<br>
🎯 **Evaluation Rounds**: 2 Phases.<br>
🎓 **College ID card is mandatory.**
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>⏰ Event Schedule</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
🕒 **Start Time**: March 11, 11:30 AM<br>
🕛 **End Time**: March 12, 12:00 PM<br>
🏆 **Winner Announcement**: March 15, 12:30 PM
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🔌 Facilities Provided</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
🍽️ **Meals**: Dinner, Breakfast & Lunch<br>
☕ **Refreshments & Drinks**<br>
🌐 **WiFi & Power Supply**
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>🏆 Prizes & Registration</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
💰 **Total Prize Pool**: ₹30,000<br>
🥇 **1 winner from each domain** (₹10,000 each)<br>
🎟️ **Entry Fee**: ₹400 per team
</div>
""", unsafe_allow_html=True)

# 🔗 Dummy Links
st.markdown("""
<div class='links-container'>
    <a href='https://example.com/register' class='link neon-glow' target='_blank'>🔗 Register Here</a>
    <a href='https://example.com/submit' class='link neon-glow' target='_blank'>📤 Submit Your Project</a>
</div>
""", unsafe_allow_html=True)

st.warning("⚠️ Please read the rules carefully before participating!")

st.markdown("<div class='footer'>Powered by Streamlit 🚀</div>", unsafe_allow_html=True)
