
# Customer Query Classification Using Prompt Engineering

## Project Overview
This project classifies e-commerce customer queries
into predefined categories using prompt engineering.

## Categories
1. Delivery
2. Shipping
3. Refund
4. Payment
5. Cancellation
6. Defect
7. Return
8. Account
9. Unknown

## Project Files
- prompt.txt: Classification prompt and instructions.
- test_cases.csv: Test queries and expected outputs.
- README.md: Project documentation.

## How to Test
1. Copy the prompt from prompt.txt.
2. Replace {{customer_query}} with a test query.
3. Submit the prompt to your chosen AI model.
4. Compare the model's response with the expected
   category in test_cases.csv.
5. Verify that the response contains exactly one
   valid category word.

## Expected Output
The output must contain exactly one category:
Delivery, Shipping, Refund, Payment, Cancellation,
Defect, Return, Account, or Unknown.

## Objective
To classify customer queries accurately and
consistently using prompt engineering.
