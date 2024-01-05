def update(inventory, id_barang, jumlah):
    try:
        jumlah = int(jumlah)
        if id_barang in inventory:
            inventory[id_barang]['stok'] += jumlah
            return True, f"Stok barang dengan ID {id_barang} berhasil diupdate."
        else:
            return False, f"Tidak dapat menemukan barang dengan ID {id_barang} dalam inventory."
    except ValueError:
        return False, "Input jumlah harus berupa angka."
