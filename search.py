import os,sys,time

# SEARCH MENU
search = input("What do you want to search? \n1) Google \n2) Yahoo \n3) Youtube \n4) Twitter \n5) Facebook \n6) Stackoverflow \n7) Github \n8) Tokopedia \n9) Shopee (ID/PH/MY/SG/TH/VN/TW) \n10) ID News \nChoose : ")

# GOOGLE SEARCH
if (search == "1"):
  os.system("clear")
  googlesearch = input("Search : ")
  googlesearch = googlesearch.replace(" ", "+")
  print("Here is your link : https://www.google.com/search?q=" + googlesearch)

# YAHOO SEARCH
elif (search == "2"):
  os.system("clear")
  yahoosearch = input("Search : ")
  yahoosearch = yahoosearch.replace(" ", "+")
  print("Here is your link : https://search.yahoo.com/search?p=" + yahoosearch)

# YOUTUBE SEARCH
elif (search == "3"):
  os.system("clear")
  ytsearch = input("Search : ")
  ytsearch = ytsearch.replace(" ", "+")
  print("Here is your link : https://www.youtube.com/results?sp=mAEA&search_query=" + ytsearch)

# TWITTER SEARCH
elif (search == "4"):
    os.system("clear")
    twtsearch = input("Search : ")
    twtsearch = twtsearch.replace(" ","+")
    print("Here iz your link : https://twitter.com/search?q=" + twtsearch)

# FACEBOOK SEARCH
elif (search == "5"):
    os.system("clear")
    fbsearch = input("Search : ")
    fbsearch = fbsearch.replace(" ","+")
    print("Here is your link : https://facebook.com/search/top/?q=" + fbsearch)

# STACKOVERFLOW SEARCH
elif (search == "6"):
  os.system("clear")
  sofsearch = input("Search : ")
  sofsearch = sofsearch.replace(" ", "+")
  print("Here is your link : https://www.stackoverflow.com/search?q=" + sofsearch)

# GITHUB SEARCH
elif (search == "7"):
    os.system("clear")
    gitsearch = input("Search : ")
    gitsearch = gitsearch.replace(" ","+")
    print("Here is your link : https://github.com/search?q=" + gitsearch)

# TOKOPEDIA SEARCH
elif (search == "8"):
  os.system("clear")
  tokopediasearch = input("Search : ")
  tokopediasearch = tokopediasearch.replace(" ", "+")
  print("Here is your link : https://www.tokopedia.com/search?q=" + tokopediasearch)

# SHOPEE SEARCH
elif (search == "9"):
    os.system("clear")
    shopeesearch = input("1) Shopee Indonesia \n2) Shopee Philippines \n3) Shopee Malaysia \n4) Shopee Singapore \n5) Shopee Thailand \n6) Shopee Vietnam \n7) Shopee Taiwan \nChoose : ")
    
    if (shopeesearch == "1"):
        os.system("clear")
        shidsearch = input("Search : ")
        shidsearch = shidsearch.replace(" ","+")
        print("Here is your link : https://shopee.co.id/search?keyword=" + shidsearch)
        
    elif (shopeesearch == "2"):
        os.system("clear")
        shphsearch = input("Search : ")
        shphsearch = shphsearch.replace(" ","+")
        print("Here is your link : https://shopee.ph/search?keyword=" + shphsearch)
    
    elif (shopeesearch == "3"):
        os.system("clear")
        shmysearch = input("Search : ")
        shmysearch = shmysearch.replace(" ","+")
        print("Here is your link : https://shopee.com.my/search?keyword=" + shmysearch)
        
    elif (shopeesearch == "4"):
        os.system("clear")
        shsgsearch = input("Search : ")
        shsgsearch = shsgsearch.replace(" ","+")
        print("Here is your link : https://shopee.sg/search?keyword=" + shsgsearch)
        
    elif (shopeesearch == "5"):
        os.system("clear")
        shthsearch = input("Search : ")
        shthsearch = shthsearch.replace(" ","+")
        print("Here is your link : https://shopee.th/search?keyword=" + shthsearch)
        
    elif (shopeesearch == "6"):
        os.system("clear")
        shvnsearch = input("Search : ")
        shvnsearch = shvnsearch.replace(" ","+")
        print("Here is your link : https://shopee.vn/search?keyword=" + shvnsearch)
        
    elif (shopeesearch == "7"):
        os.system("clear")
        shtwsearch = input("Search : ")
        shtwsearch = shtwsearch.replace(" ","+")
        print("Here is your link : https://shopee.tw/search?keyword=" + shtwsearch)
        
    else:
        print("Please select 1/2/3/4/5/6/7 !")
        
# ID NEWS SEARCH
elif (search == "10"):
        os.system("clear")
        idnews = input("1) Kompas.com \n2) CnnIndonesia \n3) Liputan6 \n4) Bola.com \n5) Suara \nChoose : ")
        
        if (idnews == "1"):
            os.system("clear")
            kompasnews = input("Search : ")
            kompasnews = kompasnews.replace(" ","+")
            print("Here is your link : https://search.kompas.com/search/?q=" + kompasnews)
            
        elif (idnews == "2"):
            os.system("clear")
            cnnnews = input("Search : ")
            cnnnews = cnnnews.replace(" ","+")
            print("Here is your link : https://www.cnnindonesia.com/search?query=" + cnnnews)
            
        elif (idnews == "3"):
            os.system("clear")
            liputannews = input("Search : ")
            liputannews = liputannews.replace(" ","+")
            print("Here is your link : https://www.liputan6.com/search?q=" + liputannews)
            
        elif (idnews == "4"):
            os.system("clear")
            bolanews = input("Search : ")
            bolanews = bolanews.replace(" ","+")
            print("Here is your link : https://www.bola.com/search?q=" + bolanews)
            
        elif (idnews == "5"):
            os.system("clear")
            suaranews = input("Search : ")
            suaranews = suaranews.replace(" ","+")
            print("Here is your link : https://www.suara.com/search?q=" + suaranews)
            
        else:
            print("Please select 1/2/3/4/5 !")
            
# 
        
# ELSE
else:
    print("Please select 1/2/3/4/5/6/7/8/9 !")