# model.py

questions = [
    {
        "question": "Apa jenis aktivitas yang paling sering Anda lakukan?",
        "options": ["Aktivitas outdoor atau olahraga", "Pekerjaan di dalam ruangan atau aktivitas sehari-hari", "Berjalan jauh atau berdiri dalam waktu lama"]
    },
    {
        "question": "Seberapa sering Anda terkena air atau kelembapan saat beraktivitas?",
        "options": ["Sering terpapar air atau berada di lingkungan basah", "Sesekali terkena air, tetapi tidak terlalu sering", "Jarang sekali atau hampir tidak pernah"]
    },
    {
        "question": "Apa masalah utama yang ingin Anda hindari saat menggunakan plaster?",
        "options": ["Luka basah atau infeksi akibat air", "Luka terbuka yang butuh perlindungan jangka panjang", "Lecet atau gesekan pada kaki saat berjalan"]
    }
]

def get_product_recommendation(answers):
    if answers == ['a', 'a', 'a']:
        return ("Hansaplast Plaster Aqua Protect", "assets/left.jpg")
    elif answers == ['b', 'b', 'b']:
        return ("Hansaplast Universal Plaster", "assets/middle.jpg")
    elif answers == ['c', 'c', 'c']:
        return ("Hansaplast Foot Plaster", "assets/right.jpg")
    else:
        return (None, None)
