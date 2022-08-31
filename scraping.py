import requests
from bs4 import BeautifulSoup

oyo_url="https://www.oyorooms.com/search/?checkin=31%2F08%2F2022&checkout=01%2F09%2F2022&city=Bangalore&filters%5Bcity_id%5D=4&filters%5Broom_pricing%5D%5Bmax%5D=1409&filters%5Broom_pricing%5D%5Bmin%5D=410&guests=2&location=Bangalore%2C+Karnataka%2C+India&roomConfig%5B%5D=2&rooms=1&searchType=city "
req=requests.get(oyo_url)
content=req.content
soup=BeautifulSoup(content, "html.parser")
all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
for hotel in all_hotels:
    hotel_name=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
    hotel_address=hotel.find("span",{"itemprop":"streetAddress"}).text
    print(hotel_name,hotel_address)
    
