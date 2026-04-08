from pathlib import Path

import gradio as gr
from fastapi import FastAPI
from backend import HospitalExpertSystem
from embedded_css import CUSTOM_CSS

engine = HospitalExpertSystem()

def run_expert_system(symptoms, age, pain_scale, duration):
    result = engine.evaluate(set(symptoms), int(age), int(pain_scale), duration)
    return result["triage"], result["diagnosis"], result["care_plan"], result["reasoning"]

# Read CSS at module load time using __file__ (works on Vercel serverless)
_css_file = Path(__file__).with_name("style.css")
if _css_file.exists():
    custom_css = _css_file.read_text(encoding="utf-8")
    print(f"CSS loaded from: {_css_file} ({len(custom_css)} chars)")
else:
    # Fallback to embedded CSS so serverless packaging cannot break styling.
    custom_css = CUSTOM_CSS
    print(f"WARNING: style.css not found next to app.py; using embedded CSS ({len(custom_css)} chars)")

with gr.Blocks(
    title="Hospital & Medical Facilities Expert System",
    css=custom_css,
    theme=gr.themes.Base(
        font=gr.themes.GoogleFont("Inter"),
        primary_hue=gr.themes.colors.emerald,
        neutral_hue=gr.themes.colors.slate,
    ),
) as demo:

    # -- Hero --
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

    # -- Equal Two-Column Layout --
    with gr.Row(elem_classes=["equal-cols"], equal_height=False):

        # LEFT - Patient Input
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
            pain_scale = gr.Slider(0, 10, value=3, step=1, label="Pain Level  (0 = None - 10 = Severe)")

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

        # RIGHT - Clinical Results
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
        Developed by <strong>SN</strong> &nbsp;-&nbsp;
        For educational &amp; demonstration use only &nbsp;-&nbsp;
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





