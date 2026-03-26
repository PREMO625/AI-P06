from typing import Dict, List


class StockTradingExpertSystem:
    """Rule-based stock market trading advisor (educational)."""

    def evaluate(
        self,
        trend: str,
        rsi: int,
        volume: str,
        news_sentiment: str,
        risk_profile: str,
    ) -> Dict[str, str]:
        bullish = 0
        bearish = 0

        if trend == "Uptrend":
            bullish += 3
        elif trend == "Downtrend":
            bearish += 3

        if rsi < 30:
            bullish += 2
        elif rsi > 70:
            bearish += 2

        if volume == "High":
            bullish += 1
            bearish += 1

        if news_sentiment == "Positive":
            bullish += 2
        elif news_sentiment == "Negative":
            bearish += 2

        if bullish - bearish >= 3:
            base_signal = "BUY"
        elif bearish - bullish >= 3:
            base_signal = "SELL"
        else:
            base_signal = "HOLD"

        if risk_profile == "Conservative" and base_signal == "BUY":
            final_signal = "ACCUMULATE (Small Position)"
        elif risk_profile == "Conservative" and base_signal == "SELL":
            final_signal = "REDUCE EXPOSURE"
        else:
            final_signal = base_signal

        steps: List[str] = [
            f"Base signal: {base_signal}",
            f"Risk-adjusted signal: {final_signal}",
            "Use stop-loss and position sizing discipline.",
            "Re-evaluate if macro/news context changes.",
        ]

        if base_signal == "BUY":
            steps.append("Consider staged entry rather than all-at-once buying.")
        elif base_signal == "SELL":
            steps.append("Protect capital and avoid averaging into weakness.")
        else:
            steps.append("Wait for confirmation before entering new trades.")

        confidence = min(95, 50 + abs(bullish - bearish) * 10)

        reasoning = (
            f"Indicators -> Trend: {trend}, RSI: {rsi}, Volume: {volume}, "
            f"News: {news_sentiment}, Risk: {risk_profile}."
        )

        return {
            "signal": final_signal,
            "confidence": f"{confidence}%",
            "plan": "\n".join(f"- {step}" for step in steps),
            "reasoning": reasoning,
            "disclaimer": "Educational output only. Not financial advice.",
        }
