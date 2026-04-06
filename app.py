import streamlit as st

st.set_page_config(page_title="Restaurant Dashboard", layout="wide")

# 🔥 Background + Blur + Modern UI
page_bg = """
<style>

/* Background */
.stApp {
    background: url("https://images.unsplash.com/photo-1498654896293-37aacf113fd9") no-repeat center center fixed;
    background-size: cover;
}

/* Blur + dark overlay */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    backdrop-filter: blur(12px);
    background: rgba(0,0,0,0.65);
    z-index: -1;
}

/* Glass container */
.block-container {
    background: rgba(0, 0, 0, 0.75);
    padding: 30px;
    border-radius: 20px;
}

/* Card style */
.card {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    margin: 10px;
}

/* Text */
h1, h2, h3, p {
    color: white !important;
    text-align: center;
}

/* Button */
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# 🔥 Title
st.title("🍴 Smart Restaurant Dashboard")

st.write("### Choose Your Items")

# 🔥 Cards layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">🍕 Pizza - ₹200</div>', unsafe_allow_html=True)
    pizza = st.checkbox("Select Pizza")

    st.markdown('<div class="card">🍔 Burger - ₹120</div>', unsafe_allow_html=True)
    burger = st.checkbox("Select Burger")

with col2:
    st.markdown('<div class="card">🍝 Pasta - ₹150</div>', unsafe_allow_html=True)
    pasta = st.checkbox("Select Pasta")

    st.markdown('<div class="card">🍟 Fries - ₹80</div>', unsafe_allow_html=True)
    fries = st.checkbox("Select Fries")

with col3:
    st.markdown('<div class="card">🍛 Biryani - ₹250</div>', unsafe_allow_html=True)
    biryani = st.checkbox("Select Biryani")

    st.markdown('<div class="card">☕ Coffee - ₹50</div>', unsafe_allow_html=True)
    coffee = st.checkbox("Select Coffee")

# 🔥 Button
if st.button("Generate Bill 💳"):

    total = 0
    items = []

    if pizza:
        total += 200
        items.append("Pizza")
    if burger:
        total += 120
        items.append("Burger")
    if pasta:
        total += 150
        items.append("Pasta")
    if fries:
        total += 80
        items.append("Fries")
    if biryani:
        total += 250
        items.append("Biryani")
    if coffee:
        total += 50
        items.append("Coffee")

    if total == 0:
        st.warning("⚠️ Please select items")
    else:
        st.success("✅ Order Placed!")

        # 🔥 Result box
        st.markdown(f"""
        <div class="card">
        <h3>🧾 Items: {', '.join(items)}</h3>
        <h2>💰 Total: ₹{total}</h2>
        </div>
        """, unsafe_allow_html=True)