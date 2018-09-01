# Cedato_API_Integration
Project integrates with Cedato's v1 API. It connects to the API and authenticates. Once complete, it uses the returned authorization token to pull down all of the unique supply IDs. Once complete, it pulls demand performance for each supply id, runs the performance through a series of filters using the pandas library, and then unaligns poor performing demand sources that don't pass the filter. 

The project dependencies are:
  - pandas
  - requests
