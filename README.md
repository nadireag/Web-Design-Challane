# Web-Design-Challane

Use HTML, CSS and BOOTSTRAP to create a web page that displays visualizations and the data that is used to create the visualizations.

## Web Visualization Dashboard

Create a visualization dashboard website using climate visualization plots.

Create individual pages for each plot and navigate between them. These pages contain the visualizations and their corresponding explanations.

Landing page that has a comparison of all of the plots, and another page where the data displays as an html table.

### Website Details:

* A [landing page] containing:
  * An explanation of the project.
  * Links to each visualizations page.

* Four [visualization pages] each with:
  * A descriptive title and heading tag.
  * The plot/visualization itself for the selected comparison.
  * A paragraph describing the plot and its significance.

* A ["Comparisons" page] that:
  * Contains all of the visualizations on the same page so we can easily visually compare them.
  * Uses a bootstrap grid for the visualizations.
    * The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.

* A ["Data" page](#data-page) that:
  * Displays a responsive table containing the data used in the visualizations.
    * The table must be a bootstrap table component.
    * The data must come from exporting the `.csv` file as HTML, or converting it to HTML. Try using a tool you already know, pandas. Pandas has a nifty method approprately called `to_html` that allows you to generate a HTML table from a pandas dataframe. See the documentation [here](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.to_html.html)
