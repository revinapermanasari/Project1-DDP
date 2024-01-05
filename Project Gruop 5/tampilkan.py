def tampilkan(inventory, label):
    text = "Inventory:\n"
    for id_barang, barang in inventory.items():
        text += f"ID: {id_barang}, Nama: {barang['nama']}, Stok: {barang['stok']}, Harga: {barang['harga']}\n"
    label.config(text=text)
