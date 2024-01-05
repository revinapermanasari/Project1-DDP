def hapus(inventory, id_barang):
    if id_barang in inventory:
        del inventory[id_barang]
        return True, f"Barang dengan ID {id_barang} berhasil dihapus dari inventory."
    else:
        return False, f"Tidak dapat menemukan barang dengan ID {id_barang} dalam inventory."
