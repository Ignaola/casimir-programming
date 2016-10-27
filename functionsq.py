def make_url(query, n=1):
    """
    this function get a API formated query and
    return the full path query to use as an argument in 
    feedparser
    imputs:
    query: string formated as a API query
    n: integer 
    
    """
    return 'http://export.arxiv.org/api/query?search_query={0}&start={1}&max_results=100'.format(query,n)