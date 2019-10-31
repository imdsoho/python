class Rating():
    def __init__(self, rating=3):
        self.rating = rating
        self.recommend = False

    def __set__(self, instance, value):
        if  5 < value < 0:
            raise ValueError("rating must be 0~5")
        else:
            print ("__set__() : {} . {} ".format(instance, value))
            setattr(instance, 'rating', value)

    def __get__(self, instance, owner):
        #print ("__get__()")
        return getattr(instance, 'rating')

    '''def __getattr__(self, item):
        #print("__getattr__()")
        pass

    def __getattribute__(self, item):
        #print("__getattribute__()")
        #print("__getattribute__ : {}".format(item))
        return self.rating

    def __setattr__(self, key, value):
        #print("__setattr__()")
        #print("__setattr__ : {} is {}".format(key, value))
        pass'''

class MovieReview():
    story = Rating()
    print("init : {}".format(id(story)))
    #print("repr : {}".format(dir(story)))
    #print("rating : {}".format(story.rating))
    #print("recommend : {}".format(story.recommend))


movie = MovieReview()
#movie.story = 5
#movie.story.recommend = True

print("instance : {}".format(id(movie)))
#print("instance : {}".format(id(movie.story)))
print("instance : {}".format(type(movie)))
print("instance : {}".format(dir(movie)))
#print("instance : {}".format(dir(movie.story)))
#print("instance : {}".format(type(movie.story)))
#print("rating : {}".format(movie.story.rating))
#print("recommend : {}".format(movie.story.recommend))
