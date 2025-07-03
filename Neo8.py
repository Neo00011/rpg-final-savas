import os
import time
import random

enemys={"Haydut":{"can":50,"güç":10,"ödül":20},"Troll":{"can":30,"güç":10,"ödül":20},"Kara Büyücü":{"can":50,"güç":35,"ödül":50},
"Arzathor":{"can":100,"güç":40,"ödül":1000}}

karakter={}



def exit():
    karar=print("Tekrar oynamak ister misiniz? (e/h): ")
    while True:
        if karar=="e":
            giris()
        elif karar=="h":
            break
        else:
            continue

def karar():
    while True:
        onay=input("Kararınızı değiştirmek ister misiniz ?(e\h):")
        if onay=="e":
            return True
        elif onay=="h":
            return False
        else:
            continue





def cesme():
    print()
    print("Duyduklarına göre çeşmeler iyileştirici etkisinin yanında\n" \
    "zehirli olanlarıda varmış.")
    while True:
        karar=input("İçmek istiyor musun?(e\h): ")
        print()
        if karar =="e":
            water=random.randint(0,1)
            if water==0:
                print("Suyu içiyorsun...İçtikten sonra başın dönmeye başladı ve\n" \
                "bu suyun zehirli olduğunu anlıyorsun.(-30 can)")
                karakter["can"]-=30
                time.sleep(3)
                if karakter["can"]==0:
                    print("Öldün... Buraya kadar.")
                return
            elif water==1:
                print("Suyu içiyorsun...Kendini iyi hissetmeye başlıyorsun ve enerjin yerine\n" \
                "geliyor(+30 can)")
                karakter["can"]+=30
                if karakter["can"]>karakter["max"]:
                    karakter["can"]=karakter["max"]
                return
        elif karar =="h":
            print("İçine bir his doğdu ve suyu içmedin.Yoluna devam et",karakter["isim"])
            return
        else:
            continue        
    



def savas(dusman):
    print(f"Karşına bir {dusman} çıktı.",enemys[dusman])
    print("Senin durumun :  Can:",karakter["can"],"Güç:",karakter["güç"])
    
    if not karakter["final"]:
        while True:
            karar=input("Savaş yada kaç.(S\K),(Kaçarsan,-20 can): ").lower()
            if karar=="s":
                print("Seçimini yaptın.")
                break
            elif karar=="k":
                print("Kaçmaya karar verdin.")
                karakter["can"]-=30
                return

    time.sleep(2)
    if karakter["türü"]=="Savaşçı":
        print(f"Kılıcını çekip korkusuzca {dusman} üstüne yürüyorsun!")
    elif karakter["türü"]=="Okçu":
        print(f"Çocukluğundan belli yoldaşın olan o yayınla {dusman} üstüne gidiyorsun!")
    elif karakter["türü"]=="Büyücü":
        print("Ustan tarafından verilen asayı çeşitli büyülerle kızdırıyorsun ve onu bir yıldırım asasına dönüştürüyorsun",karakter["isim"],".")
    print("İlk saldırıya geçiyorsun...")
    print()
    time.sleep(3)                                                               #WAR
    karaktercanı=karakter["can"]
    dusmancanı=enemys[dusman]["can"]
    while karaktercanı and dusmancanı>0:
        time.sleep(2)
        hasar1=random.randint(karakter["güç"]-5,karakter["güç"]+5)
        hasar2=random.randint(enemys[dusman]["güç"]-5,enemys[dusman]["güç"]+5)
        print()
        print("Saldırını yapıyorsun...")
        time.sleep(2)
        print(f"Saldırını yaptın ve düşmana ve {hasar1} hasar verdin.")
        time.sleep(2)
        dusmancanı-=hasar1
        
        if dusmancanı <=0:
            print()
            print(f"Savaşı kazandın {karakter["isim"]},yoluna devam edebilirsin.")
            karakter["para"]+=enemys[dusman]["ödül"]
            print("Düşmandan",enemys[dusman]["ödül"],"altın kazandın." )
            return
        print()
        print(f"{dusman} saldırıya geçiyor!")
        time.sleep(2)
        time.sleep(2)
        print(F"{dusman} saldırısını yaptı ve sana {hasar2} hasar verdi.")
        karaktercanı-=hasar2
        karakter["can"]-=hasar2
        if karaktercanı<=0:
            print()
            print("Öldün...Buraya kadar.")
            exit()
            


def enter_scene():
    os.system("cls")
    time.sleep(3)
    print("Ormanın derinliklerinde uyanıyorsun...")
    print()
    time.sleep(2)
    print("Aniden bir ses duydun.")
    time.sleep(2)
    savas("Troll")
    print()
    print(f"Can: {karakter["can"]} Para: {karakter["para"]}")
    



def sisli_bataklik():
    time.sleep(2)
    print("Bir kahraman gibi ilerliyorsun",karakter["isim"])
    print()
    time.sleep(3)
    print("Şimdi sisli bir bataklığa geldin.Ayakların çamura saplanıyor.\n" \
    "Zorlanıyorsun ama bir yolunu buluyorsun.Biraz yürüdükten sonra \n" \
    "karşıda bir çeşme görüyorsun.Susamış ve bitkinsin.")
    time.sleep(4)
    cesme()
    print(f"Can: {karakter["can"]} Para: {karakter["para"]}")
    time.sleep(3)
    print("\nÇeşmeyi geçtikten bir süre yürüdükten sonra,biraz ileride yol ayrılıyor.\n" \
    "Sağ taraf orman yoluna devam ediyor,sol taraf ise küçük bir kasabaya gidiyor.")
    
    
    while True:
        yon=input(f"\nNe tarafa gitmek istersin {karakter["isim"]}?,(Sağ/Sol): ").lower()
        if yon=="sağ":
            print("Orman yoluna devam ederek macera peşindesin...")
            time.sleep(3)
            karakter["köy"]=False
            ormanyolu()
        
        elif yon=="sol":
            print("Kasaba yoluna girerek o yolda ilerliyorsun...")
            time.sleep(3)
            karakter["köy"]=True
            kasaba()
        else: continue


def kasaba():
    time.sleep(2)
    print("Kasaba girişinde bir haydutun köylü kadını yağmaladığını görüyorsun.")
    time.sleep(3)
    
    while True:
        print("1-Karışma\n" \
    "2-Köylü kadına yardım et")
        yardım=input("Kararın (1,2):")
        if yardım=="1":
            print("Haydutu görmezden gelip kasabanın merkezine doğru yürümeye devam ediyorsun.")
            karakter["yardım"]=False
            break
        
        if yardım=="2":
            time.sleep(4)
            print("Güçlü ve heybetli bir sesle'BIRAK O KADINI'diye bağırıyorsun.\n" \
            "Haydut bunu bir tehdit olarak algılayarak sana meydan okuyor.Kılıçlar çekildi ve savaşacaksınız!")
            savas("Haydut")
            print()
            time.sleep(4)
            print("Köylü kadın sana,hayatını kurtardığı için minnet duyuyuor.")
            karakter["yardım"]=True
            break
        else:
            continue
    time.sleep(5)
    print("Kısa bir yürüyüşten sonra köyün merkezine ulaşıyorsun.\n" \
    "Kendini yorgun hissediyorsun ve kararmış bir havada hana gidip dinlenip yemek yemek fena olmazdı.")
    time.sleep(5)
    print("Hana giriyorsun ve bir yahni bir kadeh şarap istiyorsun.")
    time.sleep(5)
    print("Hancıyla konuşup bu gece orada kalıyorsun.")
    time.sleep(5)
    print(f"Canın Doldu.")
    karakter["can"]=karakter["max"]
    print("Uyandıktan sonra hemen yola koyulmak için hazırlanıyorsun.\n" \
    "Hesabı ödemek için hancının yanına gidiyorsun.")
    print()
    time.sleep(5)
    print("Hancıya hesabın kaç altın tuttuğunu sorduğunda;")
    time.sleep(3)
    if karakter["yardım"]:
        print("Hancı:Senden ücret alamam evlat.Sen benim kızımı o alçak haydutlardan kurtarmışsın.\n" \
        "Ne zaman istersen gelip burada kalabilirsin.")
        time.sleep(3)
        print("Ne kadar ısrar etsende parayı almayan hancıyla vedalaşıp yoluna koyuluyorsun.")
        shop()
    if not karakter["yardım"]:
        print("Hancı: Borcunuz 30 altın.")
        if karakter["para"]<30:
            print("Yeterli altının yok ne yapıcaksın?" \
            "1-Parayı ödemeden kaç" \
            "2-Hancıya paranın karşılığı için ondan görev talep et")
            karar=input("Kararın(1,2): ")
            while True:
                if karar=="1":
                    print("Hancının dikkatinin dağıldığı anda koşturmaya başlıyorsun." \
                    "Hancıda bir süre seni kovalıyor ama biraz yaşlı olduğu için yetişemiyor.")
                    karakter["kötülük"]=True
                    break
                elif karar=="2":
                    print("Hancıdan iş talep edip borcunu kapatmak istiyorsun.")
                    time.sleep(3)
                    print("Hancı bu teklifi kabul edip bir günlüğüne hanın işlerini yapıyorsun")
                    time.sleep(3)
                    print("Nihayet işlerin bittiğinde yoluna koyuluyorsun.")
                    break
        print("Hancıya parasını altınını ödeyip devam ediyorsun...")
        shop()
def shop():
    while True:
        print("Köy merkezinden geçerken bir mağazaya uğruyorsun.")
        print("1-Şovalye kılıcı(+5 güç)(30 altın)\n" \
        "2-Kuvvet karışımı(+7 güç),(40 altın)\n" \
        "3-Sağaltıcı iksir(+10 can,30 altın")
        al=input("Hangisini alırsın kahraman? (0=hiçbiri,1,2,3):")
        if al=="1":
            if karakter["para"]<50:
                print("Yeterli altının yok.")
            else:
                print("Şovalye kılıcını aldın.(+5 güç,-50 altın)")
                karakter["para"]-=50
                karakter["güç"]+=5
                
        elif al=="2":
            if karakter["para"]<60:
                print("Yeterli altının yok.")    
            else:
                print("Kuvvet karışımını aldın.(+7 güç,-60 altın)")
                karakter["para"]-=60
                karakter["güç"]+=7
            
        elif al=="3":
            if karakter["para"]<40:
                print("Yeterli altının yok.")
            else:
                print("Sağaltıcı iksirini aldın.(+10 can,-40 altın)")
                karakter["para"]-=40
                karakter["can"]+=10
                if karakter["can"]>karakter["max"]:
                    karakter["can"]=karakter[max]
            
        
        elif al=="0":
            break
        else:
            continue
    print("Mağazadan çıkıyorsun")
    time.sleep(4)
    koy_yaslısı()

def koy_yaslısı():
    print("Uzaktan gördüğün kasabanın yaşlısının yanına geliyorsun." \
    "'Köyün durumu nasıl?'diye soruyorsun.\n" \
    "Köyün yaşlısı: Kasabamızı bazı büyücüler çok zarar vermekte evladım." \
    "Bu yüzden köyün durumu son zamanlarda pek iyi değil.Sen güçlü kuvvetli birisine benziyorsun." \
    "Bizim için onları halledersen karşılığında 300 altın veririz.")
    time.sleep(7)
    
    while True:
        
        karar=input("Kararın (e/h):")
        if karar=="e":
            print("Teklifi kabul edip düşmanların üstesinden gelmek için hazırlanıyorsun.")
            gorev()
        elif karar=="h":
            print("Teklifi reddedip tekrar ormana doğru yola çıkıyorsun.")
            ormanyolu()


        else:
            continue

def ormanyolu():
    print("Orman yolunda devam ediyorsun...")
    time.sleep(4)
    if karakter["köy"]:
        print("Günlerce yürüyorsun...Yorgun ve bitkin bir haldesin...Dinlenmek için bir mağaraya sığınıyorsun.\n"
        "Mağarada yorgunluktan bir süre uyuya kalıyorsun...Uykudayken bir süre sonra etrafını büyücüler sarmış bir şekilden\n"
        "uyanıyorsun.Başka seçeneğin yok ve 5 büyücü ile savaşmak zorundasın...")
        savas("Kara Büyücü")
        savas("Kara Büyücü")
        savas("Kara Büyücü")
        savas("Kara Büyücü")
        savas("Kara Büyücü")
        



    if not karakter["köy"]:
        print("Bir süre yürüdükten sonra karşına aniden 10 kişilik bir Troll sürüsü çıkıyor.")
        print("1-Kasabaya kaç")
        print("2-Korkusuzca dövüş.")
        karar=input("Kararın (1,2): ")
        while True:
            if karar=="1":
                print("Telaşla kasabaya gitmek zorunda kalıyorsun...")
                time.sleep(3)
                kasaba()
            elif karar=="2":
                print("10 tane trolle karşı teksin ve savaşmaya gidiyorsun...")
                savas("Troll")
                savas("Troll")
                savas("Troll")
                savas("Troll")
                savas("Troll")
                savas("Troll")
                savas("Troll")
                savas("Troll")
                savas("Troll")
            else:
                continue





def gorev():
    os.system("cls")
    print()
    time.sleep(3)
    print("Yaşlının söylediğine göre kasaba girişinin yakınlarında bir mağara varmış." \
    "Kara büyücüler burada çeşitli büyüler yapıp kasaba halkına satar yada onlara zarar verirmiş.")
    karabuyuculer()

def karabuyuculer():
    karakter["final"]=True
    print()
    os.system("cls")
    print("Kararını vererek Kara Büyücülerin inlerine doğru yola çıktın...")
    time.sleep(4)
    print("Hava kararmaya başladı ve hafiften üreperiyorsun...")
    time.sleep(4)
    print("Sessiz sessiz yürürken mağara yakınlarında anlamadığın garip garip sözler söyleyen bir adam görüyorsun." \
    "Bir süre adamı izledikten sonra bunun bir büyücü olduğunu anladın.")
    print()
    time.sleep(4)
    print("Büyücünün karşısına aniden çıkarak 'hepinizi öldürmeye geldim,artık kaçışınız yok'dedin ve " \
    "büyücü pis pis gülerek bu meydan okumaya karşılık vermek için hazırlandı...")
    time.sleep(4)
    savas("Kara Büyücü")
    time.sleep(3)
    print("Büyücü yerde son nefesini verecekken son gücüyle fısıldıyarak;")
    time.sleep(4)
    print("'Arzathonn...'dedi")
    time.sleep(4)
    print("Bu isimi ilk defa duymana rağmen kalbine bir ürperti geldi.")
    time.sleep(3)
    print("\nÖnemli bir kişi olduğunu sezdin ve bu ismi köyün yaşlısıyla konuşmaya gittin.")
    time.sleep(4)
    print("\nKasaba yaşlısına telaşlı bir şekilde gelerek 'İhtiyar... öldürdüğüm bir büyücü Arzathor'un adını söyledi... onu dahaönce duydun mu?' dedin." \
    "Kasaba yaşlısı kısık bir sesle;")
    time.sleep(4)
    print()
    print("O ismi...uzun zamandır duymamıştım.Bir zamanlar kardeşim gibiydi.Aynı ustanın elinde büyümüş," \
    "aynı yeminleri etmiştik")
    time.sleep(3)
    print("Sen şaşkınlıkla 'Onu tanıyor musun?' dedin.")
    time.sleep(4)
    print("Kasabanın yaşlısı ayağa kalkarak 'Hayır...onu artık tanımıyorum...Arzathor güce açtı." \
    "Kara büyüyü yasak olmasına rağmen kullandı...Onu defalarca yolundan döndürmeye çalıştım,ama olmadı.")
    time.sleep(5)
    print("Derin bir sessizlik olur ve kasabanın yaşlısı yavaşça sana bakarak," \
    "'Ve sen...sende onun kadar özelsin...Çünkü sen Elradion'un torunusun.'")
    time.sleep(3)
    print("Şaşırarak,'Elradion mu?'kasabanın yaşlısı başını sallayarak," \
    "'Evet...senin büyükbaban.O bizim ustamızın son varisiydi.Ve sen onun kanını taşıyorsun...")
    time.sleep(4)
    print("Gel evlat... Artık sana herşeyi anlatmanın vakti geldi.Köyün hemen dışındaki kadim ormanın derinliklerinde\n" \
    "olan tapınağa gitmemiz gerekiyor.Orada kutsal gücünü uyandıracağız...")
    time.sleep(3)
    print("Kasabanın yaşlısını takip ediyorsun...Bu tapınağı daha önce duymuştun.Efsanlerde birçok kez yer edinmiş,\n" \
    "civar halkı tarafından sayılı kişilerin girdiği,korkulan ve saygı duyulan kutsal bir yerdi.")
    time.sleep(6)
    print("Bir süre yürüdükten sonra tapınağa ulaşıyorsunuz...Yaklaştıkça adeta kanında bir ruh geziyordu...")
    time.sleep(4)
    print("Kasabanın yaşlısı tapınağın kapısına elini koyarak bir süre bekledi...Ve kapı yavaş yavaş açılmaya başladı...")
    time.sleep(5)
    print("Ortada büyük bir taş parçası ve onun üstünde sen yaklaştıkça parlayan kırmızı bir enerji taşı...")
    time.sleep(5)
    print("Kasabanın yaşlısı sana bakıp gülümsedi... Ve 'Artık Azareth's Flame'yi çağırmanın vakti geldi evlat'dedi.")
    time.sleep(5)
    print("Taşa yavaş yavaş elini uzatıyorsun...Ve dokunuyorsun...Elradionun sana bahşettiği özel gücü alıyorsun...")
    karakter["ulti"]=" Azareth's Flame"
    print(f"Yeni güç yüklendi.  Azareth's Flame")
    time.sleep(10)
    
    
    print("Kasabanın yaşlısı 'Artık hazırsın evlat...Güç uyandı...Artık Arzathora gidebiliriz...'")
    time.sleep(5)
    print("1-Arzathora git")
    print("2-Tüccara git")

    x=input("Karar (1,2):")
    while True:
        if x=="1":
            break
           
        elif x=="2":
            shop()
            break
        else:
            continue
    print("Kasabanın yaşlısı ile hazırlanıp Arzathorun kulesine doğru yola çıkıyorsunuz...")
    time.sleep(5)
    final()
    print()



def final():
    os.system("cls")
    print("Kasabadan 2 günlük mesafede olan Arzathorun kulesi,kızgın volkanların tepesinde bulunuyor...\n" \
    "Daha önce oraya gitmeye kimse cesaret edememiş...Elradion hariç...Arzathonu durdurmak için büyükbaban Elradion\n" \
    "oraya gitmişti...Lakin Arzathorun daha sonradan öğrendiği kara büyü,Elraedion için güçlü gelmişti...\n" \
    f"Ama sen {karakter["isim"]}...Elradionun kanını yerde bırakmayacaksın...")
    time.sleep(15)
    print()
    print("1 günlük sürenin ardından Kasabanın yaşlısıyla yorulmaya başladınız...Havada yavaş yavaş kararmaya başlamıştı...\n" \
    "Arzathorun kulesinin tepesi görünmeye başlamıştı...")
    time.sleep(4)
    print("Derken karşınıza 2 Kara Büyücü çıkmıştı.")
    time.sleep(4)
    print("Kasabanın yaşlısı:Bunlar Arzathonun adamları...Koru kendini evlat!!")
    time.sleep(4)
    print("Kasabanın yaşlısı cesurca kılıcını çekmiş.Yaşlıda olsa gözleri ateş püskürüyordu...")
    savas("Kara Büyücü")
    print("Kasabanın yaşlısı büyücü öldürmüştü...Ama kendisi harap ve bitap düşmüştü...")
    time.sleep(4)
    print("Büyücüler bir bir yere serildikten sonra Kasabanın yaşlısı yeniden yürüyüşe geçer, bastonuna yaslanarak sana bakar:")
    time.sleep(4)
    print("\nGörüyorsun... Arzathor sadece güçle değil, zihinle de savaş açıyor. Son kapıdan önce son dersini aldın.")
    print()
    print()
    print("Bir süre daha yürüdükten sonra,uzakta gökyüzünü yaran yıldırımlar eşliğinde, Arzathor’un karanlık kalesi bütün heybetiyle karşınızda belirir.")
    print()
    time.sleep(4)
    print(f"'Artık hazırsın {karakter["isim"]}...Gidelim ve bu kötülüğe bir son verelim.'dedi kasaba yaşlısı.")
    print()
    print("Sonunda o görkemli kuleye varmıştınız.")
    print()
    print("Kalenin dev kapıları, çürümüş demir sesiyle ağır ağır açıldı...Sizin geldiğinizi biliyordu. ")
    time.sleep(3)
    print("Ortalık karanlık ve sessizdir... Adımların yankılanır.")
    time.sleep(4)
    print("Ortalık karanlık ve sessizdir... Adımların yankılanır.\n")

    print(" Sen (derin nefes alıp, kararlı):")
    print("“Bu kalenin taşları, binlerce yıldır saklar acıyı...")
    print("Ama bugün, o acının son yankısı olacak.”\n")
    time.sleep(4)
    print(" Kasabanın yaşlısı (bastonu yere vurarak):")
    print("“Evlat, unutma... Bu taşlar altında sadece geçmiş değil,")
    print("bir zamanlar umut ve cesaret de gömülü.”\n")
    time.sleep(4)
    print(" Sen (kılıcını çekerken):")
    print("“Umut ve cesaret, Arzathor!")
    print("Bugün onları yeniden dirilteceğiz.”\n")
    time.sleep(4)
    print(" Kapı ardında bir uğultu... Kalenin derinliklerinden yaklaşan sesler...\n")
    time.sleep(4)
    print(" Sen (sesini yükselterek):")
    print("“İçeri gireceğiz, korku yok!")
    print("Çünkü biz, karanlığın içine doğan ışığız!”")
    time.sleep(4)
    print("\n Kalenin kapıları ağır ağır kapanırken,")
    print("içeriden Arzathor’un derin ve soğuk sesi duyulur...\n")
    time.sleep(4)
    print(" Arzathor (alaycı, sert):")
    print("“Kasabanın yaşlısı Eldrin, seni unuttuğumu mu sandın?") 
    print("Ama artık yaşlandın, gücün tükendi.”\n")
    time.sleep(4)
    print(" Eldrin (gözleri parlıyor, bastonunu yere vuruyor):")
    print("“Gücüm tükenmiş olabilir... ama Azareth’in alevi hiç sönmez!”\n")
    time.sleep(4)
    print(" Eldrin’in cubbesi rüzgarla havalanıyor, etrafında alevler dans ediyor.")
    print("Yerden yükselen ateş sütunları kaleyi sarıyor, karanlık aydınlanıyor!\n")
    time.sleep(4)
    print(" Eldrin (bağırarak):")
    print("“Azareth’s Flame! Küllerimden doğan ateş, şimdi yıkıma!”\n")
    time.sleep(4)
    print(" Devasa bir alev patlaması Arzathor’un önünde yükseliyor,")
    print("Arzathor büyük bir darbe alıp savruluyor...\n")  
    time.sleep(4)
    print("\n Eldrin’in ultisi patladı, alevler etrafı sardı.")
    print("Bastonunu yere bırakırken ağır nefes alıyor.\n")
    time.sleep(4)
    print(" Eldrin (zayıf ama gururlu):")
    print("“Bu ateş... sadece kaleyi değil, umutları da yeniden doğuracak.")
    print("Sen... son umudumuzsun... devam et...”\n")
    time.sleep(4)
    print(" Eldrin yere yığılır, gözleri yavaşça kapanır.\n")
    time.sleep(4)
    print("\n Arzathor (nefes nefese, sinirli):")
    print("“Bu sefer olmayacak! Son gücünü göster!”\n")
    time.sleep(4)
    print(" Sen (kılıcını sıkarak):")
    print("“Eldrin’in mirasını taşıyorum! Hazır ol!”\n")
    time.sleep(4)
    print(" Kılıcın alevle parlıyor, karanlık arasında ışık saçar.")
    print("Son darbeyi indiriyorsun!\n")
    time.sleep(4)
    print(" Arzathor geriye sendeleyerek yere yığılır.")
    print("Sessizlik... Ve ardından güneşin ilk ışıkları kaleyi aydınlatır.\n")
    time.sleep(4)
    print(" Sen (gözlerin dolu):")
    print("“Artık özgürüz, Eldrin... Dinlen artık.”\n")
    time.sleep(20)
    exit()






























def giris():
    os.system("cls")

    print("______________Karanlık Çağın Şafağı______________")
    time.sleep(4)

    print()
    print()
    print()
    print("Merhaba kahraman.Ben bu diyarların ileri gelenlerinden Roff.\n" 
    "Sana bu tehlikeli yollarda rehberlik etmek için vazifelendirildim.Bu diyarın senin gibi\n"
    "kahramanlara ihtiyacı var.")
    while True:
        print()
        ad=input("Kahramanın adı: ")
        if ad.isalpha():
            break
        else:
            print("Geçersiz isim.")
    time.sleep(2)
    print()
    print("Şimdi evlat bu diyarda nasıl savaşacağını seçmen gerekiyor.")
    while True:
        print()
        print("1-Savaşçı('125 can','15 saldırı gücü')")
        print("2-Okçu('100 can','25 saldırı gücü')")
        print("3-Büyücü('80 can','30 büyü gücü')")


        char=input("[1,2,3] :")
        if char=="1":
            print("Savaşçı seçildi.")
            x=karar()
            if x==True:
                continue
            if x==False:
                pass
            
            karakter["isim"]=ad
            karakter["türü"]="Savaşçı"
            karakter["can"]=125
            karakter["güç"]=15
            karakter["max"]=125
            karakter["para"]=20
            karakter["final"]=False
            print("Oyun yükleniyor...")
            time.sleep(2)
            enter_scene()
            sisli_bataklik()
        
        
        elif char=="2":
            print("Okçu seçildi.")
            x=karar()
            if x==True:
                continue
            if x==False:
                pass
            
            karakter["isim"]=ad
            karakter["türü"]="Okçu"
            karakter["can"]=100
            karakter["güç"]=20
            karakter["max"]=100
            karakter["para"]=20
            karakter["final"]=False
            print("Oyun yükleniyor...")
            time.sleep(2)
            enter_scene()
            sisli_bataklik()
        
        elif char=="3":
            print("Büyücü seçildi")
            x=karar()
            if x==True:
                continue
            if x==False:
                pass
            karakter["isim"]=ad
            karakter["türü"]="Büyücü"
            karakter["can"]=80
            karakter["güç"]=25
            karakter["max"]=80
            karakter["para"]=20
            karakter["final"]=False
            print("Oyun yükleniyor...")
            time.sleep(2)
            enter_scene()
            sisli_bataklik()
        
        else:
            continue

giris()
