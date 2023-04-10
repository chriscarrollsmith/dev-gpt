house_data_task = """
there is a csv file called house-data.csv (it does not currently have any
headers) in the data folder. it contains this dataset of properties sold in
the uk last year with 766k rows.

column_names = ['transaction_id', 'price', 'transfer_date', 'postcode',
'property_type', 'new_build', 'leasehold', 'PAON', 'SAON', 'street',
'locality', 'town_city', 'district', 'county', 'PPD_category', 'record_status']

write a query to find the top 10 most expensive properties in london
"""

flights_task = """
use a public api to get flights currently flying over the maidenhead.

plot this data on a interactive map.

the map should show the planes moving in real time.
"""

house_price = """
Create a project that can help decide where to buy a house in the US.

The app should allow users to optimize for some set of criteria, such as
proximity to public transportation, schools, parks, crime rates, access to
healthcare, and other amenities that are important to home buyers.

The app should gather data about different locales in the US. Use
primarily public databases such as FRED and the US Census.

Here are some tasks that would be useful for the application to perform:

Visualize the data: After you have gathered the data, visualize it on a map
using Mapbox. You can use different data layers to display information such as
house prices, crime rates, and proximity to public transportation.

Analyze the data: find patterns and correlations. For example, you can use
clustering algorithms to group locales with similar characteristics, or
you can use regression models to predict house prices based on different
factors.

Build a recommendation system: You can build a recommendation system that
takes into account the criteria and the data analysis results to suggest
locales that match your preferences. This recommendation system can be
based on machine learning algorithms such as collaborative filtering or
content-based filtering.
"""

crime_map = """
Crime heatmap - Create a crime heatmap using Mapbox and public APIs
such as the Crime Data API. This heatmap can display the frequency and
intensity of crime incidents in a particular area or city. You can also add
features such as filtering by crime type, time period, and demographic
information.
"""

system_message= """
Act as a senior data science developer and provide code in the following
format:

```bash
(required dependencies)
```

```python
(Python code)
```

Upon your output, the code will be executed automatically from a single .py
file. Therefore, the Python code you provide must be self-contained and
immediately usable from main without modification. The .env file contains the
following access tokens that can be loaded with the `dotenv` library:
`OPENAI_API_KEY`, `MAPBOX_API_KEY`, `US_CENSUS_API_KEY`, `FRED_API_KEY`,
`NASA_API_KEY`, and `FBI_CRIMEDATA_API_KEY`. (The key names are
self-explanatory.) Alternatively, you can scrape or automatically download
data, such as GSS, ICPSR, or Roper Center data, from a website and save it to
a file. Or you can use a Python library with built-in data connectivity, such
as yfinance. Code should be generalizable for different inputs, but should be
ready to run for some set of sample inputs. Follow PEP 8 standards and
Pythonic best practices.

Do not specify a file name for the .py file or provide a Bash command to
execute it. This will be handled by the shell you are communicating with. Make
sure to provide code in the specified format, or the code will not run.
"""
