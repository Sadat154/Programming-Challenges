import html
import urllib.request

def read_website(url):
    urlRead = url.read() ### reads html as bytes
    decodeUrl = urlRead.decode("utf-8") # decodes bytes to string
    decodeUrl = html.unescape(decodeUrl) # converts special characters
    url.close() # closes file
    return decodeUrl # returns the file contents

def get_titles(mystr):
    position = mystr.find('<div class="title">') # the index of where the str is
    count = 1

    nameposition = mystr.find('<div class="artist">')
    namecount = 1

    while position > -1 and count <=10: # because you want top 10

        start = mystr.find('>',position+len('<div class="title">')+1) # add one to the start because you dont want the string u only want title
        stop = mystr.find('<',start) # the next < is where title ends

        title = mystr[start+1:stop] # start+1 because you dont want the > from the beginning
        #if "&#39;" in test:
        #    test = test.replace("&#39;", "'")

        #print(f"{count} = {title}")
        position = mystr.find('<div class="title">',stop)
        count += 1





        namestart = mystr.find(">",nameposition+ len('<div class="artist">')+1)
        namestop = mystr.find("<",namestart)

        print(f"{namecount} = {title} [{mystr[namestart+1:namestop]}]")
        namecount += 1
        nameposition = mystr.find('<div class="artist">',namestop)





if __name__ =="__main__":
    fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/") #url
    webString = read_website(fp) # reads and opens url
    get_titles(webString) # scrapes first 10 titles
    #get_song_artist(webString)