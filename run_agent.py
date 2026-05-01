#!/usr/bin/env python3
"""Minimal SignalForge opportunity card generator.

This script is intentionally dependency-free. It creates a first-pass opportunity
card for the current GuanWei Career Timing experiment or adjacent ideas.
"""

from __future__ import annotations

import argparse
from textwrap import dedent


def build_card(topic: str, market: str) -> str:
    return dedent(
        f"""
        # Opportunity Card

        ## Topic

        {topic}

        ## Market

        {market}

        ## Signal

        AI-era career uncertainty is a persistent public anxiety. Users are asking whether AI will replace, amplify, or force them to redefine their work.

        ## User Anxiety

        The user does not only want a prediction. They want a structured way to think about strengths, blind spots, timing, and next moves.

        ## Product Hypothesis

        A BaZi-based career timing product can convert this anxiety into a useful reflective experience if it avoids deterministic claims and gives practical career language.

        ## Free Entry

        AI Era BaZi Career Archetype.

        ## Paid Offer

        AI Era Career Timing Report:

        - $9 mini report
        - $39 deep report
        - $99-$149 human-reviewed report

        ## Distribution Test

        Use LinkedIn for credibility, X for founder-led short insights, and Reddit for question discovery.

        ## Success Metrics

        - landing page visit to test start: > 25%
        - test start to completion: > 35%
        - completion to email capture: > 10%
        - completion to paid click: > 5%
        - purchase conversion: > 1%

        ## Decision Rule

        Continue if the test produces real replies, email captures, or paid clicks. Revise if engagement happens but paid intent is weak. Stop or reposition if there is neither interaction nor conversion signal after a focused traffic test.
        """
    ).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default="AI career anxiety")
    parser.add_argument("--market", default="US / English")
    args = parser.parse_args()
    print(build_card(args.topic, args.market))


if __name__ == "__main__":
    main()
