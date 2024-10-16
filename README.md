# Sentence Maker Script

This script takes user input in the form of phrases and formats them as grammatically correct sentences. It capitalizes the first letter of each phrase and adds the appropriate punctuation based on whether the phrase is an interrogative (question) or a regular statement.

## Objective

The primary objective of this script is to create properly formatted sentences from user input. It automatically detects if a phrase is a question (interrogative) or a statement, capitalizes the first letter, and appends either a question mark `?` or a period `.` accordingly. The program continues accepting input until the user types `/end`, at which point it outputs the formatted sentences as a single string.

## Structure

1. **Function: `sentence_maker(phrase)`**
    - This function processes each phrase entered by the user.
    - It checks whether the phrase begins with an interrogative word such as "what," "how," "why," etc.
    - Depending on whether the phrase is a question or a statement, it returns the phrase with the first letter capitalized and appends either `?` for questions or `.` for statements.

2. **List: `sentences`**
    - This empty list is used to store the formatted sentences as they are processed by the `sentence_maker` function.

3. **Loop: `while True`**
    - A continuous loop prompts the user for input.
    - It keeps running until the user inputs the termination command `/end`.
    - Each valid sentence input is processed and added to the `sentences` list.
    - After the loop ends, the script prints all the sentences as a single string, separated by spaces.

## Steps to Run

1. **Step 1:** The script prompts the user to enter a phrase or sentence.
    
2. **Step 2:** The `sentence_maker` function checks if the sentence starts with an interrogative (e.g., "where").
    - If the sentence starts with an interrogative, it is formatted as a question.
    - Otherwise, it is formatted as a statement.
    
3. **Step 3:** The formatted sentence is added to the `sentences` list.

4. **Step 4:** The script continues to prompt for input until the user types `/end`.

5. **Step 5:** Once `/end` is entered, the program exits the loop and prints all the collected sentences as a single output string, separated by spaces.

## How to Use

1. Run the script in a Python environment.
2. Enter sentences one by one.
3. Use the command `/end` to finish input and display the final formatted output.

The script will handle proper capitalization and punctuation automatically based on your input.
