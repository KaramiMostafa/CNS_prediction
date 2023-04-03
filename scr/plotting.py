import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
import kaleido


class ComparisonPlot:
    """
    A class for creating and saving a comparison plot of actual vs predicted CNS deaths by city using an ARIMA model.
    """

    def __init__(self, data_file_path, image_file_path):
        """
        Initialize a new ComparisonPlot object with the file paths for the data and image files.

        Parameters:
        data_file_path (str): The file path for the CSV data file.
        image_file_path (str): The file path for the output image file.
        """
        self.data_file_path = data_file_path
        self.image_file_path = image_file_path

    def create_plot(self):
        """
        Create a comparison plot of actual vs predicted CNS deaths by city using an ARIMA model.

        Returns:
        fig (plotly.graph_objs._figure.Figure): The Plotly figure object for the comparison plot.
        """
        # Load the data
        data = pd.read_csv(self.data_file_path)

        # Create a Plotly figure
        fig = go.Figure()

        # Add a scatter trace for the actual values with markers at specific values
        fig.add_trace(
            go.Scatter(
                x=data["cities"],
                y=data["actual"],
                mode="lines+markers",
                marker=dict(size=4),
                name="Actual",
            )
        )

        # Add a scatter trace for the predicted values with markers at specific values
        fig.add_trace(
            go.Scatter(
                x=data["cities"],
                y=data["ARIMA"],
                mode="lines+markers",
                marker=dict(size=4),
                name="Predicted",
            )
        )

        # Update the layout with axis labels and title
        fig.update_layout(
            xaxis=dict(title="Cities", tickangle=90, tickfont=dict(size=10)),
            yaxis=dict(title="Number of CNS Deaths", tickfont=dict(size=10)),
            # title=dict(text="Comparison of Actual and Predicted CNS Deaths by City - ARIMA model", font=dict(size=15))
        )

        return fig

    def save_image(self, fig, scale=3):
        """
        Save the given Plotly figure object as a static image with higher resolution.

        Parameters:
        fig (plotly.graph_objs._figure.Figure): The Plotly figure object to save as an image.
        scale (int): The scale factor for the image resolution (default is 3).
        """
        pio.write_image(fig, self.image_file_path, scale=scale)


# Create a new ComparisonPlot object with the file paths for the data and image files
plot = ComparisonPlot(
    data_file_path="comparison.csv", image_file_path="ARIMA_compare_actual_predict.tif"
)

# Create the comparison plot
fig = plot.create_plot()

# Save the plot as a static image with higher resolution
plot.save_image(fig, scale=3)
