import gradio as gr
from fastapi import FastAPI

from backend import HospitalExpertSystem


engine = HospitalExpertSystem()


def run_expert_system(symptoms, age, pain_scale, duration):
    result = engine.evaluate(set(symptoms), int(age), int(pain_scale), duration)
    return result["triage"], result["diagnosis"], result["care_plan"], result["reasoning"]


with gr.Blocks(title="Hospital and Medical Facilities Expert System") as demo:
    gr.Markdown("# Hospital and Medical Facilities Expert System")
    gr.Markdown("Rule-based triage assistant for probable condition matching and care routing.")

    with gr.Row():
        with gr.Column(scale=2):
            symptoms = gr.CheckboxGroup(
                label="Select Observed Symptoms",
                choices=engine.list_symptoms(),
                info="Choose all symptoms currently present.",
            )
            age = gr.Slider(1, 100, value=30, step=1, label="Age")
            pain_scale = gr.Slider(0, 10, value=3, step=1, label="Pain Scale (0-10)")
            duration = gr.Radio(
                choices=["< 24 hours", "1-2 days", "3-7 days", "> 1 week"],
                value="1-2 days",
                label="Symptom Duration",
            )

            with gr.Row():
                diagnose_btn = gr.Button("Run Expert Diagnosis", variant="primary")
                clear_btn = gr.ClearButton([symptoms, age, pain_scale, duration])

        with gr.Column(scale=3):
            triage = gr.Textbox(label="Triage Level")
            diagnosis = gr.Markdown(label="Most Probable Conditions")
            care_plan = gr.Markdown(label="Recommended Care Plan")
            reasoning = gr.Markdown(label="Inference Reasoning")

    diagnose_btn.click(
        fn=run_expert_system,
        inputs=[symptoms, age, pain_scale, duration],
        outputs=[triage, diagnosis, care_plan, reasoning],
    )

    gr.Markdown("---\nCourtesy of SN")


fastapi_app = FastAPI(title="Hospital and Medical Facilities Expert System")
app = gr.mount_gradio_app(fastapi_app, demo, path="/")


if __name__ == "__main__":
    demo.launch()
