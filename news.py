import click
import requests
API_KEY = 'bcf36c3fd55a48c48e855343e0fe07e4'

@click.group()#this is a decorator
def main():
        """
        NewsAPI is a news application that offers the user 4 sources where she/he is desires to choose any one .
        your choice will returns a list of the top 10 headlines,
        The news headline has a title, description and a url in case the user needs to follow up
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()#this is a decorator

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=bcf36c3fd55a48c48e855343e0fe07e4"

	# fetching data in json format (a way of formatting)
	open_source = requests.get(main_url).json() 

	# getting all articles in a string sources
	source = open_source["sources"] 

	# empty list which will contain all trending newssources 
	results = [] 
	
	for news in source: 
                results.append(news["id"])#adding it to result list
            
   	
	for current_news in results[0:4]:#return the current top four news headlines in our result list (from 0 to 4)
             print(current_news)	


@main.command()#this is a decorator
def topheadlines():
          """ enter your choice from the listsources """
          newsSource = click.prompt("Enter your choice from listsources")#allows you to enter a list of your choice
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=bcf36c3fd55a48c48e855343e0fe07e4sources="+newsSource

	# fetching data in json format 
          open_headline = requests.get(main_url).json()#here we are storing what we get from the main url into the open headline but we are storing it in json format

	# getting all headlines in a string articles 
          headline = open_headline["articles"] 

	# empty list which will contain all trending newssources
	 
          output = [] 
	
          for top_news in headline: 
                click.echo('\n')#meaning a new line
                click.secho(click.style('TITLE: ' + top_news['title'], fg='green'))
                click.secho(click.wrap_text(top_news['description']))
                click.secho(click.style('DOMAIN: ' + top_news['url'], fg='blue'))
           
           	
          for choice in output[:11]:
                print(choice)


if __name__ == '__main__':
      # main()
      print(__name__)