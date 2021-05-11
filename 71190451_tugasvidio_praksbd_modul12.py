program= True
while program==True:
    print('daftar operasi\n1.gabungn\n2.cari yang sama\n3.cari yang beda\n4.exit')
    pilihan=int(input('masukan pilihan:'))
    if pilihan == 1:
        kalimat1=input('masukan kalimat pertama:')
        kalimat2=input('masukan kalimat kedua:')
        set1=set()
        set2=set()
        for kata in kalimat1:
            set1.add(kata)
        for kata1 in kalimat2:
            set2.add(kata1)
        gabungan=set1|set2
        List=list(gabungan)
        print(List)
    elif pilihan == 2:
        kalimat1=input('masukan kalimat pertama:')
        kalimat2=input('masukan kalimat kedua:')
        set1=set()
        set2=set()
        for kata in kalimat1:
            set1.add(kata)
        for kata1 in kalimat2:
            set2.add(kata1)
        kata_sama=set1 & set2
        List=list(kata_sama)
        print(List)
    elif pilihan == 3:
        kalimat1=input('masukan kalimat pertama:')
        kalimat2=input('masukan kalimat kedua:')
        set1=set()
        set2=set()
        for kata in kalimat1:
            set1.add(kata)
        for kata1 in kalimat2:
            set2.add(kata1)
        kata_beda=set1 ^ set2
        List=list(kata_beda)
        print(List)
    elif pilihan == 4:
        print('Terima kasih sudaj menggunakan program ini')
        program=False
    elif pilihan > 4:
        print('pilihan anda salah')
        
