from kirim_telegram import kirim_telegram
import json

def filter_lokasi(listings):
    hasil = []
    for listing in listings:
        if "Surabaya" in listing['lokasi'] or "Malang" in listing['lokasi'] or "Remote" in listing['lokasi']:
            hasil.append(listing)
            
    return hasil

def tambah_listing(listings, judul, perusahaan, lokasi):
    listings.append({"judul":judul, "perusahaan":perusahaan, "lokasi":lokasi})
    return listings
 
with open("listings.json") as f:
    listings = json.load(f)
          
print(len(listings))

fil =  filter_lokasi(listings)
print(len(fil))
pesan = ""
for p in fil:
    pesan += f"{p['judul']} - {p['perusahaan']}\n"
print(pesan)
kirim_telegram(pesan)