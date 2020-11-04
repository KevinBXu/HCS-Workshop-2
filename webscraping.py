import requests
from bs4 import BeautifulSoup

shows = {}

for num in range(0,17000,50):
    url = "https://myanimelist.net/topanime.php?type=bypopularity&limit=" + str(num)

    page = requests.get(url)

    print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')

    animes = soup.find_all(class_='detail')

    for anime in animes:
        title = anime.find(class_='anime_ranking_h3').find('a').get_text()
        members = int(anime.find(class_='information').get_text().split('\n')[3].strip().split()[0].replace(',',''))
        shows[title] = members

with open("anime.html","w", encoding="utf-8") as file:
    html_template = """
<!DOCTYPE html>

<html lang="en">
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
        <link href="styles.css" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <script>
          // Searches for the anime
          function searchAnimes()
          {
            list = document.querySelectorAll("li.list-group-item");
            search = document.getElementById("search").value.toLowerCase();
            for (let element of list)
            {
              // search() returns -1 if the search is not a substring
              if (element.innerHTML.toLowerCase().search(search) != -1)
              {
                element.hidden = false;
              }
              else
              {
                element.hidden = true;
              }
            }
          }
        </script>
        <title>Projects</title>
    </head>
    <body>
        <h1>Animes</h1>
        <form>
          <input autocomplete="off" autofocus id="search" placeholder="Search" type="text">
          <input type="submit" onclick="searchAnimes(); return false;">
        </form>
        <ul class="list-group list-group-flush">
    """
    file.write(html_template)
    
    for name in shows:
        line = f"""
            <li class=\"list-group-item\">{name}: {shows[name]} members</li>
        """
        file.write(line)
    file.write("""
        </ul>
    </body>
</html>
    """)

    




