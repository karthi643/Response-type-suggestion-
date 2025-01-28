ML based - Response type suggestion based on question
Approach 1: 
-Google gemini API integration 
It is a Pay-as-you-go (prices in USD) model
Details of payments for model subscription. 
Rate limits : 2,000 RPM (requests per minute)
            : 4 million TPM (tokens per minute)

Prompts up to 128k tokens
Input Pricing : $0.075 / 1 million tokens
output Pricing : $0.30 / 1 million tokens
Context Caching : $0.01875 / 1 million tokens

Prompts longer than 128k
Input Pricing : $0.15 / 1 million tokens
output Pricing : $0.60 / 1 million tokens
Context Caching : $0.0375 / 1 million tokens

Context caching (storage) : $1.00 / 1 million tokens per hour

Tuning price : Input/output prices are the same for tuned models. Tuning service is free of charge.

Grounding with Google Search : $35 / 1K grounding requests (for up to 5K requests per day).
