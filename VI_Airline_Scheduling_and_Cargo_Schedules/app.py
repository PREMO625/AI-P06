import gradio as gr

from backend import AirlineSchedulingExpertSystem


engine = AirlineSchedulingExpertSystem()


def plan_operation(weather, aircraft_status, crew_availability, cargo_priority, airport_congestion):
    result = engine.evaluate(
        weather, aircraft_status, crew_availability, cargo_priority, airport_congestion
    )
    return result["risk"], result["decision"], result["checklist"], result["reasoning"]


with gr.Blocks(title="Airline Scheduling and Cargo Expert System") as demo:
    gr.Markdown("# Airline Scheduling and Cargo Expert System")
    gr.Markdown("Support decisions for flight scheduling and cargo handling under constraints.")

    with gr.Row():
        with gr.Column(scale=1):
            weather = gr.Radio(["Clear", "Moderate", "Severe"], label="Weather", value="Clear")
            aircraft_status = gr.Radio(
                ["On Time", "Minor Delay", "Technical Issue"],
                label="Aircraft Status",
                value="On Time",
            )
            crew_availability = gr.Radio(["High", "Medium", "Low"], label="Crew Availability", value="High")
            cargo_priority = gr.Radio(["Standard", "Priority", "Critical"], label="Cargo Priority", value="Standard")
            airport_congestion = gr.Radio(["Low", "Medium", "High"], label="Airport Congestion", value="Low")
            run_btn = gr.Button("Evaluate Schedule", variant="primary")

        with gr.Column(scale=1):
            risk = gr.Textbox(label="Operational Risk")
            decision = gr.Textbox(label="Schedule Decision")
            checklist = gr.Markdown(label="Action Checklist")
            reasoning = gr.Textbox(label="Inference Reasoning")

    run_btn.click(
        fn=plan_operation,
        inputs=[weather, aircraft_status, crew_availability, cargo_priority, airport_congestion],
        outputs=[risk, decision, checklist, reasoning],
    )

    gr.Markdown("---\nCourtesy of Premo's SN")


if __name__ == "__main__":
    demo.launch()
