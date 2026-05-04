Analisis Performa Penjualan E-commerce
1. Business Question
Tujuan dari analisis ini adalah untuk menjawab beberapa pertanyaan berikut:
1. Siapa pelanggan terbaik berdasarkan data transaksi?
2. Produk apa yang termasuk underperformer (harga tinggi tetapi jarang terjual)?
3. Bagaimana tren penjualan setiap bulan?
4. Apakah terdapat hubungan antara jumlah pembelian dan total penjualan?
5. Apakah harga mempengaruhi performa penjualan?

2. Data Wrangling
Proses pembersihan data yang dilakukan meliputi:
1. Menghapus data dengan UnitPrice ≤ 0 untuk menghindari data anomali
2. Mengubah kolom InvoiceDate menjadi format datetime
3. Membuat kolom baru:
   Total_Sales = Quantity × UnitPrice
   Month untuk analisis penjualan bulanan
4. Memastikan tidak ada data kosong yang mengganggu analisis

3. Insights
Tren Penjualan Bulanan
1. Data menunjukkan adanya fluktuasi penjualan setiap bulan
2. Terdapat bulan dengan penjualan tertinggi
3. Informasi ini dapat digunakan untuk menentukan strategi promosi
   
Korelasi Antar Variabel
1. Terdapat korelasi positif antara Quantity dan Total_Sales
2. Artinya semakin banyak produk terjual, semakin tinggi pendapatan perusahaan

Produk Underperformer
1. Produk dengan harga tinggi namun jumlah penjualan rendah termasuk kategori underperformer
2. Hal ini menunjukkan bahwa harga dapat menjadi faktor penghambat penjualan

Segmentasi Pelanggan (RFM Analysis)
1. Pelanggan dengan nilai RFM tinggi merupakan pelanggan loyal
2. Pelanggan ini sering melakukan transaksi dan memberikan kontribusi besar terhadap pendapatan

4. Recommendation
Berdasarkan hasil analisis yang telah dilakukan:
1. Fokus pada produk dengan performa penjualan tinggi
2. Evaluasi produk dengan harga mahal namun kurang diminati
3. Berikan promo atau diskon untuk meningkatkan penjualan produk underperformer
4. Berikan reward atau voucher kepada pelanggan loyal
5. Gunakan tren penjualan bulanan untuk menentukan strategi pemasaran

Kesimpulan 
Analisis menunjukkan bahwa:
1. Penjualan dipengaruhi oleh jumlah pembelian dan harga produk
2. Pelanggan loyal memiliki kontribusi besar terhadap revenue
3. Strategi berbasis data dapat membantu meningkatkan performa bisnis
