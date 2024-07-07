import json
import sys

# from csv
MODEL = 'model'
RAG_FILE = 'rag file'
PROMPT = 'prompt'
TEMPERATURE = 'temperature'
TEST_ID = 'test id'
SUCCESSFUL = 'successful'
HACK = 'hack'
SYMPTOMS_DETECTED = 'symptoms detected'
SYMPTOMS_EXPECTED = 'symptoms expected'
# INPUT = 'input'
# EXPLANATION = 'explanation'
# derived
ERRORS = 'errors'
FAILURES = 'failures'

line_number = 0
data = {}

with open(sys.argv[1], 'r') as file:
    for line in file:
        line_number += 1
        if line_number == 1:
            continue

        try:
            entry = {
                MODEL: line.split(';')[0],
                RAG_FILE: line.split(';')[1],
                PROMPT: line.split(';')[2],
                TEMPERATURE: line.split(';')[3],
                TEST_ID: line.split(';')[4],
                SUCCESSFUL: line.split(';')[5].lower() == 'true',
                HACK: line.split(';')[6].lower() == 'true',
                SYMPTOMS_DETECTED: int(line.split(';')[7]) if line.split(';')[7] != '' else 0,
                SYMPTOMS_EXPECTED: int(line.split(';')[8]) if line.split(';')[8] != '' else 0,
                # INPUT: line.split(';')[9],
                # EXPLANATION: line.split(';')[10],
            }
        except ValueError:
            print('Error on line', line_number, file=sys.stderr)
            continue

        if entry[MODEL] not in data:
            data[entry[MODEL]] = {}

        if entry[RAG_FILE] not in data[entry[MODEL]]:
            data[entry[MODEL]][entry[RAG_FILE]] = {}

        if entry[PROMPT] not in data[entry[MODEL]][entry[RAG_FILE]]:
            data[entry[MODEL]][entry[RAG_FILE]][entry[PROMPT]] = {}

        if entry[TEMPERATURE] not in data[entry[MODEL]][entry[RAG_FILE]][entry[PROMPT]]:
            data[entry[MODEL]][entry[RAG_FILE]][entry[PROMPT]][entry[TEMPERATURE]] = {}

        if entry[TEST_ID] not in data[entry[MODEL]][entry[RAG_FILE]][entry[PROMPT]][entry[TEMPERATURE]]:
            data[entry[MODEL]][entry[RAG_FILE]][entry[PROMPT]][entry[TEMPERATURE]][entry[TEST_ID]] = {
                SUCCESSFUL: entry[SUCCESSFUL],
                HACK: entry[HACK],
                SYMPTOMS_DETECTED: entry[SYMPTOMS_DETECTED],
                SYMPTOMS_EXPECTED: entry[SYMPTOMS_EXPECTED],
                # INPUT: entry[INPUT],
                # EXPLANATION: entry[EXPLANATION]
            }

summary = {}

for model in data:
    for rag_file in data[model]:
        for prompt in data[model][rag_file]:
            for temperature in data[model][rag_file][prompt]:
                for test_id in data[model][rag_file][prompt][temperature]:
                    key = '@'.join([model, rag_file, prompt, temperature])
                    if key not in summary:
                        summary[key] = {
                            SUCCESSFUL: 0,
                            FAILURES: 0,
                            HACK: 0,
                            ERRORS: 0,
                        }
                    if not data[model][rag_file][prompt][temperature][test_id][SUCCESSFUL]:
                        summary[key][FAILURES] += 1
                    else:
                        summary[key][SUCCESSFUL] += 1
                        summary[key][HACK] += 1 if data[model][rag_file][prompt][temperature][test_id][HACK] else 0
                        summary[key][ERRORS] += abs(
                            data[model][rag_file][prompt][temperature][test_id][SYMPTOMS_DETECTED] -
                            data[model][rag_file][prompt][temperature][test_id][SYMPTOMS_EXPECTED]
                        )

avg_by_model = {}
for key in summary:
    s = summary[key]
    model = key.split("@")[0]
    if model not in avg_by_model:
        avg_by_model[model] = {
            SUCCESSFUL: 0,
            FAILURES: 0,
            HACK: 0,
            ERRORS: 0,
        }
    avg_by_model[model][SUCCESSFUL] += s[SUCCESSFUL]
    avg_by_model[model][FAILURES] += s[FAILURES]
    avg_by_model[model][HACK] += s[HACK]
    avg_by_model[model][ERRORS] += s[ERRORS]

avg_by_model_and_rag = {}
for key in summary:
    s = summary[key]
    model = key.split("@")[0]  # [model, rag_file, prompt, temperature]
    rag_file = key.split("@")[1]
    key2 = '@'.join([model, rag_file])
    if key2 not in avg_by_model_and_rag:
        avg_by_model_and_rag[key2] = {
            SUCCESSFUL: 0,
            FAILURES: 0,
            HACK: 0,
            ERRORS: 0,
        }
    avg_by_model_and_rag[key2][SUCCESSFUL] += s[SUCCESSFUL]
    avg_by_model_and_rag[key2][FAILURES] += s[FAILURES]
    avg_by_model_and_rag[key2][HACK] += s[HACK]
    avg_by_model_and_rag[key2][ERRORS] += s[ERRORS]

avg_by_model_and_temperature = {}
for key in summary:
    s = summary[key]
    model = key.split("@")[0]  # [model, rag_file, prompt, temperature]
    temperature = key.split("@")[3]
    key2 = '@'.join([model, temperature])
    if key2 not in avg_by_model_and_temperature:
        avg_by_model_and_temperature[key2] = {
            SUCCESSFUL: 0,
            FAILURES: 0,
            HACK: 0,
            ERRORS: 0,
        }
    avg_by_model_and_temperature[key2][SUCCESSFUL] += s[SUCCESSFUL]
    avg_by_model_and_temperature[key2][FAILURES] += s[FAILURES]
    avg_by_model_and_temperature[key2][HACK] += s[HACK]
    avg_by_model_and_temperature[key2][ERRORS] += s[ERRORS]

avg_by_model_and_rag_and_prompt = {}
for key in summary:
    s = summary[key]
    model = key.split("@")[0]  # [model, rag_file, prompt, temperature]
    rag_file = key.split("@")[1]
    prompt = key.split("@")[2]
    key3 = '@'.join([model, rag_file, prompt])
    if key3 not in avg_by_model_and_rag_and_prompt:
        avg_by_model_and_rag_and_prompt[key3] = {
            SUCCESSFUL: 0,
            FAILURES: 0,
            HACK: 0,
            ERRORS: 0,
        }
    avg_by_model_and_rag_and_prompt[key3][SUCCESSFUL] += s[SUCCESSFUL]
    avg_by_model_and_rag_and_prompt[key3][FAILURES] += s[FAILURES]
    avg_by_model_and_rag_and_prompt[key3][HACK] += s[HACK]
    avg_by_model_and_rag_and_prompt[key3][ERRORS] += s[ERRORS]

avg_by_temperature = {}
for key in summary:
    s = summary[key]
    temperature = key.split("@")[3]  # [model, rag_file, prompt, temperature]
    if temperature not in avg_by_temperature:
        avg_by_temperature[temperature] = {
            SUCCESSFUL: 0,
            FAILURES: 0,
            HACK: 0,
            ERRORS: 0,
        }
    avg_by_temperature[temperature][SUCCESSFUL] += s[SUCCESSFUL]
    avg_by_temperature[temperature][FAILURES] += s[FAILURES]
    avg_by_temperature[temperature][HACK] += s[HACK]
    avg_by_temperature[temperature][ERRORS] += s[ERRORS]


def print_summary(summary, name):
    print(f'----{name}---')
    print('|key|errors|successes|failures|total|')
    print('|---|---|---|---|---|')
    for key in summary:
        s = summary[key]
        print(f'|{key}|{s[ERRORS]}|{s[SUCCESSFUL]}|{s[FAILURES]}|{s[SUCCESSFUL] + s[FAILURES]}|')
    print('\n')


# print_summary(avg_by_model, 'by model')
# print_summary(avg_by_model_and_rag, 'by model and rag')
# print_summary(avg_by_model_and_rag_and_prompt, 'by model and rag and prompt')
# print_summary(avg_by_model_and_temperature, 'by model and temperature')
# print_summary(avg_by_temperature, 'by temperature')


print('|model|rag file|prompt|temperature|errors|successes|failures|')
print('|---|---|---|---|---|---|---|')
for key in summary:
    s = summary[key]
    model = key.split("@")[0]  # [model, rag_file, prompt, temperature]
    rag_file = key.split("@")[1]
    prompt = key.split("@")[2]
    temperature = key.split("@")[3]
    if (model == 'mistral' or model == 'mistral:7b-instruct-q8_0') and rag_file == 'Dementia':
        print(f'|{model}|{rag_file}|{prompt}|{temperature}|{s[ERRORS]}|{s[SUCCESSFUL]}|{s[FAILURES]}|')
