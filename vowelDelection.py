def sesli_sil(metin):
    sesliler = "aeıioöuüAEIİOÖUÜ"
    sonuc = ""
    for harf in metin:
        if harf not in sesliler:
            sonuc += harf
    return sonuc
print(sesli_sil("dı0wajodwğka"))
