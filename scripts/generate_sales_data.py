"""  
Sales Data Generator Script
Generates realistic sales data for analysis and visualization
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

class SalesDataGenerator:
    def __init__(self, num_records=5000):
        self.num_records = num_records
        self.products = [
            'Laptop', 'Desktop', 'Tablet', 'Smartphone', 'Monitor',
            'Keyboard', 'Mouse', 'Printer', 'Router', 'Webcam',
            'Headphones', 'Speaker', 'USB Drive', 'External HDD', 'SSD'
        ]
        self.regions = ['North', 'South', 'East', 'West']
        self.segments = ['B2B', 'B2C', 'Enterprise']
        self.channels = ['Online', 'Retail Store', 'Distributor']
        
    def generate_date_range(self):
        """Generate random dates between 2022 and 2024"""
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2024, 12, 31)
        dates = []
        
        for _ in range(self.num_records):
            random_days = random.randint(0, (end_date - start_date).days)
            random_date = start_date + timedelta(days=random_days)
            dates.append(random_date)
            
        return dates
    
    def generate_sales_data(self):
        """Generate complete sales dataset"""
        print(f"Generating {self.num_records} sales records...")
        
        # Generate Order IDs
        order_ids = [f'ORD{str(i+10000).zfill(6)}' for i in range(self.num_records)]
        
        # Generate dates
        dates = self.generate_date_range()
        
        # Generate products
        products = np.random.choice(self.products, self.num_records)
        
        # Generate quantities (1-50 units)
        quantities = np.random.randint(1, 51, self.num_records)
        
        # Generate unit prices based on product type
        unit_prices = []
        for product in products:
            if product in ['Laptop', 'Desktop']:
                price = round(np.random.uniform(800, 2000), 2)
            elif product in ['Tablet', 'Smartphone']:
                price = round(np.random.uniform(300, 1200), 2)
            elif product == 'Monitor':
                price = round(np.random.uniform(150, 500), 2)
            else:
                price = round(np.random.uniform(20, 150), 2)
            unit_prices.append(price)
        
        # Calculate total sales
        total_sales = [round(q * p, 2) for q, p in zip(quantities, unit_prices)]
        
        # Generate regions
        regions = np.random.choice(self.regions, self.num_records)
        
        # Generate customer segments
        segments = np.random.choice(self.segments, self.num_records)
        
        # Generate sales channels
        channels = np.random.choice(self.channels, self.num_records)
        
        # Create DataFrame
        df = pd.DataFrame({
            'Order_ID': order_ids,
            'Date': dates,
            'Product': products,
            'Quantity': quantities,
            'Unit_Price': unit_prices,
            'Total_Sales': total_sales,
            'Region': regions,
            'Customer_Segment': segments,
            'Sales_Channel': channels
        })
        
        # Sort by date
        df = df.sort_values('Date').reset_index(drop=True)
        
        # Add some missing values (3% of data)
        missing_indices = np.random.choice(df.index, int(len(df) * 0.032), replace=False)
        df.loc[missing_indices, 'Customer_Segment'] = np.nan
        
        # Add some duplicates
        duplicate_rows = df.sample(n=156)
        df = pd.concat([df, duplicate_rows], ignore_index=True)
        
        print(f"✓ Generated {len(df)} records (including duplicates)")
        print(f"✓ Date range: {df['Date'].min()} to {df['Date'].max()}")
        print(f"✓ Total revenue: ${df['Total_Sales'].sum():,.2f}")
        
        return df
    
    def save_data(self, df, filename='data/raw_sales_data.csv'):
        """Save data to CSV file"""
        df.to_csv(filename, index=False)
        print(f"\n✓ Data saved to {filename}")
        print(f"\nDataset Info:")
        print(df.info())
        print(f"\nSample Data:")
        print(df.head(10))

if __name__ == "__main__":
    # Generate sales data
    generator = SalesDataGenerator(num_records=5000)
    sales_df = generator.generate_sales_data()
    
    # Save to CSV
    generator.save_data(sales_df)
    
    print("\n" + "="*50)
    print("Sales data generation completed successfully!")
    print("="*50)
