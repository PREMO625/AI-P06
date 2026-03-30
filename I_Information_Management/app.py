import gradio as gr
from fastapi import FastAPI

from backend import InformationManagementExpertSystem


engine = InformationManagementExpertSystem()


def run_assessment(data_type, sensitivity, access_frequency, regulatory_required, criticality):
    result = engine.evaluate(
        data_type=data_type,
        sensitivity=sensitivity,
        access_frequency=access_frequency,
        regulatory_required=regulatory_required,
        business_criticality=criticality,
    )
    return result["classification"], result["summary"], result["actions"], result["reasoning"]


with gr.Blocks(title="Information Management Expert System") as demo:
    gr.Markdown("# Information Management Expert System")
    gr.Markdown("Classify information and get storage, security, retention, and backup guidance.")

    with gr.Row():
        with gr.Column(scale=1):
            data_type = gr.Dropdown(
                ["Operational", "Financial", "Legal", "Employee Records", "Knowledge Base"],
                label="Data Type",
                value="Operational",
            )
            sensitivity = gr.Radio(["Low", "Medium", "High"], label="Sensitivity", value="Medium")
            access_frequency = gr.Radio(
                ["Daily", "Weekly", "Monthly", "Rarely"],
                label="Access Frequency",
                value="Weekly",
            )
            regulatory_required = gr.Radio(["Yes", "No"], label="Regulatory Requirement", value="No")
            criticality = gr.Radio(["Low", "Medium", "High"], label="Business Criticality", value="Medium")
            run_btn = gr.Button("Run Classification", variant="primary")

        with gr.Column(scale=1):
            classification = gr.Textbox(label="Recommended Classification")
            summary = gr.Textbox(label="Policy Summary")
            actions = gr.Markdown(label="Actions")
            reasoning = gr.Textbox(label="Inference Reasoning")

    run_btn.click(
        fn=run_assessment,
        inputs=[data_type, sensitivity, access_frequency, regulatory_required, criticality],
        outputs=[classification, summary, actions, reasoning],
    )

    gr.Markdown("---\nCourtesy of SN")


fastapi_app = FastAPI(title="Information Management Expert System")
app = gr.mount_gradio_app(fastapi_app, demo, path="/")


if __name__ == "__main__":
    demo.launch()
