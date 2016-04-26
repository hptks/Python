import movies
import fresh_tomatoes

toy_story=movies.Movie("Toy Story", "A movie about a boy and his toys which come to life.",
                "https://www.google.co.uk/search?q=toy+story+poster&biw=1280&bih=611&tbm=isch&imgil=n-lIBdXUraGumM%253A%253BCDmHEFjlzoEYTM%253Bhttp%25253A%25252F%25252Fdisney.wikia.com%25252Fwiki%25252FFile%25253AToy-story-movie-posters-4.jpg&source=iu&pf=m&fir=n-lIBdXUraGumM%253A%252CCDmHEFjlzoEYTM%252C_&usg=__HyyRYuzh41wbkbc_j51axmTASYA%3D&ved=0ahUKEwiGgf6d1qzMAhVHAsAKHQeSDEQQyjcINA&ei=kpAfV4bwHseEgAaHpLKgBA#imgrc=n-lIBdXUraGumM%3A",
                "https://www.youtube.com/watch?v=4KPTXpQehio")

movies=[toy_story]
fresh_tomatoes.open_movies_page(movies)
