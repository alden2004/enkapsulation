class Kelassaya:
    def __init__(self, variable_private, variable_proteksi):
        self._variable_private = variable_private
        self._variable_proteksi = variable_proteksi

    def tampilkan_nilai(self):
        print(f"Variable private: {self._variable_private}")
        print(f"Variable proteksi: {self._variable_proteksi}")

class Kelasturunan(Kelassaya):
    def akses_proteksi(self):
        print(f"Mengakses variable proteksi: {self._variable_proteksi}")

obj = Kelassaya(10, 11)
obj.tampilkan_nilai()

obj_turunan = Kelasturunan(30, 40)  
obj_turunan.akses_proteksi()