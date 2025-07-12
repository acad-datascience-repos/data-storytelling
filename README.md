# Data Storytelling with Plotly Assignment

## Problem Description

In this assignment, you will use the Plotly library to create two interactive visualizations to explore the "tips" dataset. This will help you practice communicating insights from data through effective data storytelling.

## Learning Objectives

By completing this assignment, you will learn:
- How to create interactive visualizations using Plotly Express
- How to tell stories with data through effective plotting
- How to use different plot types (scatter plots, box plots) for data exploration
- How to add interactive elements like hover data and color coding
- Best practices for data visualization and storytelling

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas
   - seaborn
   - plotly
   - numpy

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `create_tips_visualizations()`.
3. Your tasks are to:
   *   **Task 1**: Load the "tips" dataset from the seaborn library.
   *   **Task 2**: Create an interactive scatter plot of `total_bill` vs `tip`. The color of the points should represent the `day` and the size of the points should represent the `size` of the party.
   *   **Task 3**: Create an interactive box plot showing the distribution of `total_bill` for each `day`.
   *   The function should return both Plotly figure objects as a tuple: `(scatter_fig, box_fig)`.

## Hints

*   Use `seaborn.load_dataset('tips')`.
*   Use `plotly.express` for both plots.
*   For the scatter plot, use `px.scatter` and set the `x`, `y`, `color`, and `size` parameters.
*   For the box plot, use `px.box` to show the distribution of a numerical variable across different categories.
*   Add `hover_data=['sex', 'smoker']` to the scatter plot for better interactivity.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That your function returns the correct types (Plotly Figure objects)
- That both plots contain the expected data
- That the plots are of the correct types (scatter and box)
- That the dataset is loaded correctly

## Expected Output

Your function should return a tuple containing two Plotly Figure objects:
- `scatter_fig`: An interactive scatter plot showing total_bill vs tip
- `box_fig`: An interactive box plot showing total_bill distribution by day

## Further Exploration (Optional)

*   How would you add a title to your plots? (Hint: `fig.update_layout(title_text=...)`)
*   Can you create a third plot, like a violin plot (`px.violin`), to show the relationship between `day` and `tip`?
*   Look into creating subplots with Plotly to display both of your charts in a single figure.
*   How would you customize the color scheme of your plots?
*   Can you add annotations to highlight interesting patterns in your data?

## Resources

- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [Seaborn Datasets](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [Data Storytelling Best Practices](https://www.storytellingwithdata.com/)