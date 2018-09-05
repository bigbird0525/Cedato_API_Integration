# Cedato_API_Integration
Project integrates with Cedato's v1 API. It connects to the API and authenticates with a pre-generated key. Once authenticated, we are able to pull down a variety of performance metrics. After pulling down the performance for the entire network's supply source per each demand ID, the script will unalign poor performing demand IDs via the Cedato API. 

The project dependencies are:
  - pandas
  - requests
