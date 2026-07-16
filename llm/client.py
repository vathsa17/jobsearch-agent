"""
LLM Client

Responsible for talking to the language model.
"""

import json
import certifi
import httpx

from openai import OpenAI

from config import (
    OPENROUTER_API_KEY,
    OPENROUTER_URL,
    MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
)

from utils.logger import setup_logger

logger = setup_logger()


class LLMClient:

    def __init__(self):

        self.http_client = httpx.Client(
            verify=certifi.where()
        )

        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_URL,
            http_client=self.http_client,
        )

    # ----------------------------------------------------------

    def ask_json(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> dict:

        logger.info("Calling LLM...")

        completion = self.client.chat.completions.create(

            model=MODEL,

            temperature=TEMPERATURE,

            max_tokens=MAX_OUTPUT_TOKENS,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        # ----------------------------
        # OpenRouter returned an error
        # ----------------------------

        if getattr(completion, "error", None):

            raise RuntimeError(
                completion.error["message"]
            )

        if completion.choices is None:

            raise RuntimeError(
                "No choices returned from model."
            )

        result = completion.choices[0].message.content

        if result is None:

            raise RuntimeError(
                "Model returned empty response."
            )

        result = result.strip()

        # ----------------------------
        # Remove markdown
        # ----------------------------

        if result.startswith("```"):

            result = (
                result
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        logger.info("LLM response received.")

        return json.loads(result)