import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 1. Read the datasets
df_orders = pd.read_csv('Transactions.csv')
df_tickets = pd.read_csv('Customer_Tickets.csv')

# 2. Merge (Join) the two tables on the common OrderID column
df_merged = pd.merge(df_tickets, df_orders, on='OrderID', how='inner')

# 3. Filter data: Focus only on returned Electronics in Spain
problem_area = df_merged[(df_merged['Country'] == 'Spain') & 
                         (df_merged['Category'] == 'Electronics') & 
                         (df_merged['IsReturned'] == 'Yes')]

print(f"Number of analyzed tickets for Spain-Electronics: {len(problem_area)}")

# 4. Text processing function for complaint tagging (NLP Tagging)
def tag_complaint(text):
    text = str(text).lower()
    if any(word in text for word in ['damage', 'broken', 'crush']):
        return 'Packaging & Physical Damage'
    elif any(word in text for word in ['delay', 'late', 'week']):
        return 'Shipping Delay'
    else:
        return 'General / Changed Mind'

# Apply the function to create a Root Cause column
problem_area['Root_Cause'] = problem_area['CustomerComment'].apply(tag_complaint)

# 5. Final Reporting
print("\n--- Root Cause Analysis ---")
print(problem_area['Root_Cause'].value_counts())