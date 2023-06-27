import pandas as pd
import os

# Open the medical record file and read it into a dataframe
df = pd.read_excel('C:/Users/86152/Desktop/鼻咽癌病历.xlsx')

# Initialize an empty list to store the formatted sentences
sentences = []

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    # Initialize an empty list to store attribute-value pairs
    attr_val_pairs = []

    # Iterate through each attribute in the row and store the non-NA values in attr_val_pairs
    for attr, val in row.iloc[2:44].items():
        if attr != "时间" and val != "NA" and pd.notna(val):
            attr_val_pairs.append(f"{attr}为{val}")

    # Construct the query sentence by joining the attribute-value pairs with "，"
    query_sentence = "患者" + "，".join(attr_val_pairs) + "，请问应该吃什么药才能康复"

    # Store the query sentence in the sentences list
    sentences.append(query_sentence)

    # Construct the prescription by selecting columns after column AR and filtering for 1 values
    # prescription = "，".join(row.iloc[44:][row.iloc[44:] == 1].index.tolist())
    prescription = "，".join(row.iloc[44:100][row.iloc[44:100] == 1].index.tolist())
    zhenjiu = ""
    if row.iloc[101] != 0:
        zhenjiu = f"切脉针灸{row.iloc[101]}次"
        if row.iloc[100] !=0:
            zhenjiu = f"切脉针灸{row.iloc[100]}个穴位{row.iloc[101]}次"
    later = "，".join(row.iloc[102:][row.iloc[102:] == 1].index.tolist())
    if later != "":
        prescription = prescription + "，" + later
    if zhenjiu != "":
        prescription = prescription + "，" + zhenjiu

    if prescription == "":
        continue



    # Replace # in the target sentence with the prescription
    target_sentence = "\"#。\"".replace("#", prescription)

    # Write the target sentence and query sentence to a file
    with open(os.path.expanduser("~/Desktop/鼻咽癌训练集.txt"), "a") as f:
        final_sentence = f"\"content\"：\"{query_sentence}？\", \"summary\"：{target_sentence}"
        # final_sentence = f"\"context\"：\"{query_sentence}？\", \"summary\"：{target_sentence}"
        f.write(f'{{{final_sentence}}}\n')
        # f.write(f"context: 问题：{query_sentence}？\n回答: {target_sentence}\n")

