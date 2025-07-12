import plotly.express as px
import seaborn as sns

def create_tips_visualizations():
  """
  Creates interactive visualizations for the tips dataset.

  This function demonstrates data storytelling by creating two interactive plots:
  1. A scatter plot showing the relationship between total bill and tip
  2. A box plot showing the distribution of total bills by day

  Returns:
    A tuple containing two Plotly figures: (scatter_fig, box_fig).
  """
  # Task 1: Load the tips dataset
  # Hint: Use sns.load_dataset('tips')
  tips_df = None
  # Your code here

  # Task 2: Create an interactive scatter plot
  # Hint: Use px.scatter() with x="total_bill", y="tip", color="day", size="size"
  # Add hover_data=['sex', 'smoker'] for better interactivity
  scatter_fig = None
  # Your code here

  # Task 3: Create an interactive box plot
  # Hint: Use px.box() with x="day", y="total_bill", color="smoker"
  box_fig = None
  # Your code here

  return scatter_fig, box_fig