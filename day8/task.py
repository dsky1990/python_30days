import requests
import json
class SimpleCrawler:
  def crawl(self, params=None):
    url = "https://follow-api-ms.juejin.im/v1/getUserFolloweeList"
    params = {
      "uid": "59a7a5a96fb9a02487554b86",
      "currentUid": "5786ea76d342d3005894f33c",
      "src": "web"
    }
    headers = {
      "Host": "follow-api-ms.juejin.im",
      "Origin": "https://juejin.im",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    }
    response = requests.get(url, headers=headers, params=params)
    context = []
    print("get url: ", response.url)
    # print("response data: ", response.json())
    for follower in response.json().get("d"):
      print(follower["followee"]["username"])
      context.append({
        "objectId": follower["followee"]["objectId"],
        "username": follower["followee"]["username"]
      })
    with open("user.json", "w") as f:
      json.dump(context, f)
if __name__ == "__main__":
  SimpleCrawler().crawl()
