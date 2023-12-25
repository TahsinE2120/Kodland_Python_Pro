meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":"bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY":"korkunç",
            "AGGRO":"agresifleşmek/sinirlenmek",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

for i in range(0,10):
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Bu kelime henüz yok")
