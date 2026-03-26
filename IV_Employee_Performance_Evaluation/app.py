import gradio as gr

from backend import EmployeePerformanceExpertSystem


engine = EmployeePerformanceExpertSystem()


def evaluate_employee(productivity, quality, collaboration, attendance, learning):
    result = engine.evaluate(
        int(productivity), int(quality), int(collaboration), int(attendance), int(learning)
    )
    return (
        result["score"],
        result["rating"],
        result["action"],
        result["recommendations"],
        result["reasoning"],
    )


with gr.Blocks(title="Employee Performance Evaluation Expert System") as demo:
    gr.Markdown("# Employee Performance Evaluation Expert System")
    gr.Markdown("Assess employee performance and generate role-aware recommendations.")

    with gr.Row():
        with gr.Column(scale=1):
            productivity = gr.Slider(1, 10, value=7, step=1, label="Productivity")
            quality = gr.Slider(1, 10, value=7, step=1, label="Work Quality")
            collaboration = gr.Slider(1, 10, value=7, step=1, label="Collaboration")
            attendance = gr.Slider(1, 10, value=8, step=1, label="Attendance")
            learning = gr.Slider(1, 10, value=6, step=1, label="Learning Agility")
            run_btn = gr.Button("Evaluate", variant="primary")

        with gr.Column(scale=1):
            score = gr.Textbox(label="Weighted Score")
            rating = gr.Textbox(label="Performance Rating")
            action = gr.Textbox(label="Management Action")
            recommendations = gr.Markdown(label="Recommendations")
            reasoning = gr.Textbox(label="Inference Reasoning")

    run_btn.click(
        fn=evaluate_employee,
        inputs=[productivity, quality, collaboration, attendance, learning],
        outputs=[score, rating, action, recommendations, reasoning],
    )

    gr.Markdown("---\nCourtesy of Premo's SN")


if __name__ == "__main__":
    demo.launch()
