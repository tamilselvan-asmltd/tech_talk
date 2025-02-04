import pandas as pd

# Function to copy data from overwrite.csv to rules.csv
def overwrite_rules():
    # Load data from overwrite.csv
    overwrite_df = pd.read_csv('/Users/tamilselvans/tech_talk/overwrite.csv')
    
    # Write the data to rules.csv, overwriting it
    overwrite_df.to_csv('/Users/tamilselvans/tech_talk/rules.csv', index=False)
    
    print('rules.csv has been successfully overwritten with the data from overwrite.csv.')

# Run the function
if __name__ == "__main__":
    overwrite_rules()
