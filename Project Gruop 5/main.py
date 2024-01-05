import tkinter as tk
from tambah import tambah
from tampilkan import tampilkan
from update import update
from hapus import hapus
from simpan import simpan

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Inventory")

        self.inventory = {
            
        }

        self.label_id_barang = tk.Label(self, text="ID Barang:")
        self.label_id_barang.grid(row=0, column=0)
        self.entry_id_barang = tk.Entry(self)
        self.entry_id_barang.grid(row=0, column=1)

        self.label_nama = tk.Label(self, text="Nama Barang:")
        self.label_nama.grid(row=1, column=0)
        self.entry_nama = tk.Entry(self)
        self.entry_nama.grid(row=1, column=1)

        self.label_stok = tk.Label(self, text="Stok:")
        self.label_stok.grid(row=2, column=0)
        self.entry_stok = tk.Entry(self)
        self.entry_stok.grid(row=2, column=1)

        self.label_harga = tk.Label(self, text="Harga:")
        self.label_harga.grid(row=3, column=0)
        self.entry_harga = tk.Entry(self)
        self.entry_harga.grid(row=3, column=1)

        self.button_tambah = tk.Button(self, text="Tambah Barang", command=self.tambah_barang)
        self.button_tambah.grid(row=4, column=0)

        self.button_hapus = tk.Button(self, text="Hapus Barang", command=self.hapus_barang)
        self.button_hapus.grid(row=4, column=1)

        self.button_simpan = tk.Button(self, text="Simpan Data", command=self.simpan_data)
        self.button_simpan.grid(row=7, column=1)

        self.label_inventory = tk.Label(self, text="")
        self.label_inventory.grid(row=5, column=0, columnspan=2)

        self.label_status = tk.Label(self, text="")
        self.label_status.grid(row=6, column=0, columnspan=2)

    def tambah_barang(self):
        id_barang = self.entry_id_barang.get()
        nama = self.entry_nama.get()
        stok = self.entry_stok.get()
        harga = self.entry_harga.get()

        result, message = tambah(self.inventory, id_barang, nama, stok, harga)
        self.label_status.config(text=message)
        tampilkan(self.inventory, self.label_inventory)

        self.entry_id_barang.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_stok.delete(0, tk.END)
        self.entry_harga.delete(0, tk.END)

    def simpan_data(self):
        nama_file = "inventory.json"
        result, message = simpan(self.inventory, nama_file)
        self.label_status.config(text=message)    

    def hapus_barang(self):
        id_barang = self.entry_id_barang.get()

        result, message = hapus(self.inventory, id_barang)
        self.label_status.config(text=message)
        tampilkan(self.inventory, self.label_inventory)

        self.entry_id_barang.delete(0, tk.END)

if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()
