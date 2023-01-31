import cv2
#image = cv2.imread("dog.jpg")
print("Välkommen till bildhanteraren! För hjälp, skriv 'hjälp'.")
while True:
    commandLine = input("Kommando: ")
    cmd = commandLine.split()
    if len(cmd) == 0:
        pass
    elif cmd[0] == "hjälp":
        print("För att använda programmet: Skriv: ")
        print("  'ladda bild' - för att att ladda valfri bild (format: 'xxxx.jpg')")
        print("  'visa bild'  - för att visa bild, tryck x på bildrutan för att komma till nästa redigerade bild")
        print("  'spara bild' - för att spara bild enlgit önskemål")
        print("  'sluta'      - för att sluta programmet")
    elif cmd[0] == "sluta":
        print("Tack för att du använde bildhanteraren!")
        exit()
    elif cmd[0] == "ladda" and cmd[1] == "bild":
        print("Skriv in namnet på bilden du vill ladda: ")
        image = input("Jag vill ladda bilden: ")
        img = cv2.imread(image)
    elif cmd[0] == "visa" and cmd[1] == "bild":
        cv2.imshow("Original Image", img)
        cv2.waitKey(0)
        #make a black and white picture
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Black and white Image", gray_image)
        cv2.waitKey(0)
        #make a inverted picture
        inverted_image = 255 - gray_image
        cv2.imshow("Inverted", inverted_image)
        cv2.waitKey()
        #make detected edges
        edge_image = cv2.Canny(img, 100, 200)
        cv2.imshow("Detected Edges", edge_image)
        cv2.waitKey(0)
        #make a sketch picture
        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        cv2.imshow("Sketch", pencil_sketch)
        cv2.waitKey(0)
    elif cmd[0] == "spara" and cmd[1] == "bild":
        print("Vilken bild vill du spara? Ange siffra: ")
        print("    1 - 'Black and white Image'")
        print("    2 - 'Inverted'")
        print("    3 - 'Detected Edges'")
        print("    4 - 'Sketch'")
        output = input("Jag vill spara bild nummer: ")
        if output == "1":
            cv2.imwrite("Black and white Image.jpg", gray_image)
        elif output == "2":
            cv2.imwrite("Inverted.jpg", inverted_image)
        elif output == "3":
            cv2.imwrite("Detected Edges.jpg", edge_image)
        elif output == "4":
            cv2.imwrite("Sketch.jpg", pencil_sketch)
        else:
            print(f"Okänt val: {output}")
        #cv2.imwrite("Sketch.jpg", pencil_sketch)
        print("Bilden sparades enligt önskemål.")
    else:
        print(f"Okänt kommando: {cmd[0]}")
