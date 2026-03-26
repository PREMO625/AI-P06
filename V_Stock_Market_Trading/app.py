import gradio as gr

from backend import StockTradingExpertSystem


engine = StockTradingExpertSystem()


def analyze_trade(trend, rsi, volume, news_sentiment, risk_profile):
    result = engine.evaluate(trend, int(rsi), volume, news_sentiment, risk_profile)
    return result["signal"], result["confidence"], result["plan"], result["reasoning"], result["disclaimer"]


with gr.Blocks(title="Stock Market Trading Expert System") as demo:
    gr.Markdown("# Stock Market Trading Expert System")
    gr.Markdown("Rule-based trading signal assistant for educational use.")

    with gr.Row():
        with gr.Column(scale=1):
            trend = gr.Radio(["Uptrend", "Sideways", "Downtrend"], label="Market Trend", value="Sideways")
            rsi = gr.Slider(1, 100, value=50, step=1, label="RSI")
            volume = gr.Radio(["Low", "Normal", "High"], label="Volume", value="Normal")
            news_sentiment = gr.Radio(["Positive", "Neutral", "Negative"], label="News Sentiment", value="Neutral")
            risk_profile = gr.Radio(["Conservative", "Balanced", "Aggressive"], label="Risk Profile", value="Balanced")
            run_btn = gr.Button("Generate Signal", variant="primary")

        with gr.Column(scale=1):
            signal = gr.Textbox(label="Signal")
            confidence = gr.Textbox(label="Confidence")
            plan = gr.Markdown(label="Action Plan")
            reasoning = gr.Textbox(label="Inference Reasoning")
            disclaimer = gr.Textbox(label="Disclaimer")

    run_btn.click(
        fn=analyze_trade,
        inputs=[trend, rsi, volume, news_sentiment, risk_profile],
        outputs=[signal, confidence, plan, reasoning, disclaimer],
    )

    gr.Markdown("---\nCourtesy of Premo's SN")


if __name__ == "__main__":
    demo.launch()
