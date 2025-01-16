# Metode-Komputasi
PEMODELAN NUMERIK DAN ANALITIK PENDULUM GANDA

## Anggota Kelompok Santai
- 10221038_Kevin Winata
- 10222007_Jonathan Sugijanto
- 10222049_Afrah Damara Yani
- 10222066_Melinda Alberta

## Deskripsi
Kami berencana membuat aplikasi simulasi pendulum ganda sederhana dengan Python. Parameter kedua massa, kedua panjang batang, percepatan gravitasi, posisi awal bandul, dan kecepatan awal bandul dapat diatur pengguna. Persamaan gerak dari pendulum dikerjakan tiap iterasi waktu dengan metode numerik penyelesaian persamaan diferensial. Posisi kemudian didapatkan tiap waktunya, sehingga dapat ditampilkan lintasan yang telah dilalui bandul. Data posisi tiap waktunya dapat didiferensiasikan untuk mendapat kecepatan dan percepatan tiap waktu (ditampilkan ke pengguna). Terakhir, kita tahu dengan aproksimasi sudut kecil, sistem ini dapat diselesaikan secara analitik (osilasi terkopel). Penyelesaian analitik yang melibatkan eigenvalue problem juga dilakukan aplikasi untuk dibandingkan dengan lintasan sebenarnya. Perbandingan secara kuantitatif dilakukan dengan melakukan regresi nonlinear data lintasan sebenarnya terhadap lintasan solusi analitik, sehingga didapat nilai R^2 yang menggambarkan error.

## Daftar isi
- numeric.ipynb
    * Deskripsi: algoritma utama metode numerik RK4.
- analytic.ipynb
    * Deskripsi: kumpulan algoritma utama metode analitik, serta perbandingan numerik RK4 dan analitik dengan regresi nonlinear.
- regression_sweep.ipynb
    * Deskripsi: hasil regresi nonlinear terhadap besar sudut gangguan (tidak masuk laporan).
- Interpretasi_Fisik.ipynb
    * Deskripsi: Animasi Bandul ganda menggunakan Metode Euler.
- Karakteristik_Chaos.py
    * Deskripsi: Berisikan tentang code yang membuat animasi gerak 2 pendulum dengan iterasi selama 10 detik.
- Persamaan_Differensial.py
    * Deskripsi: Berisikan tentang code yang akan menghasilkan output berupa waktu, posisi kartesian kedua pendulum, kecepatan dan percepatan kartesian, serta kecepatan dan percepatan total kedua pendulum.
- hasil iterasi data/
    * Deskripsi: Folder berisi hasil dari code iterasi 10 detik.