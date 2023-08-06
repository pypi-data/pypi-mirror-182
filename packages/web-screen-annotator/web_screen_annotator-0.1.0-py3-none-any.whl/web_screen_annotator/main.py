from data_annotator import DataAnnotator


urls = [
        "C:\\Users\\DELL\\Projects\\First Demo\\login.html",
        "https://www.airbnb.com",
        "https://www.booking.com/index.en.html?label=booking-com-flights-english-en-emea-PFec5W0BhAuapBypmW_G0gS228626892855%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-28170420%3Alp9075946%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg;gclid=CjwKCAiAqaWdBhAvEiwAGAQltq26F5tIDYx6aTm5aqJk3zTLc9e0f8enpbU4qjXyEigyytUyaJOzLhoCXckQAvD_BwE;aid=309654;ws=",
        "https://booking.kayak.com/?&sid=8372d02c388c86cc91e6165098f10494&aid=309654&label=booking-com-flights-english-en-emea-PFec5W0BhAuapBypmW_G0gS228626892855%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-28170420%3Alp9075946%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg"
    ]

annotator = DataAnnotator(urls,depth = 5)
annotator.execute(viz=True)

exit(0)