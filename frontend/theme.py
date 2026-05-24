import streamlit as st

DARK = {
    "bg":          "#050B18",
    "surface":     "#0D1B2E",
    "surface2":    "#142035",
    "border":      "#1E3A5F",
    "accent":      "#F0C040",
    "accent_glow": "rgba(240,192,64,0.35)",
    "text":        "#F1F5F9",
    "muted":       "#94A3B8",
    "success":     "#22D3A5",
    "danger":      "#F43F5E",
    "hero_grad":   "linear-gradient(135deg, #0A2040 0%, #0F3060 60%, #142850 100%)",
    "btn_color":   "#050B18",
}

LIGHT = {
    "bg":          "#F8FAFC",
    "surface":     "#FFFFFF",
    "surface2":    "#F1F5F9",
    "border":      "#CBD5E1",
    "accent":      "#1D4ED8",
    "accent_glow": "rgba(29,78,216,0.2)",
    "text":        "#0F172A",
    "muted":       "#475569",
    "success":     "#059669",
    "danger":      "#DC2626",
    "hero_grad":   "linear-gradient(135deg, #1D4ED8 0%, #2563EB 60%, #1E40AF 100%)",
    "btn_color":   "#FFFFFF",
}


def _p():
    return DARK if st.session_state.get("dark_mode", True) else LIGHT


def load_css():
    p = _p()
    st.markdown(
        """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">""",
        unsafe_allow_html=True
    )
    css = f"""
<style>
html, body, [class*="css"], .stApp {{
    font-family: 'Inter', sans-serif !important;
    background-color: {p["bg"]} !important;
    color: {p["text"]} !important;
}}

/* ── Sidebar ──────────────────────────────────────── */
section[data-testid="stSidebar"] {{
    background: {p["surface"]} !important;
    border-right: 1px solid {p["border"]} !important;
}}
section[data-testid="stSidebar"] * {{
    color: {p["text"]} !important;
}}
section[data-testid="stSidebar"] a {{
    color: {p["accent"]} !important;
    text-decoration: none !important;
}}
section[data-testid="stSidebarNav"] li span,
section[data-testid="stSidebarNav"] li a {{
    color: {p["text"]} !important;
    font-weight: 500 !important;
}}
section[data-testid="stSidebarNav"] li a:hover {{
    color: {p["accent"]} !important;
}}

/* ── Main layout ──────────────────────────────────── */
.block-container {{
    padding-top: 1.5rem !important;
    max-width: 1200px;
}}

/* ── Headings ─────────────────────────────────────── */
h1, h2, h3, h4, h5, h6 {{
    color: {p["text"]} !important;
    font-weight: 700 !important;
}}

/* ── All plain text / paragraph / spans ───────────── */
p, span, li, div {{
    color: {p["text"]};
}}
.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span {{
    color: {p["text"]} !important;
}}

/* ── Widget LABELS (radio, checkbox, input, select) ── */
.stRadio label,
.stRadio > label,
.stRadio div > label,
.stCheckbox label,
.stCheckbox > label,
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stSlider label,
.stMultiSelect label,
.stFileUploader label,
.stNumberInput label,
.stDateInput label,
.stTimeInput label,
div[data-testid="stWidgetLabel"],
div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] span,
div[data-baseweb="label"],
div[data-baseweb="label"] span {{
    color: {p["text"]} !important;
    font-weight: 500 !important;
}}

/* ── Radio button items ───────────────────────────── */
.stRadio div[role="radiogroup"] label,
.stRadio div[role="radiogroup"] span,
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] span {{
    color: {p["text"]} !important;
}}
div[data-baseweb="radio"] > div {{
    background-color: {p["surface2"]} !important;
    border-color: {p["border"]} !important;
}}
div[data-baseweb="radio"] svg {{
    fill: {p["accent"]} !important;
}}

/* ── Select / Dropdown ────────────────────────────── */
.stSelectbox > div > div,
.stMultiSelect > div > div {{
    background-color: {p["surface2"]} !important;
    color: {p["text"]} !important;
    border: 1.5px solid {p["border"]} !important;
    border-radius: 10px !important;
    font-size: 0.95rem !important;
}}
.stSelectbox svg, .stMultiSelect svg {{
    fill: {p["muted"]} !important;
}}
ul[data-testid="stSelectboxVirtualDropdown"],
ul[data-testid="stSelectboxVirtualDropdown"] li,
ul[role="listbox"],
ul[role="listbox"] li,
div[data-baseweb="popover"],
div[data-baseweb="menu"],
div[data-baseweb="menu"] li,
li[role="option"] {{
    background-color: {p["surface2"]} !important;
    color: {p["text"]} !important;
}}
div[data-baseweb="menu"] li:hover,
div[data-baseweb="menu"] li[data-highlighted="true"],
div[data-baseweb="menu"] li[aria-selected="true"],
div[data-baseweb="menu"] li[data-focused="true"],
ul[data-testid="stSelectboxVirtualDropdown"] li:hover,
ul[data-testid="stSelectboxVirtualDropdown"] li[aria-selected="true"],
ul[role="listbox"] li:hover,
ul[role="listbox"] li[aria-selected="true"],
ul[role="listbox"] li[data-highlighted="true"],
li[role="option"]:hover,
li[role="option"][aria-selected="true"],
li[role="option"][data-highlighted="true"] {{
    background-color: {p["accent"]} !important;
    color: #FFFFFF !important;
}}
div[data-baseweb="menu"] li:hover *,
div[data-baseweb="menu"] li[aria-selected="true"] *,
ul[data-testid="stSelectboxVirtualDropdown"] li:hover *,
ul[role="listbox"] li:hover *,
ul[role="listbox"] li[aria-selected="true"] *,
li[role="option"]:hover *,
li[role="option"][aria-selected="true"] * {{
    color: #FFFFFF !important;
}}

/* ── Text inputs & Text areas ─────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {{
    background-color: {p["surface2"]} !important;
    color: {p["text"]} !important;
    border: 1.5px solid {p["border"]} !important;
    border-radius: 10px !important;
    font-size: 0.95rem !important;
}}
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {{
    color: {p["muted"]} !important;
    opacity: 0.8 !important;
}}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {{
    border-color: {p["accent"]} !important;
    box-shadow: 0 0 0 2px {p["accent_glow"]} !important;
    outline: none !important;
}}

/* ── Buttons ──────────────────────────────────────── */
.stButton > button {{
    background: {p["accent"]} !important;
    color: {p["btn_color"]} !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.55rem 1.2rem !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 18px {p["accent_glow"]} !important;
    transition: all 0.2s ease !important;
}}
.stButton > button:hover {{
    filter: brightness(1.15) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px {p["accent_glow"]} !important;
}}
.stButton > button:active {{
    transform: translateY(0px) !important;
}}
.stDownloadButton > button {{
    background: {p["surface2"]} !important;
    color: {p["text"]} !important;
    border: 1.5px solid {p["accent"]} !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}}

/* ── Progress bar ─────────────────────────────────── */
.stProgress > div > div > div > div {{
    background: {p["accent"]} !important;
}}

/* ── Expanders ────────────────────────────────────── */
.streamlit-expanderHeader,
div[data-testid="stExpander"] summary {{
    background: {p["surface2"]} !important;
    border: 1px solid {p["border"]} !important;
    border-radius: 8px !important;
    color: {p["text"]} !important;
    font-weight: 600 !important;
}}
.streamlit-expanderContent,
div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {{
    background: {p["surface"]} !important;
    border: 1px solid {p["border"]} !important;
    border-top: none !important;
    color: {p["text"]} !important;
}}
div[data-testid="stExpander"] p,
div[data-testid="stExpander"] span {{
    color: {p["text"]} !important;
}}

/* ── Tabs ─────────────────────────────────────────── */
button[data-baseweb="tab"],
div[data-testid="stTabs"] button {{
    color: {p["muted"]} !important;
    font-weight: 600 !important;
}}
button[data-baseweb="tab"][aria-selected="true"],
div[data-testid="stTabs"] button[aria-selected="true"] {{
    color: {p["accent"]} !important;
    border-bottom: 2px solid {p["accent"]} !important;
}}

/* ── Metrics ──────────────────────────────────────── */
div[data-testid="metric-container"] label,
div[data-testid="metric-container"] div,
div[data-testid="metric-container"] p {{
    color: {p["text"]} !important;
}}

/* ── Spinner / status messages ────────────────────── */
.stSpinner > div > div {{
    border-top-color: {p["accent"]} !important;
}}
div[data-testid="stStatusWidget"] {{
    color: {p["text"]} !important;
}}

/* ── Alerts / Notifications ───────────────────────── */
div[data-baseweb="notification"] {{
    border-radius: 10px !important;
}}
.stAlert p, .stAlert span, .stAlert div {{
    color: inherit !important;
}}

/* ── Slider ───────────────────────────────────────── */
div[data-testid="stSlider"] div[data-baseweb="slider"] div {{
    background-color: {p["border"]} !important;
}}
div[data-testid="stSlider"] div[data-baseweb="slider"] div[role="slider"] {{
    background-color: {p["accent"]} !important;
    border-color: {p["accent"]} !important;
}}

/* ── File uploader ────────────────────────────────── */
div[data-testid="stFileUploader"] section {{
    background-color: {p["surface2"]} !important;
    border: 2px dashed {p["border"]} !important;
    border-radius: 10px !important;
    color: {p["muted"]} !important;
}}
div[data-testid="stFileUploader"] section button,
div[data-testid="stFileUploaderDropzone"] button {{
    background-color: {p["accent"]} !important;
    color: {p["btn_color"]} !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}}
div[data-testid="stFileUploaderDropzoneInstructions"],
div[data-testid="stFileUploaderDropzoneInstructions"] span,
div[data-testid="stFileUploaderDropzoneInstructions"] small,
div[data-testid="stFileUploader"] section span,
div[data-testid="stFileUploader"] section small {{
    color: {p["muted"]} !important;
}}

/* ── HR divider ───────────────────────────────────── */
hr {{
    border-color: {p["border"]} !important;
    opacity: 1 !important;
}}

/* ── Scrollbar ────────────────────────────────────── */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: {p["surface"]}; }}
::-webkit-scrollbar-thumb {{ background: {p["border"]}; border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: {p["accent"]}; }}
</style>
"""
    st.markdown(css, unsafe_allow_html=True)


def render_theme_toggle():
    p = _p()
    icon = "Sun" if st.session_state.get("dark_mode", True) else "Moon"
    label = "Light Mode" if st.session_state.get("dark_mode", True) else "Dark Mode"
    with st.sidebar:
        st.markdown(
            f"""<div style="background:{p['surface2']};border:1.5px solid {p['border']};
border-radius:12px;padding:10px 14px;margin-bottom:12px;text-align:center;color:{p['muted']};
font-size:0.82rem;">Current Mode: <b style="color:{p['accent']};">{'Dark' if st.session_state.get('dark_mode', True) else 'Light'}</b></div>""",
            unsafe_allow_html=True
        )
        if st.button(f"Switch to {label}", use_container_width=True):
            st.session_state["dark_mode"] = not st.session_state.get("dark_mode", True)
            st.rerun()


def render_hero(title, subtitle):
    p = _p()
    st.markdown(
        f"""<div style="background:{p['hero_grad']};padding:44px 40px;border-radius:20px;
margin-bottom:28px;border:1px solid {p['border']};
box-shadow:0 8px 32px {p['accent_glow']};text-align:center;overflow:hidden;">
<div style="font-size:2.4rem;font-weight:800;color:#FFFFFF;letter-spacing:-0.5px;
margin-bottom:10px;text-shadow:0 2px 12px rgba(0,0,0,0.4);">{title}</div>
<div style="font-size:1.05rem;color:rgba(255,255,255,0.78);font-weight:400;
max-width:600px;margin:0 auto;">{subtitle}</div>
<div style="display:inline-block;margin-top:14px;background:rgba(255,255,255,0.15);
border:1px solid rgba(255,255,255,0.3);border-radius:50px;padding:4px 18px;
font-size:0.75rem;color:rgba(255,255,255,0.85);letter-spacing:1px;
font-weight:600;text-transform:uppercase;">AI-Powered Legal Intelligence</div>
</div>""",
        unsafe_allow_html=True
    )


def render_card(title, text):
    p = _p()
    st.markdown(
        f"""<div style="background:{p['surface']};padding:22px 24px;border-radius:16px;
border:1.5px solid {p['border']};box-shadow:0 2px 12px rgba(0,0,0,0.25);margin-bottom:16px;">
<div style="color:{p['accent']};font-size:1.05rem;font-weight:700;margin-bottom:8px;">{title}</div>
<div style="color:{p['muted']};font-size:0.92rem;line-height:1.6;">{text}</div>
</div>""",
        unsafe_allow_html=True
    )


def render_action_card(title, text, link):
    p = _p()
    st.markdown(
        f"""<a href="{link}" target="_self" style="text-decoration:none;display:block;margin-bottom:12px;">
<div style="background:{p['surface']};padding:24px;border-radius:16px;
border:1.5px solid {p['border']};box-shadow:0 2px 12px rgba(0,0,0,0.2);cursor:pointer;">
<div style="color:{p['accent']};font-size:1.05rem;font-weight:700;margin-bottom:6px;">{title}</div>
<div style="color:{p['muted']};font-size:0.9rem;">{text}</div>
</div></a>""",
        unsafe_allow_html=True
    )


def render_answer_box(content):
    import html as _html
    p = _p()
    safe_content = _html.escape(str(content)).replace("\n", "<br>")
    st.markdown(
        f"""<div style="background:{p['surface']};border-left:5px solid {p['success']};
border-radius:12px;padding:20px 24px;box-shadow:0 2px 12px rgba(0,0,0,0.2);
color:{p['text']};font-size:0.97rem;line-height:1.75;margin:10px 0 16px;">
<div style="color:{p['success']};font-weight:700;margin-bottom:8px;font-size:0.82rem;
letter-spacing:1px;text-transform:uppercase;">Legal Answer</div>
{safe_content}</div>""",
        unsafe_allow_html=True
    )


def render_legal_section_card(title, description, punishment):
    p = _p()
    st.markdown(
        f"""<div style="background:{p['surface']};border:1.5px solid {p['border']};
border-radius:14px;padding:20px 22px;margin-bottom:14px;
box-shadow:0 2px 10px rgba(0,0,0,0.2);">
<div style="color:{p['accent']};font-weight:700;font-size:1rem;margin-bottom:6px;">{title}</div>
<div style="color:{p['text']};font-size:0.92rem;margin-bottom:10px;line-height:1.6;">{description}</div>
<div style="background:{p['surface2']};border-left:4px solid {p['success']};
border-radius:6px;padding:8px 12px;color:{p['muted']};font-size:0.87rem;">
Punishment/Remedy: {punishment}</div>
</div>""",
        unsafe_allow_html=True
    )


def render_disclaimer(text):
    p = _p()
    st.markdown(
        f"""<div style="background:{p['surface']};padding:14px 18px;border-radius:10px;
border-left:4px solid {p['accent']};margin-top:30px;color:{p['muted']};
font-size:0.88rem;line-height:1.5;">
<b style="color:{p['text']};">Disclaimer:</b> {text}</div>""",
        unsafe_allow_html=True
    )


def render_section_header(text):
    p = _p()
    st.markdown(
        f"""<div style="display:flex;align-items:center;gap:10px;margin:20px 0 12px;">
<div style="width:4px;height:22px;background:{p['accent']};border-radius:4px;"></div>
<span style="color:{p['text']};font-size:1.15rem;font-weight:700;">{text}</span>
</div>""",
        unsafe_allow_html=True
    )
