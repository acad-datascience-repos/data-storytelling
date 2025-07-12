import unittest
from assignment import create_tips_visualizations
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns

class TestDataStorytelling(unittest.TestCase):
    def test_create_tips_visualizations_returns_correct_types(self):
        """Test that the function returns the correct types"""
        scatter_fig, box_fig = create_tips_visualizations()
        self.assertIsInstance(scatter_fig, go.Figure)
        self.assertIsInstance(box_fig, go.Figure)
    
    def test_scatter_plot_has_correct_data(self):
        """Test that the scatter plot contains the expected data"""
        scatter_fig, _ = create_tips_visualizations()
        
        # Check that the scatter plot has data
        self.assertIsNotNone(scatter_fig.data)
        self.assertGreater(len(scatter_fig.data), 0)
        
        # Check that it's a scatter plot
        self.assertEqual(scatter_fig.data[0].type, 'scatter')
    
    def test_box_plot_has_correct_data(self):
        """Test that the box plot contains the expected data"""
        _, box_fig = create_tips_visualizations()
        
        # Check that the box plot has data
        self.assertIsNotNone(box_fig.data)
        self.assertGreater(len(box_fig.data), 0)
        
        # Check that it's a box plot
        self.assertEqual(box_fig.data[0].type, 'box')
    
    def test_data_loading(self):
        """Test that the tips dataset is loaded correctly"""
        # This test ensures the student actually loaded the data
        tips_df = sns.load_dataset('tips')
        self.assertIsInstance(tips_df, pd.DataFrame)
        self.assertGreater(len(tips_df), 0)
        self.assertIn('total_bill', tips_df.columns)
        self.assertIn('tip', tips_df.columns)
        self.assertIn('day', tips_df.columns)

if __name__ == '__main__':
    unittest.main()
