from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        # Entry does not exist
        return render(request, "encyclopedia/error.html", {
            "error_message": "The request entry does not exist."
        })
    else:
        # Entry Exists
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry_content
        })
        

def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    
    # Check is the query matches an entry title
    if util.get_entry(query) is not None:
        return entry(request, query)
    
    # Search for entries containing the query as a substring
    search_results = [entry for entry in entries if query.lower() in entry.lower()]
    
    return render(request, "encyclopedia/search,html", {
        "search_results": search_results,
        "query": query
    })

