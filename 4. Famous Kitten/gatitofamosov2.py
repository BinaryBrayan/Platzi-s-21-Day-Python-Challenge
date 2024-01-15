def find_famous_cat(cats):
    stars=[]
    max_follower=0
    for x in cats:
        suma=0
        for num_follows in x['followers']:
            suma+=num_follows
        if suma>max_follower:
            stars.clear()
            max_follower=suma
            stars.append(x['name'])
        elif suma==max_follower:
            stars.append(x['name'])
        suma=0
    print(stars)




find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300,600]
  },
])