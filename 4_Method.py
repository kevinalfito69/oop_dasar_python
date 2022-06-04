
class siswa():
    # class variabel
    jumlah_siswa = 0
    def __init__(self, namaSiswa, umurSiswa, kelasSiswa, alamatSiswa):
        # instance variabel
        self.nama   = namaSiswa
        self.umur   = umurSiswa
        self.kelas  = kelasSiswa
        self.alamat = alamatSiswa
        siswa.jumlah_siswa += 1
    # Void function/Method
    def Entod(self):
        print("nama saya adalah " + self.nama)
    # Method dengan argumen
    def Kelas(self, naik):
        self.kelas += naik
    # method dengan return
    def getKelas(self):
        return self.kelas

siswa1   = siswa('Juki',16,5,'Cirebon')
siswa2   = siswa('Asep', 12, 3, 'Sunda')

siswa1.Entod()
siswa1.Kelas(1)
print(siswa1.getKelas())
# print(siswa1.__dict__)
# print(siswa2.__dict__)