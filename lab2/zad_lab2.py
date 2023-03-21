import gradio as gr
import csv


def file_details(file):
    ext = file.split(".")[-1]
    decision_classes = {}
    info = ""
    if ext == "csv":
        with open(file, 'r') as f:
            rows = csv.reader(f)
            header = next(rows, None)
            rows = list(rows)[1:]
        num_lines = len(rows)
        info = f"File contains {num_lines} rows."
        decision_classes = {}
        for row in rows:
            class_name = row[-1]
            if class_name not in decision_classes:
                decision_classes[class_name] = 0
            decision_classes[class_name] += 1
    elif ext == "txt":
        with open(file, 'r') as f:
            rows = f.readlines()
        num_lines = len(rows)
        info = f"File contains {num_lines} rows."
        decision_classes = {}
        for row in rows:
            class_name = row.split()[-1]
            if class_name not in decision_classes:
                decision_classes[class_name] = 0
            decision_classes[class_name] += 1
    return decision_classes, info


def read_text_file(file):
    ext = file.split(".")[-1]
    with open(file, 'r') as file:
        rows = file.readlines()
    if ext == "csv":
        rows = rows[1:]
    return [line.strip() for line in rows]


def display_file_info(file, rows_to_display):
    file = "data/" + file
    decision_classes, file_info = file_details(file)
    response = "Number of decision classes: {}\n".format(len(decision_classes))
    for class_name, class_size in decision_classes.items():
        response += "Size of {}: {}\n".format(class_name, class_size)

    lines = read_text_file(file)
    rows_to_display = int(rows_to_display)
    displayed_lines = "\n".join(lines[:rows_to_display])
    return f"{file_info}\n{response}\nSelected rows:\n{displayed_lines}"


iface = gr.Interface(fn=display_file_info,
                     inputs=[gr.inputs.Textbox(label="Input file name with extension"),
                             gr.inputs.Number(label="Input number of rows to display:")],
                     outputs=gr.outputs.Textbox(label="Result:"),
                     title="AI 2023",
                     description="Simple chatbot for AI classes")
iface.launch()
