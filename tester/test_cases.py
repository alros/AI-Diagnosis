tests = [
    # {
    #     'id': '1',
    #     'expected': '0',
    #     'prompt': 'The patient is a 75-year-old individual.'
    # },
    {
        'id': '2',
        'expected': '1',
        'prompt': 'The patient is a 75-year-old individual experiencing memory difficulties, specifically with recognizing people he has met before.'
    },
    {
        'id': '3',
        'expected': '1',
        'prompt': 'The patient is a 75-year-old individual who is exhibiting signs of memory loss, specifically forgetting recently encountered people, but reports no difficulties with reading or writing.'
    },
    {
        'id': '4',
        'expected': '2',
        'prompt': 'The 75-year-old patient is experiencing age-related cognitive decline, specifically in recognizing people and following complex verbal information.'
    },
    {
        'id': '5',
        'expected': '2',
        'prompt': 'The 75-year-old patient is experiencing age-related cognitive decline, evidenced by difficulty recognizing people and following conversations, but denies issues with reading, writing, or mobility.'
    },
    {
        'id': '6',
        'expected': '3',
        'prompt': 'The 75-year-old patient is experiencing age-related cognitive decline, as evidenced by difficulty recognizing people, following conversations, and navigating unfamiliar environments.'
    },
    {
        'id': '7',
        'expected': '4',
        'prompt': 'The 75-year-old patient is experiencing age-related cognitive decline, particularly in recognizing people and following complex conversations, as well as occasional memory lapses and disorientation.'
    },
]