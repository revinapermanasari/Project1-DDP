def tambah(inventory, id_barang, nama, stok, harga):
    try:
        # Konversi input stok dan harga ke tipe data yang sesuai
        stok = int(stok)
        harga = float(harga)

        # Pastikan ID barang unik, jika tidak tambahkan barang baru
        if id_barang not in inventory:
            inventory[id_barang] = {'nama': nama, 'stok': stok, 'harga': harga}
            return True, f"Barang {nama} berhasil ditambahkan ke inventory."
        else:
            return False, f"Barang dengan ID {id_barang} sudah ada dalam inventory."

    except ValueError:
        return False, "Input stok dan harga harus berupa angka."
