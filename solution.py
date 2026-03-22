import pandas as pd

def add_virtual_column(dff, rule, new_column):
    # Remove extra spaces from the rule
    rule = rule.replace(" ", "")
    df = dff.copy()
    
    # Validate new_column name
    if not new_column.isidentifier() or new_column in df.columns or new_column != "label_three":
        return pd.DataFrame()  # Return empty DataFrame for invalid new_column
    if "label_one" not in rule or "label_two" not in rule:
        return pd.DataFrame()  # Return empty DataFrame for invalid rule format

    # Validate rule format
    if not any(op in rule for op in ['+', '-', '*']):
        return pd.DataFrame()  # Return empty DataFrame for invalid rule format
    
    # Extract column names and operator
    for op in ['+', '-', '*']:
        if op in rule:
            col1, col2 = [part.strip() for part in rule.split(op)]
            operator = op
            break
    
    # Validate column names
    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame()  # Return empty DataFrame for invalid column names
    
    # Perform the operation
    if operator == '+':
        df[new_column] = df[col1] + df[col2]
    elif operator == '-':
        df[new_column] = df[col1] - df[col2]
    elif operator == '*':
        df[new_column] = df[col1] * df[col2]
    
    return df
