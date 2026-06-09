##ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ – ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΣΑΒΒΑΤΟ 6 ΙΟΥΝΙΟΥ 2026
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Δ
##Ένας εκδοτικός οίκος επιθυμεί να μελετήσει την εμπορική πορεία των
##σαράντα (40) βιβλίων που διαθέτει. Για τον σκοπό αυτό θα καταγράψει για
##κάθε βιβλίο τον τίτλο του καθώς και τον αριθμό των πωλήσεών του, κατά τη
##διάρκεια του τελευταίου έτους.
##Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο:
##Δ1. α) Να διαβάζει τον τίτλο κάθε βιβλίου και να τον καταχωρίζει σε μία
##λίστα με όνομα TITLES. (μον. 2)
##β) Να διαβάζει τον αριθμό πωλήσεων του κάθε βιβλίου κάνοντας έλεγχο
##εγκυρότητας, ώστε ο αριθμός των πωλήσεων να είναι μη αρνητικός και να
##τον καταχωρίζει σε μία λίστα με όνομα SALES. (μον. 4)
##Μονάδες 6
##Δ2. Να υπολογίζει και να εμφανίζει:
##α) τις συνολικές πωλήσεις όλων των βιβλίων. (μον. 3)
##β) τον μέσο όρο των πωλήσεων όλων των βιβλίων. (μον. 1)
##Μονάδες 4
##Δ3. Να καλεί συνάρτηση με όνομα MEGISTOS(), η οποία θα δέχεται τη λίστα
##SALES και τη λίστα TITLES, θα υπολογίζει και θα επιστρέφει τον τίτλο του
##βιβλίου με τις περισσότερες πωλήσεις και στη συνέχεια θα τον εμφανίζει
##με το μήνυμα “Ο τίτλος του βιβλίου με τις περισσότερες πωλήσεις είναι ”.
##Σημείωση: Θεωρήστε ότι υπάρχει ένας μόνο τίτλος βιβλίου με μέγιστο αριθμό πωλήσεων.
##Μονάδες 9
##Δ4. Να ταξινομεί τη λίστα TITLES σε αλφαβητική σειρά με χρήση του
##αλγορίθμου ταξινόμησης ευθείας ανταλλαγής (φυσαλίδα ‐ bubble sort),
##αναδιατάσσοντας συγχρόνως τη λίστα SALES. Στο τέλος, να εμφανίζει τις
##λίστες TITLES και SALES.
##
def MEGISTOS(TITLES,SALES):
    max_sale = 0
    max_title = ""
    for i in range(len(SALES)):
        if max_sale < SALES[i]:
           max_sale = SALES[i]
           max_title = TITLES[i]
    return max_title

BOOKS = 40
TITLES = []
SALES = []

##synolikes_pwliseis = 0
##for book in range(1, BOOKS+1):
##    title = input("Τιτλος βιβλίου {}: ".format(book))
##    TITLES.append(title)
##    sale = ""
##    while not sale.isdigit() or int(sale) < 0:
##        sale = input("Αριθμός πωλήσεων βιβλίου {}: ".format(book))
##    SALES.append(int(sale))
##    synolikes_pwliseis += int(sale)

try:
    print("Ανάγνωση του αρχείου εισόδου...\n")
    INPUTFILENAME="vivlia.txt"
    with open(INPUTFILENAME, 'r', encoding="utf-8") as inputfile:
        synolikes_pwliseis = 0
        for book in range(1, BOOKS+1):
            title = inputfile.readline().strip('\n').strip('\ufeff')
            print("Τιτλος βιβλίου {}: {}".format(book, title))
            TITLES.append(title)
            sale = ""
            while not sale.isdigit() or int(sale) < 0:
                sale = inputfile.readline().strip('\n').strip('\ufeff')
                print("Αριθμός πωλήσεων βιβλίου {}: {}".format(book, sale))
            SALES.append(int(sale))
            synolikes_pwliseis += int(sale)
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)

print("Συνολικές πωλήσεις όλων των βιβλίων: {}".format(synolikes_pwliseis))
print("Μέσος όρος πωλήσεων όλων των βιβλίων: {:.1f}".format(synolikes_pwliseis / BOOKS))
print("Ο τίτλος του βιβλίου με τις περισσότερες πωλήσεις είναι: {}".format(MEGISTOS(TITLES,SALES)))

N = len(TITLES)
for i in range(N-1): # range(0, N–1, 1)
    for j in range(N-1 , i , -1): # μέχρι και i–1
        if TITLES[j] < TITLES[j-1]:
            TITLES[j], TITLES[j-1] = TITLES[j-1], TITLES[j]
            SALES[j], SALES[j-1] = SALES[j-1], SALES[j]

print("-------------------------------------------------------------------")
print("Τίτλοι βιβλίων με αλφαβητική σειρά και οι αντίστοιχες πωλήσεις τους")
print("-------------------------------------------------------------------")
for i in range(len(TITLES)):
    print("{}\t{}".format(TITLES[i], SALES[i]))
