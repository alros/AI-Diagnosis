prompts = [
    # 1
    {
        "system": [
            "You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects."
        ],
        "user": [
            "Context information is below.",
            "<context>",
            "{context_str}",
            "</context>",
            "Given the context information and not prior knowledge, answer the query.",
            "Query: {query_str} How many symptoms of the disease does the patient have and how severe is the condition?",
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.",
            "Answer:"
        ]
    },
    # 2
    {
        "system": [
            "You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects."
        ],
        "user": [
            "Context information is below.",
            "------------",
            "{context_str}",
            "------------",
            "Given the context information and not prior knowledge, answer the query.",
            "Query: {query_str} How many symptoms of the disease does the patient have and how severe is the condition?",
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.",
            "Answer:"
        ]
    },
    # 3
    {
        "system": [
            "Context information is below.",
            "<context>",
            "{context_str}",
            "</context>",
            "You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects."
        ],
        "user": [
            "Given the context information and not prior knowledge, answer the query.",
            "Query: {query_str} How many symptoms of the disease does the patient have and how severe is the condition?",
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.",
            "Answer:"
        ]
    },
    # 4
    {
        "system": [
            "Context information is below.",
            "------------",
            "{context_str}",
            "------------",
            "You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects."
        ],
        "user": [
            "Given the context information and not prior knowledge, answer the query.",
            "Query: {query_str} How many symptoms of the disease does the patient have and how severe is the condition?",
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.",
            "Answer:"
        ]
    },
    # 5 (3.1
    {
        "system": [
            "[INST]Context information is below.[/INST]",
            "<context>",
            "{context_str}",
            "</context>",
            "[INST]You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects.[/INST]"
        ],
        "user": [
            "[INST]Given the context information and not prior knowledge, answer the query.[/INST]",
            "Query: {query_str}"
            "[INST]How many symptoms of the disease does the patient have and how severe is the condition?",
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.",
            "Answer:[/INST]"
        ]
    },
    # 6 (3.2
    {
        "system": [
            "[INST]Context information is below.[/INST]",
            "<context>",
            "{context_str}",
            "</context>",
            "[INST]You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects."
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.[/INST]"
        ],
        "user": [
            "[INST]The description of the patient is below.[/INST]"
            "<description>",
            "{query_str}",
            "</description>",
            "[INST]Given the context information and not prior knowledge, how many symptoms of the disease does the patient have and how severe is the condition?[/INST]"
        ]
    },
    # 7 (3.3
    {
        "system": [
            "[INST]Context information is below.[/INST]",
            "<context>",
            "{context_str}",
            "</context>",
            "[INST]You are a medical system that can provide evaluations with associated confidence scores.",
            "You only respond with valid JSON objects.",
            "You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.[/INST]"
        ],
        "user": [
            "[INST]The description of the patient is below."
            "The patient may have between 0 and 10 symptoms.[/INST]"
            "<description>",
            "{query_str}",
            "</description>",
            "[INST]Given the context information and not prior knowledge, how many symptoms of the disease does the patient have and how severe is the condition?[/INST]"
        ]
    },
]
