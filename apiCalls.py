

import requests as r


def getMovies() -> list:
    f = open("movies.txt", "r")
    l = f.readlines()
    return l


def getYear(s: str) -> int:
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    l = s.split()
    index = 0

    for i in range(0, len(l)):
        if l[i] in months:
            index = i
    return int(l[index + 2])


def getTitle(s: str) -> str:
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    l = s.split()
    title = ""
    for i in range(0, len(l)):
        if l[i] in months:
            break
        else:
            title += str(l[i] + " ")
    return title


def prepRequest(s: str) -> dict:
    d = {'t': getTitle(s), 'type': 'movie', 'y': getYear(s)}
    return d


def getRuntimesRatings(movies: list) -> list:
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    apiKey = "9d7dfd66&"
    url = "http://www.omdbapi.com/?apikey="
    data = []
    try:
        for i in range(0, len(movies)):
            parameters = prepRequest(str(movies[i]))
            result = r.get(url + apiKey, params=parameters)
            j = result.json()
            runtime = j['Runtime']
            rating = j["Ratings"][0]['Value']
            temp = [runtime, rating]
            data.append(temp)
            #print(runtime, rating, i+1)

    except KeyError:
        print("error")
    return data


def test():
    s = "Star Wars: The Rise of Skywalker Dec 18, 2019 $275,000,000"
    apiKey = "9d7dfd66&"
    url = "http://www.omdbapi.com/?apikey="
    parameters = prepRequest(s)
    result = r.get(url + apiKey, params=parameters)
    j = result.json()
    print(j['Ratings'])
    runtime = j['Runtime']
    rating = j["Ratings"][0]['Value']


def getBudgets(movies: list) -> list:
    budgets = []
    for i in range(0, len(movies)):
        temp = movies[i].split()
        budgets.append(temp.pop())
    return budgets


def main():
    movies = getMovies()
    runtimeAndRatings = getRuntimesRatings(movies)
    budgets = getBudgets(movies)
    with open("data.txt", "w", encoding="utf-8") as f:
        for i in range(0, len(movies)):
            runtime = runtimeAndRatings[i][0].split()[0]
            rating = runtimeAndRatings[i][1].split("/")[0]
            budget = budgets[i].split("$")[1].replace(",", "")
            temp = runtime + " " + budget + " " + rating
            f.write(temp)
            f.write('\n')
            print(runtime, budget, rating)


if __name__ == '__main__':
    main()



