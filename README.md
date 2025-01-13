# Metode-Komputasi
PEMODELAN NUMERIK DAN ANALITIK PADA DINAMIKA CHAOS PENDULUM GANDA

Kelompok Santai
- 10221038_Kevin Winata
- 10222007_Janathan Sugijanto
- 10222049_Afrah Damara Yani
- 10222066_Melinda Alberta

Kami berencana membuat aplikasi simulasi pendulum ganda sederhana dengan Python. Parameter kedua massa, kedua panjang batang, percepatan gravitasi, posisi awal bandul, dan kecepatan awal bandul dapat diatur pengguna. Persamaan gerak dari pendulum dikerjakan tiap iterasi waktu dengan metode numerik penyelesaian persamaan diferensial. Posisi kemudian didapatkan tiap waktunya, sehingga dapat ditampilkan lintasan yang telah dilalui bandul. Data posisi tiap waktunya dapat didiferensiasikan untuk mendapat kecepatan dan percepatan tiap waktu (ditampilkan ke pengguna). Terakhir, kita tahu dengan aproksimasi sudut kecil, sistem ini dapat diselesaikan secara analitik (osilasi terkopel). Penyelesaian analitik yang melibatkan eigenvalue problem juga dilakukan aplikasi untuk dibandingkan dengan lintasan sebenarnya. Perbandingan secara kuantitatif dilakukan dengan melakukan regresi nonlinear data lintasan sebenarnya terhadap lintasan solusi analitik, sehingga didapat nilai \frac {R^2} yang menggambarkan error.
