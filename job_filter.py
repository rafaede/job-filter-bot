from kirim_telegram import kirim_telegram

def filter_lokasi(listings):
    hasil = []
    for listing in listings:
        if "Surabaya" in listing['lokasi'] or "Malang" in listing['lokasi'] or "Remote" in listing['lokasi']:
            hasil.append(listing)
            
    return hasil
            

listings = [{"judul": "Programmer","perusahaan":"PT. Lestari Mulia Sentosa","lokasi":"Sidoarjo, Jawa Timur"},
       {"judul": "Software Developer","perusahaan":"PT Mitra Binamandiri Makmur","lokasi":"Gempol, Jawa Timur"},
       {"judul": "Software and Network Technician","perusahaan":"PT Karya Solusi Prima Sejahtera","lokasi":"Surabaya, Jawa Timur"},
       {"judul": "Backend Developer (Rust)","perusahaan":"PT Codein Digital Inspiration","lokasi":"Surabaya, Jawa Timur"},
       {"judul": "Software Engineer (AI Developer)","perusahaan":"PT Sinar Cemaramas Abadi","lokasi":"Surabaya, Jawa Timur"},
       {"judul": "FULL-STACK DEVELOPER","perusahaan":"PT Grandville Food Indonesia","lokasi":"Surabaya, Jawa Timur"}
       ]

print(len(listings))
fil =  filter_lokasi(listings)
print(len(fil))
pesan = ""
for p in fil:
    pesan += f"{p['judul']} - {p['perusahaan']}\n"
print(pesan)
kirim_telegram(pesan)