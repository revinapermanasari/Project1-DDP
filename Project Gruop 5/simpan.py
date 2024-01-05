import json

def simpan(inventory, nama_file):
    try:
        with open(nama_file, 'w') as file:
            json.dump(inventory, file)
        return True, f"Data inventory berhasil disimpan ke dalam file {nama_file}."
    except Exception as e:
        return False, f"Terjadi kesalahan saat menyimpan data: {str(e)}"
