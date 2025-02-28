import requests

#url="https://script.google.com/macros/s/AKfycbxBYdfpngAJDlM43LNkbqNjKpo4hZYDX6HHTkK-WteP-S-psZ9hUGCdxgVHfGUQmVM/exec"
#kosterのサンプルURL＝https://script.google.com/macros/s/AKfycbwENkDKou-SNUiJrTA5RYElSfXGxNjF33h630yyugrxnqn6iBiqJ27aegYRbgqlN2wpFA/exec
#テストURLhttps://script.google.com/macros/s/AKfycbxJS-vFBZBn3ILiWTtYJKiJDvuIE0EBYoRW751F_r_C/dev
def main(url="https://script.google.com/macros/s/AKfycbxBYdfpngAJDlM43LNkbqNjKpo4hZYDX6HHTkK-WteP-S-psZ9hUGCdxgVHfGUQmVM/exec"):

  response=requests.get(url)
  data=response.json()
  data.remove(data[0])
  for row in data:
    print(row)
  return data

if __name__ == "__main__":
    main()