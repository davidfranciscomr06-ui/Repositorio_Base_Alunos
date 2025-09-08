n1 = int(input("digite o numero"))
i = 1

while i <= n1:
    if i % 2 == 0:
        print(i)

    situaçao= i + 1
with open("media.txt", "a", encoding="utf-8") as media_arquivo:
    media_arquivo.write(f"{n1} com média {i:.1f} está: {situaçao}\n")