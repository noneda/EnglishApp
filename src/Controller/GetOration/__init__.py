class Oration:
    def __init__(self) -> None:
        pass

    def OrdenBySentences(self, drop_zone : tuple , labels : list):
        x1 , y1, x2, y2 = drop_zone

        texts = []
        for label in labels.values():
            text = label.text
            x, y, = label.actPos

            if x1 <= x <= x2 and y1 <= y <= y2:
                texts.append(
                    (text, x)
                )

        n = len(texts)
        for i in range(n):
            for j in range(0, n-i-1):
                if texts[j][1] > texts[j+1][1]:
                    texts[j] . texts[j+1] = texts[j-1], texts[j]

        sorted = [
            text for text , _ in texts
        ]
        sentece = ''.join(sorted)

        return sentece