##ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ
##HMEΡΗΣΙΩΝ – ΕΣΠΕΡΙΝΩΝ ΕΠΑΓΓΕΛΜΑΤΙΚΩΝ ΛΥΚΕΙΩΝ
##ΣΑΒΒΑΤΟ 6 ΙΟΥΝΙΟΥ 2026
##ΕΞΕΤΑΖΟΜΕΝΟ ΜΑΘΗΜΑ:
##ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ ΥΠΟΛΟΓΙΣΤΩΝ
##
##ΘΕΜΑ Γ
##Οι πέντε (5) κριτές ενός τηλεοπτικού διαγωνισμού τραγουδιού βαθμολογούν
##τους διαγωνιζόμενους που συμμετέχουν σε αυτόν, με βαθμολογία που
##κυμαίνεται από 1 έως 10 ακέραιες μονάδες.
##Η τελική βαθμολογία κάθε διαγωνιζόμενου προκύπτει από τον μέσο όρο των
##βαθμών των πέντε (5) κριτών.
##Να αναπτύξετε πρόγραμμα σε γλώσσα προγραμματισμού Python το οποίο για
##κάθε διαγωνιζόμενο:
##Γ1. α) Να διαβάζει το όνομα του διαγωνιζόμενου. (μον. 1)
##β) Να διαβάζει τις βαθμολογίες των πέντε (5) κριτών. (μον. 3)
##γ) Η εισαγωγή να τερματίζει, όταν δοθεί ως όνομα διαγωνιζόμενου η λέξη ˈΤΕΛΟΣˈ. (μον. 3)
##Σημείωση: Θεωρήστε ότι υπάρχει τουλάχιστον ένας (1) διαγωνιζόμενος.
##Μονάδες 7
##Γ2. Να υπολογίζει και να εμφανίζει την τελική βαθμολογία κάθε διαγωνιζόμενου.
##Μονάδες 4
##Γ3. Να γράφει σε αρχείο με όνομα ˈresults.txtˈ το όνομα του
##διαγωνιζόμενου, αν η τελική του βαθμολογία είναι μεγαλύτερη από 7 μονάδες.
##Μονάδες 6
##Γ4. Να υπολογίζει και να εμφανίζει το ποσοστό των διαγωνιζόμενων που η
##τελική τους βαθμολογία είναι μικρότερη ή ίση από 7 μονάδες.
##Μονάδες 8
##Σημείωση: Δεν απαιτούνται έλεγχοι εγκυρότητας τιμών.
##
KRITES = 5
PANW = 1
KATW = 10
ARXEIO_EXODOY = "results.txt"

onoma = ""
diagonizomenoi = 0
bathm_mikrot = 0

##while onoma != "ΤΕΛΟΣ":
##    onoma = input("Όνομα διαγωνιζόμενου: ")
##    if onoma == "ΤΕΛΟΣ":
##        print("Τερματισμός εισαγωγής δεδομένων")
##    else:
##        diagonizomenoi += 1
##        synolo_bathm = 0
##        for kritis in range(1, KRITES+1):
##            bathmologia = ""
##            while not bathmologia.isdigit() \
##              or int(bathmologia) not in range(PANW, KATW+1):
##              bathmologia = input("Βαθμολογία κριτή {}: ".format(kritis))
##            synolo_bathm += int(bathmologia)
##        teliki_bathm = synolo_bathm/KRITES
##        print("Τελική βαθμολογία του {}: {:.2f}".format(onoma, teliki_bathm))
##        print("Η τελική βαθμολογία του διαγωνιζόμενου είναι ", end="")
##        if teliki_bathm > 7.00:
##            print("μεγαλύτερη από 7 μονάδες")
##            arxeio_exodou = open(ARXEIO_EXODOY, 'a', encoding="utf-8")
##            arxeio_exodou.write(onoma + "\n")
##            arxeio_exodou.close()
##        else:
##            print("μικρότερη ή ίση από 7 μονάδες")
##            bathm_mikrot += 1

try:
    print("Ανάγνωση του αρχείου εισόδου...\n")
    INPUTFILENAME="diagonizomenoi.txt"
    with open(INPUTFILENAME, 'r', encoding="utf-8") as inputfile:
        while onoma != "ΤΕΛΟΣ":
            onoma = inputfile.readline().strip('\n').strip('\ufeff')
            print("Όνομα διαγωνιζόμενου: {}".format(onoma))
            if onoma == "ΤΕΛΟΣ":
                print("Τερματισμός εισαγωγής δεδομένων")
            else:
                diagonizomenoi += 1
                synolo_bathm = 0
                for kritis in range(1, KRITES+1):
                    bathmologia = ""
                    while not bathmologia.isdigit() \
                      or int(bathmologia) not in range(PANW, KATW+1):
                      bathmologia = inputfile.readline().strip('\n').strip('\ufeff')
                      print("Βαθμολογία κριτή {}: {}".format(kritis, bathmologia))
                    synolo_bathm += int(bathmologia)
                teliki_bathm = synolo_bathm/KRITES
                print("Τελική βαθμολογία του {}: {:.2f}".format(onoma, teliki_bathm))
                print("Η τελική βαθμολογία του διαγωνιζόμενου είναι ", end="")
                if teliki_bathm > 7.00:
                    print("μεγαλύτερη από 7 μονάδες")
                    arxeio_exodou = open(ARXEIO_EXODOY, 'a', encoding="utf-8")
                    arxeio_exodou.write(onoma + "\n")
                    arxeio_exodou.close()
                else:
                    print("μικρότερη ή ίση από 7 μονάδες")
                    bathm_mikrot += 1
except Exception as err:
    print("Σφάλμα στην ανάγνωση του αρχείου εισόδου!", err)

print("Ποσοστό των διαγωνιζόμενων που η τελική τους βαθμολογία είναι μικρότερη ή ίση από 7 μονάδες: {:.1%} ({}/{})".format(bathm_mikrot / diagonizomenoi, bathm_mikrot, diagonizomenoi))
