from django.shortcuts import render
from django.http import HttpResponse

from operator import itemgetter
import requests
import json

# Create your views here.
def navigator(request):
    search_term = request.GET.get('search_term')
    
    sorted_repos = None
    response_error = False

    if search_term is not None:
        
        try:
            # Authenticate with yout Github username and password to increase the limit 
            # of requests per hour you can make from 60 to 5000
            repositories_res = requests.get('https://api.github.com/search/repositories', 
                                            params={'q': search_term},
                                            auth=('felipegalvao', '!Fmg34567'))
            # Uncomment the lines below and comment the ones above to make requests without 
            # authentication
            # repositories_res = requests.get('https://api.github.com/search/repositories', 
            #                                 params={'q': search_term})
            
            # Extract the items from the JSON response and sort them through the creation date
            repositories = json.loads(repositories_res.text)['items']
            sorted_repos = sorted(repositories, key=itemgetter('created_at'), reverse=True)[:5]

            for i, repository in enumerate(sorted_repos):
                try:
                    # Make request to get info about the commits on the repo
                    commits_res = requests.get('https://api.github.com/repos/' + 
                                               repository['owner']['login'] + '/' + 
                                               repository['name'] + '/commits',
                                               auth=('felipegalvao', '!Fmg34567'))

                    # Uncomment the lines below and comment the lines above to make the request 
                    # without authentication
                    # commits_res = requests.get('https://api.github.com/repos/' + 
                    #                            repository['owner']['login'] + '/' + 
                    #                            repository['name'] + '/commits')

                    # Extract SHA, message and author of last commit
                    master_commit_info = json.loads(commits_res.text)[0]
                    sorted_repos[i]['last_commit_sha'] = master_commit_info['sha']
                    sorted_repos[i]['last_commit_message'] = master_commit_info['commit']['message']
                    sorted_repos[i]['last_commit_author'] = master_commit_info['commit']['author']['name']
                except:                    
                    response_error = True
                
        except:        
            response_error = True

    return render(request, 'navigator.html', {'repositories': sorted_repos, 'search_term': search_term, 'response_error': response_error})
    