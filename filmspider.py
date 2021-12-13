import requests
import time
import random
import re
import bs4

head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
find_url = re.compile(r'<p><a target=\\\"_blank\\\" href=\\\"(.*?)\\\">')
base_url = "http://service.channel.mtime.com/service/search.mcs?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Pages.SearchService&Ajax_CallBackMethod=SearchMovieByCategory&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2Fmovie%2Fsearch%2Fsection%2F%23sortType%3D4%26viewType%3D0%26pageIndex%3D1%26rating%3D2_10&t=20209812434290816&Ajax_CallBackArgument0=&Ajax_CallBackArgument1=0&Ajax_CallBackArgument2=0&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=0&Ajax_CallBackArgument5=0&Ajax_CallBackArgument6=0&Ajax_CallBackArgument7=0&Ajax_CallBackArgument8=&Ajax_CallBackArgument9=0&Ajax_CallBackArgument10=0&Ajax_CallBackArgument11=2&Ajax_CallBackArgument12=10&Ajax_CallBackArgument13=0&Ajax_CallBackArgument14=1&Ajax_CallBackArgument15=0&Ajax_CallBackArgument16=1&Ajax_CallBackArgument17=4&Ajax_CallBackArgument19=0&Ajax_CallBackArgument18="

def main():
    for i in range (1, 60):
        url = base_url + str(i)
        #print("requesting " + url)
        response = requests.get(url, headers=head).text
        urls = re.findall(find_url, response)
        for movie_url in urls:
            print(movie_url)
        time.sleep(3)


if __name__ == "__main__":
    main()
