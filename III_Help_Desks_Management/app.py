import gradio as gr

from backend import HelpDeskExpertSystem


engine = HelpDeskExpertSystem()


def triage_ticket(issue_type, impact, urgency, vip_user, downtime):
    result = engine.evaluate(issue_type, impact, urgency, vip_user, downtime)
    return result["priority"], result["team"], result["sla"], result["checklist"], result["reasoning"]


with gr.Blocks(title="Help Desk Management Expert System") as demo:
    gr.Markdown("# Help Desk Management Expert System")
    gr.Markdown("Classify tickets, set priority, and route to the correct support team.")

    with gr.Row():
        with gr.Column(scale=1):
            issue_type = gr.Dropdown(
                ["Software", "Hardware", "Network", "Security", "Access"],
                label="Issue Type",
                value="Software",
            )
            impact = gr.Radio(["Low", "Medium", "High"], label="Business Impact", value="Medium")
            urgency = gr.Radio(["Low", "Medium", "High"], label="Urgency", value="Medium")
            vip_user = gr.Radio(["Yes", "No"], label="VIP User", value="No")
            downtime = gr.Radio(["Yes", "No"], label="Service Downtime", value="No")
            run_btn = gr.Button("Evaluate Ticket", variant="primary")

        with gr.Column(scale=1):
            priority = gr.Textbox(label="Priority")
            team = gr.Textbox(label="Assigned Team")
            sla = gr.Textbox(label="SLA")
            checklist = gr.Markdown(label="Action Checklist")
            reasoning = gr.Textbox(label="Inference Reasoning")

    run_btn.click(
        fn=triage_ticket,
        inputs=[issue_type, impact, urgency, vip_user, downtime],
        outputs=[priority, team, sla, checklist, reasoning],
    )

    gr.Markdown("---\nCourtesy of SN")


if __name__ == "__main__":
    demo.launch()
