import lekcja1_do_importu

wybor = input(""" Wybierz figurę , której chcesz obliczyć:
1. Prostokąt
2. Kwadrat
3. Trójkąt
4. Trapez
5. Koło 
""")

if wybor == '1':
        x = int(input("Wprowadź długość pierwszego boku: "))
        y = int(input("Wprowadź długość drugiego boku: "))
        print("Pole prostokąta jest równe:",lekcja1_do_importu.poleProstokata(x,y))
elif wybor == '2':
        x = int(input("Wprowadź długość boku: "))
        print("Pole kwadratu jest równe:",lekcja1_do_importu.poleKwadratu(x))
elif wybor == '3':
        x = int(input("Wprowadź długość boku: "))
        h = int(input("Wprowadź długość wysokości: "))
        print("Pole trójkąta jest równe:",lekcja1_do_importu.poleTrojkata(x,h))
elif wybor == '4':
        x = int(input("Wprowadź długość pierwszej podstawy: "))
        y = int(input("Wprowadź długość drugiej podstawy: "))
        h = int(input("Wprowadź długość wysokości: "))
        print("Pole trapezu jest równe:",lekcja1_do_importu.poleTrapezu(x,y,h))
elif wybor == '5':
        r = int(input("Wprowadź długość średnicy: "))
        print("Pole koła jest równe:",lekcja1_do_importu.poleKola(r))
elif wybor == '6':
        print("No to pa")
else:
        print("Nie ma takiego wyboru spróbuj ponownie")