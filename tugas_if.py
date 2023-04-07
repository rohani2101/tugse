def nilai_maksimal (list):
  nilai_terbesar = list[0]

  if len(list) > 1:
    # proses rekursif
    next_nilai_terbesar = nilai_maksimal(list[1:])

    if next_nilai_terbesar > nilai_terbesar:
      nilai_terbesar = next_nilai_terbesar

  return nilai_terbesar
b = [25,90,40,95,35,70,50,20,80,65]
print('nilai dari',b)
print('dan nilai terbesar adalah :', nilai_maksimal(b))
