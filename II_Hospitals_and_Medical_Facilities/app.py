import gradio as gr
from fastapi import FastAPI
from backend import HospitalExpertSystem

engine = HospitalExpertSystem()

def run_expert_system(symptoms, age, pain_scale, duration):
    result = engine.evaluate(set(symptoms), int(age), int(pain_scale), duration)
    return result["triage"], result["diagnosis"], result["care_plan"], result["reasoning"]

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --green-900: #0f2d22;
    --green-700: #1a4a38;
    --green-500: #25735a;
    --green-400: #2e9070;
    --green-100: #e6f4ef;
    --green-50:  #f2faf7;
    --gold:      #b8934a;
    --gold-pale: #f5e9d0;
    --white:     #ffffff;
    --gray-50:   #f8fafb;
    --gray-100:  #f0f4f3;
    --gray-200:  #dde8e4;
    --gray-400:  #8aada4;
    --gray-700:  #2d4a42;
    --gray-900:  #111f1b;
}

*, *::before, *::after { box-sizing: border-box; }

body,
.gradio-container,
.gradio-container > .main,
.gradio-container > .main > .wrap {
    background: var(--gray-50) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--gray-900) !important;
}

/* ── Hero ── */
.hero {
    background: linear-gradient(160deg, var(--green-900) 0%, var(--green-700) 55%, var(--green-500) 100%);
    padding: 64px 5vw 56px;
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 50% 80% at 80% -10%, rgba(184,147,74,0.15) 0%, transparent 60%),
        radial-gradient(ellipse 30% 40% at 10% 110%, rgba(255,255,255,0.04) 0%, transparent 50%);
    pointer-events: none;
}
.hero-inner {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(184,147,74,0.18);
    border: 1px solid rgba(184,147,74,0.40);
    color: #e8c97a;
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 100px;
    margin-bottom: 24px;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(32px, 4vw, 52px);
    font-weight: 600;
    color: #ffffff;
    line-height: 1.15;
    letter-spacing: -0.5px;
    margin-bottom: 16px;
}
.hero-sub {
    font-size: 15px;
    font-weight: 300;
    color: rgba(255,255,255,0.68);
    line-height: 1.7;
    max-width: 480px;
}
.hero-rule {
    width: 48px;
    height: 2px;
    background: var(--gold);
    margin: 20px 0;
    border-radius: 2px;
}

/* ── Equal two-column row ── */
.equal-cols {
    padding: 36px 24px 0 !important;
    max-width: 1240px !important;
    margin: 0 auto !important;
    gap: 24px !important;
    align-items: flex-start !important;
}
.equal-cols > div,
.equal-cols > div.gr-column {
    flex: 1 1 0% !important;
    min-width: 0 !important;
    max-width: calc(50% - 12px) !important;
    width: calc(50% - 12px) !important;
}

/* ── Cards ── */
.card {
    background: var(--white) !important;
    border: 1px solid var(--gray-200) !important;
    border-radius: 20px !important;
    box-shadow: 0 4px 20px rgba(15,45,34,0.09) !important;
    padding: 36px 32px 32px !important;
    position: relative !important;
    overflow: hidden !important;
    transition: box-shadow 0.3s ease !important;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 32px;
    width: 40px; height: 3px;
    background: var(--gold);
    border-radius: 0 0 3px 3px;
}
.card:hover { box-shadow: 0 12px 48px rgba(15,45,34,0.14) !important; }

.card-eyebrow {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--green-400);
    margin-bottom: 6px;
}
.card-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 24px;
    font-weight: 600;
    color: var(--green-900);
    margin-bottom: 28px;
    padding-bottom: 18px;
    border-bottom: 1px solid var(--gray-200);
}

/* ── Checkbox Group ── */
.gradio-checkboxgroup {
    background: var(--gray-50) !important;
    border: 1px solid var(--gray-200) !important;
    border-radius: 12px !important;
    padding: 18px 20px !important;
}
.gradio-checkboxgroup > .wrap,
.gradio-checkboxgroup fieldset > div {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
}
.gradio-checkboxgroup label {
    background: var(--white) !important;
    border: 1.5px solid var(--gray-200) !important;
    border-radius: 100px !important;
    padding: 6px 16px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: var(--gray-700) !important;
    cursor: pointer !important;
    transition: all 0.18s ease !important;
    white-space: nowrap;
    user-select: none;
}
.gradio-checkboxgroup label:hover {
    border-color: var(--green-400) !important;
    color: var(--green-500) !important;
    background: var(--green-50) !important;
}
.gradio-checkboxgroup label:has(input:checked) {
    background: var(--green-700) !important;
    border-color: var(--green-700) !important;
    color: #ffffff !important;
    box-shadow: 0 2px 8px rgba(26,74,56,0.25) !important;
}
.gradio-checkboxgroup input[type="checkbox"] { display: none !important; }

/* ── Form labels ── */
.gradio-checkboxgroup > label > span,
.gradio-slider      > label > span,
.gradio-radio       > label > span {
    font-family: 'Inter', sans-serif !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: var(--gray-700) !important;
    margin-bottom: 10px !important;
    display: block !important;
}

/* ── Sliders ── */
.gradio-slider { margin: 4px 0 8px !important; }
.gradio-slider input[type="range"] {
    accent-color: var(--green-500) !important;
    cursor: pointer !important;
}
.gradio-slider input[type="number"] {
    background: var(--green-50) !important;
    border: 1.5px solid var(--green-100) !important;
    border-radius: 8px !important;
    color: var(--green-700) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

/* ── Radio ── */
.gradio-radio fieldset {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
.gradio-radio label {
    background: var(--white) !important;
    border: 1.5px solid var(--gray-200) !important;
    border-radius: 100px !important;
    padding: 7px 18px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: var(--gray-700) !important;
    cursor: pointer !important;
    transition: all 0.18s !important;
    user-select: none;
}
.gradio-radio label:hover {
    border-color: var(--green-400) !important;
    background: var(--green-50) !important;
}
.gradio-radio label:has(input:checked) {
    background: var(--green-700) !important;
    border-color: var(--green-700) !important;
    color: #ffffff !important;
}
.gradio-radio input[type="radio"] { display: none !important; }

/* ── Buttons ── */
button.lg.primary,
.gr-button-primary {
    background: linear-gradient(135deg, var(--green-900) 0%, var(--green-500) 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 100px !important;
    padding: 14px 32px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 16px rgba(15,45,34,0.28) !important;
    transition: all 0.22s ease !important;
    cursor: pointer !important;
    margin-top: 12px !important;
}
button.lg.primary:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 28px rgba(15,45,34,0.38) !important; }

button.lg.secondary,
.gr-button-secondary {
    background: var(--white) !important;
    color: var(--gray-700) !important;
    border: 1.5px solid var(--gray-200) !important;
    border-radius: 100px !important;
    padding: 14px 24px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    transition: all 0.18s ease !important;
    cursor: pointer !important;
    margin-top: 12px !important;
}
button.lg.secondary:hover { border-color: var(--green-400) !important; color: var(--green-500) !important; }

/* ── Triage output ── */
.triage-box textarea {
    background: var(--green-100) !important;
    border: 2px solid var(--green-400) !important;
    border-radius: 12px !important;
    color: var(--green-900) !important;         /* FIXED: dark text */
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding: 18px 24px !important;
    text-align: center !important;
    min-height: 70px !important;
}
.triage-box > label > span {
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    color: var(--green-400) !important;
    margin-bottom: 8px !important;
}

/* ── Result output blocks — clean card, no inner box ── */
.out-block {
    background: var(--white) !important;
    border: 1px solid var(--gray-200) !important;
    border-radius: 14px !important;
    padding: 20px 24px !important;
    margin-top: 16px !important;
    box-shadow: 0 1px 4px rgba(15,45,34,0.06) !important;
    overflow: hidden !important;
}
.out-block > label {
    display: block !important;
    margin-bottom: 14px !important;
    padding-bottom: 12px !important;
    border-bottom: 1px solid var(--gray-100) !important;
}
.out-block > label > span {
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: var(--gold) !important;
    display: block !important;
    margin: 0 !important;
}

/* ── Kill the nested inner box Gradio injects ── */
/* Gradio wraps markdown in extra divs with their own border/bg — strip them all */
.out-block > div,
.out-block .wrap,
.out-block .prose,
.out-block [data-testid="markdown"],
.out-block .gap,
.out-block .svelte-10ogue4,
.out-block > div > div {
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* All text in outputs — force dark + readable */
.out-block,
.out-block *,
.out-block p,
.out-block li,
.out-block h1,
.out-block h2,
.out-block h3,
.out-block h4,
.out-block span,
.out-block div,
.out-block strong,
.out-block em {
    color: var(--gray-900) !important;
    font-family: 'Inter', sans-serif !important;
}

/* Headings inside output */
.out-block h2, .out-block h3 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    color: var(--green-700) !important;
    margin: 18px 0 8px !important;
    padding-top: 16px !important;
    border-top: 1px solid var(--gray-200) !important;
}
.out-block h2:first-child,
.out-block h3:first-child {
    margin-top: 0 !important;
    padding-top: 0 !important;
    border-top: none !important;
}
.out-block h4 {
    font-weight: 600 !important;
    color: var(--green-700) !important;
    font-size: 14px !important;
    margin: 10px 0 4px !important;
}

/* Lists */
.out-block ul {
    list-style: none !important;
    padding: 0 !important;
    margin: 8px 0 !important;
}
.out-block ul li {
    position: relative !important;
    padding: 7px 0 7px 20px !important;
    border-bottom: 1px solid var(--gray-100) !important;
    font-size: 14px !important;
    line-height: 1.6 !important;
    color: var(--gray-900) !important;
}
.out-block ul li:last-child { border-bottom: none !important; }
.out-block ul li::before {
    content: '' !important;
    position: absolute !important;
    left: 0 !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    width: 6px !important;
    height: 6px !important;
    background: var(--green-400) !important;
    border-radius: 50% !important;
}
.out-block ol { padding-left: 18px !important; margin: 8px 0 !important; }
.out-block ol li { padding: 4px 0 !important; font-size: 14px !important; line-height: 1.6 !important; }
.out-block p { margin: 6px 0 !important; font-size: 14px !important; line-height: 1.75 !important; }
.out-block strong { color: var(--green-700) !important; font-weight: 600 !important; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 32px 24px;
    font-size: 12.5px;
    color: var(--gray-400);
    border-top: 1px solid var(--gray-200);
    margin: 28px 0 0;
}
.footer strong { color: var(--green-500); }

/* Hide Gradio chrome */
.gradio-container footer,
footer.svelte-1ax1toq { display: none !important; }

/* =============================================
   RESPONSIVE — MOBILE FIRST
   ============================================= */

/* Tablet: 768px and below — stack columns */
@media (max-width: 768px) {

    /* Hero padding tighter */
    .hero {
        padding: 40px 20px 36px !important;
    }
    .hero-title {
        font-size: 28px !important;
    }
    .hero-title br {
        display: none !important;
    }
    .hero-sub {
        font-size: 14px !important;
        max-width: 100% !important;
    }

    /* Stack the two columns vertically */
    .equal-cols {
        flex-direction: column !important;
        padding: 20px 16px 0 !important;
        gap: 16px !important;
    }
    .equal-cols > div,
    .equal-cols > div.gr-column {
        max-width: 100% !important;
        width: 100% !important;
        flex: none !important;
    }

    /* Card padding */
    .card {
        padding: 24px 20px 20px !important;
        border-radius: 16px !important;
    }
    .card-title {
        font-size: 20px !important;
        margin-bottom: 20px !important;
    }

    /* Checkbox pills wrap nicely */
    .gradio-checkboxgroup {
        padding: 14px 14px !important;
    }
    .gradio-checkboxgroup label {
        font-size: 12px !important;
        padding: 5px 12px !important;
    }

    /* Buttons full width stacked */
    .equal-cols .gr-row {
        flex-direction: column !important;
        gap: 10px !important;
    }
    button.lg.primary,
    button.lg.secondary {
        width: 100% !important;
        text-align: center !important;
        padding: 13px 20px !important;
    }

    /* Triage box */
    .triage-box textarea {
        font-size: 18px !important;
    }

    /* Result blocks */
    .out-block {
        padding: 16px 18px !important;
        border-radius: 12px !important;
    }

    /* Footer */
    .footer {
        font-size: 11.5px !important;
        padding: 24px 16px !important;
        line-height: 1.8 !important;
    }
}

/* Small phone: 480px and below */
@media (max-width: 480px) {

    .hero {
        padding: 32px 16px 28px !important;
    }
    .hero-eyebrow {
        font-size: 9px !important;
        letter-spacing: 1.5px !important;
        padding: 5px 12px !important;
    }
    .hero-title {
        font-size: 24px !important;
        line-height: 1.2 !important;
    }
    .hero-sub {
        font-size: 13px !important;
    }

    .equal-cols {
        padding: 16px 12px 0 !important;
    }
    .card {
        padding: 20px 16px 16px !important;
        border-radius: 14px !important;
    }
    .card-title {
        font-size: 18px !important;
    }
    .card-eyebrow {
        font-size: 9px !important;
    }

    .gradio-checkboxgroup label {
        font-size: 11.5px !important;
        padding: 5px 11px !important;
    }

    /* Slider number input smaller */
    .gradio-slider input[type="number"] {
        width: 48px !important;
        font-size: 12px !important;
    }

    .triage-box textarea {
        font-size: 16px !important;
        padding: 14px 16px !important;
    }

    .out-block {
        padding: 14px 14px !important;
        margin-top: 12px !important;
    }
    .out-block p,
    .out-block li {
        font-size: 13px !important;
    }
}

/* Large desktop: extra breathing room */
@media (min-width: 1200px) {
    .equal-cols {
        padding: 40px 40px 0 !important;
    }
    .hero {
        padding: 72px 6vw 64px !important;
    }
}

/* =============================================
   SMOOTH GPU-ACCELERATED STAGGERED ANIMATIONS
   ============================================= */

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translate3d(0, 22px, 0); }
    to   { opacity: 1; transform: translate3d(0, 0, 0);    }
}
@keyframes fadeSlideDown {
    from { opacity: 0; transform: translate3d(0, -14px, 0); }
    to   { opacity: 1; transform: translate3d(0, 0, 0);     }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* Prepare GPU layers upfront */
.hero, .hero-eyebrow, .hero-title, .hero-rule, .hero-sub,
.equal-cols > div,
.gradio-checkboxgroup, .gradio-slider, .gradio-radio,
button.lg, .triage-box, .out-block, .footer {
    will-change: opacity, transform;
    backface-visibility: hidden;
}

/* Hero — top-down reveal */
.hero         { animation: fadeSlideDown 0.6s  cubic-bezier(0.16,1,0.3,1) 0.05s both; }
.hero-eyebrow { animation: fadeSlideDown 0.5s  cubic-bezier(0.16,1,0.3,1) 0.20s both; }
.hero-title   { animation: fadeSlideDown 0.55s cubic-bezier(0.16,1,0.3,1) 0.32s both; }
.hero-rule    { animation: fadeIn        0.4s  ease                        0.46s both; }
.hero-sub     { animation: fadeSlideDown 0.5s  cubic-bezier(0.16,1,0.3,1) 0.54s both; }

/* Cards */
.equal-cols > div:first-child { animation: fadeSlideUp 0.65s cubic-bezier(0.16,1,0.3,1) 0.60s both; }
.equal-cols > div:last-child  { animation: fadeSlideUp 0.65s cubic-bezier(0.16,1,0.3,1) 0.75s both; }

/* Left card internals */
.gradio-checkboxgroup { animation: fadeSlideUp 0.5s cubic-bezier(0.16,1,0.3,1) 0.90s both; }
.gradio-slider        { animation: fadeSlideUp 0.45s cubic-bezier(0.16,1,0.3,1) 1.02s both; }
.gradio-radio         { animation: fadeSlideUp 0.45s cubic-bezier(0.16,1,0.3,1) 1.14s both; }
button.lg             { animation: fadeSlideUp 0.45s cubic-bezier(0.16,1,0.3,1) 1.24s both; }

/* Right card internals */
.triage-box               { animation: fadeSlideUp 0.5s  cubic-bezier(0.16,1,0.3,1) 0.84s both; }
.out-block:nth-of-type(1) { animation: fadeSlideUp 0.45s cubic-bezier(0.16,1,0.3,1) 0.96s both; }
.out-block:nth-of-type(2) { animation: fadeSlideUp 0.45s cubic-bezier(0.16,1,0.3,1) 1.08s both; }
.out-block:nth-of-type(3) { animation: fadeSlideUp 0.45s cubic-bezier(0.16,1,0.3,1) 1.20s both; }

/* Footer */
.footer { animation: fadeIn 0.5s ease 1.35s both; }

/* Result flash on each diagnosis run */
@keyframes resultPop {
    0%   { opacity: 0; transform: translate3d(0, 18px, 0); }
    100% { opacity: 1; transform: translate3d(0, 0, 0);    }
}
.result-flash {
    animation: resultPop 0.45s cubic-bezier(0.16,1,0.3,1) both !important;
    will-change: opacity, transform !important;
}
"""

with gr.Blocks(
    title="Hospital & Medical Facilities Expert System",
    css=custom_css,
    theme=gr.themes.Base(
        font=gr.themes.GoogleFont("Inter"),
        primary_hue=gr.themes.colors.emerald,
        neutral_hue=gr.themes.colors.slate,
    ),
) as demo:

    # ── Hero ──
    gr.HTML("""
    <div class="hero">
      <div class="hero-inner">
        <div class="hero-eyebrow">
          <svg width="12" height="12" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6l4 2m6-2a10 10 0 1 1-20 0 10 10 0 0 1 20 0z"/>
          </svg>
          Clinical Decision Support System
        </div>
        <h1 class="hero-title">Hospital &amp; Medical Facilities<br>Expert System</h1>
        <div class="hero-rule"></div>
        <p class="hero-sub">
          A rule-based triage assistant for probable condition matching,
          clinical assessment, and personalised care routing.
        </p>
      </div>
    </div>
    """)

    # ── Equal Two-Column Layout ──
    with gr.Row(elem_classes=["equal-cols"], equal_height=False):

        # LEFT — Patient Input
        with gr.Column(scale=1, elem_classes=["card"]):
            gr.HTML("""
            <div class="card-eyebrow">Step 01</div>
            <div class="card-title">Patient Information</div>
            """)

            symptoms = gr.CheckboxGroup(
                label="Observed Symptoms",
                choices=engine.list_symptoms(),
                info="Select all symptoms currently present.",
            )

            age = gr.Slider(1, 100, value=30, step=1, label="Patient Age")
            pain_scale = gr.Slider(0, 10, value=3, step=1, label="Pain Level  (0 = None · 10 = Severe)")

            duration = gr.Radio(
                choices=["< 24 hours", "1-2 days", "3-7 days", "> 1 week"],
                value="1-2 days",
                label="Duration of Symptoms",
            )

            with gr.Row():
                diagnose_btn = gr.Button("Run Expert Diagnosis", variant="primary", size="lg")
                clear_btn = gr.ClearButton(
                    [symptoms, age, pain_scale, duration],
                    value="Clear All",
                    variant="secondary",
                    size="lg",
                )

        # RIGHT — Clinical Results
        with gr.Column(scale=1, elem_classes=["card"]):
            gr.HTML("""
            <div class="card-eyebrow">Step 02</div>
            <div class="card-title">Clinical Results</div>
            """)

            triage = gr.Textbox(
                label="Triage Level",
                placeholder="Run diagnosis to see triage classification",
                lines=1,
                interactive=False,
                elem_classes=["triage-box"],
            )

            diagnosis = gr.Markdown(
                label="Most Probable Conditions",
                value="",
                elem_classes=["out-block"],
            )
            care_plan = gr.Markdown(
                label="Recommended Care Plan",
                value="",
                elem_classes=["out-block"],
            )
            reasoning = gr.Markdown(
                label="Inference Reasoning",
                value="",
                elem_classes=["out-block"],
            )

    gr.HTML("""
    <div class="footer">
        Developed by <strong>SN</strong> &nbsp;·&nbsp;
        For educational &amp; demonstration use only &nbsp;·&nbsp;
        Not a substitute for professional medical advice
    </div>

    <script>
    (function() {
        function flashResults() {
            const targets = document.querySelectorAll('.triage-box, .out-block');
            targets.forEach((el, i) => {
                el.classList.remove('result-flash');
                void el.offsetWidth;
                el.style.animationDelay = (i * 0.13) + 's';
                el.classList.add('result-flash');
            });
        }
        function attachListener() {
            const buttons = document.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.textContent.trim().includes('Run Expert Diagnosis') && !btn._animListened) {
                    btn._animListened = true;
                    btn.addEventListener('click', () => setTimeout(flashResults, 650));
                }
            });
        }
        let tries = 0;
        const iv = setInterval(() => { attachListener(); if (++tries > 20) clearInterval(iv); }, 400);
    })();
    </script>
    """)

    diagnose_btn.click(
        fn=run_expert_system,
        inputs=[symptoms, age, pain_scale, duration],
        outputs=[triage, diagnosis, care_plan, reasoning],
    )

fastapi_app = FastAPI(title="Hospital and Medical Facilities Expert System")
app = gr.mount_gradio_app(fastapi_app, demo, path="/")

if __name__ == "__main__":
    demo.launch()