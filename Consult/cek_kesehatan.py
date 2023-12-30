from flask import Flask, render_template, request, redirect
#flask adalah library yang di gunakan untuk mengakses python di web
#render_templat software yang mengambil template yang dibuat menggunakan bahasa template,nanti hasilnya berupa konten seperti dokumen teks
#request yaitu modul pada Python yang bisa digunakan untuk mengirim berbagai request HTTP contohnya url atau data
#redirect untuk mengarahkan ke url yang telah di seting


aplikasi = Flask(__name__)
#untuk mmengubah variabel ke nama modul, sehingga nilai variabel ini akan bervariasi tergantung pada file sumber Python tempat Anda menggunakannya.

USERNAME = 'admin'
PASSWORD = '123456'

def diagnosa_penyakit(gejala):
#def untuk memanggil fungsi
    #Logika untuk mendiagnosis penyakit berdasarkan gejala
    
    penyakit = {
        'demam': 'Anda mungkin terkena flu.',
        'pusing': 'Gejala pusing dapat disebabkan oleh berbagai hal, sebaiknya berkonsultasi dengan dokter.',
        'batuk': 'Batuk dapat menjadi tanda penyakit pernapasan.',
        'mual': 'Mual bisa disebabkan oleh berbagai faktor, terutama terkait dengan gangguan pencernaan.',
        'penurunan berat badan tanpa sebab': 'penurunan berat badan tanpa sebab yang paling sering teradi akibat kanker pankreas,perut,esofagus,atau paru-paru.',
        'kerusakan gigi': 'Gigi yang mudah rusak bisa menjadi tanda dari sakit maag dikarenakan asam lambung naik ke kerongkongan (refluks)yang bisa mengikis pelindungan gigi.',
        'mendengkur': 'Ini merupakan gejala umum sleep apena,yang dikaitkan dengan peningkatan reiko penyakit jantung.',
        'sulit tidur disertai kecemasan': 'Merupakan gejala penyakit insomnia'
    }
    #Untuk Mengambil Penyakit apa yang telah dipilih
    deskripsi_penyakit = [penyakit[gejala] for gejala in gejala if gejala in penyakit]
    return deskripsi_penyakit

# Route untuk halaman home
@aplikasi.route('/')
def home():
    return render_template('komplain_formulir.html')

@aplikasi.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            # Jika login berhasil, arahkan ke halaman survei
            return render_template('komplain_formulir.html')
        else:
            # Jika login gagal, tampilkan pesan kesalahan
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

#@aplikasi.route('/')
#def index():
#    return render_template('komplain_formulir.html')
#route digunakan untuk mendefinisikan URL apa yang memanggil fungsi dibawahnya
@aplikasi.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # untuk mengambil keluhan kesehatan dari list yang sudah di buat
        gejala = request.form.getlist('gejala')
        # untuk diagnosa penyakit berdasarkan keluhan
        diagnosis = diagnosa_penyakit(gejala)
        return render_template('hasil.html', diagnosis=diagnosis)

@aplikasi.route('/whatsapp_doctor')
def whatsapp_doctor():
    return redirect('https://wa.me/+6281234567890')

# Halaman dokter spesialis
@aplikasi.route('/dokter_spesialis')
def dokter_spesialis():
    return render_template('dokter_spesialis.html')

# Halaman alamat
@aplikasi.route('/alamat')
def alamat():
    return render_template('alamat.html')

# Halaman contact person
@aplikasi.route('/contact_person')
def contact_person():
    return render_template('contact_person.html')

if __name__ == '__main__':
    aplikasi.run(debug=True)
